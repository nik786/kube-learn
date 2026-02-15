# flight-backend/rag_store.py

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document


import os

VECTOR_DB_PATH = "./vector_db"

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

def build_vector_store():
    os.makedirs(VECTOR_DB_PATH, exist_ok=True)

    docs = [
        Document(
            page_content="Varanasi is best visited from October to March with pleasant weather.",
            metadata={"source": "travel-guide"}
        ),
        Document(
            page_content="Digha is ideal from October to February; summers are hot and humid.",
            metadata={"source": "travel-guide"}
        ),
        Document(
            page_content="Kolkata to Digha train journey typically takes 3.5 to 4.5 hours.",
            metadata={"source": "rail-info"}
        ),
        Document(
            page_content="Hotels near Varanasi ghats usually include breakfast but lunch and dinner are paid.",
            metadata={"source": "hotel-info"}
        ),
    ]

    vectordb = Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        persist_directory=VECTOR_DB_PATH
    )
    vectordb.persist()

    print("✅ Vector DB built")

def load_vector_store():
    return Chroma(
        persist_directory=VECTOR_DB_PATH,
        embedding_function=embeddings
    )

