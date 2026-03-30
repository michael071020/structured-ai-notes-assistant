import argparse
import json
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


def save_output_json(data: dict, file_path: Path) -> None:
    """
    Save the structured result to a JSON file.

    This makes the project feel more complete because the output
    is not only printed to the terminal, but also saved as a file.
    """
    file_path.parent.mkdir(parents=True, exist_ok=True)

    with file_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


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
    if result["action_items"]:
        for item in result["action_items"]:
            print(f"- {item}")
    else:
        print("- No clear action items found.")
    print()

    print("Tags:")
    print(", ".join(result["tags"]))
    print()


def parse_args() -> argparse.Namespace:
    """
    Parse command-line arguments.

    This gives the project a simple CLI interface so users can
    choose input and output paths more explicitly.
    """
    parser = argparse.ArgumentParser(
        description="Generate structured notes from long-form text."
    )

    parser.add_argument(
        "--input",
        type=str,
        default="examples/input.txt",
        help="Path to the input text file",
    )

    parser.add_argument(
        "--output",
        type=str,
        default="examples/output.json",
        help="Path to save the structured JSON output",
    )

    return parser.parse_args()


def main() -> None:
    args = parse_args()

    input_file = Path(args.input)
    output_file = Path(args.output)

    text = load_input_text(input_file)

    print("=== Input Loaded ===")
    print(f"Input file: {input_file}")
    print(f"Characters: {len(text)}")
    print()

    raw_output = generate_notes(text)

    # Keep raw output visible during development so prompt quality
    # and model behavior can be inspected more easily.
    print("=== Raw Model Output ===")
    print(raw_output)
    print()

    result = parse_json_output(raw_output)
    validate_notes(result)

    print_notes(result)

    save_output_json(result, output_file)

    print("=== Output Saved ===")
    print(f"Saved structured JSON to: {output_file}")


if __name__ == "__main__":
    main()