import os
from dotenv import load_dotenv
from openai import OpenAI

# Load variables from .env into environment variables.
load_dotenv()


def generate_notes(text: str) -> str:
    """
    Send input text to the LLM and ask for a JSON-only response.
    """

    api_key = os.getenv("OPENAI_API_KEY")
    model = os.getenv("OPENAI_MODEL", "gpt-5.4-mini")

    if not api_key:
        raise ValueError("OPENAI_API_KEY is not set.")

    client = OpenAI(api_key=api_key)

    # The prompt now explicitly defines the required JSON structure.
    # This helps make the output more stable and easier to parse.
    prompt = f"""
            You are a helpful assistant for note-taking.

            Read the following long-form text and return ONLY valid JSON.

            Required JSON format:
            {{
            "title": "string",
            "summary": "string",
            "key_points": ["string", "string"],
            "action_items": ["string", "string"],
            "tags": ["string", "string"]
            }}

            Rules:
            - Return valid JSON only.
            - Do not add markdown fences.
            - Do not add explanations before or after the JSON.
            - "title" should be a short descriptive title for the text.
            - "summary" should be concise but informative.
            - "key_points" should contain 3 to 5 items.
            - "action_items" should contain 2 to 4 items when applicable.
            - "tags" should contain 3 to 5 short tags.

            Text:
            {text}
            """.strip()

    response = client.responses.create(
        model=model,
        input=prompt,
    )

    return response.output_text.strip()