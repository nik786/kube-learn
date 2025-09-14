from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline

model_id = "google/flan-t5-small"

# Load model & tokenizer
model = AutoModelForSeq2SeqLM.from_pretrained(model_id)
tokenizer = AutoTokenizer.from_pretrained(model_id)

# Create pipeline for text generation
pipe = pipeline(
    "text2text-generation",
    model=model,
    tokenizer=tokenizer,
    device=-1  # Force CPU
)

# Run inference
result = pipe("Tell me a short story about a dragon and a cat.", max_new_tokens=100)
print(result[0]['generated_text'])


