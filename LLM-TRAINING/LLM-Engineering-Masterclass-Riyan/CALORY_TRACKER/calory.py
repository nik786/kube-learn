from openai import OpenAI
import os
from dotenv import load_dotenv
from PIL import Image

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables")

client = OpenAI(api_key=openai_api_key)

image_filename = "images/food_image.jpg"

img = Image.open(image_filename)

print(f"Image: '{image_filename}' loaded successfully")
print(f"Format: {img.format}")
print(f"Size: {img.size}")
print(f"Mode: {img.mode}")

# For terminal usage
img.show()

