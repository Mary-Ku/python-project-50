build:
	uv build

check-project:
	uv run ruff check .
	mypy .
