import sqlite3
from langchain.docstore.document import Document
from langchain_community.vectorstores import Chroma


from langchain_community.embeddings import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5",
    model_kwargs={'device': 'cpu'},
    encode_kwargs={'normalize_embeddings': False}
)



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



try:
  vector_db = Chroma.from_documents(doc, embedding_model)
except Exception as error:
    print("An exception occurred:", type(error).__name__)


query = "conflicts involving UK"
docs = vector_db.similarity_search(query, k=6)
print(docs)



