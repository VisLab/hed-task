# Makefile for hed-task development

.PHONY: help install test lint format type-check clean dev api docs

help: ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install dependencies
	uv sync --all-extras

install-dev: ## Install development dependencies
	uv sync --all-extras --dev
	uv run pre-commit install

test: ## Run tests
	uv run pytest

test-cov: ## Run tests with coverage
	uv run pytest --cov=hed_task --cov-report=html --cov-report=term

lint: ## Run linting
	uv run ruff check .

format: ## Format code
	uv run ruff format .

type-check: ## Run type checking
	uv run mypy src/

check: lint type-check test ## Run all checks (lint, type-check, test)

clean: ## Clean cache and build artifacts
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf dist/
	rm -rf build/
	rm -rf *.egg-info/
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete

dev: ## Start development environment
	uv run python -m hed_task.cli

api: ## Start API server
	uv run uvicorn hed_task.api:app --reload --host 0.0.0.0 --port 8000

docs: ## Open API documentation
	@echo "Starting API server and opening docs..."
	@echo "API docs will be available at: http://localhost:8000/docs"
	uv run uvicorn hed_task.api:app --reload &
	sleep 3
	@if command -v start > /dev/null 2>&1; then \
		start http://localhost:8000/docs; \
	elif command -v open > /dev/null 2>&1; then \
		open http://localhost:8000/docs; \
	else \
		echo "Please open http://localhost:8000/docs in your browser"; \
	fi

build: ## Build package
	uv build

pre-commit: ## Run pre-commit on all files
	uv run pre-commit run --all-files
