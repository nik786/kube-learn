import os
from openai import OpenAI
from dotenv import load_dotenv
import gradio as gr


class AITutor:
    """
    AI Tutor usable from Terminal and Gradio UI
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
# Shared Tutor Instance
# -----------------------------
tutor = AITutor()


# -----------------------------
# Gradio wrapper function
# -----------------------------
def gradio_ask(question):
    if not question.strip():
        return "Please enter a question."
    return tutor.ask(question)


# -----------------------------
# Gradio Interface
# -----------------------------
ai_tutor_interface = gr.Interface(
    fn=gradio_ask,
    inputs=gr.Textbox(
        lines=5,
        placeholder="Ask the AI Tutor anything...",
        label="Your Question"
    ),
    outputs=gr.Textbox(label="AI Tutor's Answer"),
    title="🤖 My Awesome AI Explainer",
    description="AI Explainer will provide an explanation.",
    allow_flagging="never",
)


# -----------------------------
# Main (Terminal / Vim execution)
# -----------------------------
if __name__ == "__main__":
    # Launch Gradio UI
    print("Launching Gradio Interface...")
    ai_tutor_interface.launch()

    # Terminal test (optional)
    question = (
        "Could you give the definition of AI?"
    )

    print("\nAsking the AI Tutor:")
    print(question)

    answer = tutor.ask(question)

    print("\n🤖 AI Tutor's Response:\n")
    print(answer)

