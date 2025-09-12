
# Zero-Shot Text Classification with Transformers

## 📌 Summary of the Code
This script uses Hugging Face’s `transformers` library to perform **zero-shot classification** with the `typeform/distilbert-base-uncased-mnli` model.  
Key points:
- **Setup**: Uses `pipeline("zero-shot-classification")` with CPU (`device=-1`) and optimized CPU threading.  
- **Inputs**: Classifies multiple text sequences (emails, sales forecast, bug reports, cooking query, sports statement).  
- **Outputs**: Provides probabilities for each candidate label.  
- **Post-Processing**: For one example (Virat Kohli statement), the script extracts the label with the highest score programmatically.  

---

## ✅ Suggested Improvements
1. **Batch Processing**  
   Instead of classifying one sequence at a time, process multiple sequences in a single batch for efficiency.
   ```python
   outputs = roberta([sequence_to_classify_01, sequence_to_classify_02], [candidate_labels_01, candidate_labels_02])

2. **Automatic Device Selection**
    Detect GPU availability for faster inference:
    device = 0 if torch.cuda.is_available() else -1


3. **Clean Output Formatting**
    Save results in structured JSON or CSV format instead of raw print statements.

4. **Consistent Candidate Labels**
   Refine and standardize labels (e.g., fix typo "infiormation" → "information") to improve accuracy.

5. **Error Handling & Logging**
   Add try-except blocks and logging to make the script more robust for production use.

6. **Alternative Approaches & Models**
   
   1. Larger and More Accurate Model

  

## Model: facebook/bart-large-mnli

   Why: Higher accuracy on English classification tasks, widely used in production.

        - Trade-off: Slower inference compared to DistilBERT.
        - Multilingual Support

## Model: joeddav/xlm-roberta-large-xnli

   Why: Supports 100+ languages, useful for global datasets.

     - Trade-off: Heavier model, requires more resources.
     - Embedding + Semantic Similarity


## Model: sentence-transformers/all-mpnet-base-v2

  - Approach: Instead of direct zero-shot classification, generate embeddings and compare with label embeddings using cosine similarity.

     - Why: More flexible, works well when labels are semantically rich.

     - Trade-off: Requires extra logic for similarity scoring.

## References

- Hugging Face Transformers Documentation

- Zero-Shot Classification Pipeline

- Hugging Face Model Hub
