
from langchain_groq import ChatGroq
import os
from pdf2image import convert_from_path
import matplotlib.pyplot as plt
from unstructured.partition.pdf import partition_pdf

# ✅ Set your Groq API key here (or export it in your shell before running)
os.environ["GROQ_API_KEY"] = os.getenv(
    "GROQ_API_KEY", ""
)

# Initialize Groq LLM
llm = ChatGroq(model_name="llama-3.3-70b-versatile")


# Convert PDF into images (one per page)
pages = convert_from_path("arso.pdf", dpi=200)

# Partition PDF into structured elements
raw_pdf_elements = partition_pdf(
    filename="arso.pdf",
    infer_table_structure=True,
)

# Separate tables and images
tables = [el for el in raw_pdf_elements if el.category == "Table"]
images = [el for el in raw_pdf_elements if el.category == "Image"]

# Summarize extracted tables
for i, table in enumerate(tables, start=1):
    table_text = getattr(table, "text", None) or getattr(table.metadata, "text", None)
    if not table_text:
        print(f"[!] Skipping table {i}: no text extracted")
        continue

    print(f"\n=== Summarizing Table {i} ===")
    query = (
        "You are a document assistant. Summarize the following table found in a research paper on robots:\n\n"
        + table_text
    )
    response = llm.invoke(query)
    print(response.content)
