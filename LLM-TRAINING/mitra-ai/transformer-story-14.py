
import locale
locale.getpreferredencoding = lambda: "UTF-8"

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_experimental.utilities import PythonREPL
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

# --- Helpers ---
def _sanitize_output(text: str):
    if "```python" in text:
        _, after = text.split("```python", 1)
        return after.split("```", 1)[0]
    return text.strip()

def to_str(prompt_value):
    return prompt_value.to_string()

def hf_pipeline_to_str(outputs):
    if isinstance(outputs, list) and len(outputs) > 0:
        if "generated_text" in outputs[0]:
            return outputs[0]["generated_text"]
        elif "summary_text" in outputs[0]:
            return outputs[0]["summary_text"]
    return str(outputs)

# --- Prompt ---
template = """Write python code to solve the user's problem: {problem}.

Return only python code in Markdown format, e.g.:

```python
....
```"""
prompt = ChatPromptTemplate.from_template(template)

# --- Text model ---
model_id = "google/flan-t5-small"  # ✅ lightweight CPU-friendly
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSeq2SeqLM.from_pretrained(model_id)  # ✅ fixed

llm_pipeline = pipeline(
    "text2text-generation",
    model=model,
    tokenizer=tokenizer,
    do_sample=True,
    temperature=0.7,
    top_p=0.95,
    max_new_tokens=128,
    pad_token_id=tokenizer.eos_token_id
)

# --- LangChain chain ---
chain = (
    prompt 
    | to_str 
    | llm_pipeline 
    | hf_pipeline_to_str
    | StrOutputParser() 
    | _sanitize_output 
    | PythonREPL().run
)

print("\n--- CHAIN TEST ---")
print(chain.invoke({"problem": "What is 2 plus 2"}))

# --- Image classification ---
print("\n--- IMAGE TEST ---")
vision_classifier = pipeline(
    "image-classification",
    model="facebook/deit-tiny-patch16-224"
)

preds = vision_classifier("1200px-2019_Toyota_Corolla_Icon_Tech_VVT-i_Hybrid_1.8.jpg")
preds = [{"score": round(pred["score"], 4), "label": pred["label"]} for pred in preds]
print(preds)

# --- Audio transcription ---
print("\n--- AUDIO TEST ---")
transcriber = pipeline(
    task="automatic-speech-recognition",
    model="openai/whisper-tiny"
)
print("Ready for audio transcription (use transcriber('audio.mp3'))")
