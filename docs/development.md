# Development Setup

This guide will help you set up the development environment for hed-task.

## Prerequisites

- Python 3.9 or higher
- [uv](https://docs.astral.sh/uv/) package manager

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd hed-task
```

2. Install uv if you haven't already:
```bash
# On Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# On macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

3. Create virtual environment and install dependencies:
```bash
uv sync --all-extras
```

4. Activate the virtual environment:
```bash
# On Windows
.venv\Scripts\activate

# On macOS/Linux
source .venv/bin/activate
```

5. Install pre-commit hooks:
```bash
uv run pre-commit install
```

## Development Workflow

### Running Tests
```bash
# Run all tests
uv run pytest

# Run tests with coverage
uv run pytest --cov=hed_task

# Run specific test file
uv run pytest tests/test_cli.py
```

### Code Quality
```bash
# Lint code
uv run ruff check .

# Format code
uv run ruff format .

# Type checking
uv run mypy src/
```

### Running the Application

#### CLI
```bash
# Using uv
uv run hed-task --help
uv run hed-task hello Alice

# Or with activated environment
hed-task --help
```

#### API Server
```bash
# Development server
uv run uvicorn hed_task.api:app --reload

# Or with activated environment
uvicorn hed_task.api:app --reload
```

The API will be available at http://localhost:8000, with interactive docs at http://localhost:8000/docs.

## Project Structure

```
hed-task/
├── src/hed_task/          # Main package
│   ├── __init__.py        # Package initialization
│   ├── cli.py             # CLI interface (Typer)
│   └── api.py             # FastAPI application
├── tests/                 # Test files
│   ├── conftest.py        # Test configuration
│   ├── test_cli.py        # CLI tests
│   └── test_api.py        # API tests
├── .github/workflows/     # GitHub Actions
├── pyproject.toml         # Project configuration
├── .pre-commit-config.yaml # Pre-commit hooks
└── README.md             # Project documentation
```

## Adding Dependencies

```bash
# Add a runtime dependency
uv add package-name

# Add a development dependency
uv add --dev package-name

# Add from git repository
uv add git+https://github.com/user/repo.git
```

## Git Workflow

1. Create a feature branch
2. Make your changes
3. Run tests and linting
4. Commit (pre-commit hooks will run automatically)
5. Push and create a pull request

The CI pipeline will automatically run tests, linting, and type checking on your pull requests.
