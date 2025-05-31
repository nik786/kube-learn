

- Modern documents have a lotof tables and the textual content is not easy to extract in conventional ways. 
- We will use the state of the art transformers. Very useful for RPA and other applications


```

!apt install -y tesseract-ocr
!apt install poppler-utils
!apt install libtesseract-dev
!pip install -q -U nltk pytesseract unstructured[all-docs] pydantic lxml timm #PDF related

```

```

from IPython.display import display
import requests
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt

image_url = "https://templates.invoicehome.com/invoice-template-us-neat-750px.png"
response = requests.get(image_url)
image = Image.open(BytesIO(response.content))
plt.figure(figsize=(10, 10))
plt.imshow(image)
plt.axis('off')
plt.show()

```

```

from transformers import pipeline
from PIL import Image
layoutlm = pipeline(model="impira/layoutlm-document-qa")

```

```
layoutlm(image=image_url,question="What is the total amount due?")

layoutlm(image=image_url,question="Who is this billed to")

layoutlm(image=image,question="What is the address of the biller")

layoutlm(image=image_url,question="What is the invoice date?")

donutvqa = pipeline("document-question-answering", model="naver-clova-ix/donut-base-finetuned-docvqa")
#Ignore the warning 'Could not find image processor' class for now. Not FATAL.

donutvqa(question="What is the invoice date?", image=image)

```

## Puttingthe models to use with Unstructured IO

!gdown 1I8Ga_BK23OA8EEv3DtAmo5zw_Quud0ew


```

from pdf2image import convert_from_path
import matplotlib.pyplot as plt

pages = convert_from_path("arso.pdf", dpi=200)

num_pages_to_display = min(len(pages), 6)

fig, axes = plt.subplots(nrows=1, ncols=num_pages_to_display, figsize=(20, 15))

# Ensure axes is an iterable for the case of a single subplot
if num_pages_to_display == 1:
    axes = [axes]

for ax, page_image in zip(axes, pages[:num_pages_to_display]):
    ax.imshow(page_image)
    ax.axis('off')  # Hide axes for a cleaner visualization

plt.tight_layout()
plt.show()

```


```
from unstructured.partition.pdf import partition_pdf

raw_pdf_elements = partition_pdf(
    filename="arso.pdf", # https://drive.google.com/file/d/1I8Ga_BK23OA8EEv3DtAmo5zw_Quud0ew/view?usp=sharing
    infer_table_structure=True,
)

```


```

tables = [el for el in raw_pdf_elements if el.category == "Table"]
for table in tables:
    print("\n",table.text)


```


```

titles = [el for el in raw_pdf_elements if el.category == "Title"]
for title in titles:
  print(title.category, title.text, title.metadata.page_number)

```


```

tables = [el for el in raw_pdf_elements if el.category == "Table"]
for table in tables:
  print(table.category, "Page number: ",table.metadata.page_number, table.metadata.coordinates)

```

```
for i, table in enumerate(tables):
    # Extracting coordinates and page number for the current table
    points = table.metadata.coordinates.points
    page_num = table.metadata.page_number - 1  # Adjusting for zero-based index
    page_image = pages[page_num]

    # Adding padding around the table region
    pad = 10
    left, upper = points[0][0] - pad, points[0][1] - pad
    right, lower = points[2][0] + pad, points[2][1] + pad

    # Crop the table region from the page image
    table_region = page_image.crop((left, upper, right, lower))

    # Display the cropped table region
    plt.figure(figsize=(10, 8))
    plt.imshow(table_region)
    plt.axis('off')  # Hide axes for better visualization
    plt.title(f"Table {i+1}")  # Title each figure with the table number
    plt.show()

```

```
from IPython.display import HTML
html_table = tables[0].metadata.text_as_html
HTML(html_table)

```

```
images = [el for el in raw_pdf_elements if el.category == "Image"]
for i, img in enumerate(images):
    # Extracting coordinates and page number for the current table
    points = img.metadata.coordinates.points
    page_num = img.metadata.page_number - 1  # Adjusting for zero-based index
    page_image = pages[page_num]

    # Adding padding around the table region
    pad = 10
    left, upper = points[0][0] - pad, points[0][1] - pad
    right, lower = points[2][0] + pad, points[2][1] + pad

    # Crop the table region from the page image
    table_region = page_image.crop((left, upper, right, lower))

    # Display the cropped image region
    plt.figure(figsize=(10, 8))
    plt.imshow(table_region)
    plt.axis('off')  # Hide axes for better visualization
    plt.title(f"Image {i+1}")  # Title each figure with the Image number
    plt.show()


```

## Summarize the tables with LLM

```
!pip install -U -q langchain-groq
from langchain_groq import ChatGroq
from google.colab import userdata
import os

os.environ["GROQ_API_KEY"] = userdata.get("GROQ_API_KEY")
llm = ChatGroq(model_name="llama3-70b-8192")
```
```

for table in tables:
    print("**Summarizing the table**")
    query = "You are a document assistant. You will summarize the following table found in a research paper on robots. " + table.text
    print(llm.invoke(query).content)

```











