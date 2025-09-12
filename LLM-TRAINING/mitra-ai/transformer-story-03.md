
# 📰 News Summarization with Hugging Face Transformers

## 📌 Summary of the Code
This script demonstrates the use of Hugging Face’s `transformers` library for **summarization** and **zero-shot classification** tasks.  

- **Setup**:  
  - `pipeline("zero-shot-classification")` with `typeform/distilbert-base-uncased-mnli` for classification.  
  - `pipeline("summarization")` with `Falconsai/text_summarization` for news summarization.  

- **Task**:  
  The provided input is a long news article about **BCCI’s central contracts decision** involving Shreyas Iyer, Ishan Kishan, and Hardik Pandya.  

- **Output**:  
  The summarizer condenses the article into a concise form highlighting:  
  - Shreyas Iyer and Ishan Kishan dropped for skipping Ranji Trophy.  
  - Hardik Pandya retained after assuring participation in white-ball domestic tournaments.  
  - BCCI tightening rules for contracted players regarding domestic participation.  
  - Concerns raised by former cricketers about fairness in contract decisions.  

---

## ✅ Suggested Improvements
1. **Set Maximum Lengths for Summarizer**  
   Control summary length with `max_length` and `min_length` for more consistent outputs.  
   ```python
   output = summarizer(news, max_length=150, min_length=50, do_sample=False)
Automatic Device Selection
Run on GPU if available for faster summarization:

```
device = 0 if torch.cuda.is_available() else -1

```

## Batch Summarization
 - Summarize multiple articles at once instead of running pipeline individually.

## Clean Output Formatting
 - Save summarized outputs to JSON/CSV for structured storage instead of raw print statements.

## Model Selection Flexibility
 - Allow switching between different summarization models via config/CLI argument.



### Alternative Approaches & Models
   - 1. Abstractive Summarization with BART
      - Model: facebook/bart-large-cnn
      - Why: State-of-the-art model for news and article summarization.
      - Trade-off: Slower and heavier than DistilBERT variants.

   - 2. PEGASUS for Long-Form Summaries
     - Model: google/pegasus-xsum
     - Why: Pretrained specifically for abstractive summarization, especially for long texts.
     - Trade-off: Requires more memory and computational resources.


  3. Long Document Summarization with LongT5
     - Model: google/long-t5-local-base
       Why: Handles very long documents efficiently by extending Transformer context length.
       Trade-off: Experimental and slower than BART/PEGASUS on short texts.

## References
- Hugging Face Summarization Pipeline
- Falconsai/text_summarization Model
- Hugging Face Model Hub
