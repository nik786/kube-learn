
# 📑 Document QA, Sentiment Analysis & Text Generation with Hugging Face Transformers  

## 📌 Summary of the Code  
This script integrates **three NLP tasks** using Hugging Face pipelines:  

- **Document Question Answering (DQA)**  
  Uses `naver-clova-ix/donut-base-finetuned-docvqa` to extract structured answers (e.g., balance due) directly from documents like invoices.  

- **Sentiment Analysis**  
  Uses `lxyuan/distilbert-base-multilingual-cased-sentiments-student` to evaluate sentiment across multiple languages with probability scores.  

- **Text Generation**  
  Uses `gpt2` to generate free-form completions for prompts (e.g., company description, constitutional summary).  

The code also includes **logging suppression** and **locale fixes** for smoother execution.  

---

## ✅ Suggested Improvements  

1. **GPU Support**  
   Automatically detect and use GPU (`device=0`) if available for faster inference.  

2. **Result Formatting**  
   Save outputs (answers, sentiments, generations) into structured formats like **JSON/CSV** instead of raw prints.  

3. **Prompt Engineering**  
   Improve GPT-2 generations by using **context-aware structured prompts** and controlling temperature/penalty parameters.  

4. **Error Handling**  
   Add try-except blocks for missing documents, invalid input text, or model loading failures.  

5. **Upgrade Model Choices**  
   Replace `gpt2` with newer instruction-tuned or larger-scale LLMs for better text generation quality.  

---

## 🚀 Alternative Approaches & Models  

### 1. Document QA  
**Model**: `microsoft/layoutlmv3-base`  
- **Why**: Combines text + layout embeddings for stronger structured document understanding.  
- **Trade-off**: Requires OCR preprocessing (unlike Donut).  

### 2. Sentiment Analysis  
**Model**: `cardiffnlp/twitter-roberta-base-sentiment-latest`  
- **Why**: Optimized for modern sentiment tasks, especially on short-form and noisy text.  
- **Trade-off**: English-only (no multilingual support).  

### 3. Text Generation  
**Model**: `tiiuae/falcon-7b-instruct`  
- **Why**: Instruction-tuned, more coherent and context-aware generations than GPT-2.  
- **Trade-off**: Requires GPU/large memory resources.  

---

## 📂 References  
- [Donut Document QA](https://huggingface.co/naver-clova-ix/donut-base-finetuned-docvqa)  
- [Multilingual Sentiment Model](https://huggingface.co/lxyuan/distilbert-base-multilingual-cased-sentiments-student)  
- [GPT-2 Text Generation](https://huggingface.co/gpt2)  
- [LayoutLMv3](https://huggingface.co/microsoft/layoutlmv3-base)  
- [Falcon-7B Instruct](https://huggingface.co/tiiuae/falcon-7b-instruct)  
