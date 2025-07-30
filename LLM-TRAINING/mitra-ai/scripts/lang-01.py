import sqlite3
from langchain.docstore.document import Document
from langchain_community.vectorstores import Chroma



# Connect to SQLite DB
conn = sqlite3.connect('worldevents.db')
cur = conn.cursor()


# Fetch rows from DB
cur.execute("SELECT [Name of Incident], [Type of Event], Impact, [Place Name] FROM world_events")
rows = cur.fetchall()

doc = []

cur = conn.cursor()
cur.execute("SELECT [Name of Incident],[Type of Event], Impact, [Place Name]  FROM world_events")
rows = cur.fetchall()


for row in rows:
    page = Document(page_content=row[0]+ ". Impact of the event:"+ row[2], metadata={' "Type of Event"': row[1], ' "Place Name"': row[3]})
    doc.append(page)

print(doc)

