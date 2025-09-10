# 🛠️ Mimi – Kubernetes RAG Assistant

Mimi is a **Kubernetes-native chatbot** that combines live API queries with **RAG (Retrieval-Augmented Generation)** using ChromaDB.  
It can answer both **real-time cluster questions** (e.g., pod counts, CPU usage) and **FAQ-style queries** (e.g., error explanations).

---

## ✨ Features

- Connects to **Kubernetes API** (via Python client).  
- Stores structured cluster state (Pods, Deployments, Services, Events) in **ChromaDB**.  
- Uses **embeddings + LLM** to provide natural language answers.  
- **Hybrid approach**:
  - Direct API calls for real-time state.  
  - RAG retrieval for knowledge, docs, FAQs.  
- Extendable into a **Gradio/Streamlit chatbot UI**.  

---

## ⚙️ Setup

### 1. Install Dependencies
```bash
pip install kubernetes langchain chromadb sentence-transformers gradio


```
Configure Kube Access
from kubernetes import client, config

# Load config (works in local ~/.kube/config or in-cluster)
config.load_kube_config()
v1 = client.CoreV1Api()

🔹 Step 1: Fetch Data from Kubernetes
pods = v1.list_namespaced_pod(namespace="hr")
print("Pods in hr namespace:", len(pods.items))

# Convert structured objects to docs
docs = []
for pod in pods.items:
    doc = {
        "type": "Pod",
        "name": pod.metadata.name,
        "namespace": pod.metadata.namespace,
        "status": pod.status.phase,
    }
    docs.append(str(doc))

```


🔹 Step 2: Store in ChromaDB
```
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

vectorstore = Chroma(
    collection_name="k8s_data",
    embedding_function=embedding_model
)

vectorstore.add_texts(docs)
```


🔹 Step 3: Retriever + LLM

```
from langchain.chains import ConversationalRetrievalChain
from langchain_community.chat_models import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

qa_chain = ConversationalRetrievalChain.from_llm(llm, retriever)

```

🔹 Step 4: Hybrid Chat Logic
```
def mimi_chat(user_input, chat_history=[]):
    if "pods" in user_input and "namespace" in user_input:
        ns = user_input.split("namespace")[-1].strip()
        pods = v1.list_namespaced_pod(namespace=ns)
        return f"{len(pods.items)}"
    else:
        result = qa_chain({"question": user_input, "chat_history": chat_history})
        return result["answer"]
```

💬 Example Conversation
```
Mimi: Have a good day! I'm Mimi, your K8s assistant. How may I help you?  
User: Can you tell me how many pods are running in hr namespace?  
Mimi: 3  

```

🚀 Best Practices
```
Live Queries → For real-time metrics, always hit the K8s API.

RAG → For knowledge-based Q&A, use Chroma.

Background Sync → Update Chroma with cluster state every X minutes.

RBAC Controls → Prevent exposure of sensitive namespaces.

Scalability → For larger clusters, consider Pinecone or Weaviate instead of Chroma.

```


📊 System Flow (Mermaid Diagram)
flowchart TD
    User[User Query] --> Mimi[Mimi Chatbot]
    Mimi -->|Real-time Request| K8sAPI[Kubernetes API]
    Mimi -->|Knowledge Request| ChromaDB[ChromaDB + Embeddings]
    ChromaDB --> LLM[LLM (GPT/Claude/etc.)]
    K8sAPI --> Mimi
    LLM --> Mimi
    Mimi --> Response[Final Answer to User]

✅ Summary
```
Mimi = Hybrid chatbot for Kubernetes.

Combines real-time API queries + RAG-based answers.

Built with LangChain, ChromaDB, Kubernetes API.

Extendable to UI with Gradio/Streamlit.

Scales with Weaviate/Pinecone for enterprise clusters.

```

