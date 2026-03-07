"""Модуль содержит точку входа gendiff."""

import argparse
import json
import logging
import pathlib

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(message)s',
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def generator_diff(first_file_path: str, second_file_path: str) -> None:
    """Сравнивает два файла и возвращает их различия."""
    with pathlib.Path(first_file_path).open(encoding='utf-8') as f1:
        first_file_data = json.load(f1)

    with pathlib.Path(second_file_path).open(encoding='utf-8') as f2:
        second_file_data = json.load(f2)

    all_rows = set(first_file_data) | set(second_file_data)
    result = ''
    for row_key in sorted(all_rows):
        is_in_first = row_key in first_file_data
        is_in_second = row_key in second_file_data
        is_in_both = is_in_first and is_in_second

        # Если есть в обоих файлах - выяснить, одинаковые ли значения
        if is_in_both:
            if first_file_data[row_key] == second_file_data[row_key]:
                result += f'  {row_key}: {first_file_data[row_key]}\n'
            else:
                # Строка из первого файла выводится первой
                result += f'- {row_key}: {first_file_data[row_key]}\n'
                result += f'+ {row_key}: {second_file_data[row_key]}\n'
        # Если только в первом
        elif is_in_first:
            result += f'- {row_key}: {first_file_data[row_key]}\n'
        else:
            result += f'+ {row_key}: {second_file_data[row_key]}\n'

    formatted_result = '\n{\n' + result + '\n}'
    logger.info(formatted_result)


def main() -> None:
    """Точка входа утилиты gendiff."""
    parser = argparse.ArgumentParser(
        usage='gendiff first_file second_file',
        description='Compares two configuration files and shows a difference.',
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        default='stylish',
        help='set format of output',
    )

    args = parser.parse_args()
    generator_diff(args.first_file, args.second_file)


if __name__ == '__main__':
    main()
