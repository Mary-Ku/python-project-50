install:
	uv install

build:
	uv build

publish:
	uv publish --dry-run

package-install:
	uv tool install dist/*.whl

lint:
	uv run flake8 gendiff
	uv run flake8 tests

diff:
	uv run gendiff tests/fixtures/file1.json tests/fixtures/file2.json

diff_plain:
	uv run gendiff tests/fixtures/file1.yml tests/fixtures/file2.yml -f plain

diff_json:
	uv run gendiff tests/fixtures/file1.yml tests/fixtures/file2.yml -f json

test:
	uv run pytest

check:
	uv run flake8 gendiff
	uv run flake8 tests
	uv run pytest

test-cov:
	uv run coverage run -m pytest
	uv run coverage report

.PHONY: install build publish package-install lint diff diff-json diff-plain test test-coverage check