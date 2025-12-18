import os
from openai import OpenAI
from dotenv import load_dotenv


class AITutor:
    """
    A simple AI Tutor for terminal usage (Vim-friendly).
    """

    def __init__(self, model="gpt-4o-mini", temperature=0.7):
        load_dotenv()

        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")

        self.client = OpenAI(api_key=self.api_key)
        self.model = model
        self.temperature = temperature

        self.system_prompt = (
            "You are a helpful and patient AI Tutor. "
            "Explain concepts clearly and concisely."
        )

        print("OpenAI client configured successfully.")
        print(f"Key starts with: {self.api_key[:10]}...")

    def ask(self, question: str) -> str:
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": question},
                ],
                temperature=self.temperature,
            )
            return response.choices[0].message.content

        except Exception as e:
            return f"Error while fetching response: {e}"


# -----------------------------
# Main (Terminal / Vim execution)
# -----------------------------
if __name__ == "__main__":
    tutor = AITutor()

    question = (
        "Could you give the definition of AI and its effect on mankind"
    )

    print("\nAsking the AI Tutor:")
    print(question)

    answer = tutor.ask(question)

    print("\n🤖 AI Tutor's Response:\n")
    print(answer)

