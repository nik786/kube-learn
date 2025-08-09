import os
import sqlite3
from langchain.docstore.document import Document
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_community.utilities import SQLDatabase
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# ========== SETUP ==========

# Initialize LLM (Groq)
llm_groq = ChatGroq(model_name="llama3-70b-8192")

# ========== CREATE / LOAD VECTOR DB ==========
# Connect to SQLite DB
conn = sqlite3.connect('worldevents.db')
cur = conn.cursor()

# Fetch rows from DB (adjust column names if different)
cur.execute("SELECT [Name of Incident], [Type of Event], Impact, [Place Name] FROM world_events")
rows = cur.fetchall()

# Convert to LangChain Documents
docs = []
for row in rows:
    content = f"Incident: {row[0]}, Type: {row[1]}, Impact: {row[2]}"
    docs.append(Document(page_content=content))

# Create embeddings using HuggingFace (local, no API calls)
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Build Chroma vector store
vector_db = Chroma.from_documents(
    docs,
    embedding=embeddings,
    persist_directory="my_vectordb"
)

# ========== VECTOR DB QUERY CHAIN ==========
prompt_retrieval = ChatPromptTemplate.from_template(
    "Answer this question in detail: {question} from these documents {context} pulled from our database. "
    "Correct the names if needed. If possible, tell us how these events are connected. "
    "At the end, parse the original context as citations. Remove duplicates from citations."
)

chain_retrieval = (
    {
        "context": lambda x: vector_db.as_retriever().get_relevant_documents(x),
        "question": RunnablePassthrough()
    }
    | prompt_retrieval
    | llm_groq
    | StrOutputParser()
)

print(chain_retrieval.invoke("conflicts involving UK"))

# ========== SQL QUERY GENERATION CHAIN ==========
template_sql = """Based on the table schema below, write a SQL query that would answer the user's question:
{schema}

Question: {question}
Give ONLY the query without the prepending ```sql and no explanation around the code.
"""
prompt_sql = ChatPromptTemplate.from_template(template_sql)

# Connect to SQLite DB via LangChain utility
db = SQLDatabase.from_uri("sqlite:///worldevents.db")

# Helper functions
def get_schema(_):
    return db.get_table_info()

def run_query(query):
    return db.run(query)

sql_response = (
    RunnablePassthrough.assign(schema=get_schema)
    | prompt_sql
    | llm_groq.bind(stop=["\nSQLResult:"])
    | StrOutputParser()
)

print(sql_response.invoke({"question": "How many wars are involving India and China?"}))

