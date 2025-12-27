
import requests
import pypdf
from io import BytesIO

pdf_url = "https://www.happiestminds.com/whitepapers/devops.pdf"

print(f"Downloading PDF from {pdf_url}...")

response = requests.get(pdf_url, timeout=30)
response.raise_for_status()

pdf_bytes = BytesIO(response.content)

reader = pypdf.PdfReader(pdf_bytes)
num_pages = len(reader.pages)

print(f"PDF has {num_pages} pages.")

all_pages_text = []

for i, page in enumerate(reader.pages, start=1):
    text = page.extract_text()
    if text:
        all_pages_text.append(text)

pdf_text = "\n".join(all_pages_text)

print("✅ Successfully extracted text")
print(f"Total characters: {len(pdf_text)}")
