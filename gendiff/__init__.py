import json
import pathlib


def _format_value(value):
    """Преобразует значение в строку в стиле stylish (для примитивов)."""
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return str(value)


def generate_diff(filepath1: str, filepath2: str) -> str:
    """Сравнивает два плоских JSON-файла
    и возвращает строку с разницей в формате stylish.
    """
    with pathlib.Path(filepath1).open('r') as f1:
        data1 = json.load(f1)
    with pathlib.Path(filepath2).open('r') as f2:
        data2 = json.load(f2)

    all_keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff_lines = []

    for key in all_keys:
        if key not in data2:
            # Удалено
            line = f'  - {key}: {_format_value(data1[key])}'
            diff_lines.append(line)
        elif key not in data1:
            # Добавлено
            line = f'  + {key}: {_format_value(data2[key])}'
            diff_lines.append(line)
        elif data1[key] == data2[key]:
            # Без изменений
            line = f'    {key}: {_format_value(data1[key])}'
            diff_lines.append(line)
        else:
            # Изменено: сначала старое, потом новое
            line1 = f'  - {key}: {_format_value(data1[key])}'
            line2 = f'  + {key}: {_format_value(data2[key])}'
            diff_lines.extend([line1, line2])

    return '{\n' + '\n'.join(diff_lines) + '\n}'
