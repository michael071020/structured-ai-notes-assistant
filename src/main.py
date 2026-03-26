from pathlib import Path

from llm.client import generate_notes
from utils.parser import parse_json_output, validate_notes


def load_input_text(file_path: Path) -> str:
    """
    Read the input text file and return its content as a string.
    """
    if not file_path.exists():
        raise FileNotFoundError(f"Input file not found: {file_path}")

    return file_path.read_text(encoding="utf-8").strip()


def print_notes(result: dict) -> None:
    """
    Print the structured result in a human-readable format.
    """
    print("=== Structured Notes ===")
    print(f"Title: {result['title']}")
    print()
    print("Summary:")
    print(result["summary"])
    print()

    print("Key Points:")
    for item in result["key_points"]:
        print(f"- {item}")
    print()

    print("Action Items:")
    for item in result["action_items"]:
        print(f"- {item}")
    print()

    print("Tags:")
    print(", ".join(result["tags"]))
    print()


def main() -> None:
    """
    Day 3 pipeline:
    1. Load input text
    2. Generate JSON output from the LLM
    3. Parse JSON into a Python dict
    4. Validate the structure
    5. Print the result
    """
    input_file = Path("examples/input.txt")
    text = load_input_text(input_file)

    print("=== Input Loaded ===")
    print(f"Characters: {len(text)}")
    print()

    raw_output = generate_notes(text)

    print("=== Raw Model Output ===")
    print(raw_output)
    print()

    result = parse_json_output(raw_output)
    validate_notes(result)

    print_notes(result)


if __name__ == "__main__":
    main()