
# 🌍 LangChain + SQLite + Chroma Semantic Search Engine

## 📘 Summary
- **Objective:**  
  This Python script connects an **SQLite database (`worldevents.db`)** containing global events to a **Chroma Vector Store** for semantic search using **HuggingFace embeddings** (`BAAI/bge-small-en-v1.5`).

- **Key Steps:**
  1. **Embedding Setup:**  
     Loads a HuggingFace model for sentence embeddings on CPU.  
  2. **Database Validation:**  
     Connects to `worldevents.db` and checks for the presence of the `world_events` table.  
     If absent, attempts to create it from a DataFrame (`df`).  
  3. **Data Retrieval:**  
     Fetches event details — `Name of Incident`, `Type of Event`, `Impact`, and `Place Name`.  
  4. **Document Conversion:**  
     Transforms each record into a **LangChain `Document`** object with content and metadata.  
  5. **Vector Store Creation:**  
     Embeds documents and stores them in a **Chroma** vector database.  
  6. **Semantic Querying:**  
     Performs similarity search (e.g., “conflicts involving UK”) and prints the top 6 matching results.  
  7. **Detailed Output:**  
     Displays each event’s description, type, and location for better readability.  

- **Output Highlights:**  
  - Confirmation of database/table readiness.  
  - Number of loaded and embedded documents.  
  - Search results based on semantic similarity.  
  - Readable event summaries with metadata.

---

## 🚀 Suggested Improvements

1. **Implement Persistent Storage for VectorDB**  
   - *Save the Chroma database to disk (via `persist_directory`) to avoid re-embedding data each time the script runs.*

2. **Add Configurable Query Interface**  
   - *Allow users to input custom queries dynamically instead of using a hardcoded string.*

3. **Enhance Error Logging & Recovery**  
   - *Integrate structured logging with `logging` module for better debugging and tracking of DB or embedding errors.*

4. **Normalize and Sanitize Text Before Embedding**  
   - *Preprocess text (e.g., lowercase, remove special characters) to ensure uniform embeddings and better retrieval accuracy.*

5. **Visualize or Export Search Results**  
   - *Output top search results in tabular format (e.g., Pandas DataFrame) or export them to a CSV/HTML report for analysis.*

---

## 🤖 Alternative Models / Approaches

1. **Model: `sentence-transformers/all-MiniLM-L6-v2`**  
   *A lighter and faster model with excellent semantic performance, suitable for low-resource or real-time applications.*

2. **Vector Store: `FAISS` by Facebook AI**  
   *Highly efficient for large-scale similarity search and optimized for CPU/GPU acceleration compared to Chroma.*

3. **Approach: LangChain Retriever Chain**  
   *Use a structured retriever pipeline that combines embeddings with metadata filtering and reranking for smarter context-aware results.*

---

**🧩 Developer’s Note:**  
This implementation demonstrates how to merge **traditional relational databases** with **modern vector-based retrieval** systems, enabling semantic search over structured data. With persistent storage, UI integration, and scalable embeddings, this project can evolve into a production-grade **knowledge search engine**.
