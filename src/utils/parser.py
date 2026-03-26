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

    This function assumes the model should return JSON text.
    If the JSON is invalid, json.loads will raise an exception.
    """
    return json.loads(raw_output)


def validate_notes(data: dict) -> None:
    """
    Perform basic validation on the parsed result.

    Checks:
    - required fields exist
    - each field has the expected type
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