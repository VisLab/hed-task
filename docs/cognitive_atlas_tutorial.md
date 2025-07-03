# Cognitive Atlas Data Collection Tutorial

This tutorial guides you through collecting task data from the Cognitive Atlas using the `hed-task` package.

## Table of Contents

1. [Overview](#overview)
2. [Quick Start](#quick-start)
3. [Basic Usage](#basic-usage)
4. [Advanced Usage](#advanced-usage)
5. [Understanding the Output](#understanding-the-output)
6. [Troubleshooting](#troubleshooting)
7. [Best Practices](#best-practices)

## Overview

The Cognitive Atlas (http://www.cognitiveatlas.org/) is a collaborative knowledge-building project that characterizes the state of current thought in cognitive science. This package provides tools to systematically collect and organize task data from their API.

### What You'll Get

- **Task Summary**: A comprehensive list of all available tasks with basic information
- **Detailed Task Data**: Individual JSON files with complete task information including conditions, concepts, and relationships
- **Organized Structure**: Data organized in directories by task ID for easy navigation

## Quick Start

### Installation

```bash
# Install the package
uv add hed-task

# Or if using pip
pip install hed-task
```

### Simplest Example

```python
from hed_task.cognitive_atlas_collector import CognitiveAtlasCollector

# Create collector and collect all data
collector = CognitiveAtlasCollector()
summary_df = collector.collect_all_task_data()

print(f"Collected {len(summary_df)} tasks")
```

This will:
1. Create a `H:\CogTaskResults` directory
2. Download summary information for all tasks
3. Save detailed information for each task in individual directories
4. Create a summary TSV file

## Basic Usage

### 1. Setting Up the Collector

```python
from hed_task.cognitive_atlas_collector import CognitiveAtlasCollector

# Basic setup with default settings
collector = CognitiveAtlasCollector()

# Custom setup
collector = CognitiveAtlasCollector(
    output_dir="./my_results",    # Custom output directory
    delay_seconds=2.0             # Faster requests (be respectful!)
)
```

### 2. Getting Task Summary Only

If you just want a list of available tasks without downloading detailed data:

```python
# Get summary DataFrame
summary_df = collector.get_all_tasks_summary()

print(f"Found {len(summary_df)} tasks")
print(summary_df.head())

# Save to file
summary_df.to_csv("task_list.csv", index=False)
```

### 3. Full Data Collection

To collect complete data for all tasks:

```python
# This will take a while (854+ tasks with 5-second delays)
summary_df = collector.collect_all_task_data()

print(f"Successfully collected data for {len(summary_df)} tasks")
```

Expected output:
```
Starting Cognitive Atlas data collection...
Found 854 tasks
Saved task summary to: H:\CogTaskResults\task_summary.tsv
Fetching details for task: Go/No-go Task (ID: trm_4f24126c8c83a)
Saved details to: H:\CogTaskResults\trm_4f24126c8c83a\trm_4f24126c8c83a_details.json
Waiting 5.0 seconds before next request...
...
Collection complete!
Successfully collected details for 849 tasks
Failed to collect details for 5 tasks
```

## Advanced Usage

### 1. Collecting Specific Tasks

When you only need data for certain tasks:

```python
# Define specific task IDs
task_ids = [
    "trm_4f24126c8c83a",  # Go/No-go Task
    "trm_4cacee4a1d875",  # Stroop Task
    "trm_50df0cb04fa79"   # N-back Task
]

# Collect only these tasks
filtered_df = collector.collect_specific_tasks(task_ids)
print(f"Collected {len(filtered_df)} specific tasks")
```

### 2. Finding Task IDs

To find task IDs for tasks you're interested in:

```python
# Get all tasks summary
summary_df = collector.get_all_tasks_summary()

# Search for tasks by name
stroop_tasks = summary_df[summary_df['name'].str.contains('Stroop', case=False)]
print(stroop_tasks[['id', 'name']])

# Search by keyword in definition
memory_tasks = summary_df[summary_df['definition_text'].str.contains('memory', case=False)]
print(f"Found {len(memory_tasks)} tasks related to memory")
```

### 3. Resuming Interrupted Collections

If your collection was interrupted, you can resume by checking what's already collected:

```python
import os
from pathlib import Path

# Check what's already collected
results_dir = Path("H:\\CogTaskResults")
existing_dirs = [d.name for d in results_dir.iterdir() if d.is_dir()]

# Get full task list
summary_df = collector.get_all_tasks_summary()

# Find missing tasks
missing_tasks = summary_df[~summary_df['id'].isin(existing_dirs)]
print(f"Need to collect {len(missing_tasks)} remaining tasks")

# Collect only missing tasks
if len(missing_tasks) > 0:
    missing_ids = missing_tasks['id'].tolist()
    collector.collect_specific_tasks(missing_ids)
```

### 4. Batch Processing with Custom Timing

For large collections, you might want custom timing:

```python
# Faster collection (use carefully - respect the API)
fast_collector = CognitiveAtlasCollector(delay_seconds=1.0)

# Conservative collection (for unreliable networks)
slow_collector = CognitiveAtlasCollector(delay_seconds=10.0)
```

## Understanding the Output

### Directory Structure

After collection, you'll have:

```
H:\CogTaskResults\
├── task_summary.tsv              # Summary of all tasks
├── trm_4f24126c8c83a\           # Task directory (Go/No-go Task)
│   └── trm_4f24126c8c83a_details.json
├── trm_4cacee4a1d875\           # Task directory (Stroop Task)
│   └── trm_4cacee4a1d875_details.json
└── ...
```

### Summary File (task_summary.tsv)

Tab-separated file with columns:
- `id`: Unique task identifier
- `name`: Human-readable task name
- `concept_class`: Concept class identifier
- `definition_text`: Brief task definition

### Detail Files (*_details.json)

Each task's detail file contains comprehensive information:

```json
{
  "id": "trm_4f24126c8c83a",
  "name": "Go/No-go Task",
  "type": "task",
  "definition_text": "A task requiring participants to respond to certain stimuli...",
  "conditions": [
    {
      "name": "go trial",
      "condition_description": "Trial requiring a response"
    }
  ],
  "concepts": [
    {
      "name": "response inhibition",
      "definition_text": "The ability to suppress inappropriate responses"
    }
  ],
  "implementations": [...],
  "contrasts": [...],
  "references": [...]
}
```

## Troubleshooting

### Common Issues

1. **Network Timeouts**
   ```python
   # Increase delay for unstable connections
   collector = CognitiveAtlasCollector(delay_seconds=10.0)
   ```

2. **Permission Errors**
   ```python
   # Use a directory you have write access to
   collector = CognitiveAtlasCollector(output_dir="./results")
   ```

3. **Memory Issues (Large Collections)**
   ```python
   # Process in batches
   summary_df = collector.get_all_tasks_summary()
   task_ids = summary_df['id'].tolist()

   # Process 100 tasks at a time
   batch_size = 100
   for i in range(0, len(task_ids), batch_size):
       batch = task_ids[i:i+batch_size]
       collector.collect_specific_tasks(batch)
   ```

4. **API Rate Limiting**
   ```
   Error: Too many requests
   ```
   Solution: Increase `delay_seconds` parameter

### Debugging

Enable verbose output:

```python
import logging
logging.basicConfig(level=logging.DEBUG)

# Your collection code here
```

Check API status:

```python
from cognitiveatlas.api import get_task

# Test basic connectivity
try:
    response = get_task()
    print(f"API working - found {len(response.json)} tasks")
except Exception as e:
    print(f"API issue: {e}")
```

## Best Practices

### 1. Respectful API Usage

- **Use appropriate delays**: Default 5 seconds is respectful
- **Don't run multiple collectors simultaneously**
- **Consider off-peak hours** for large collections

### 2. Data Management

- **Check existing data** before re-collecting
- **Use version control** for your analysis scripts
- **Document your collection parameters**

### 3. Error Handling

```python
try:
    summary_df = collector.collect_all_task_data()
except Exception as e:
    print(f"Collection failed: {e}")
    # Log the error, check network, etc.
```

### 4. Monitoring Progress

```python
import time
start_time = time.time()

summary_df = collector.collect_all_task_data()

duration = time.time() - start_time
print(f"Collection took {duration/60:.1f} minutes")
```

### 5. Data Validation

```python
# Verify collection completeness
summary_df = collector.get_all_tasks_summary()
results_dir = Path("H:\\CogTaskResults")

collected_ids = {d.name for d in results_dir.iterdir() if d.is_dir()}
expected_ids = set(summary_df['id'])

missing = expected_ids - collected_ids
print(f"Missing {len(missing)} tasks: {list(missing)[:5]}...")
```

## Example Workflows

### Workflow 1: Exploratory Analysis

```python
# 1. Get task summary
collector = CognitiveAtlasCollector()
summary_df = collector.get_all_tasks_summary()

# 2. Explore available tasks
print("Task categories:")
print(summary_df['concept_class'].value_counts())

# 3. Find interesting tasks
attention_tasks = summary_df[
    summary_df['definition_text'].str.contains('attention', case=False)
]

# 4. Collect detailed data for interesting tasks
if len(attention_tasks) < 50:  # Reasonable number
    attention_ids = attention_tasks['id'].tolist()
    collector.collect_specific_tasks(attention_ids)
```

### Workflow 2: Complete Data Archive

```python
# Full collection with monitoring
import time
from pathlib import Path

collector = CognitiveAtlasCollector(
    output_dir="./cognitive_atlas_archive",
    delay_seconds=5.0
)

print("Starting complete Cognitive Atlas collection...")
start_time = time.time()

try:
    summary_df = collector.collect_all_task_data()

    duration = time.time() - start_time
    print(f"\n✅ Collection complete!")
    print(f"Time taken: {duration/3600:.1f} hours")
    print(f"Tasks collected: {len(summary_df)}")

    # Create completion report
    report = f"""
Cognitive Atlas Collection Report
================================
Date: {time.strftime('%Y-%m-%d %H:%M:%S')}
Duration: {duration/3600:.1f} hours
Tasks: {len(summary_df)}
Output: {collector.output_dir.absolute()}
"""

    with open(collector.output_dir / "collection_report.txt", "w") as f:
        f.write(report)

except KeyboardInterrupt:
    print("\n⚠️  Collection interrupted by user")
except Exception as e:
    print(f"\n❌ Collection failed: {e}")
```

### Workflow 3: Targeted Research Collection

```python
# Collect tasks relevant to specific research
research_keywords = ['memory', 'attention', 'executive', 'working memory']

collector = CognitiveAtlasCollector()
summary_df = collector.get_all_tasks_summary()

# Find relevant tasks
relevant_tasks = pd.DataFrame()
for keyword in research_keywords:
    matches = summary_df[
        summary_df['definition_text'].str.contains(keyword, case=False) |
        summary_df['name'].str.contains(keyword, case=False)
    ]
    relevant_tasks = pd.concat([relevant_tasks, matches]).drop_duplicates()

print(f"Found {len(relevant_tasks)} tasks relevant to research")

# Collect detailed data
if len(relevant_tasks) > 0:
    task_ids = relevant_tasks['id'].tolist()
    detailed_df = collector.collect_specific_tasks(task_ids)

    # Save research-specific summary
    relevant_tasks.to_csv("research_relevant_tasks.csv", index=False)
```

## Next Steps

After collecting your data:

1. **Explore the detailed JSON files** to understand task structure
2. **Use pandas** to analyze the summary data
3. **Extract specific information** (conditions, concepts, etc.) for your research
4. **Cross-reference with other databases** using task IDs
5. **Create visualizations** of task relationships and categories

For more advanced usage, see:
- [API Reference](api_info.md)
- [Development Guide](development.md)
- [Example Scripts](../examples/)
