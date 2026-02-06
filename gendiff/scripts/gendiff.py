"""Модуль содержит точку входа gendiff."""

import argparse


def main():
    """Точка входа утилиты gendiff."""
    parser = argparse.ArgumentParser(
        usage='gendiff [-h] first_file second_file',
        description='Compares two configuration files and shows a difference.',
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.print_help()


if __name__ == "__main__":
    main()
