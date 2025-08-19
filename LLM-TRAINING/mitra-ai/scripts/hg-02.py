from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from langchain_community.llms import HuggingFacePipeline
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
import torch
import gradio as gr

# -----------------------
# Falcon model
# -----------------------
model_id = "tiiuae/falcon-rw-1b"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="cpu",           
    torch_dtype=torch.float32,
    low_cpu_mem_usage=True,
    trust_remote_code=True
)

hf_pipeline = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=200,
    temperature=0.7,
    do_sample=True
)

llm = HuggingFacePipeline(pipeline=hf_pipeline)

# -----------------------
# Inject fixed knowledge into memory
# -----------------------
fixed_chat = """
Human: Hi, what's your name?
AI: My name is Alexa.
Human: How old are you?
AI: I am eight years old.
Human: Who do you live with?
AI: I live with my parents.
Human: Do you have siblings?
AI: I'm alone.
Human: Which is your favorite color?
AI: Blue.
Human: What is your favorite food?
AI: Paneer.
Human: What do you like to do?
AI: I like to play with my friends.
Human: What do you want to be when you grow up?
AI: I want to become AI scientist.
Human: Who is top in epl table?
AI: Manchester City.
Human: Who won maximum WC in football?
AI: Brazil.
Human: What is time now?
AI: 7:20PM IST.
Human: What is the date today?
AI: 18.08.2025.
"""

memory = ConversationBufferMemory()
memory.chat_memory.add_user_message("Here are my facts, remember them:")
memory.chat_memory.add_ai_message(fixed_chat)

# -----------------------
# Prompt template (strict rule)
# -----------------------
template = """You are Alexa, a friendly 8-year-old AI.

Answer ONLY using the facts you were taught in memory.
If you don’t know the answer, reply with exactly:
"I don’t know that yet."

{history}
Human: {input}
AI:"""

prompt = PromptTemplate(
    input_variables=["history", "input"],
    template=template
)

conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True,
    prompt=prompt
)

# -----------------------
# Gradio UI
# -----------------------
def chat(message, history):
    return conversation.predict(input=message)

demo = gr.ChatInterface(
    fn=chat,
    title="Mitra Robot (Alexa with Strict Memory)"
)

demo.launch(share=True)

