# 🧩 LLM-24: Groq-Powered Retrieval-Augmented Generation (RAG) Pipeline

## 📘 Summary
- **Objective:**  
  The script (`llm-24.py`) builds a **retrieval-augmented generation (RAG)** pipeline using **Groq-hosted Llama models** integrated with **LangChain** and **Chroma vector store** for intelligent question-answering over stored event data.

- **Key Components:**
  1. **Environment & Security:**  
     - Secure API key handling via environment variables (`GROQ_API_KEY`).  
     - Prevents accidental key exposure in source code.
  2. **Groq LLM Integration:**  
     - Uses `ChatGroq` to interact with Groq-hosted **Llama and Mixtral models**.  
     - Implements automatic model fallback in case of decommissioned models.
  3. **Embeddings & Vector Database:**  
     - Employs `HuggingFaceEmbeddings` (`BAAI/bge-small-en-v1.5`) for text encoding.  
     - Uses **Chroma** as a local persistent vector database (`chroma_store`).
  4. **Prompt Design:**  
     - A context-aware `ChatPromptTemplate` that instructs the model to:  
       - Answer questions using retrieved documents.  
       - Correct entity names.  
       - Explain event connections.  
       - Provide clean citation output.
  5. **Model Fallback Mechanism:**  
     - Tries `llama-3.3-70b-versatile` first.  
     - Falls back to `llama3-8b-8192` or `mixtral-8x7b-32768` automatically if the primary model fails.
  6. **End-to-End Query Flow:**  
     - Fetches relevant embeddings from Chroma.  
     - Passes the query through the prompt chain.  
     - Outputs a structured and detailed AI-generated answer with citations.

---

## 🚀 Suggested Improvements

1. **Add Structured Logging with Tracebacks**  
   - *Replace print statements with the `logging` module (e.g., `logging.info`, `logging.error`) for robust, timestamped logs.*

2. **Parallelize Fallback Model Attempts**  
   - *Attempt fallback model initialization concurrently using `asyncio` or `concurrent.futures` to reduce downtime.*

3. **Integrate Dynamic Model Health Check**  
   - *Query Groq’s API status endpoint to confirm active models before attempting connection, reducing unnecessary exceptions.*

4. **Expand Prompt Flexibility**  
   - *Include user persona and style parameters (e.g., “Explain like a historian” or “Summarize concisely”) to adapt tone and depth dynamically.*

5. **Add Streamed Response Mode**  
   - *Enable token streaming for long responses using LangChain’s `stream` API, providing real-time output for interactive experiences.*

---

## 🤖 Alternative Models / Approaches

1. **Approach: LangChain RetrievalQA Chain**  
   *Use LangChain’s built-in `RetrievalQA` chain, which natively integrates retrievers, prompts, and LLMs with better modularity and error control.*

2. **Model: `gpt-4o-mini` or `gpt-4-turbo` (OpenAI)**  
   *Offers high reasoning quality and robust context understanding for event-based Q&A, with strong multilingual and factual accuracy.*

3. **Model: `mistralai/mixtral-8x22b` with FAISS Backend**  
   *A larger Mixture-of-Experts model delivering improved contextual linkage and retrieval coherence, ideal for large-scale event datasets.*

---

**🧠 Developer’s Note:**  
This script demonstrates a **production-ready hybrid RAG setup** blending **fast retrieval** (Chroma + embeddings) with **Groq’s low-latency LLM inference**. With better model management, configurable prompts, and response streaming, it can scale into an enterprise-grade semantic intelligence pipeline.
