from openai import OpenAI
import os
from dotenv import load_dotenv
from PIL import Image
import base64
import io
import json
import re

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
    model="gpt-4o-mini",
    max_tokens=150
):
    base64_image = encode_image_to_base64(image)

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

# ---------------- RESPONSE CLEANING ----------------

def extract_json(raw_text: str) -> dict:
    """
    Handles:
    - ```json ... ```
    - plain JSON
    """
    cleaned = re.sub(r"```json|```", "", raw_text).strip()
    return json.loads(cleaned)

def normalize_fields(data: dict) -> dict:
    """
    Supports multiple schema versions
    """
    return {
        "food": data.get("food") or data.get("food_name", "Unknown"),
        "calories_kcal": data.get("calories") or data.get("calories_kcal"),
        "protein_g": data.get("protein_g") or data.get("protein_grams"),
        "fat_g": data.get("fat_g") or data.get("fat_grams"),
        "carbohydrates_g": data.get("carbohydrates_g", 0),
        "fiber_g": data.get("fiber_g", 0),
        "confidence": data.get("confidence") or data.get("confidence_level", "Unknown"),
    }

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

    structured_nutrition_prompt = """
Identify the food and estimate nutrition for ONE serving.

Return ONLY JSON (no explanation):

{
  "food_name": "string",
  "serving_description": "string",
  "calories": number,
  "fat_grams": number,
  "protein_grams": number,
  "confidence_level": "Low | Medium | High"
}
"""

    print("Querying OpenAI Vision...\n")

    raw_output = query_openai_vision(
        client=client,
        image=image,
        prompt=structured_nutrition_prompt,
    )

    print("--- Raw Model Output ---")
    print(raw_output)

    try:
        parsed = extract_json(raw_output)
        data = normalize_fields(parsed)

        print_summary_table(data)

        print("\n✅ What’s Good in This Meal")
        for s in generate_suggestions(data):
            print(s)

        print("\nThis is an excellent meal for:\n")
        for g in health_goals(data):
            print(g)

        print(f"\nConfidence level: {data['confidence']}")

    except Exception as e:
        print("❌ Failed to process model output:", e)

