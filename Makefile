.PHONY: lint test

lint:
	uv run ruff check .
	uv run ruff format --check .

test:
	uv run coverage run -m pytest
	uv run coverage report
