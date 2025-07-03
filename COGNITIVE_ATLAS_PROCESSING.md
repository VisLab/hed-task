# Cognitive Atlas Task Processing

This directory contains scripts to process all tasks from the Cognitive Atlas API.

## What it does

The processing workflow:

1. **Retrieves the full list of tasks** from the Cognitive Atlas API
2. **Creates directories** for each task ID under the output directory
3. **Downloads detailed task information** for each task and saves it as `{id}_details.json`
4. **Creates a summary DataFrame** with top-level information from all tasks
5. **Saves the summary** as both CSV and JSON files

## Files

- `src/get_task_info` - Main module with processing functions
- `run_task_processing.py` - Simple script to run the workflow
- `process_cognitive_atlas_tasks.py` - Full-featured command-line script

## Usage

### Quick Start

Run from the repository root:

```bash
python run_task_processing.py
```

This will create a `cognitive_atlas_tasks` directory with all processed data.

### Custom Output Directory

```bash
python run_task_processing.py --output-dir my_custom_directory
```

### Using the Full Script

```bash
python process_cognitive_atlas_tasks.py [output_directory]
```

## Output Structure

After running, you'll get:

```
cognitive_atlas_tasks/
├── task_summary.csv          # Summary of all tasks
├── task_summary.json         # Summary in JSON format
├── task_id_1/
│   └── task_id_1_details.json
├── task_id_2/
│   └── task_id_2_details.json
└── ...
```

## Requirements

- Python 3.9+
- cognitiveatlas package
- pandas

The dependencies are already defined in `pyproject.toml`.

## Example Usage in Code

```python
from src.get_task_info import process_all_tasks, retrieve_tasks, retrieve_task_info

# Get just the task list
task_df = retrieve_tasks()

# Get detailed info for a specific task
task_details = retrieve_task_info("task_id", "task_name")

# Run the full processing workflow
summary_df = process_all_tasks("output_directory")
```
