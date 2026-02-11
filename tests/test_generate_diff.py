import os
import pathlib

from gendiff import generate_diff


def test_generate_diff_flat_json():
    file1 = os.path.join(os.path.dirname(__file__), 'test_data', 'file1.json')
    file2 = os.path.join(os.path.dirname(__file__), 'test_data', 'file2.json')
    expected_path = os.path.join(os.path.dirname(
        __file__), 'test_data', 'expected_stylish.txt',
    )

    with pathlib.Path(expected_path).open() as f:
        expected = f.read().strip()

    result = generate_diff(file1, file2).strip()
    assert result == expected
