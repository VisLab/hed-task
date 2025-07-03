# HED Task

[![CI](https://github.com/VisLab/hed-task/actions/workflows/ci.yml/badge.svg)](https://github.com/VisLab/hed-task/actions/workflows/ci.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/YOUR_REPO_ID/maintainability)](https://codeclimate.com/github/VisLab/hed-task/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/YOUR_REPO_ID/test_coverage)](https://codeclimate.com/github/VisLab/hed-task/test_coverage)
[![codecov](https://codecov.io/gh/VisLab/hed-task/branch/main/graph/badge.svg)](https://codecov.io/gh/VisLab/hed-task)

Exploration of task structure and its annotation with HED (Hierarchical Event Descriptors), with comprehensive tools for collecting and analyzing task data from the Cognitive Atlas.

## Features

- **Cognitive Atlas Data Collection**: Comprehensive tools for collecting task data from the Cognitive Atlas API
- **CLI Interface**: Command-line tool built with Typer
- **REST API**: FastAPI-based web API
- **Data Organization**: Automated directory structure creation and file management
- **Rate-Limited Collection**: Respectful API usage with configurable delays
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

### Cognitive Atlas Data Collection

#### Quick Example
```python
from hed_task.cognitive_atlas_collector import CognitiveAtlasCollector

# Collect all task data (takes ~1 hour)
collector = CognitiveAtlasCollector()
summary_df = collector.collect_all_task_data()
print(f"Collected {len(summary_df)} tasks!")
```

#### Targeted Collection
```python
# Collect specific tasks only
task_ids = ["trm_4f24126c8c83a", "trm_4cacee4a1d875"]
collector = CognitiveAtlasCollector(output_dir="./results")
filtered_df = collector.collect_specific_tasks(task_ids)
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

## Documentation

- **📚 [Quick Start Guide](docs/quickstart.md)** - Get running in 5 minutes
- **📖 [Complete Tutorial](docs/cognitive_atlas_tutorial.md)** - Comprehensive guide with examples
- **🔍 [API Reference](docs/api_reference.md)** - Detailed method documentation
- **⚙️ [Development Guide](docs/development.md)** - Setup and contribution workflow

## Examples

See the [examples/](examples/) directory for:
- **Basic collection workflows**
- **Targeted data gathering**
- **Data analysis patterns**
- **Integration examples**

## Development

See [docs/development.md](docs/development.md) for detailed development setup and workflow.

## Dependencies

- **FastAPI**: Modern web framework for building APIs
- **Typer**: CLI framework based on Python type hints
- **pandas**: Data manipulation and analysis
- **cognitiveatlas**: Cognitive Atlas Python interface
- **pytest**: Testing framework
- **ruff**: Fast Python linter and formatter
- **mypy**: Static type checker

## License

This project is licensed under the terms specified in the LICENSE file.
