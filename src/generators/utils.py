"""Shared utility functions for the HED Task documentation generators."""

from __future__ import annotations

import json
from pathlib import Path


def load_json(path: Path) -> dict | list:
    """Load a JSON file with UTF-8 encoding."""
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def write_page(path: Path, content: str) -> None:
    """Write a UTF-8 text file, creating parent dirs as needed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    # newline="" suppresses the Windows CRLF translation that would otherwise
    # conflict with the eol=lf policy in .gitattributes.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(content)


def task_page_path(hedtsk_id: str) -> str:
    """Return relative path from docs/ root to a task page (no .md extension)."""
    return f"tasks/{hedtsk_id}"


def category_page_path(category_id: str) -> str:
    """Return relative path from docs/ root to a category page (no .md extension)."""
    return f"processes/{category_id}"


def process_link(process_id: str, process_name: str, category_id: str) -> str:
    """Return a Markdown link to a process on its category page.

    Path is relative from docs/ root.
    """
    return f"[{process_name}](processes/{category_id}.md#{process_id})"


def process_link_from_tasks(process_id: str, process_name: str, category_id: str) -> str:
    """Return a Markdown link to a process, from a file inside docs/tasks/."""
    return f"[{process_name}](../processes/{category_id}.md#{process_id})"


def task_link(hedtsk_id: str, canonical_name: str) -> str:
    """Return a Markdown link to a task page (from docs/ root)."""
    return f"[{canonical_name}](tasks/{hedtsk_id}.md)"


def task_link_from_processes(hedtsk_id: str, canonical_name: str) -> str:
    """Return a Markdown link to a task page, from a file inside docs/processes/."""
    return f"[{canonical_name}](../tasks/{hedtsk_id}.md)"


def truncate(text: str, max_len: int = 100) -> str:
    """Truncate text to max_len characters, appending ellipsis if needed."""
    if len(text) <= max_len:
        return text
    return text[:max_len].rstrip() + "\u2026"
