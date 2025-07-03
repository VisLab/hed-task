# API Reference

Complete reference for the `hed-task` Cognitive Atlas collection package.

## CognitiveAtlasCollector

### Class: `CognitiveAtlasCollector`

Main class for collecting task data from the Cognitive Atlas API.

```python
from hed_task.cognitive_atlas_collector import CognitiveAtlasCollector
```

#### Constructor

```python
CognitiveAtlasCollector(output_dir="H:\\CogTaskResults", delay_seconds=5.0)
```

**Parameters:**
- `output_dir` (str): Directory to save results to. Created if it doesn't exist.
  - Default: `"H:\\CogTaskResults"`
  - Example: `"./my_results"`, `"/path/to/data"`
- `delay_seconds` (float): Delay between API requests in seconds.
  - Default: `5.0`
  - Minimum recommended: `1.0`
  - Range: `0.1` to `60.0`

**Attributes:**
- `output_dir` (Path): Resolved output directory path
- `delay_seconds` (float): Request delay setting

#### Methods

##### `get_all_tasks_summary()`

Retrieve summary information for all tasks.

```python
summary_df = collector.get_all_tasks_summary()
```

**Returns:**
- `pd.DataFrame`: Summary data with columns:
  - `id` (str): Unique task identifier (e.g., "trm_4f24126c8c83a")
  - `name` (str): Human-readable task name (e.g., "Go/No-go Task")
  - `concept_class` (str): Concept class identifier
  - `definition_text` (str): Brief task definition

**Raises:**
- `ValueError`: If API request fails or returns no data
- `requests.RequestException`: If network request fails

**Example:**
```python
collector = CognitiveAtlasCollector()
df = collector.get_all_tasks_summary()
print(f"Found {len(df)} tasks")
print(df.head())
```

##### `get_task_details(task_id, task_name)`

Get detailed information for a specific task.

```python
details = collector.get_task_details(task_id, task_name)
```

**Parameters:**
- `task_id` (str): Task identifier (required)
- `task_name` (str): Task name (required for API call)

**Returns:**
- `Dict[str, Any]` or `None`: Task details dictionary or None if failed

**Task Details Structure:**
```python
{
    "id": "trm_4f24126c8c83a",
    "name": "Go/No-go Task",
    "type": "task",
    "definition_text": "Description...",
    "conditions": [
        {
            "name": "go trial",
            "condition_description": "..."
        }
    ],
    "concepts": [
        {
            "name": "response inhibition",
            "definition_text": "..."
        }
    ],
    "implementations": [...],
    "contrasts": [...],
    "references": [...]
}
```

**Example:**
```python
details = collector.get_task_details("trm_4f24126c8c83a", "Go/No-go Task")
if details:
    print(f"Task: {details['name']}")
    print(f"Conditions: {len(details.get('conditions', []))}")
```

##### `save_task_details(task_details, task_id)`

Save task details to a JSON file.

```python
collector.save_task_details(task_details, task_id)
```

**Parameters:**
- `task_details` (Dict[str, Any]): Task details dictionary
- `task_id` (str): Task identifier for directory/filename

**Side Effects:**
- Creates directory: `{output_dir}/{task_id}/`
- Creates file: `{output_dir}/{task_id}/{task_id}_details.json`

**Example:**
```python
details = collector.get_task_details("trm_123", "Task Name")
if details:
    collector.save_task_details(details, "trm_123")
```

##### `collect_all_task_data()`

Comprehensive method to collect all available task data.

```python
summary_df = collector.collect_all_task_data()
```

**Process:**
1. Retrieves task summary via `get_all_tasks_summary()`
2. Saves summary to `task_summary.tsv`
3. For each task:
   - Gets detailed information
   - Saves to individual JSON file
   - Applies rate limiting delay
4. Reports success/failure statistics

**Returns:**
- `pd.DataFrame`: Task summary (same as `get_all_tasks_summary()`)

**Side Effects:**
- Creates `{output_dir}/task_summary.tsv`
- Creates `{output_dir}/{task_id}/{task_id}_details.json` for each task

**Example:**
```python
collector = CognitiveAtlasCollector(delay_seconds=3.0)
summary_df = collector.collect_all_task_data()
print(f"Collected {len(summary_df)} tasks")
```

##### `collect_specific_tasks(task_ids)`

Collect data for specific tasks only.

```python
filtered_df = collector.collect_specific_tasks(task_ids)
```

**Parameters:**
- `task_ids` (List[str]): List of task IDs to collect

**Returns:**
- `pd.DataFrame`: Filtered summary data for requested tasks

**Side Effects:**
- Creates `{output_dir}/task_summary_filtered.tsv`
- Creates detail files for each specified task

