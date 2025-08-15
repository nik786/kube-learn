from transformers import BitsAndBytesConfig, AutoModelForCausalLM, AutoTokenizer, pipeline
import torch

# 4-bit quantization config for CPU
quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float32,  # float32 for CPU stability
    bnb_4bit_quant_type="nf4",
    bnb_4bit_use_double_quant=True
)

# Model & tokenizer
model_id = "mistralai/Mistral-7B-Instruct-v0.1"

model_4bit = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map={"": "cpu"},  # Force CPU
    quantization_config=quantization_config,
    torch_dtype=torch.float32,  # CPU-safe precision
    trust_remote_code=True
)

tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)

# Pipeline for inference
pipe = pipeline(
    "text-generation",
    model=model_4bit,
    tokenizer=tokenizer,
    max_new_tokens=200,
    device=-1  # Force CPU
)

print(pipe("Tell me a short story about a dragon and a cat:")[0]['generated_text'])

