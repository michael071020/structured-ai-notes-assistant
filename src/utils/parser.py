import json


REQUIRED_FIELDS = {
    "title": str,
    "summary": str,
    "key_points": list,
    "action_items": list,
    "tags": list,
}


def parse_json_output(raw_output: str) -> dict:
    """
    Parse the raw model output into a Python dictionary.

    If the model output is not valid JSON, json.loads will raise an error.
    """
    return json.loads(raw_output)


def validate_notes(data: dict) -> None:
    """
    Perform basic validation on the parsed result.

    Checks:
    - required fields exist
    - each field has the expected type
    - list-based fields contain strings
    - some fields have reasonable minimum content quality
    """
    for field_name, expected_type in REQUIRED_FIELDS.items():
        if field_name not in data:
            raise ValueError(f"Missing required field: {field_name}")

        if not isinstance(data[field_name], expected_type):
            raise ValueError(
                f"Field '{field_name}' must be of type {expected_type.__name__}"
            )

    # Validate that list-based fields contain strings.
    for list_field in ["key_points", "action_items", "tags"]:
        if not all(isinstance(item, str) for item in data[list_field]):
            raise ValueError(f"All items in '{list_field}' must be strings")

    # Basic content quality checks.
    if not data["title"].strip():
        raise ValueError("Field 'title' must not be empty")

    if not data["summary"].strip():
        raise ValueError("Field 'summary' must not be empty")

    # Expect key_points to contain at least 3 items for this project.
    if len(data["key_points"]) < 3:
        raise ValueError("Field 'key_points' must contain at least 3 items")

    # Tags should not be empty because they are part of the core output.
    if len(data["tags"]) < 1:
        raise ValueError("Field 'tags' must contain at least 1 item")