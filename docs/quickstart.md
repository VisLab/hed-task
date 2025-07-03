# Quick Start Guide

Get up and running with Cognitive Atlas data collection in 5 minutes.

## Prerequisites

- Python 3.8+
- Internet connection
- ~1GB free disk space (for full collection)

## Installation

```bash
# Using uv (recommended)
uv add hed-task

# Using pip
pip install hed-task
```

## 30-Second Example

```python
from hed_task.cognitive_atlas_collector import CognitiveAtlasCollector

# Collect all tasks (this will take ~1 hour)
collector = CognitiveAtlasCollector()
summary_df = collector.collect_all_task_data()

print(f"✅ Collected {len(summary_df)} tasks!")
```

## 5-Minute Targeted Collection

```python
from hed_task.cognitive_atlas_collector import CognitiveAtlasCollector

# 1. Initialize collector
collector = CognitiveAtlasCollector(
    output_dir="./my_results",
    delay_seconds=2.0  # Faster for small collections
)

# 2. Get task summary to explore
summary_df = collector.get_all_tasks_summary()
print(f"Available tasks: {len(summary_df)}")

# 3. Find tasks of interest
memory_tasks = summary_df[
    summary_df['definition_text'].str.contains('memory', case=False)
]
print(f"Memory-related tasks: {len(memory_tasks)}")

# 4. Collect detailed data for subset (fast!)
if len(memory_tasks) <= 20:  # Keep it manageable
    memory_ids = memory_tasks['id'].tolist()
    detailed_df = collector.collect_specific_tasks(memory_ids)
    print(f"✅ Collected detailed data for {len(detailed_df)} memory tasks")
```

## Command Line Usage

```bash
# Collect all tasks
python -m hed_task.cognitive_atlas_collector

# Or from examples directory
python examples/cognitive_atlas_collection.py
```

## What You Get

Your results will be in `./my_results/` (or `H:\CogTaskResults\` by default):

```
my_results/
├── task_summary.tsv                    # All tasks overview
├── trm_4f24126c8c83a/                 # Go/No-go Task
│   └── trm_4f24126c8c83a_details.json
├── trm_4cacee4a1d875/                 # Stroop Task
│   └── trm_4cacee4a1d875_details.json
└── ...
```

## Common Use Cases

### Just Browse Available Tasks
```python
collector = CognitiveAtlasCollector()
summary = collector.get_all_tasks_summary()
print(summary[['id', 'name']].head(10))
```

### Collect Specific Tasks
```python
task_ids = ["trm_4f24126c8c83a", "trm_4cacee4a1d875"]
collector.collect_specific_tasks(task_ids)
```

### Search and Collect
```python
# Find Stroop-related tasks
stroop_tasks = summary[summary['name'].str.contains('Stroop', case=False)]
stroop_ids = stroop_tasks['id'].tolist()
collector.collect_specific_tasks(stroop_ids)
```

## Next Steps

- 📖 Read the [Full Tutorial](cognitive_atlas_tutorial.md) for comprehensive examples
- 🔍 Check [API Documentation](api_info.md) for detailed reference
- 💡 See [Example Scripts](../examples/) for real-world usage patterns
- 🚀 Start exploring your collected data with pandas/jupyter

## Quick Tips

- ⏱️ Full collection takes ~1 hour (854 tasks × 5 seconds)
- 🔒 Be respectful: don't reduce delay below 1 second
- 💾 Results are resumable - rerun to collect missing tasks
- 🎯 Start small with specific tasks before full collection
