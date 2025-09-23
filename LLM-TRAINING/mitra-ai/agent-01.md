
# 🤖 Agent-01: Multi-Agent Workflow with Groq + CrewAI  

## 📌 Summary  
This script demonstrates a **multi-agent collaboration workflow** using **CrewAI** with the **Groq LLM (llama-3.3-70b-versatile)** for research and content generation.  

- **🔑 API Setup**  
  - Configures `GROQ_API_KEY` and `SERPER_API_KEY` for LLM and search.  

- **🧠 LLM Integration**  
  - Uses `ChatGroq` wrapper for low-latency inference.  

- **🔍 Tools**  
  - Integrates `SerperDevTool` for web-based search (returns top 5 results).  

- **👨‍💻 Agents**  
  - **Researcher Agent** → Extracts 3–5 insights about AI in manufacturing.  
  - **Writer Agent** → Crafts engaging Tweets based on research.  

- **📋 Tasks**  
  - Task 1: Research AI agents in manufacturing.  
  - Task 2: Generate Twitter content from insights.  

- **🚀 Orchestration**  
  - `Crew` runs agents sequentially with `max_rpm=4` and `max_steps=5`.  

---

## 🔧 Suggested Improvements  

1. **Add Error Handling**  
   - Ensure fallback mechanisms if API keys are missing or invalid.  

2. **Parameterize Inputs**  
   - Make task prompts configurable via CLI arguments or `.env` file.  

3. **Enhance Output Formatting**  
   - Return results in Markdown or JSON for easier integration.  

4. **Add Logging & Monitoring**  
   - Use structured logs to trace agent reasoning and task execution.  

5. **Improve Task Flexibility**  
   - Support dynamic chaining (e.g., Writer refines Researcher’s output automatically).  

---

## 🚀 Alternative Models/Approaches  

1. *Use **OpenAI GPT-4.1** with function calling* → Better reasoning and structured outputs for research + tweet generation.  
2. *Adopt **Anthropic Claude 3.5 Sonnet** with memory-enabled conversations* → More contextual and safety-focused agent collaboration.  
3. *Use **Mistral Large** with local vector DB (ChromaDB/Faiss)* → Faster retrieval-augmented generation without external search dependency.  

---
