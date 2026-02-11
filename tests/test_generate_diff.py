import os
import pytest
from gendiff import generate_diff


def read_fixture(path):
    with open(path, 'r') as f:
        return f.read().strip()


@pytest.mark.parametrize("file1,file2", [
    ("file1.json", "file2.json"),
    ("file1.yml", "file2.yml"),
])
def test_generate_diff_flat_formats(file1, file2):
    base_dir = os.path.join(os.path.dirname(__file__), 'test_data')
    path1 = os.path.join(base_dir, file1)
    path2 = os.path.join(base_dir, file2)
    expected = read_fixture(os.path.join(base_dir, 'expected_stylish.txt'))

    result = generate_diff(path1, path2).strip()
    assert result == expected
