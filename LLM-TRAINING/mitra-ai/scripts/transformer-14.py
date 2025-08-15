import locale
locale.getpreferredencoding = lambda: "UTF-8"
!pip install -U -q langchain-experimental
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_experimental.utilities import PythonREPL

def _sanitize_output(text: str):
    _, after = text.split("```python")
    return after.split("```")[0]

template = """Write python code to solve the user's problem: {problem}.

Return only python code in Markdown format, e.g.:

```python
....
```"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | llm_mistral | StrOutputParser() | _sanitize_output | PythonREPL().run


chain.invoke({"problem": "What is 2 plus 2"})

vision_classifier = pipeline(task="image-classification",model="google/vit-base-patch16-224")


preds = vision_classifier(inputs="1200px-2019_Toyota_Corolla_Icon_Tech_VVT-i_Hybrid_1.8.jpg")
preds = [{"score": round(pred["score"], 4), "label": pred["label"]} for pred in preds]
preds

transcriber = pipeline(model="openai/whisper-small", chunk_length_s=30, return_timestamps=True)


