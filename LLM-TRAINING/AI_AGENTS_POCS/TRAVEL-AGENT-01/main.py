import os
import operator
from typing import TypedDict, Annotated, Sequence, Literal
from datetime import datetime

from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

from amadeus import Client, ResponseError

from langchain_openai import ChatOpenAI
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from langchain.tools import tool
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode
from langchain_community.tools.tavily_search import TavilySearchResults

from rag_store import load_vector_store

import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)





# =========================================================
# ENV
# =========================================================

load_dotenv()

AMADEUS_CLIENT_ID = os.getenv("AMADEUS_CLIENT_ID")
AMADEUS_CLIENT_SECRET = os.getenv("AMADEUS_CLIENT_SECRET")

if not AMADEUS_CLIENT_ID or not AMADEUS_CLIENT_SECRET:
    raise ValueError("Amadeus credentials are missing in environment variables.")


# =========================================================
# FastAPI App
# =========================================================

app = FastAPI(title="TravelGeek AI Assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================================================
# LLM
# =========================================================

llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0
)


# =========================================================
# Amadeus Client
# =========================================================

amadeus_client = Client(
    client_id=AMADEUS_CLIENT_ID,
    client_secret=AMADEUS_CLIENT_SECRET,
    hostname="test"  # change to "production" when live
)


# =========================================================
# Vector DB (RAG)
# =========================================================

vectordb = load_vector_store()
retriever = vectordb.as_retriever(search_kwargs={"k": 3})


# =========================================================
# Helpers
# =========================================================

def format_duration(iso_duration: str) -> str:
    return (
        iso_duration.replace("PT", "")
        .replace("H", "h")
        .replace("M", "m")
    )


def format_time(iso_string: str) -> str:
    dt = datetime.fromisoformat(iso_string.replace("Z", ""))
    return dt.strftime("%I:%M %p")


# =========================================================
# TOOLS
# =========================================================

@tool
def knowledge_search_tool(query: str):
    """Search internal travel knowledge base."""
    try:
        docs = retriever.invoke(query)
        if not docs:
            return "No relevant knowledge found."
        return "\n".join([d.page_content for d in docs])
    except Exception as e:
        return f"Knowledge search error: {str(e)}"


@tool
def search_flights_tool(
    origin_code: str,
    destination_code: str,
    departure_date: str,
    adults: int = 1,
    currency: str = "INR",
):
    """
    Search flights using Amadeus API.
    Returns fully structured data including booking link.
    """
    try:
        params = {
            "originLocationCode": origin_code,
            "destinationLocationCode": destination_code,
            "departureDate": departure_date,
            "adults": adults,
            "currencyCode": currency,
            "max": 5,
        }

        response = amadeus_client.shopping.flight_offers_search.get(**params)

        if not response.data:
            return {
                "category": "flights",
                "data": {
                    "origin": origin_code,
                    "destination": destination_code,
                    "date": departure_date,
                    "flights": [],
                },
            }

        flights = []

        for index, offer in enumerate(response.data[:5], start=1):
            itinerary = offer["itineraries"][0]
            segments = itinerary["segments"]
            segment = segments[0]

            departure_time = segment["departure"]["at"].split("T")[1][:5]
            arrival_time = segment["arrival"]["at"].split("T")[1][:5]

            airline = segment["carrierCode"]
            flight_no = f"{segment['carrierCode']} {segment['number']}"
            duration = format_duration(itinerary["duration"])
            price = float(offer["price"]["total"])

            booking_link = offer.get("self", "https://www.google.com/flights")

            flights.append({
                "rank": index,
                "airline": airline,
                "flight_no": flight_no,
                "departure_time": departure_time,
                "arrival_time": arrival_time,
                "duration": duration,
                "price": int(price),
                "booking_link": booking_link,
            })

        return {
            "category": "flights",
            "data": {
                "origin": origin_code,
                "destination": destination_code,
                "date": departure_date,
                "flights": flights,
            },
        }

    except ResponseError as e:
        return {"error": f"Flight API error: {str(e)}"}


# Tavily search
tavily_tool = TavilySearchResults(max_results=3)


TOOLS = [
    search_flights_tool,
    tavily_tool,
    knowledge_search_tool,
]


# =========================================================
# LangGraph Agent
# =========================================================

class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]


def call_model(state: AgentState):
    model = llm.bind_tools(TOOLS)
    response = model.invoke(state["messages"])
    return {"messages": [response]}


def should_continue(state: AgentState) -> Literal["action", "__end__"]:
    last = state["messages"][-1]
    if isinstance(last, AIMessage) and getattr(last, "tool_calls", None):
        return "action"
    return END


def build_graph():
    tool_node = ToolNode(TOOLS)

    graph = StateGraph(AgentState)
    graph.add_node("agent", call_model)
    graph.add_node("action", tool_node)

    graph.set_entry_point("agent")
    graph.add_conditional_edges(
        "agent",
        should_continue,
        {"action": "action", END: END},
    )

    graph.add_edge("action", "agent")

    return graph.compile()


agent = build_graph()


# =========================================================
# API Schema
# =========================================================

class ChatRequest(BaseModel):
    message: str


# =========================================================
# API Endpoint
# =========================================================


@app.post("/chat")
def chat(req: ChatRequest):

    print("\n========= NEW REQUEST =========")
    print("Incoming message:", req.message)

    state = {
        "messages": [HumanMessage(content=req.message)]
    }

    final_state = agent.invoke(state)

    text_answer = ""
    structured_payload = None

    for msg in final_state["messages"]:

        if isinstance(msg, AIMessage) and isinstance(msg.content, str):
            text_answer = msg.content

        if isinstance(msg.content, dict):
            structured_payload = msg.content

    if structured_payload and structured_payload.get("category"):
        response = {
            "type": "structured",
            "category": structured_payload.get("category"),
            "data": structured_payload.get("data"),
        }

        print("\n=== STRUCTURED RESPONSE ===")
        print(json.dumps(response, indent=2))
        return response

    response = {
        "type": "text",
        "answer": text_answer or "I'm here to help with your travel plans."
    }

    print("\n=== TEXT RESPONSE ===")
    print(json.dumps(response, indent=2))

    return response

