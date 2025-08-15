import requests
from PIL import Image
from io import BytesIO
from transformers import pipeline

# Load vision classifier
vision_classifier = pipeline("image-classification", model="google/vit-base-patch16-224")

# If the image is on the internet:
# image_url = "https://upload.wikimedia.org/wikipedia/commons/3/36/2019_Toyota_Corolla_Icon_Tech_VVT-i_Hybrid_1.8.jpg"
# response = requests.get(image_url)
# image = Image.open(BytesIO(response.content))

# If the image is local:
image_path = "1200px-2019_Toyota_Corolla_Icon_Tech_VVT-i_Hybrid_1.8.jpg"
image = Image.open(image_path)

# Get predictions
preds = vision_classifier(image)
preds = [{"score": round(pred["score"], 4), "label": pred["label"]} for pred in preds]

print(preds)

