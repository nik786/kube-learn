from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline
from langchain import PromptTemplate, LLMChain

# Hugging Face authentication token
HF_TOKEN = ""

# Smaller CPU-friendly model
model_id = "tiiuae/falcon-1b-instruct"

print("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(model_id, use_auth_token=HF_TOKEN)

print("Loading model on CPU...")
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype="auto",     # CPU auto precision
    device_map="cpu",       # Force CPU
    use_auth_token=HF_TOKEN
)

# Create HuggingFace pipeline
hf = pipeline(
    task="text-generation",
    model=model,
    tokenizer=tokenizer,
    max_length=500,
    device=-1  # CPU mode
)

llm_falcon = HuggingFacePipeline(pipeline=hf)

# Prompt template
template = """Question: {question}

Summary: Please summarize the above question in simple, layman’s terms."""
summary_prompt = PromptTemplate(template=template, input_variables=["question"])

# LLM chain
summary_chain = LLMChain(prompt=summary_prompt, llm=llm_falcon)

# Run
result = summary_chain.run("Summary of the Indian Constitution")
print("\n--- SUMMARY ---\n", result)


template = """Give a critical commentary and explain the background for this political context for a non-US resident:
{context}
"""
prompt = PromptTemplate(template=template, input_variables=["question","context"])
chain = prompt | llm_mistral


context = """
The Biden administration told the Supreme Court that “Texas has effectively prevented Border Patrol from monitoring the border” at Shelby Park. The state has defended the seizure, with Attorney General Ken Paxton saying he “will continue to defend Texas’s efforts to protect its southern border” against the federal government's attempts to undermine it.

At a ranch outside Eagle Pass where Abbott sympathizers gathered ahead of Saturday's rally, vendors sold Donald Trump-inspired MAGA hats and Trump flags. A homemade sign read, "The federal government has lost its way. Their job is to protect the states.”

Julio Vasquez, pastor of Iglesia Luterana San Lucas in Eagle Pass, said Abbott's campaign is a waste of money because migrants “come with empty hands asking for help.”

Alicia Garcia, a lifelong Eagle Pass resident who avoids Shelby Park but attended Friday's annual rodeo-themed festival at the nearby international bridge, questioned the value of Abbott's efforts because many asylum-seekers are released by U.S. authorities to argue their cases in immigration court.

“What’s with the show?” said Garcia, 38. "Better to just break everything down if they are still crossing.”
"""

chain.invoke({"context":context})



