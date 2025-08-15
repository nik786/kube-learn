import locale
from transformers import pipeline

# Ensure UTF-8 encoding
locale.getpreferredencoding = lambda: "UTF-8"

# Load the document question answering model
vqa = pipeline(model="impira/layoutlm-document-qa")

# Image URL
image_url = "https://templates.invoicehome.com/invoice-template-us-neat-750px.png"

# Questions to ask
questions = [
    "What is the invoice date?",
    "What is the balance due?",
    "What is the address?"
]

# Ask each question
for q in questions:
    answer = vqa(image=image_url, question=q)
    print(f"Q: {q}\nA: {answer}\n")

