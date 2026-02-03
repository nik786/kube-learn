import os
import operator
from typing import TypedDict, Annotated, Sequence, Literal

from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv

from amadeus import Client, ResponseError
from fastapi.middleware.cors import CORSMiddleware

from langchain_openai import ChatOpenAI
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from langchain.tools import tool
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode

from langchain_community.tools.tavily_search import TavilySearchResults

from rag_store import load_vector_store

# ----------------------------
# ENV
# ----------------------------

load_dotenv()

# ----------------------------
# FastAPI App
# ----------------------------

app = FastAPI(title="Flight Travel Assistant")


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",   # Frontend
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ----------------------------
# LLM
# ----------------------------

llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0)

# ----------------------------
# Amadeus Client
# ----------------------------

amadeus_client = Client(
    client_id=os.environ["AMADEUS_CLIENT_ID"],
    client_secret=os.environ["AMADEUS_CLIENT_SECRET"],
    hostname="test"
)

# ----------------------------
# Vector DB (RAG)
# ----------------------------

vectordb = load_vector_store()
retriever = vectordb.as_retriever(search_kwargs={"k": 3})






# ----------------------------
# Formatting Helpers
# ----------------------------

def format_duration(iso_duration: str) -> str:
    # PT2H30M → 2h30m
    return (
        iso_duration.replace("PT", "")
        .replace("H", "h")
        .replace("M", "m")
    )


def build_flight_table(origin, destination, date, flights):
    header = f"""
Here are some flight options from {origin} to {destination} on {date}:

Flight   F_No       Source     Destination   Duration   Route             Price
--------------------------------------------------------------------------------
"""
    rows = []

    for f in flights:
        rows.append(
            f"{f['airline']:<8}"
            f"{f['flight_no']:<11}"
            f"{origin.upper():<11}"
            f"{destination.upper():<14}"
            f"{f['duration']:<11}"
            f"{f['route']:<18}"
            f"₹{int(f['price']):,}"
        )

    return header + "\n".join(rows)




@tool
def knowledge_search_tool(query: str):
    """
    Search internal knowledge base using embeddings (RAG).
    """
    docs = retriever.get_relevant_documents(query)
    if not docs:
        return "No relevant knowledge found."
    return "\n".join([d.page_content for d in docs])

# ----------------------------
# Tavily Tool
# ----------------------------

tavily_tool = TavilySearchResults(max_results=3)

# ----------------------------
# Flight Tool
# ----------------------------

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
    Returns structured flight data for formatting.
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
            return {"flights": []}

        flights = []

        for offer in response.data[:5]:
            itinerary = offer["itineraries"][0]
            segments = itinerary["segments"]

            airline = segments[0]["carrierCode"]
            flight_no = f"{segments[0]['carrierCode']}-{segments[0]['number']}"
            duration = format_duration(itinerary["duration"])
            price = float(offer["price"]["total"])

            if len(segments) == 1:
                route = "Non-stop"
            else:
                route = f"Via {segments[0]['arrival']['iataCode']}"

            flights.append({
                "airline": airline,
                "flight_no": flight_no,
                "duration": duration,
                "route": route,
                "price": price,
            })

        return {
            "origin": origin_code,
            "destination": destination_code,
            "date": departure_date,
            "flights": flights
        }

    except ResponseError as e:
        return {"error": f"Flight API error: {str(e)}"}

# ----------------------------
# LangGraph Agent
# ----------------------------

TOOLS = [
    search_flights_tool,
    tavily_tool,
    knowledge_search_tool
]

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
    graph.add_conditional_edges("agent", should_continue, {"action": "action", END: END})
    graph.add_edge("action", "agent")

    return graph.compile()

agent = build_graph()

# ----------------------------
# API Schema
# ----------------------------

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    answer: str

# ----------------------------
# API Endpoint
# ----------------------------


@app.post("/chat")
def chat(req: ChatRequest):
    state = {
        "messages": [HumanMessage(content=req.message)]
    }

    final_state = agent.invoke(state)

    answer = ""
    flight_payload = None

    for msg in final_state["messages"]:
        if isinstance(msg, AIMessage):
            answer = msg.content

        if hasattr(msg, "content") and isinstance(msg.content, dict):
            if "flights" in msg.content:
                flight_payload = msg.content

    # Return structured flights payload
    if flight_payload and flight_payload.get("flights"):
        return {
            "type": "flights",
            "origin": "Kolkata",
            "destination": "Pune",
            "date": "1 March 2026",
            "flights": flight_payload["flights"]
        }

    return {
        "type": "text",
        "answer": answer
    }

