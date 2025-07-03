"""HED Task - Exploration of task structure and its annotation with HED."""

__version__ = "0.1.0"

# Import main functions for easy access
from .citation_summary import get_citation_summary, save_citation_summary
from .task_collector import process_all_tasks, retrieve_task_info, retrieve_tasks

__all__ = [
    "process_all_tasks",
    "retrieve_tasks",
    "retrieve_task_info",
    "get_citation_summary",
    "save_citation_summary",
]
