"""Модуль содержит точку входа gendiff."""

import argparse

from gendiff import generate_diff


def main():
    """Точка входа утилиты gendiff."""
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.',
    )
    parser.add_argument('first_file', help='First file path')
    parser.add_argument('second_file', help='Second file path')
    parser.add_argument(
        '-f', '--format',
        default='stylish',
        help='set format of output',
    )
    args = parser.parse_args()

    # Пока поддерживаем только stylish
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == '__main__':
    main()
