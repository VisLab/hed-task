# Documentation Index

Welcome to the HED Task documentation! This package provides comprehensive tools for collecting and analyzing task data from the Cognitive Atlas.

## 🚀 Getting Started

New to the package? Start here:

1. **[Quick Start Guide](quickstart.md)** - Get up and running in 5 minutes
2. **[Complete Tutorial](cognitive_atlas_tutorial.md)** - Comprehensive walkthrough with examples
3. **[Example Scripts](../examples/)** - Real-world usage patterns

## 📚 Reference Documentation

- **[API Reference](api_reference.md)** - Complete method documentation
- **[Development Guide](development.md)** - Contributing and development setup
- **[Project Setup](PROJECT_SETUP.md)** - Initial project configuration

## 🎯 Use Cases

### Research Workflows
- **Systematic Data Collection**: Collect all 854+ tasks with organized file structure
- **Targeted Research**: Filter and collect tasks relevant to specific research questions
- **Data Integration**: Export data for use with other analysis tools

### Data Exploration
- **Task Discovery**: Browse and search available cognitive tasks
- **Metadata Analysis**: Analyze task definitions, conditions, and concepts
- **Relationship Mapping**: Explore connections between tasks and concepts

### Reproducible Research
- **Automated Collection**: Scriptable data gathering with error handling
- **Version Control**: Track exactly which tasks were collected when
- **Standardized Format**: Consistent JSON and TSV output formats

## 📁 Documentation Structure

```
docs/
├── README.md                     # This index file
├── quickstart.md                 # 5-minute getting started guide
├── cognitive_atlas_tutorial.md   # Complete tutorial with examples
├── api_reference.md              # Detailed API documentation
├── development.md                # Development and contribution guide
└── PROJECT_SETUP.md             # Initial project setup
```

## 🔗 External Resources

- **[Cognitive Atlas Website](http://www.cognitiveatlas.org/)** - Original data source
- **[Cognitive Atlas API](https://github.com/poldracklab/cognitiveatlas-python)** - Python client library
- **[HED Standards](https://www.hedtags.org/)** - Hierarchical Event Descriptors

## 💡 Quick Examples

### Collect All Tasks
```python
from hed_task.cognitive_atlas_collector import CognitiveAtlasCollector

collector = CognitiveAtlasCollector()
summary_df = collector.collect_all_task_data()
```

### Search and Collect
```python
# Get task summary
summary_df = collector.get_all_tasks_summary()

# Find memory-related tasks
memory_tasks = summary_df[
    summary_df['definition_text'].str.contains('memory', case=False)
]

# Collect detailed data
memory_ids = memory_tasks['id'].tolist()
collector.collect_specific_tasks(memory_ids)
```

### Browse Available Tasks
```python
summary_df = collector.get_all_tasks_summary()
print(f"Available tasks: {len(summary_df)}")
print(summary_df[['id', 'name']].head(10))
```

## 📊 Data Output

The package creates organized data structures:

```
output_directory/
├── task_summary.tsv                    # All tasks overview
├── trm_4f24126c8c83a/                 # Individual task directories
│   └── trm_4f24126c8c83a_details.json
├── trm_4cacee4a1d875/
│   └── trm_4cacee4a1d875_details.json
└── ...
```

## 🤝 Contributing

We welcome contributions! See the [Development Guide](development.md) for:
- Setting up your development environment
- Running tests and quality checks
- Submitting pull requests
- Code style guidelines

## 📧 Support

- **Issues**: Report bugs or request features on GitHub
- **Discussions**: Ask questions or share usage patterns
- **Documentation**: Suggest improvements to these docs

## 🏷️ Version Information

This documentation is for version 0.1.0 of the hed-task package.

Last updated: July 3, 2025
