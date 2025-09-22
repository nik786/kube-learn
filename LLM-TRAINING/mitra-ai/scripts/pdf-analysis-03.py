
from pdf2image import convert_from_path
import matplotlib.pyplot as plt
from unstructured.partition.pdf import partition_pdf

# Convert PDF into images (one per page)
pages = convert_from_path("arso.pdf", dpi=200)

num_pages_to_display = min(len(pages), 6)

fig, axes = plt.subplots(nrows=1, ncols=num_pages_to_display, figsize=(20, 15))


# Partition PDF into structured elements
raw_pdf_elements = partition_pdf(
    filename="arso.pdf",
    infer_table_structure=True,
)

# Extract table elements
tables = [el for el in raw_pdf_elements if el.category == "Table"]

for i, table in enumerate(tables):
    # Extract coordinates and page number
    points = table.metadata.coordinates.points
    page_num = table.metadata.page_number - 1  # zero-based index
    page_image = pages[page_num]

    # Add padding around table region
    pad = 10
    left = max(points[0][0] - pad, 0)
    upper = max(points[0][1] - pad, 0)
    right = min(points[2][0] + pad, page_image.width)
    lower = min(points[2][1] + pad, page_image.height)

    # Crop table region from page image
    table_region = page_image.crop((left, upper, right, lower))

    # Show cropped table
    plt.figure(figsize=(10, 8))
    plt.imshow(table_region)
    plt.axis('off')
    plt.title(f"Table {i+1}")
    plt.show()
