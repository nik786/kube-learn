import os
os.environ["CUDA_VISIBLE_DEVICES"] = ""  # force CPU

from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch

model_id = "tiiuae/falcon-rw-1b"  # small enough for 16GB RAM

tokenizer = AutoTokenizer.from_pretrained(model_id)

model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float16,  # saves memory
    low_cpu_mem_usage=True,
    device_map="cpu"  # load entirely on CPU
)

# Ensure float32 for CPU compatibility
model = model.to(torch.float32)

pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=200
)

prompt = "Tell me a story about a dragon and a robot."
print(pipe(prompt)[0]['generated_text'])

