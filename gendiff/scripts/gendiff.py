"""Модуль содержит точку входа gendiff."""

import argparse


def main():
    """Точка входа утилиты gendiff."""
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', help='First file path')
    parser.add_argument('second_file', help='Second file path')
    parser.add_argument(
        '-f', '--format',
        default='stylish',
        help='set format of output'
    )
    parser.parse_args()



if __name__ == "__main__":
    main()
