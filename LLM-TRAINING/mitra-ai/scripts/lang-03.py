import sqlite3
from langchain.docstore.document import Document
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# Load embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5",
    model_kwargs={'device': 'cpu'},
    encode_kwargs={'normalize_embeddings': False}
)

# Connect to SQLite DB
conn = sqlite3.connect('worldevents.db')
cur = conn.cursor()

# Check if the table exists
cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='world_events';")
table_exists = cur.fetchone()

# If table doesn't exist, create it from a DataFrame (assuming df is defined elsewhere)
if not table_exists:
    try:
        df.to_sql('world_events', conn, index=False)
        print("Table 'world_events' created and data inserted.")
    except NameError:
        print("DataFrame 'df' is not defined. Cannot create table.")
        exit(1)
else:
    print("Database and table 'world_events' already exist.")

# Fetch rows from DB
cur.execute("SELECT [Name of Incident], [Type of Event], Impact, [Place Name] FROM world_events")
rows = cur.fetchall()

# Convert rows to LangChain Document objects
docs = []
for row in rows:
    content = f"{row[0]}. Impact of the event: {row[2]}"
    metadata = {"Type of Event": row[1], "Place Name": row[3]}
    docs.append(Document(page_content=content, metadata=metadata))

print("Loaded documents:", len(docs))

# Create vector DB
try:
    vector_db = Chroma.from_documents(docs, embedding_model)
    print("Vector database created.")
except Exception as error:
    print("An exception occurred while creating vector DB:", type(error).__name__)
    exit(1)

# Perform similarity search
query = "conflicts involving UK"
try:
    results = vector_db.similarity_search(query, k=6)
    print("Search results:")
    for doc in results:
        print(doc)
except Exception as e:
    print("Error during similarity search:", type(e).__name__)

# Print document details

for doc in docs:
    # Extracting page_content and metadata for readability
    page_content = doc.page_content
    place_name = doc.metadata.get("Place Name", "Unknown")
    type_of_event = doc.metadata.get("Type of Event", "Unknown")

    # Formatting the output
    print(f"Event: {page_content}")
    print(f"Place: {place_name}")
    print(f"Type of Event: {type_of_event}\n")
