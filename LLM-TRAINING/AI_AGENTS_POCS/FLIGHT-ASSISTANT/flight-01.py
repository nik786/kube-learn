import os
import requests
import gradio as gr
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

API_BASE = "http://127.0.0.1:8001/api/v1/namespaces/default"
PODS_API = f"{API_BASE}/pods"


# ---------- Kubernetes helpers ----------

def get_pods():
    return requests.get(PODS_API).json()["items"]

def count_running_pods():
    return sum(1 for p in get_pods() if p["status"]["phase"] == "Running")

def get_pod_image(pod_name):
    for p in get_pods():
        if p["metadata"]["name"] == pod_name:
            return p["spec"]["containers"][0]["image"]
    return None

def get_running_pod_name():
    for p in get_pods():
        if p["status"]["phase"] == "Running":
            return p["metadata"]["name"]
    return None

def delete_pod(pod_name):
    r = requests.delete(f"{PODS_API}/{pod_name}")
    return r.status_code in (200, 202)

def create_pod(pod_name, image="nginx"):
    payload = {
        "apiVersion": "v1",
        "kind": "Pod",
        "metadata": {"name": pod_name},
        "spec": {
            "containers": [{
                "name": pod_name,
                "image": image
            }]
        }
    }
    r = requests.post(PODS_API, json=payload)
    return r.status_code in (200, 201)


# ---------- LLM intent parsing ----------

def parse_intent(user_input):
    prompt = f"""
You are a Kubernetes intent parser.
Return ONLY valid JSON.

Supported intents:
- COUNT_RUNNING_PODS
- GET_POD_IMAGE
- GET_RUNNING_POD_NAME
- DELETE_POD
- CREATE_POD

Input: "{user_input}"

Output format:
{{"intent": "...", "pod_name": "optional"}}
"""

    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return eval(resp.choices[0].message.content)


# ---------- Assistant router ----------

def assistant(user_input):
    intent_data = parse_intent(user_input)
    intent = intent_data["intent"]
    pod = intent_data.get("pod_name")

    if intent == "COUNT_RUNNING_PODS":
        return str(count_running_pods())

    if intent == "GET_POD_IMAGE":
        image = get_pod_image(pod)
        return image or "pod not found"

    if intent == "GET_RUNNING_POD_NAME":
        return get_running_pod_name() or "no running pod"

    if intent == "DELETE_POD":
        return "stopped" if delete_pod(pod) else "failed"

    if intent == "CREATE_POD":
        return "started" if create_pod(pod) else "failed"

    return "unsupported request"


# ---------- Gradio UI ----------

ui = gr.Interface(
    fn=assistant,
    inputs=gr.Textbox(label="Ask Kubernetes"),
    outputs=gr.Textbox(label="Answer"),
    title="🧠 Kubernetes Virtual Assistant",
    description="Ask questions in natural language"
)

if __name__ == "__main__":
    ui.launch()

