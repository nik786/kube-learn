# 🌍 SQLite + SentenceTransformer + Chroma Semantic Search Pipeline

## 📘 Summary
- **Objective:**  
  This script integrates an **SQLite world events database (`worldevents.db`)** with a **Chroma vector store** to enable semantic similarity search using the **SentenceTransformer model (`all-MiniLM-L6-v2`)**.  
  It provides a lightweight, CPU-friendly pipeline for retrieving contextually related events, such as "conflicts involving UK."

- **Core Workflow:**
  1. **SQLite Compatibility Setup:**  
     - Overrides default `sqlite3` with `pysqlite3` for **FTS5 full-text search** support.  
     - Ensures Chroma can operate with the enhanced SQLite backend.  
  2. **Embedding Model:**  
     - Uses `SentenceTransformerEmbeddings` with the model `all-MiniLM-L6-v2`, ideal for efficient text embedding on CPU.
  3. **Data Fetching:**  
     - Retrieves event data (`Name of Incident`, `Type of Event`, `Impact`, `Place Name`) from the `world_events` table.
  4. **Document Construction:**  
     - Each event is converted into a LangChain `Document` containing text content and associated metadata.
  5. **Vector Store Initialization:**  
     - Creates a **Chroma vector store** (`chroma_db` directory).  
     - If a vector store already exists, it loads it instead of recreating.  
     - Data is persisted locally for reuse.
  6. **Semantic Search Execution:**  
     - Executes a similarity search query (e.g., *"conflicts involving UK"*) to find the most relevant documents.
  7. **Results Display:**  
     - Prints the retrieved events along with their place and event type metadata.

---

## 🚀 Suggested Improvements

1. **Add Error Handling for Empty Query Results**  
   - *Handle cases where no documents match the search query by printing a user-friendly message.*

2. **Integrate Logging Instead of Print Statements**  
   - *Use Python’s `logging` module to track database access, embedding, and retrieval operations with timestamps.*

3. **Enable Dynamic Query Input**  
   - *Allow the user to input queries interactively instead of using a hardcoded query.*

4. **Optimize Text Preprocessing**  
   - *Clean and normalize event descriptions (remove duplicates, punctuation, extra spaces) before embedding to improve semantic accuracy.*

5. **Add Metadata Filtering Support**  
   - *Allow users to filter searches by event type or region (e.g., conflicts only, or events in Europe).*

---

## 🤖 Alternative Models / Approaches

1. **Model: `BAAI/bge-small-en-v1.5`**  
   *A high-performance embedding model optimized for English retrieval tasks; provides better semantic clustering than MiniLM.*

2. **Vector Store: `FAISS` (Facebook AI Similarity Search)**  
   *FAISS is faster for large datasets and provides efficient approximate nearest-neighbor search for scalable retrieval.*

3. **Approach: LangChain `RetrievalQA` Pipeline**  
   *Combine retrieval with an LLM (like `llama3` or `mixtral`) to generate detailed contextual answers, not just retrieve documents.*

---

**🧩 Developer’s Note:**  
This implementation provides a **simple, CPU-friendly semantic search system** that can scale with minimal dependencies. By extending it with a **RetrievalQA** chain and **persistent vector indexing**, it can evolve into a full-fledged **knowledge-based Q&A assistant** for event analysis and research.
