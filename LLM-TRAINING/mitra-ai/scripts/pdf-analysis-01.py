
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
