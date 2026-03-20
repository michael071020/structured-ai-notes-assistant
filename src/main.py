from pathlib import Path
from llm.client import generate_notes


def load_input_text(file_path: Path) -> str:
    """
    Read the input text file and return its content as a string.
    """
    if not file_path.exists():
        raise FileNotFoundError(f"Input file not found: {file_path}")

    return file_path.read_text(encoding="utf-8").strip()


def main() -> None:
    """
    Minimal Day 2 pipeline:
    1. Load sample input text
    2. Send it to the LLM
    3. Print the raw output
    """
    input_file = Path("examples/input.txt")
    text = load_input_text(input_file)

    print("=== Input Loaded ===")
    print(f"Characters: {len(text)}")
    print()

    result = generate_notes(text)

    print("=== Model Output ===")
    print(result)


if __name__ == "__main__":
    main()