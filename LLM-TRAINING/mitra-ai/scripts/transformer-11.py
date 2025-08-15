import os
os.environ["CUDA_VISIBLE_DEVICES"] = ""  # Force CPU

from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch
from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline
from langchain import PromptTemplate, LLMChain

model_id = "tiiuae/falcon-rw-1b"

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_id)
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

# Load model in float32 (CPU-friendly)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float32,
    device_map=None  # Force no accelerate device mapping
)

# Build pipeline
hf_pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=512,
    temperature=0.7,
    top_p=0.95,
    repetition_penalty=1.1,
    pad_token_id=tokenizer.pad_token_id,
    eos_token_id=tokenizer.eos_token_id,
    device=-1  # Force CPU in pipeline
)

llm = HuggingFacePipeline(pipeline=hf_pipe)

# Summarization chain
summary_template = """Question: {question}

Summary: Please summarize the above question in simple, layman’s terms."""
summary_prompt = PromptTemplate(template=summary_template, input_variables=["question"])
summary_chain = LLMChain(prompt=summary_prompt, llm=llm)

summary = summary_chain.invoke({"question": "Summary of the Indian Constitution"})
print("\n--- SUMMARY ---\n", summary["text"] if isinstance(summary, dict) else summary)

# Commentary chain
commentary_template = """Give a critical commentary and explain the background for this political context for a non-US resident:
{context}
"""
commentary_prompt = PromptTemplate(template=commentary_template, input_variables=["context"])
commentary_chain = LLMChain(prompt=commentary_prompt, llm=llm)

context = """
The Biden administration told the Supreme Court that “Texas has effectively prevented Border Patrol from monitoring the border” at Shelby Park...
"""
commentary = commentary_chain.invoke({"context": context})
print("\n--- COMMENTARY ---\n", commentary["text"] if isinstance(commentary, dict) else commentary)

