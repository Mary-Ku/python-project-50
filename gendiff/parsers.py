import json
import os
import pathlib
from typing import Any

import yaml


def parse_file(filepath: str) -> dict[str, Any]:
    """Парсит JSON или YAML файл в словарь."""
    _, ext = os.path.splitext(filepath)

    with pathlib.Path(filepath).open('r') as file:
        if ext in ('.json',):
            return json.load(file)
        if ext in ('.yml', '.yaml'):
            return yaml.safe_load(file)
        raise ValueError(f'Unsupported file extension: {ext}')
