import os
import logging
from datetime import datetime, timedelta
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from dateutil import parser

from amadeus import Client, ResponseError
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults


# =========================================================
# CONFIG
# =========================================================

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

AMADEUS_CLIENT_ID = os.getenv("AMADEUS_CLIENT_ID")
AMADEUS_CLIENT_SECRET = os.getenv("AMADEUS_CLIENT_SECRET")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

app = FastAPI(title="TravelGeek AI Assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================================================
# LLM MODELS
# =========================================================

class FlightQuery(BaseModel):
    origin_city: str
    destination_city: str
    departure_date: str
    adults: Optional[int] = 1


class HotelQuery(BaseModel):
    city: str
    check_in: Optional[str] = None
    check_out: Optional[str] = None
    adults: Optional[int] = 1


flight_llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0).with_structured_output(FlightQuery)
hotel_llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0).with_structured_output(HotelQuery)
planner_llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0.7)
classifier_llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0)
summarizer_llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0)

# =========================================================
# CLIENTS
# =========================================================

amadeus_client = Client(
    client_id=AMADEUS_CLIENT_ID,
    client_secret=AMADEUS_CLIENT_SECRET,
    hostname="test"
)

tavily = TavilySearchResults(max_results=5)

# =========================================================
# HELPERS
# =========================================================

def detect_intent(prompt: str):
    response = classifier_llm.invoke(
        f"Classify this travel query into one of: flights, hotels, places, itinerary.\nQuery: {prompt}\nReturn only one word."
    )
    return response.content.strip().lower()


def normalize_date(date_str: Optional[str]):
    if not date_str:
        return None
    try:
        parsed = parser.parse(date_str, fuzzy=True)
        return parsed.strftime("%Y-%m-%d")
    except:
        return None


def format_duration(iso_duration: str):
    return (
        iso_duration.replace("PT", "")
        .replace("H", "h ")
        .replace("M", "m")
        .strip()
    )


# =========================================================
# ROBUST IATA RESOLUTION
# =========================================================

def get_iata(city: str):

    if not city:
        return None

    key = city.lower().strip()

    manual_map = {
        "delhi": "DEL",
        "new delhi": "DEL",
        "ncr": "DEL",
        "bangalore": "BLR",
        "bengaluru": "BLR",
        "mumbai": "BOM",
        "kolkata": "CCU",
        "howrah": "CCU",
        "pune": "PNQ",
        "chennai": "MAA",
        "madras": "MAA",
        "hyderabad": "HYD",
        "goa": "GOI",
        "dubai": "DXB",
        "thane": "BOM"
    }

    if key in manual_map:
        return manual_map[key]

    try:
        resp = amadeus_client.reference_data.locations.get(
            keyword=city,
            subType="CITY,AIRPORT"
        )
        if resp.data:
            return resp.data[0]["iataCode"]
    except:
        pass

    if "," in city:
        tail = city.split(",")[-1].strip()
        try:
            resp = amadeus_client.reference_data.locations.get(
                keyword=tail,
                subType="CITY,AIRPORT"
            )
            if resp.data:
                return resp.data[0]["iataCode"]
        except:
            pass

    return None


# =========================================================
# FLIGHTS
# =========================================================

def fetch_flights(origin, destination, date, adults):
    try:
        response = amadeus_client.shopping.flight_offers_search.get(
            originLocationCode=origin,
            destinationLocationCode=destination,
            departureDate=date,
            adults=adults or 1,
            currencyCode="INR",
            max=5
        )

        flights = []

        for i, offer in enumerate(response.data[:5], 1):
            itinerary = offer["itineraries"][0]
            segment = itinerary["segments"][0]

            flights.append({
                "rank": i,
                "airline": segment["carrierCode"],
                "flight_no": f"{segment['carrierCode']} {segment['number']}",
                "departure": segment["departure"]["at"].split("T")[1][:5],
                "arrival": segment["arrival"]["at"].split("T")[1][:5],
                "duration": format_duration(itinerary["duration"]),
                "price": float(offer["price"]["total"])
            })

        return {
            "type": "structured",
            "category": "flights",
            "data": {
                "origin": origin,
                "destination": destination,
                "date": date,
                "flights": flights
            }
        }

    except Exception as e:
        return {"type": "error", "message": str(e)}