**Example:**
```python
task_ids = ["trm_4f24126c8c83a", "trm_4cacee4a1d875"]
df = collector.collect_specific_tasks(task_ids)
print(f"Collected {len(df)} specific tasks")
```

## Utility Functions

### `main()`

Command-line entry point for the module.

```python
from hed_task.cognitive_atlas_collector import main
main()
```

Equivalent to:
```bash
python -m hed_task.cognitive_atlas_collector
```

## Data Formats

### Summary TSV Format

Tab-separated values file with columns:

| Column | Type | Description | Example |
|--------|------|-------------|---------|
| id | str | Task identifier | trm_4f24126c8c83a |
| name | str | Task name | Go/No-go Task |
| concept_class | str | Concept class | tsk_4a57abb949b60 |
| definition_text | str | Task definition | A task requiring... |

### Detail JSON Format

Each task detail file follows this structure:

```json
{
  "id": "string",
  "name": "string",
  "type": "task",
  "definition_text": "string",
  "alias": "string",
  "event_stamp": "timestamp",
  "uri": "url",
  "conditions": [
    {
      "id": "string",
      "name": "string",
      "condition_description": "string"
    }
  ],
  "concepts": [
    {
      "id": "string",
      "name": "string",
      "definition_text": "string"
    }
  ],
  "implementations": [...],
  "contrasts": [...],
  "references": [...]
}
```

## Error Handling

### Common Exceptions

- `ValueError`: API returned no data or invalid response
- `requests.RequestException`: Network connectivity issues
- `FileNotFoundError`: Output directory permissions issue
- `json.JSONDecodeError`: Malformed API response
- `KeyboardInterrupt`: User interruption (handled gracefully)

### Error Recovery

The collector handles errors gracefully:

```python
try:
    summary_df = collector.collect_all_task_data()
except Exception as e:
    print(f"Collection failed: {e}")
    # Partial results may still be available in output directory
```

### Resumable Operations

Collections can be resumed by re-running. The collector will:
- Skip tasks that already have detail files
- Continue from where it left off
- Append to existing summary files

## Performance Considerations

### Memory Usage

- Summary data: ~1-2 MB for all tasks
- Detail files: ~1-50 KB per task
- Total collection: ~50-100 MB

### Network Usage

- Summary request: 1 API call
- Detail requests: 1 API call per task (854+ total)
- Rate limiting: Built-in delays prevent overwhelming the API

### Time Estimates

| Collection Type | Delay | Estimated Time |
|----------------|-------|----------------|
| Full (854 tasks) | 5.0s | ~70 minutes |
| Full (854 tasks) | 2.0s | ~30 minutes |
| Subset (50 tasks) | 5.0s | ~4 minutes |
| Summary only | N/A | ~10 seconds |

## Configuration Examples

### Conservative (Recommended)
```python
collector = CognitiveAtlasCollector(
    output_dir="./results",
    delay_seconds=5.0
)
```

### Fast (Use Carefully)
```python
collector = CognitiveAtlasCollector(
    output_dir="./results",
    delay_seconds=1.0  # Minimum recommended
)
```

### Research Archive
```python
collector = CognitiveAtlasCollector(
    output_dir="/data/cognitive_atlas_archive",
    delay_seconds=10.0  # Very conservative
)
```

## Integration Examples

### With Pandas
```python
import pandas as pd

summary_df = collector.get_all_tasks_summary()

# Filter and analyze
memory_tasks = summary_df[
    summary_df['definition_text'].str.contains('memory', case=False)
]

# Export for other tools
memory_tasks.to_excel('memory_tasks.xlsx', index=False)
```

### With Jupyter
```python
# In a Jupyter notebook
%matplotlib inline
import matplotlib.pyplot as plt

summary_df = collector.get_all_tasks_summary()

# Visualize task name lengths
name_lengths = summary_df['name'].str.len()
plt.hist(name_lengths, bins=20)
plt.title('Distribution of Task Name Lengths')
plt.show()
```

### With JSON Processing
```python
import json
from pathlib import Path

# Process all collected detail files
results_dir = Path("./results")
for detail_file in results_dir.glob("*/*_details.json"):
    with open(detail_file) as f:
        task_data = json.load(f)

    # Extract specific information
    conditions = task_data.get('conditions', [])
    print(f"{task_data['name']}: {len(conditions)} conditions")
```

## Version Compatibility

- Python: 3.8+
- cognitiveatlas: 0.2.0+
- pandas: 1.0+
- pathlib: Built-in (Python 3.4+)

## See Also

- [Cognitive Atlas Tutorial](cognitive_atlas_tutorial.md) - Comprehensive guide with examples
- [Quick Start Guide](quickstart.md) - Get running in 5 minutes
- [Example Scripts](../examples/) - Real-world usage patterns
- [Cognitive Atlas Website](http://www.cognitiveatlas.org/) - Original data source
