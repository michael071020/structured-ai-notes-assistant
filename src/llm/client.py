import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

# Load variables from .env into environment variables.
load_dotenv()


def load_prompt_template(file_path: Path) -> str:
    """
    Read the prompt template from a text file.

    This lets us separate prompt content from Python code,
    which makes the project easier to maintain and extend.
    """
    if not file_path.exists():
        raise FileNotFoundError(f"Prompt file not found: {file_path}")

    return file_path.read_text(encoding="utf-8").strip()


def generate_notes(text: str) -> str:
    """
    Send input text to the LLM and return raw JSON text.
    """

    api_key = os.getenv("OPENAI_API_KEY")
    model = os.getenv("OPENAI_MODEL", "gpt-5.4-mini")

    if not api_key:
        raise ValueError("OPENAI_API_KEY is not set.")

    client = OpenAI(api_key=api_key)

    # Load the reusable prompt template from the prompts folder.
    prompt_path = Path("prompts/note_prompt.txt")
    prompt_template = load_prompt_template(prompt_path)

    # Use a custom placeholder instead of str.format().
    # This avoids conflicts with JSON curly braces in the prompt template.
    prompt = prompt_template.replace("__INPUT_TEXT__", text)

    response = client.responses.create(
        model=model,
        input=prompt,
    )

    return response.output_text.strip()