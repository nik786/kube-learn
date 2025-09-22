
from IPython.display import display
import requests
from PIL import Image
from io import BytesIO
from transformers import pipeline

# Load image
image_url = "https://templates.invoicehome.com/invoice-template-us-neat-750px.png"
response = requests.get(image_url)
image = Image.open(BytesIO(response.content))

# Display image (optional)
display(image)

# Use Hugging Face pipeline for document QA
layoutlm = pipeline(model="impira/layoutlm-document-qa")

# Ask questions
m = layoutlm(image=image, question="What is the total amount due?")
print("Total Amount Due:", m)

n = layoutlm(image=image, question="Who is this billed to?")
print("Billed To:", n)

o = layoutlm(image=image, question="What is the address of the biller?")
print("Biller Address:", o)

p = layoutlm(image=image, question="What is the invoice date?")
print("Invoice Date:", p)
