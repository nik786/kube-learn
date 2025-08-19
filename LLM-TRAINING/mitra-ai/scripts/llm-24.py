import os
import sys
import pysqlite3
from langchain_groq import ChatGroq
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.utilities import SQLDatabase

# --- Patch sqlite3 to use pysqlite3 (for FTS5 support) ---
sys.modules["sqlite3"] = pysqlite3

# ✅ Set Groq API key safely
os.environ["GROQ_API_KEY"] = os.getenv(
    "GROQ_API_KEY", ""
)

llm_groq = ChatGroq(model_name="llama3-70b-8192")

# --- Embeddings + Vector DB setup ---
embedding_model = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5",
    model_kwargs={"device": "cpu"},   # ✅ force CPU
    encode_kwargs={"normalize_embeddings": False},
)

# --- Chroma setup ---
persist_dir = "chroma_store"
try:
    vector_db = Chroma(
        persist_directory=persist_dir,
        embedding_function=embedding_model
    )
except Exception as e:
    print(f"Chroma init failed, wiping store: {e}")
    import shutil
    shutil.rmtree(persist_dir, ignore_errors=True)
    vector_db = Chroma(
        persist_directory=persist_dir,
        embedding_function=embedding_model
    )

# --- Retrieval QA chain ---
qa_prompt = ChatPromptTemplate.from_template(
    "Answer this question in detail: {question} from these documents {context} pulled from our database. "
    "Correct the names if needed. If possible, tell us how these events are connected. "
    "At the end print the original context as citations. Remove duplicates from citations."
)

qa_chain = (
    {"context": vector_db.as_retriever(), "question": RunnablePassthrough()}
    | qa_prompt
    | llm_groq
    | StrOutputParser()
)

print("🔎 Retrieval QA Output:")
print(qa_chain.invoke("conflicts involving UK"))

# --- SQLDatabase Section ---
db = SQLDatabase.from_uri("sqlite:///worldevents.db")

def get_schema(_=None):
    return db.get_table_info()

print("\n📑 Database Schema:")
print(get_schema())

# --- SQL generation chain ---
sql_prompt = ChatPromptTemplate.from_template(
    """Based on the table schema below, write a SQL query that would answer the user's question:
{schema}

Question: {question}
Give ONLY the query without ```sql and no explanation."""
)

sql_gen_chain = (
    RunnablePassthrough.assign(schema=get_schema)
    | sql_prompt
    | llm_groq.bind(stop=["\nSQLResult:"])
    | StrOutputParser()
)

# Example 1: wars involving India and China
sql_query = sql_gen_chain.invoke({"question": "How many wars are involving India and China?"})
print("\n📝 Generated SQL Query:")
print(sql_query)

print("\n📊 SQL Execution Result:")
print(db.run(sql_query))

# Example 2: political party creation in India
sql_query2 = sql_gen_chain.invoke({"question": "Give me the political party creation in India"})
print("\n📝 Generated SQL Query (Party creation):")
print(sql_query2)

print("\n📊 SQL Execution Result (Party creation):")
print(db.run(sql_query2))

