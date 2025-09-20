
import chromadb
import pysqlite3
import os
import sys

# Override sqlite3 globally so Chroma uses FTS5-enabled version
sys.modules["sqlite3"] = pysqlite3
import sqlite3 as sql  



# Initialize client
chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="auth_testing2")

# Document 1: Public financial summary (auth_level 1)
collection.add(
    documents=["This is a public summary of the financial performance in Q1. Overall, the company has shown..."],
    metadatas=[{"auth_level": 1, "category": "Summary", "quarter": "Q1", "year": "2024", "department": "sales/GCC"}],
    ids=["id1"]
)

# Document 2: Internal financial analysis (auth_level 2)
collection.add(
    documents=["Internal analysis reveals that the Q1 performance, while positive, indicates potential risks..."],
    metadatas=[{"auth_level": 2, "category": "Internal Analysis", "quarter": "Q1", "year": "2024"}],
    ids=["id2"]
)

# Document 3: Confidential investment strategy (auth_level 3)
collection.add(
    documents=["Confidential: The investment strategy for Q2 involves focusing on emerging markets..."],
    metadatas=[{"auth_level": 3, "category": "Investment Strategy", "source": "mywebsite.com", "quarter": "Q2", "year": "2024"}],
    ids=["id3"]
)


def vector_search_with_rbac(query_text, user_auth_level):
    """
    Run a vector search with Role-Based Access Control (RBAC).
    Users can only see documents at their exact auth_level.
    """
    if not isinstance(user_auth_level, int) or user_auth_level < 0:
        raise ValueError("Invalid user_auth_level. Must be a non-negative integer.")

    try:
        results = collection.query(
            query_texts=[query_text],
            n_results=10,
            where={"auth_level": user_auth_level}
        )
        return results.get("documents", [])
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


# Example queries
print(vector_search_with_rbac("Tell me about the performance for this quarter", 1))
print(vector_search_with_rbac("Tell me about the performance for this quarter", 2))
print(vector_search_with_rbac("Tell me about the performance for this quarter", 3))

