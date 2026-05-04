.PHONY: install run test lint format type-check security docker-build docker-run check

install:
	python -m pip install --upgrade pip
	python -m pip install -r requirements-dev.txt

run:
	uvicorn secure_api.main:app --reload

test:
	pytest

lint:
	ruff check src tests

format:
	ruff format src tests

type-check:
	mypy

security:
	bandit -r src
	pip-audit

docker-build:
	docker build -t ci-cd-secure-api .

docker-run:
	docker run --rm -p 8000:8000 ci-cd-secure-api

check: lint type-check test security