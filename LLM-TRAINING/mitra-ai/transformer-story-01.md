
# Zero-Shot Classification with Hugging Face Transformers

## 📌 Summary of the Code
This script demonstrates the use of Hugging Face's `transformers` library to perform **zero-shot classification** using the `pipeline` API.  
- It imports the `pipeline` function and sets up PyTorch threading for faster CPU inference.  
- The model used is **`typeform/distilbert-base-uncased-mnli`**, optimized for natural language inference.  
- Two example sentences are classified into predefined candidate labels without requiring task-specific fine-tuning:
  1. A sentence related to **health insurance claim**.
  2. A sentence involving **confidential vs public information**.  

The script outputs classification results with scores for each candidate label.

---

## ✅ Potential Improvements
1. **Batch Inference** – Process multiple sentences at once to improve efficiency:
   ```python
   roberta([sequence_to_classify_01, sequence_to_classify_02], [candidate_labels_01, candidate_labels_02])



Use GPU if available – Set device=0 instead of -1 for much faster inference on CUDA-enabled systems.

Model Caching – Explicitly define a cache_dir to avoid re-downloading the model every run.

Better Candidate Labels – Use more refined and hierarchical labels for improved classification accuracy.

Structured Output – Store results in a JSON/CSV format instead of just printing, enabling easier downstream processing.

🚀 Alternative & Better Models

Depending on accuracy/speed trade-offs, consider these alternative models for zero-shot classification:

facebook/bart-large-mnli
Larger, more accurate but slower model for English zero-shot tasks.

joeddav/xlm-roberta-large-xnli
Multilingual model supporting 100+ languages.

MoritzLaurer/mDeBERTa-v3-base-mnli-xnli
State-of-the-art multilingual zero-shot classifier with high accuracy.

vicgalle/xlm-roberta-large-xnli-anli
Extended version trained with ANLI dataset for more robust reasoning.

sentence-transformers/all-mpnet-base-v2 (with cosine similarity)
Not a direct zero-shot classifier, but embeddings can be used for flexible semantic similarity-based classification.

📂 References

Hugging Face Zero-Shot Classification

Model Hub: Zero-Shot Models

