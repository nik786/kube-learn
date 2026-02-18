# travel-backend/rag_store.py

import os
from typing import List

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

VECTOR_DB_PATH = "./vector_db"

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

def _seed_documents() -> List[Document]:
    """
    Base travel knowledge documents.
    You can later replace this with file loaders.
    """
    return [
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


def build_vector_store():
    """
    Build vector DB with chunking and persistence.
    """
    os.makedirs(VECTOR_DB_PATH, exist_ok=True)

    raw_docs = _seed_documents()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(raw_docs)

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=VECTOR_DB_PATH
    )

    vectordb.persist()
    print("✅ Vector DB built with chunking.")


def load_vector_store():
    """
    Load existing DB.
    If missing, build automatically.
    """
    if not os.path.exists(VECTOR_DB_PATH) or not os.listdir(VECTOR_DB_PATH):
        print("⚠️ Vector DB not found. Building new one...")
        build_vector_store()

    return Chroma(
        persist_directory=VECTOR_DB_PATH,
        embedding_function=embeddings
    )

