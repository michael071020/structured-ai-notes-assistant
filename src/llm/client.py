import os
from dotenv import load_dotenv
from openai import OpenAI

# Load variables from .env into environment variables.
load_dotenv()


def generate_notes(text: str) -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    model = os.getenv("OPENAI_MODEL", "gpt-5.4-mini")

    if not api_key:
        raise ValueError("OPENAI_API_KEY is not set.")

    client = OpenAI(api_key=api_key)

    prompt = f"""
            You are a helpful assistant for note-taking.

            Read the following long-form text and produce:
            1. A short summary
            2. 3 to 5 key points
            3. 2 to 4 action items
            4. 3 to 5 tags

            Text:
            {text}
            """.strip()

    response = client.responses.create(
        model=model,
        input=prompt,
    )

    return response.output_text.strip()