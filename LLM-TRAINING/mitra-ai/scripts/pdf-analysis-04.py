

from pdf2image import convert_from_path
import matplotlib.pyplot as plt
from unstructured.partition.pdf import partition_pdf

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

# ✅ Print first table as HTML (if available)
if tables:
    html_table = tables[0].metadata.text_as_html
    print("\n=== First Extracted Table (HTML) ===\n")
    print(html_table)

# ✅ Crop and display detected images
for i, img in enumerate(images):
    points = img.metadata.coordinates.points
    page_num = img.metadata.page_number - 1  # zero-based index
    page_image = pages[page_num]

    # Add padding
    pad = 10
    left = max(points[0][0] - pad, 0)
    upper = max(points[0][1] - pad, 0)
    right = min(points[2][0] + pad, page_image.width)
    lower = min(points[2][1] + pad, page_image.height)

    # Crop the image region
    image_region = page_image.crop((left, upper, right, lower))

    # Show cropped image
    plt.figure(figsize=(10, 8))
    plt.imshow(image_region)
    plt.axis('off')
    plt.title(f"Image {i+1}")
    plt.show()
