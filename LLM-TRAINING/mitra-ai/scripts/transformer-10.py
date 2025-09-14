from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline
from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline
from langchain import PromptTemplate, LLMChain

# Lightweight CPU-friendly model
model_id = "google/flan-t5-base"

print("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(model_id)

print("Loading model on CPU...")
model = AutoModelForSeq2SeqLM.from_pretrained(
    model_id,
    torch_dtype="auto",      # auto precision for CPU
    low_cpu_mem_usage=True   # helps reduce RAM load
)

# HuggingFace pipeline
hf_pipeline = pipeline(
    task="text2text-generation",
    model=model,
    tokenizer=tokenizer,
    max_length=300,
    device=-1  # CPU mode
)

llm_flan = HuggingFacePipeline(pipeline=hf_pipeline)

# -------- Example 1: Summarization --------
template = """Question: {question}

Summary: Please summarize the above question in simple, layman’s terms."""
summary_prompt = PromptTemplate(template=template, input_variables=["question"])
summary_chain = LLMChain(prompt=summary_prompt, llm=llm_flan)

result = summary_chain.run("Summary of the Indian Constitution")
print("\n--- SUMMARY ---\n", result)

# -------- Example 2: Critical Commentary --------
context = """
The Biden administration told the Supreme Court that “Texas has effectively prevented Border Patrol 
from monitoring the border” at Shelby Park. The state has defended the seizure, with Attorney General 
Ken Paxton saying he “will continue to defend Texas’s efforts to protect its southern border” against 
the federal government's attempts to undermine it.

At a ranch outside Eagle Pass where Abbott sympathizers gathered ahead of Saturday's rally, vendors sold 
Donald Trump-inspired MAGA hats and Trump flags. A homemade sign read, "The federal government has lost 
its way. Their job is to protect the states.”

Julio Vasquez, pastor of Iglesia Luterana San Lucas in Eagle Pass, said Abbott's campaign is a waste of 
money because migrants “come with empty hands asking for help.”

Alicia Garcia, a lifelong Eagle Pass resident who avoids Shelby Park but attended Friday's annual 
rodeo-themed festival at the nearby international bridge, questioned the value of Abbott's efforts because 
many asylum-seekers are released by U.S. authorities to argue their cases in immigration court.

“What’s with the show?” said Garcia, 38. "Better to just break everything down if they are still crossing.”
"""

template_commentary = """Give a critical commentary and explain the background for this political context for a non-US resident:
{context}
"""
commentary_prompt = PromptTemplate(template=template_commentary, input_variables=["context"])
commentary_chain = LLMChain(prompt=commentary_prompt, llm=llm_flan)

commentary_result = commentary_chain.run(context)
print("\n--- COMMENTARY ---\n", commentary_result)
