import os
import sqlite3 as sql
import pandas as pd
from langchain.docstore.document import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
import pysqlite3
import sys
sys.modules["sqlite3"] = pysqlite3





os.environ["CUDA_VISIBLE_DEVICES"] = ""  # force CPU

db_path = "worldevents.db"
conn = sql.connect(db_path)
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='world_events';")
table_exists = cursor.fetchone()

if not table_exists:
    df = pd.DataFrame([
        {"Name of Incident": "Flood in City A", "Type of Event": "Natural Disaster", "Impact": "Severe flooding", "Place Name": "City A"}
    ])
    df.to_sql("world_events", conn, index=False, if_exists="replace")
    print("Table 'world_events' created and data inserted.")
else:
    print("Database and table 'world_events' already exist.")

embedding_model = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5",
    model_kwargs={"device": "cpu"},
    encode_kwargs={"normalize_embeddings": False},
)

doc = []
cur = conn.cursor()
cur.execute("SELECT [Name of Incident],[Type of Event], Impact, [Place Name]  FROM world_events")
rows = cur.fetchall()


for row in rows:
    page = Document(page_content=row[0]+ ". Impact of the event:"+ row[2], metadata={' "Type of Event"': row[1], ' "Place Name"': row[3]})
    doc.append(page)

print(doc)
