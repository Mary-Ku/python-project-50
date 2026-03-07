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
    with pathlib.Path(args.first_file).open(encoding='utf-8') as f1:
        first_file_data = json.load(f1)
        logger.info('first file: %s', first_file_data)

    with pathlib.Path(args.second_file).open(encoding='utf-8') as f2:
        second_file_data = json.load(f2)
        logger.info('second file: %s', second_file_data)


if __name__ == '__main__':
    main()
