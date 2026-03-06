"""Модуль содержит точку входа gendiff."""

import argparse


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

    parser.parse_args()


if __name__ == '__main__':
    main()
