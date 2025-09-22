
from pdf2image import convert_from_path
import matplotlib.pyplot as plt
from unstructured.partition.pdf import partition_pdf





raw_pdf_elements = partition_pdf(
    filename="arso.pdf",
    infer_table_structure=True,

)


tables = [el for el in raw_pdf_elements if el.category == "Table"]
for table in tables:
    print("\n",table.text)


titles = [el for el in raw_pdf_elements if el.category == "Title"]
for title in titles:
  print(title.category, title.text, title.metadata.page_number)


tables = [el for el in raw_pdf_elements if el.category == "Table"]
for table in tables:
  print(table.category, "Page number: ",table.metadata.page_number, table.metadata.coordinates)

