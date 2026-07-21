"""

Purpose:
Provides reusable utility functions for reading and writing JSON files.

"""

import json
from pathlib import Path


def save_json(data, filepath):
    """
    Save Python data to a JSON file.

    Args:
        data: Any JSON-serializable Python object.
        filepath: Path where the JSON file should be saved.
    """

    path = Path(filepath)

    # Create parent directories if they don't exist.
    path.parent.mkdir(parents=True, exist_ok=True)

    # Write the JSON data.
    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def load_json(filepath):
    """
    Load JSON data from a file.

    Args:
        filepath: Path to the JSON file.

    Returns:
        Python object created from the JSON data.
    """

    path = Path(filepath)

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)