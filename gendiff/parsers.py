import json
import os
from typing import Any, Dict

import yaml


def parse_file(filepath: str) -> Dict[str, Any]:
    """Парсит JSON или YAML файл в словарь."""
    _, ext = os.path.splitext(filepath)
    with open(filepath, 'r') as f:
        if ext in ('.json',):
            return json.load(f)
        elif ext in ('.yml', '.yaml'):
            return yaml.safe_load(f)
        else:
            raise ValueError(f"Unsupported file extension: {ext}")