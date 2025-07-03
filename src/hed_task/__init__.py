"""HED Task - Exploration of task structure and its annotation with HED."""

__version__ = "0.1.0"

# Import main functions for easy access
from .download_pubmed import process_citations, save_pubmed_summary
from .summarize_citations import summarize_citations
from .task_collector import process_all_tasks, retrieve_task_info, retrieve_tasks

__all__ = [
    "process_all_tasks",
    "retrieve_tasks",
    "retrieve_task_info",
    "summarize_citations",
    "process_citations",
    "save_pubmed_summary",
]
