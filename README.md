# HED Task

Exploration of task structure and its annotation with HED (Hierarchical Event Descriptors).

## Features

- **CLI Interface**: Command-line tool built with Typer
- **REST API**: FastAPI-based web API
- **Modern Python**: Uses latest Python features and best practices
- **Comprehensive Testing**: pytest with coverage reporting
- **Code Quality**: Ruff for linting and formatting, mypy for type checking
- **CI/CD**: GitHub Actions workflows
- **Development Tools**: Pre-commit hooks, uv for dependency management

## Quick Start

### Installation

1. Install [uv](https://docs.astral.sh/uv/) if you haven't already:
```bash
# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Clone and setup the project:
```bash
git clone <your-repo-url>
cd hed-task
uv sync --all-extras
```

### Usage

#### CLI
```bash
# Get help
uv run hed-task --help

# Say hello
uv run hed-task hello "World"

# Check version
uv run hed-task version
```

#### API Server
```bash
# Start development server
uv run uvicorn hed_task.api:app --reload
```

Visit http://localhost:8000/docs for interactive API documentation.

## Development

See [docs/development.md](docs/development.md) for detailed development setup and workflow.

## Dependencies

- **FastAPI**: Modern web framework for building APIs
- **Typer**: CLI framework based on Python type hints
- **pandas**: Data manipulation and analysis
- **cogat**: Cognitive Atlas Python interface
- **pytest**: Testing framework
- **ruff**: Fast Python linter and formatter
- **mypy**: Static type checker

## License

This project is licensed under the terms specified in the LICENSE file.
