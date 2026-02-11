# gendiff/__init__.py

from .parsers import parse_file


def _format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return str(value)


def generate_diff(filepath1: str, filepath2: str) -> str:
    data1 = parse_file(filepath1)
    data2 = parse_file(filepath2)

    all_keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff_lines = []

    for key in all_keys:
        if key not in data2:
            diff_lines.append(f"  - {key}: {_format_value(data1[key])}")
        elif key not in data1:
            diff_lines.append(f"  + {key}: {_format_value(data2[key])}")
        elif data1[key] == data2[key]:
            diff_lines.append(f"    {key}: {_format_value(data1[key])}")
        else:
            diff_lines.append(f"  - {key}: {_format_value(data1[key])}")
            diff_lines.append(f"  + {key}: {_format_value(data2[key])}")

    return "{\n" + "\n".join(diff_lines) + "\n}"
