.PHONY: install run test lint typecheck check

install:
	pip install -r requirements.txt -r requirements-dev.txt

run:
	python -m uvicorn voice_runtime.api.app:create_app --factory --reload

test:
	pytest

lint:
	ruff check . && ruff format --check .

typecheck:
	mypy

check: lint typecheck test
