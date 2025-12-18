import os
import requests
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


K8S_API_BASE = os.getenv("K8S_API_BASE")
PODS_API = f"{K8S_API_BASE}/api/v1/namespaces/default/pods"


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str


def get_pods_data():
    """Fetch pods from Kubernetes API"""
    resp = requests.get(PODS_API, timeout=5)
    resp.raise_for_status()
    return resp.json()["items"]


def extract_pod_facts(pods):
    """Convert raw K8s data into structured facts"""
    facts = []

    for pod in pods:
        name = pod["metadata"]["name"]
        phase = pod["status"]["phase"]
        containers = pod["spec"]["containers"]

        for c in containers:
            facts.append({
                "pod": name,
                "container": c["name"],
                "image": c["image"],
                "status": phase
            })

    return facts


def ask_llm(question: str, facts: list):
    system_prompt = (
        "You are Mimi, an expert Kubernetes assistant.\n"
        "You can answer questions in two ways:\n"
        "1. If the question requires live cluster data, use ONLY the provided cluster facts.\n"
        "2. If the question is conceptual or explanatory, answer from your Kubernetes knowledge.\n"
        "Be clear and concise. Do not hallucinate cluster state."
    )

    user_prompt = f"""
Live Kubernetes Cluster Facts (may be empty or irrelevant):
{facts}

User Question:
{question}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0.2,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )

    return response.choices[0].message.content.strip()


@app.post("/chat")
def chat(req: ChatRequest):
    pods = get_pods_data()
    facts = extract_pod_facts(pods)
    answer = ask_llm(req.message, facts)
    return {"reply": answer}


@app.get("/health")
def health():
    return {"status": "ok"}

