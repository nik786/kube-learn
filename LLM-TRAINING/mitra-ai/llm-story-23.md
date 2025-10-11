
# 🧠 LLM-23: LangChain + Groq Llama3 Retrieval-Augmented Pipeline

## 📘 Summary
- **Purpose:**  
  The script (`llm-23.py`) establishes a **Retrieval-Augmented Generation (RAG)** workflow combining **LangChain**, **Groq-hosted Llama3**, and **Chroma vector store** to enable intelligent question-answering over structured world event data stored in SQLite.

- **Key Workflow:**
  1. **Groq Integration:**  
     - Uses `ChatGroq` with the **Llama-3.3-70B-Versatile** model for high-quality reasoning.  
     - Groq API key is set via environment variable for security.
  2. **SQLite Compatibility Patch:**  
     - Forces the use of `pysqlite3` to ensure consistent SQLite compatibility across environments.
  3. **Embeddings Setup:**  
     - Loads `BAAI/bge-small-en-v1.5` model from HuggingFace to convert text data into embeddings.  
     - Operates on CPU for easy local deployment.
  4. **Vector Database Configuration:**  
     - Creates or loads a **Chroma** vector store from `chroma_store` directory to manage event embeddings.
  5. **RAG Prompt Template:**  
     - Defines a dynamic `ChatPromptTemplate` that instructs the model to:  
       - Answer queries in detail using retrieved documents.  
       - Correct entity names.  
       - Explain event relationships.  
       - Display citations with duplicates removed.
  6. **LangChain Chain Construction:**  
     - Combines retriever, prompt, LLM, and output parser into a single query-processing pipeline.
  7. **SQL Database Integration:**  
     - Uses LangChain’s `SQLDatabase` utility to access and inspect the schema of `worldevents.db`.

- **Example Query:**  
  Executes `"conflicts involving UK"` to generate context-rich answers referencing retrieved documents.

---

## 🚀 Suggested Improvements

1. **Remove Hardcoded API Key**  
   - *Ensure no default key is stored in the script. Use environment variable validation and raise an exception if not set.*

2. **Add Error Handling for Database and Vector Retrieval**  
   - *Wrap database and Chroma operations in try-except blocks to prevent crashes due to file access or schema errors.*

3. **Introduce Logging Instead of Prints**  
   - *Replace print statements with `logging` for better debugging, traceability, and multi-level message control.*

4. **Enable Persistent RAG Caching**  
   - *Integrate LangChain’s `Cache` mechanism or Chroma’s persistence to avoid redundant embedding calculations across sessions.*

5. **Support Interactive Query Input**  
   - *Allow dynamic user input for queries instead of a single hardcoded question to make the script more flexible and reusable.*

---

## 🤖 Alternative Models / Approaches

1. **Approach: LangChain `RetrievalQA` Chain**  
   *Utilize LangChain’s built-in `RetrievalQA` class to simplify pipeline setup and improve modularity, with automatic retriever-LLM integration.*

2. **Model: `mistralai/mixtral-8x22b` via HuggingFace or Groq**  
   *Offers strong reasoning and factual recall, ideal for multi-event correlation or historical analysis tasks.*

3. **Vector Store Alternative: `FAISS` or `Weaviate`**  
   *FAISS provides faster similarity search for large-scale embeddings, while Weaviate adds semantic filtering and hybrid search (text + vector).*

---

**🧩 Developer’s Note:**  
This script demonstrates an effective foundation for **retrieval-based question answering** combining structured (SQL) and unstructured (vector) data. By integrating better error control, dynamic user interaction, and scalable model selection, it can evolve into a robust **AI-driven research assistant** for world event analysis.
