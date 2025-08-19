from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from langchain_community.llms import HuggingFacePipeline
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
import torch

# Falcon model
model_id = "tiiuae/falcon-rw-1b"

# Load tokenizer and model on CPU
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="cpu",           # CPU-only
    torch_dtype=torch.float32,
    low_cpu_mem_usage=True,
    trust_remote_code=True
)

# HuggingFace text-generation pipeline (remove device parameter)
hf_pipeline = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=200,
    temperature=0.7,
    do_sample=True
)

# Wrap into LangChain LLM
llm = HuggingFacePipeline(pipeline=hf_pipeline)

# Custom prompt template
template = """
Your name is Mitra. You are an assistant for question-answering tasks for Mitra Robot customer support.
Use three sentences maximum and keep the answer concise.
Have a conversation related to robots and note their key details. Ask them about their key information to get started.

Current conversation:
{history}
Human: {input}
Mitra:"""

prompt = PromptTemplate(input_variables=["history", "input"], template=template)

# Conversation memory
memory = ConversationBufferMemory(memory_key="history")

# Preload memory
memory.save_context(
    {"input": "My name is Balaji and I live in Bengaluru"},
    {"output": "Thank you!"}
)

# Conversation chain
conversation = ConversationChain(
    llm=llm,
    prompt=prompt,
    memory=memory,
    verbose=True
)

# Example conversation
response = conversation.predict(input="Hi, what is the name the customer gave?")
print("Mitra:", response)

