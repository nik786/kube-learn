import os
import sys
import time
import threading
import requests
import gradio as gr
import pysqlite3

from openai import OpenAI
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain.docstore.document import Document

# -------------------------------------------------
# SQLite fix for Chroma
# -------------------------------------------------
sys.modules["sqlite3"] = pysqlite3

# -------------------------------------------------
# Environment
# -------------------------------------------------
os.environ["CUDA_VISIBLE_DEVICES"] = ""

# -------------------------------------------------
# OpenAI client
# -------------------------------------------------
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# -------------------------------------------------
# Embedding model
# -------------------------------------------------
embedding_model = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# -------------------------------------------------
# Chroma persistence
# -------------------------------------------------
persist_dir = "./chroma_db"


def chroma_exists(path: str) -> bool:
    return os.path.exists(path) and bool(os.listdir(path))


collection = Chroma(
    collection_name="k8s_docs",
    embedding_function=embedding_model,
    persist_directory=persist_dir
)

# -------------------------------------------------
# Kubernetes API
# kubectl proxy --port=8001
# -------------------------------------------------
K8S_API = "http://127.0.0.1:8001/api/v1/namespaces/default/pods"


def get_pods():
    r = requests.get(K8S_API, timeout=5)
    r.raise_for_status()
    return r.json().get("items", [])


def delete_pod(pod_name):
    r = requests.delete(f"{K8S_API}/{pod_name}")
    return r.status_code in (200, 202)


def create_pod(pod_name, image="nginx:latest"):
    payload = {
        "apiVersion": "v1",
        "kind": "Pod",
        "metadata": {"name": pod_name},
        "spec": {
            "containers": [
                {"name": pod_name, "image": image}
            ]
        }
    }
    r = requests.post(K8S_API, json=payload)
    return r.status_code in (200, 201)


# -------------------------------------------------
# Initial index (ONLY if DB does not exist)
# -------------------------------------------------
def initial_index_if_needed():
    if chroma_exists(persist_dir):
        print("📦 Existing Chroma DB found. Reusing it.")
        return

    print("🆕 No Chroma DB found. Creating initial index...")
    docs = []
    ids = []

    for pod in get_pods():
        name = pod["metadata"]["name"]
        uid = pod["metadata"]["uid"]
        phase = pod["status"].get("phase", "Unknown")

        for idx, c in enumerate(pod["spec"]["containers"]):
            image = c["image"]
            doc_id = f"{uid}-{idx}"

            ids.append(doc_id)
            docs.append(
                Document(
                    page_content=(
                        f"Pod {name} is in namespace default, "
                        f"state {phase}, using image {image}"
                    )
                )
            )

    if docs:
        collection.add_documents(docs, ids=ids)
        print(f"✅ Initial index created with {len(docs)} records")


# -------------------------------------------------
# Auto-refresh (UPSERT, NOT DELETE)
# -------------------------------------------------
def refresh_chroma_index(interval=30):
    while True:
        try:
            print("🔄 Refreshing Chroma index...")

            docs = []
            ids = []

            for pod in get_pods():
                name = pod["metadata"]["name"]
                uid = pod["metadata"]["uid"]
                phase = pod["status"].get("phase", "Unknown")

                for idx, c in enumerate(pod["spec"]["containers"]):
                    image = c["image"]
                    doc_id = f"{uid}-{idx}"

                    ids.append(doc_id)
                    docs.append(
                        Document(
                            page_content=(
                                f"Pod {name} is in namespace default, "
                                f"state {phase}, using image {image}"
                            )
                        )
                    )

            if docs:
                # add_documents acts as UPSERT when IDs are reused
                collection.add_documents(documents=docs, ids=ids)

            print(f"✅ Indexed/Updated {len(docs)} pod records")

        except Exception as e:
            print(f"❌ Refresh failed: {e}")

        time.sleep(interval)


# -------------------------------------------------
# RAG Streaming Assistant
# -------------------------------------------------
def assistant(user_input):
    try:
        results = collection.similarity_search(user_input, k=3)
        context = " ".join(r.page_content for r in results)

        system_prompt = f"""
You are a Kubernetes assistant.

Context:
{context}

If the user asks to stop a pod, reply exactly:
stop:<pod-name>

If the user asks to start a pod, reply exactly:
start:<pod-name>

Otherwise, answer normally.
"""

        stream = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ],
            temperature=0.0,
            stream=True,
        )

        full_response = ""

        for chunk in stream:
            delta = chunk.choices[0].delta
            if delta and delta.content:
                full_response += delta.content
                yield full_response

        answer = full_response.strip()

        if answer.startswith("stop:"):
            pod = answer.split(":", 1)[1].strip()
            yield "🛑 Pod stopped" if delete_pod(pod) else "❌ Failed to stop pod"

        elif answer.startswith("start:"):
            pod = answer.split(":", 1)[1].strip()
            yield "▶️ Pod started" if create_pod(pod) else "❌ Failed to start pod"

    except Exception as e:
        yield f"❌ Error: {e}"


# -------------------------------------------------
# Gradio UI
# -------------------------------------------------
ui = gr.Interface(
    fn=assistant,
    inputs=gr.Textbox(
        lines=2,
        placeholder="Ask about Kubernetes pods...",
        label="Your Question"
    ),
    outputs=gr.Markdown(
        label="K8s Assistant (Streaming)"
    ),
    title="🚀 Kubernetes Virtual Assistant",
    description="RAG-based assistant with auto-refreshing live Kubernetes context",
    allow_flagging="never",
)


# -------------------------------------------------
# Main
# -------------------------------------------------
if __name__ == "__main__":
    initial_index_if_needed()

    threading.Thread(
        target=refresh_chroma_index,
        daemon=True
    ).start()

    ui.launch()

