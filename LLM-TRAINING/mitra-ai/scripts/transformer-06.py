import os
import locale
import logging
import warnings
import pandas as pd
from transformers import pipeline

# Suppress TensorFlow, PyTorch, and HuggingFace warnings
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"  # TensorFlow logs
logging.getLogger("transformers").setLevel(logging.ERROR)  # HF Transformers logs
warnings.filterwarnings("ignore")  # Python warnings

# Fix encoding issue in some environments
locale.getpreferredencoding = lambda: "UTF-8"

# Document Question Answering
vqa = pipeline(model="impira/layoutlm-document-qa")
image_url = "https://templates.invoicehome.com/invoice-template-us-neat-750px.png"

print(vqa(image=image_url, question="What is the invoice date?"))
print(vqa(image=image_url, question="What is the balance due?"))
print(vqa(image=image_url, question="What is the address?"))

# Table Question Answering
tqa = pipeline(task="table-question-answering", model="google/tapas-large-finetuned-wtq")

data = {
    "Actors": ["Brad Pitt", "Leonardo Di Caprio", "George Clooney"],
    "Number of movies": ["87", "53", "69"]
}

table_df = pd.DataFrame.from_dict(data)
print(tqa(table=table_df, query="How many movies does Leonardo Di Caprio have?"))