# =========================================================
# HOTELS
# =========================================================

def fetch_hotels(city, check_in=None, check_out=None, adults=1):

    city_code = get_iata(city)
    if not city_code:
        return {"type": "error", "message": "Unsupported city."}

    if not check_in or not check_out:
        tomorrow = datetime.today() + timedelta(days=1)
        check_in = tomorrow.strftime("%Y-%m-%d")
        check_out = (tomorrow + timedelta(days=1)).strftime("%Y-%m-%d")

    try:
        hotels_response = amadeus_client.reference_data.locations.hotels.by_city.get(
            cityCode=city_code
        )

        hotels = []

        for hotel in hotels_response.data[:10]:
            hotel_id = hotel["hotelId"]

            try:
                offer_response = amadeus_client.shopping.hotel_offers_search.get(
                    hotelIds=hotel_id,
                    checkInDate=check_in,
                    checkOutDate=check_out,
                    adults=adults or 1
                )

                if offer_response.data:
                    offer = offer_response.data[0]["offers"][0]
                    hotels.append({
                        "hotel_name": offer_response.data[0]["hotel"]["name"],
                        "price": float(offer["price"]["total"]),
                        "currency": offer["price"]["currency"]
                    })

            except:
                continue

        hotels = sorted(hotels, key=lambda x: x["price"], reverse=True)[:5]

        return {
            "type": "structured",
            "category": "hotels",
            "data": {
                "city": city,
                "hotels": hotels
            }
        }

    except:
        return {"type": "error", "message": "Hotel service unavailable in sandbox."}


# =========================================================
# PLACES (BULLET FORMAT)
# =========================================================

def fetch_places(query: str):
    results = tavily.invoke(query)

    combined_text = ""
    for r in results[:3]:
        combined_text += r.get("content", "") + "\n"

    summary = summarizer_llm.invoke(
        f"""
        Summarize into short bullet points.
        Do NOT write long paragraphs.
        Use sections if required.

        {combined_text}
        """
    )

    return {
        "type": "structured",
        "category": "places",
        "data": {
            "summary": summary.content
        }
    }


# =========================================================
# ITINERARY
# =========================================================

def generate_itinerary(prompt: str):
    response = planner_llm.invoke(
        f"Provide a concise travel plan in bullet points:\n{prompt}"
    )
    return {
        "type": "structured",
        "category": "itinerary",
        "data": {"content": response.content}
    }


# =========================================================
# ROUTER
# =========================================================

class ChatRequest(BaseModel):
    message: str


@app.post("/chat")
def chat(req: ChatRequest):

    intent = detect_intent(req.message)

    # FLIGHTS
    if intent == "flights":
        fq = flight_llm.invoke(req.message)
        date = normalize_date(fq.departure_date)

        origin = get_iata(fq.origin_city)
        destination = get_iata(fq.destination_city)

        if not origin or not destination:
            return {"type": "error", "message": "Unsupported city."}

        return fetch_flights(origin, destination, date, fq.adults)

    # HOTELS
    if intent == "hotels":
        hq = hotel_llm.invoke(req.message)
        check_in = normalize_date(hq.check_in)
        check_out = normalize_date(hq.check_out)
        return fetch_hotels(hq.city, check_in, check_out, hq.adults)

    # PLACES
    if intent == "places":
        return fetch_places(req.message)

    # ITINERARY
    if intent == "itinerary":
        return generate_itinerary(req.message)

    return {"type": "error", "message": "Unsupported request type."}

