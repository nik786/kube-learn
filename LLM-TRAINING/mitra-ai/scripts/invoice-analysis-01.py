
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
