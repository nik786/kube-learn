
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from langchain_community.llms import HuggingFacePipeline
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory, ConversationSummaryMemory
import torch
import gradio as gr

# -----------------------------
# Load Falcon model on CPU
# -----------------------------
model_id = "tiiuae/falcon-rw-1b"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="cpu",           # CPU-only
    torch_dtype=torch.float32,
    low_cpu_mem_usage=True,
    trust_remote_code=True
)

# HuggingFace text-generation pipeline
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

# -----------------------------
# Buffer Memory Conversation
# -----------------------------
buffer_memory = ConversationBufferMemory()
conversation = ConversationChain(
    llm=llm,
    memory=buffer_memory,
    verbose=True
)

def chat(message, history):
    return conversation.predict(input=message)

def clear_buffer():
    buffer_memory.clear()
    return "🧹 Buffer memory cleared!"

# -----------------------------
# Summary Memory Conversation
# -----------------------------
summary_memory = ConversationSummaryMemory(llm=llm)
conversation_with_summary = ConversationChain(
    llm=llm,
    memory=summary_memory,
    verbose=True
)

def summary_chat(message, history):
    return conversation_with_summary.predict(input=message)

def clear_summary():
    summary_memory.clear()
    return "🧹 Summary memory cleared!"

# -----------------------------
# Combine both into Tabs
# -----------------------------
with gr.Blocks() as app:
    gr.Markdown("# 🤖 Mitra Robot Chat\nChoose memory type below:")

    with gr.Tab("Buffer Memory"):
        buffer_demo = gr.ChatInterface(
            fn=chat,
            title="Buffer Memory Chat"
        )
        clear_btn1 = gr.Button("Clear Buffer Memory 🧹")
        status1 = gr.Textbox(label="Status", interactive=False)
        clear_btn1.click(fn=clear_buffer, outputs=status1)

    with gr.Tab("Summary Memory"):
        summary_demo = gr.ChatInterface(
            fn=summary_chat,
            title="Summary Memory Chat"
        )
        clear_btn2 = gr.Button("Clear Summary Memory 🧹")
        status2 = gr.Textbox(label="Status", interactive=False)
        clear_btn2.click(fn=clear_summary, outputs=status2)

# Launch single app
app.launch(share=True)
