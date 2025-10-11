import os
from langchain_groq import ChatGroq
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.utilities import SQLDatabase


import sys
import sqlite3
import pysqlite3

# Patch: force Python to use pysqlite3
sys.modules["sqlite3"] = pysqlite3


# ✅ Set Groq API key safely
os.environ["GROQ_API_KEY"] = os.getenv(
    "GROQ_API_KEY", ""
)

llm_groq = ChatGroq(model_name="llama-3.3-70b-versatile")

# --- Embeddings + Vector DB setup ---
embedding_model = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5",
    model_kwargs={"device": "cpu"},   # ✅ force CPU
    encode_kwargs={"normalize_embeddings": False},
)

# Load or create a vector store
persist_dir = "chroma_store"
vector_db = Chroma(
    persist_directory=persist_dir,
    embedding_function=embedding_model
)

# --- Retrieval QA chain ---
prompt = ChatPromptTemplate.from_template(
    "Answer this question in detail: {question} from these documents {context} pulled from our database. "
    "Correct the names if needed. If possible, tell us how these events are connected. "
    "At the end print the original context as citations. Remove duplicates from citations."
)

chain = (
    {"context": vector_db.as_retriever(), "question": RunnablePassthrough()}
    | prompt
    | llm_groq
    | StrOutputParser()
)

print("🔎 Retrieval QA Output:")
print(chain.invoke("conflicts involving UK"))

# --- SQLDatabase Section ---
db = SQLDatabase.from_uri("sqlite:///worldevents.db")

def get_schema(_=None):   # ✅ accepts optional arg for Runnable compatibility
    return db.get_table_info()

def run_query(query):
    return db.run(query)

print("\n📑 Database Schema:")
print(get_schema())
