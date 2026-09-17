"""Generate docs/index.md — the site homepage."""

from __future__ import annotations

from pathlib import Path

from generators.utils import write_page


def generate(
    docs_dir: Path,
    tasks: list[dict],
    processes: list[dict],
    categories: list[dict],
) -> None:
    """Write docs/index.md."""
    total_tasks = len(tasks)
    total_processes = len(processes)
    total_categories = len(categories)
    total_links = sum(len(t.get("hed_process_ids", [])) for t in tasks)

    content = f"""\
# HED task catalog

This catalog defines {total_tasks} standard cognitive and behavioral neuroscience tasks
and {total_processes} cognitive processes organized into {total_categories} categories.
It is part of the HED (Hierarchical Event Descriptors) standardization effort, which aims
to provide uniform, machine-readable annotation of experimental events in neuroscience data.

The catalog provides standard definitions, inclusion criteria, named variations, and
process linkages for widely used experimental paradigms, enabling consistent annotation
across laboratories and datasets.

## Catalog at a glance

| Item | Count |
|------|-------|
| Tasks | {total_tasks} |
| Cognitive processes | {total_processes} |
| Process categories | {total_categories} |
| Task-process links | {total_links} |

## Contents

```{{toctree}}
:maxdepth: 2

tasks/index
processes/index
crossref
atlas/index
methodology/index
criteria/index
```
"""
    write_page(docs_dir / "index.md", content)
