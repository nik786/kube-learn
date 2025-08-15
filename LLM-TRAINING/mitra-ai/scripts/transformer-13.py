# transformer-11.py  (CPU-only, modern LangChain)

import os, warnings
# 1) Silence TF/XLA + CUDA chatter as much as possible
os.environ["CUDA_VISIBLE_DEVICES"] = ""      # hard-disable CUDA
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"     # hide TF INFO/WARN
os.environ["TOKENIZERS_PARALLELISM"] = "false"

# Optional: globally dampen common libs warnings
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

# --- LangChain (modern) ---
# Prefer the new integration; if not installed, fall back to legacy import.
try:
    from langchain_huggingface import HuggingFacePipeline
except Exception:
    from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline  # fallback

from langchain_core.prompts import PromptTemplate

print("Device set to use CPU")

MODEL_ID = "tiiuae/falcon-rw-1b"   # ~1B params, CPU friendly

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

# Load model on CPU in float32 (safest for CPU)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    torch_dtype=torch.float32,
    device_map=None,          # IMPORTANT: avoid accelerate auto-mapping
)

# Build HF pipeline (CPU)
hf_pipe = pipeline(
    task="text-generation",
    model=model,
    tokenizer=tokenizer,
    device=-1,                # CPU
    max_new_tokens=256,
    temperature=0.7,
    top_p=0.95,
    repetition_penalty=1.1,
    pad_token_id=tokenizer.pad_token_id,
    eos_token_id=tokenizer.eos_token_id,
)

llm = HuggingFacePipeline(pipeline=hf_pipe)

# ---------- Chains using runnables ----------
# Summary
summary_prompt = PromptTemplate.from_template(
    "Question: {question}\n\nSummary: Please summarize the above question in simple, layman’s terms."
)
summary_chain = summary_prompt | llm
summary = summary_chain.invoke({"question": "Summary of the Indian Constitution"})
print("\n--- SUMMARY ---\n", summary)

# Commentary
commentary_prompt = PromptTemplate.from_template(
    "Give a critical commentary and explain the background for this political context for a non-US resident:\n{context}\n"
)
commentary_chain = commentary_prompt | llm

context = """
The Biden administration told the Supreme Court that “Texas has effectively prevented Border Patrol from monitoring the border” at Shelby Park...
"""
commentary = commentary_chain.invoke({"context": context})
print("\n--- COMMENTARY ---\n", commentary)

