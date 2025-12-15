from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables")

open_client = OpenAI(api_key=openai_api_key)

print("OpenAI client successfully configured")
print("API Key prefix:", openai_api_key[:15])

