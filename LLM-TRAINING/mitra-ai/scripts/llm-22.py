import os
import sys
import pandas as pd
import pysqlite3

# Override sqlite3 globally so Chroma uses FTS5-enabled version
sys.modules["sqlite3"] = pysqlite3
import sqlite3 as sql  

from langchain.docstore.document import Document
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings

os.environ["CUDA_VISIBLE_DEVICES"] = ""  # force CPU

db_path = "worldevents.db"
conn = sql.connect(db_path)
cursor = conn.cursor()

# ✅ Use a lightweight, free embedding model
embedding_model = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

# Fetch rows from your DB
cursor.execute('SELECT "Name of Incident","Type of Event", Impact, "Place Name" FROM world_events;')
rows = cursor.fetchall()

# Build docs
docs = []
for row in rows:
    incident, event_type, impact, place = (str(r) if r else "" for r in row)
    docs.append(Document(
        page_content=f"{incident}. Impact of the event: {impact}",
        metadata={"Type of Event": event_type, "Place Name": place}
    ))

# Create / load Chroma vectorstore
persist_dir = "chroma_db"
try:
    vector_db = Chroma.from_documents(docs, embedding_model, persist_directory=persist_dir, collection_name="world_events")
    vector_db.persist()  # save DB
    print("Chroma DB created/updated successfully.")
except Exception as error:
    print("An exception occurred while creating Chroma:", type(error).__name__, error)
    # if already exists, load instead
    vector_db = Chroma(persist_directory=persist_dir, embedding_function=embedding_model, collection_name="world_events")

# Query
query = "conflicts involving UK"
results = vector_db.similarity_search(query, k=6)

# Print results
for doc in results:
    print(f"Event: {doc.page_content}")
    print(f"Place: {doc.metadata.get('Place Name', '')}")
    print(f"Type of Event: {doc.metadata.get('Type of Event', '')}\n")
