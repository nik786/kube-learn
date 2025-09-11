__import__("pysqlite3")
import sys
sys.modules["sqlite3"] = sys.modules.pop("pysqlite3")

import sqlite3
import shutil, os

from langchain.docstore.document import Document
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings   # ✅ updated import
from langchain_groq import ChatGroq
from langchain_community.utilities import SQLDatabase
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


# ========== SETUP ==========
# Preferred + fallback models
preferred_model = "llama-3.3-70b-versatile"
fallback_models = ["llama-3.1-8b-instant", "mixtral-8x7b-32768"]

def get_llm(model_name):
    return ChatGroq(model_name=model_name)

# ========== CREATE / LOAD VECTOR DB ==========
# Connect to SQLite DB
conn = sqlite3.connect("worldevents.db")
cur = conn.cursor()

# Fetch rows from DB (adjust column names if different)
cur.execute("SELECT [Name of Incident], [Type of Event], Impact, [Place Name] FROM world_events")
rows = cur.fetchall()

# Convert to LangChain Documents
docs = [
    Document(page_content=f"Incident: {row[0]}, Type: {row[1]}, Impact: {row[2]}")
    for row in rows
]

# Create embeddings (local, lightweight)
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Build Chroma vector store
persist_dir = "my_vectordb"
if os.path.exists(persist_dir):
    shutil.rmtree(persist_dir)  # ⚠️ clears old store on every run

vector_db = Chroma.from_documents(
    docs,
    embedding=embeddings,
    persist_directory=persist_dir
)


# ========== VECTOR DB QUERY CHAIN ==========
prompt_retrieval = ChatPromptTemplate.from_template(
    "Answer this question in detail: {question} from these documents {context} pulled from our database. "
    "Correct the names if needed. If possible, tell us how these events are connected. "
    "At the end, parse the original context as citations. Remove duplicates from citations."
)

def build_chain(model_name):
    llm = get_llm(model_name)
    return (
        {
            "context": lambda x: vector_db.as_retriever().get_relevant_documents(x),
            "question": RunnablePassthrough(),
        }
        | prompt_retrieval
        | llm
        | StrOutputParser()
    )

def ask_with_fallback(query):
    try:
        return build_chain(preferred_model).invoke(query)
    except Exception as e:
        print(f"⚠️ Primary model {preferred_model} failed: {e}")
        for m in fallback_models:
            try:
                print(f"🔄 Retrying with fallback {m}...")
                return build_chain(m).invoke(query)
            except Exception as e2:
                print(f"❌ Fallback {m} failed: {e2}")
        raise RuntimeError("All models failed.")

print("🔎 Retrieval QA Output:")
print(ask_with_fallback("conflicts involving UK"))


# ========== SQL QUERY GENERATION & EXECUTION ==========
template_sql = """Based on the table schema below, write a SQL query that would answer the user's question:
{schema}

Question: {question}
Give ONLY the query without the prepending ```sql and no explanation around the code.
"""
prompt_sql = ChatPromptTemplate.from_template(template_sql)

# Connect to SQLite DB via LangChain utility
db = SQLDatabase.from_uri("sqlite:///worldevents.db")

def get_schema(_):
    return db.get_table_info()

def run_query(query):
    return db.run(query)

sql_chain = (
    RunnablePassthrough.assign(schema=get_schema)
    | prompt_sql
    | get_llm(preferred_model).bind(stop=["\nSQLResult:"])
    | StrOutputParser()
)

# Example 1: Political party creation in India
query1 = sql_chain.invoke({"question": "Give me the political party creation in India"})
print("Generated Query:", query1)
print("Results:", run_query(query1))

# Example 2: Battles in India between 1500 and 1800
query2 = sql_chain.invoke({
    "question": (
        "Give me the name and year of battles (use synonyms such as military and "
        "military battle) that happened in India between 1500 and 1800."
    )
})
print("Generated Query:", query2)
print("Results:", run_query(query2))
