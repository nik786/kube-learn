from openai import OpenAI
import os
from dotenv import load_dotenv
from PIL import Image
import base64
import io
import json

# ---------------- ENV SETUP ----------------

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise ValueError("OPENAI_API_KEY not found")

client = OpenAI(api_key=API_KEY)

IMAGE_PATH = "images/food_image.jpg"

# ---------------- IMAGE ENCODING ----------------

def encode_image_to_base64(image_input):
    if isinstance(image_input, str):
        if not os.path.exists(image_input):
            raise FileNotFoundError(f"Image not found: {image_input}")
        with open(image_input, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")

    elif isinstance(image_input, Image.Image):
        buffer = io.BytesIO()
        image_input.save(buffer, format=image_input.format or "JPEG")
        return base64.b64encode(buffer.getvalue()).decode("utf-8")

    else:
        raise ValueError("Invalid image input")

# ---------------- OPENAI VISION CALL ----------------

def query_openai_vision(
    client,
    image,
    prompt,
    model="gpt-4o-mini",   # cheapest vision model
    max_tokens=150
):
    base64_image = encode_image_to_base64(image)

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            },
                        },
                    ],
                }
            ],
            max_tokens=max_tokens,
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"API error: {e}"

# ---------------- TABLE & LOGIC ----------------

def print_summary_table(data):
    print("\nSummary Table")
    print("Nutrient\tEstimated Amount")
    print(f"Calories\t~{data['calories_kcal']} kcal")
    print(f"Protein\t\t~{data['protein_g']} g")
    print(f"Fat\t\t~{data['fat_g']} g")
    print(f"Carbohydrates\t~{data['carbohydrates_g']} g")
    print(f"Fiber\t\t~{data['fiber_g']} g")


def generate_suggestions(data):
    suggestions = []

    if data["protein_g"] >= 25:
        suggestions.append("✔ High-quality protein")

    if data["fat_g"] >= 15:
        suggestions.append("✔ Rich in omega-3 fatty acids")

    if data["carbohydrates_g"] <= 10:
        suggestions.append("✔ Low in refined carbs")

    if data["fiber_g"] >= 3:
        suggestions.append("✔ Anti-inflammatory")

    if data["protein_g"] >= 25 and data["fat_g"] >= 15:
        suggestions.append("✔ Very filling & clean")

    return suggestions


def health_goals(data):
    goals = []

    if data["calories_kcal"] <= 500:
        goals.extend(["Weight loss", "Fat loss"])

    if data["fat_g"] >= 15:
        goals.extend(["Brain health", "Heart health"])

    if data["protein_g"] >= 30:
        goals.append("Muscle maintenance")

    return goals

# ---------------- MAIN ----------------

if __name__ == "__main__":
    image = Image.open(IMAGE_PATH)

    nutrition_prompt = """
You are a nutrition analysis assistant.

Estimate nutrition for ONE serving of the food in the image.

Return ONLY valid JSON in this format:

{
  "food": "string",
  "calories_kcal": number,
  "protein_g": number,
  "fat_g": number,
  "carbohydrates_g": number,
  "fiber_g": number
}
"""

    print("Querying OpenAI Vision (cheap mode)...\n")

    result = query_openai_vision(client, image, nutrition_prompt)

    print("--- Raw Model Output ---")
    print(result)

    try:
        data = json.loads(result)

        print_summary_table(data)

        print("\n✅ What’s Good in This Meal")
        for item in generate_suggestions(data):
            print(item)

        print("\nThis is an excellent meal for:\n")
        for goal in health_goals(data):
            print(goal)

    except Exception as e:
        print("❌ Failed to parse nutrition data:", e)

