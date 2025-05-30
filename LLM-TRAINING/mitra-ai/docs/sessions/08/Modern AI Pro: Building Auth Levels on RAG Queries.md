
## Modern AI Pro: Building Auth Levels on RAG Queries.
   How do you ensure that different users get different results based on their auth level?


```

!pip install -q chromadb
import chromadb
chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="auth_testing2")

```

## We will use 3 levels of role authorisation and build a sample DB with different types of content.

```

# Document 1: Public financial summary (auth_level 1)
collection.add(documents=["This is a public summary of the financial performance in Q1. Overall, the company has shown..."],
               metadatas =[{"auth_level": 1, "category": "Summary", "quarter": "Q1", "year": "2024", "department": "sales/GCC"}],
               ids="id1")

# Document 2: Internal financial analysis (auth_level 2)
collection.add(documents=["Internal analysis reveals that the Q1 performance, while positive, indicates potential risks..."],
               metadatas =[{"auth_level": 2, "category": "Internal Analysis", "quarter": "Q1", "year": "2024"}],
               ids="id2")

# Document 3: Confidential investment strategy (auth_level 3)
collection.add(documents=["Confidential: The investment strategy for Q2 involves focusing on emerging markets..."],
               metadatas =[{"auth_level": 3, "category": "Investment Strategy",  "source": "mywebsite.com", "quarter": "Q2", "year": "2024"}],
               ids="id3")

```

## Query with auth levels

```

def vector_search_with_rbac(query_text, user_auth_level):
    if not isinstance(user_auth_level, int) or user_auth_level < 0:
        raise ValueError("Invalid user_auth_level. Must be a non-negative integer.")

    try:
        results = collection.query(query_texts=[query_text],n_results=10, where={"auth_level": user_auth_level})
        return results
    except Exception as e:
        # Handle or log the error appropriately
        print(f"An error occurred: {e}")
        return []

```

```

vector_search_with_rbac("Tell me about the performance for this quarter",1)


vector_search_with_rbac("Tell me about the performance for this quarter",2)


vector_search_with_rbac("Tell me about the performance for this quarter",3)



```








