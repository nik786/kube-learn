# llm-23-fixed.py (snippet / replacement)
import os, sys
from langchain_groq import ChatGroq
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.utilities import SQLDatabase
import pysqlite3

# Patch sqlite as before
sys.modules["sqlite3"] = pysqlite3

# --- secure API key handling (no hardcoded key) ---
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise SystemExit("GROQ_API_KEY not set. Export it in your shell (export GROQ_API_KEY=...) before running.")

os.environ["GROQ_API_KEY"] = GROQ_API_KEY

# --- model choices ---
preferred_model = "llama-3.3-70b-versatile"   # recommended migration target per Groq docs
fallback_models = [
    "llama3-8b-8192",         # smaller / cheaper Groq Llama3 model
    "mixtral-8x7b-32768",     # alternate supported model family
]

def build_chain_for_model(model_name, vector_db, prompt):
    llm = ChatGroq(model_name=model_name)
    chain = (
        {"context": vector_db.as_retriever(), "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    return chain

# --- embeddings + vector DB (your existing setup) ---
embedding_model = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5",
    model_kwargs={"device": "cpu"},
    encode_kwargs={"normalize_embeddings": False},
)
persist_dir = "chroma_store"
vector_db = Chroma(persist_directory=persist_dir, embedding_function=embedding_model)

# --- prompt ---
prompt = ChatPromptTemplate.from_template(
    "Answer this question in detail: {question} from these documents {context} pulled from our database. "
    "Correct the names if needed. If possible, tell us how these events are connected. "
    "At the end print the original context as citations. Remove duplicates from citations."
)

# --- try preferred model, fallback if Groq reports decommission ---
def ask_with_fallback(query):
    # try preferred
    try:
        chain = build_chain_for_model(preferred_model, vector_db, prompt)
        return chain.invoke(query)
    except Exception as e:
        err = str(e)
        print("Primary model failed:", err)
        # quick heuristic: if server says 'decommission' or 'decommissioned' -> try fallbacks
        if "decommission" in err.lower() or "decommissioned" in err.lower():
            for m in fallback_models:
                try:
                    print(f"Retrying with fallback model {m}...")
                    chain = build_chain_for_model(m, vector_db, prompt)
                    return chain.invoke(query)
                except Exception as e2:
                    print(f"Fallback {m} failed: {e2}")
        # re-raise if nothing worked
        raise

if __name__ == "__main__":
    print("🔎 Retrieval QA Output:")
    out = ask_with_fallback("conflicts involving UK")
    print(out)
