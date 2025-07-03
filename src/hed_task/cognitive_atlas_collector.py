"""Module for collecting task information from Cognitive Atlas.

This module provides the CognitiveAtlasCollector class for systematically
retrieving and organizing task data from the Cognitive Atlas API.

The Cognitive Atlas (http://www.cognitiveatlas.org/) is a collaborative
knowledge-building project that aims to develop a knowledge base (or ontology)
that characterizes the state of current thought in cognitive science.

Usage Examples:

    Basic collection of all tasks:
        from hed_task.cognitive_atlas_collector import CognitiveAtlasCollector

        collector = CognitiveAtlasCollector()
        summary_df = collector.collect_all_task_data()
        print(f"Collected {len(summary_df)} tasks")

    Custom configuration:
        collector = CognitiveAtlasCollector(
            output_dir="./my_cognitive_atlas_data",
            delay_seconds=2.0  # Faster collection
        )
        summary_df = collector.collect_all_task_data()

    Collect specific tasks only:
        collector = CognitiveAtlasCollector()
        task_ids = ["trm_4f24126c8c83a", "trm_4cacee4a1d875"]
        filtered_df = collector.collect_specific_tasks(task_ids)

    Get just the summary without detailed collection:
        collector = CognitiveAtlasCollector()
        summary_df = collector.get_all_tasks_summary()

    Command-line usage:
        python cognitive_atlas_collector.py

Dependencies:
    - cognitiveatlas: Python client for Cognitive Atlas API
    - pandas: Data manipulation and analysis
    - pathlib: Object-oriented filesystem paths
"""

import json
import time
from pathlib import Path
from typing import Any, Optional, cast

import pandas as pd
from cognitiveatlas.api import get_task, get_tasks


class CognitiveAtlasCollector:
    """Collector for Cognitive Atlas task data.

    This class provides a comprehensive interface for collecting task information
    from the Cognitive Atlas API. It can retrieve both summary information for
    all tasks and detailed information for individual tasks, saving the data
    in an organized directory structure.

    The collector creates the following output structure:
    - {output_dir}/task_summary.tsv: Summary of all tasks
    - {output_dir}/{task_id}/{task_id}_details.json: Detailed info for each task

    Examples:
        Basic usage - collect all tasks:
        >>> collector = CognitiveAtlasCollector()
        >>> summary_df = collector.collect_all_task_data()
        >>> print(f"Collected {len(summary_df)} tasks")

        Custom output directory with faster requests:
        >>> collector = CognitiveAtlasCollector(
        ...     output_dir="./my_results",
        ...     delay_seconds=2.0
        ... )
        >>> summary_df = collector.collect_all_task_data()

        Collect specific tasks only:
        >>> collector = CognitiveAtlasCollector()
        >>> specific_tasks = ["trm_4f24126c8c83a", "trm_4cacee4a1d875"]
        >>> filtered_df = collector.collect_specific_tasks(specific_tasks)

        Get just the summary without detailed data:
        >>> collector = CognitiveAtlasCollector()
        >>> summary_df = collector.get_all_tasks_summary()
        >>> print(summary_df.head())

    Attributes:
        output_dir (Path): Directory where results are saved
        delay_seconds (float): Delay between API requests to respect rate limits
    """

    def __init__(
        self, output_dir: str = "H:\\CogTaskResults", delay_seconds: float = 5.0
    ):
        """Initialize the collector.

        Args:
            output_dir: Directory to save results to. Will be created if it doesn't exist.
                       Defaults to "H:\\CogTaskResults"
            delay_seconds: Delay between API requests to be respectful to the service.
                          Recommended minimum is 1.0 seconds. Defaults to 5.0 seconds.

        Note:
            The delay_seconds parameter helps prevent overwhelming the Cognitive Atlas
            API servers. A delay of 5 seconds is conservative and respectful.
        """
        self.output_dir = Path(output_dir)
        self.delay_seconds = delay_seconds
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def get_all_tasks_summary(self) -> pd.DataFrame:
        """Get a summary of all tasks from Cognitive Atlas.

        This method retrieves the complete list of tasks from the Cognitive Atlas
        API and returns a DataFrame with basic information for each task.

        Returns:
            DataFrame with columns:
                - id: Unique task identifier
                - name: Human-readable task name
                - concept_class: Concept class identifier
                - definition_text: Brief definition of the task

        Raises:
            ValueError: If the API request fails or returns no data

        Example:
            >>> collector = CognitiveAtlasCollector()
            >>> summary_df = collector.get_all_tasks_summary()
            >>> print(f"Found {len(summary_df)} tasks")
            >>> print(summary_df.columns.tolist())
            ['id', 'name', 'concept_class', 'definition_text']
        """
        print("Fetching task list from Cognitive Atlas...")
        tasks_response = get_tasks()

        if not hasattr(tasks_response, "json") or not tasks_response.json:
            raise ValueError("Failed to fetch tasks from Cognitive Atlas")

        tasks_data = tasks_response.json

        # Extract summary information
        summary_data = []
        for task in tasks_data:
            summary_data.append(
                {
                    "id": task.get("id", ""),
                    "name": task.get("name", ""),
                    "concept_class": task.get("id_concept_class", ""),
                    "definition_text": task.get("definition_text", ""),
                }
            )

        return pd.DataFrame(summary_data)

    def get_task_details(
        self, task_id: str, task_name: str
    ) -> Optional[dict[str, Any]]:
        """Get detailed information for a specific task.

        Args:
            task_id: The task ID
            task_name: The task name

        Returns:
            Task details as a dictionary, or None if failed
        """
        try:
            print(f"Fetching details for task: {task_name} (ID: {task_id})")
            task_response = get_task(id=task_id, name=task_name)

            if hasattr(task_response, "json") and task_response.json:
                return cast(dict[str, Any], task_response.json)
            else:
                print(f"Warning: No details found for task {task_id}")
                return None

        except Exception as e:
            print(f"Error fetching task {task_id}: {e}")
            return None

    def save_task_details(self, task_details: dict[str, Any], task_id: str) -> None:
        """Save task details to a JSON file in a subdirectory.

        Args:
            task_details: The task details dictionary
            task_id: The task ID (used for directory and filename)
        """
        # Create subdirectory for this task
        task_dir = self.output_dir / task_id
        task_dir.mkdir(exist_ok=True)

        # Save JSON file
        json_file = task_dir / f"{task_id}_details.json"
        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(task_details, f, indent=4, ensure_ascii=False)

        print(f"Saved details to: {json_file}")

    def collect_all_task_data(self) -> pd.DataFrame:
        """Collect all task data and save to files.

        This is the main method that performs the complete workflow:
        1. Retrieves summary information for all tasks
        2. Saves the summary to a TSV file
        3. For each task, retrieves detailed information
        4. Saves detailed information to individual JSON files in subdirectories
        5. Applies rate limiting between requests

        The method creates the following file structure:
        - {output_dir}/task_summary.tsv: Tab-separated summary of all tasks
        - {output_dir}/{task_id}/{task_id}_details.json: Detailed info for each task

        Returns:
            DataFrame with task summary information (same as get_all_tasks_summary())

        Example:
            >>> collector = CognitiveAtlasCollector(output_dir="./results")
            >>> summary_df = collector.collect_all_task_data()
            Starting Cognitive Atlas data collection...
            Found 854 tasks
            Saved task summary to: ./results/task_summary.tsv
            Fetching details for task: Go/No-go Task (ID: trm_4f24126c8c83a)
            ...
            Collection complete!
            Successfully collected details for 849 tasks
            Failed to collect details for 5 tasks
        """
        print("Starting Cognitive Atlas data collection...")

        # Get summary of all tasks
        summary_df = self.get_all_tasks_summary()
        print(f"Found {len(summary_df)} tasks")

        # Save summary to TSV file
        summary_file = self.output_dir / "task_summary.tsv"
        summary_df.to_csv(summary_file, sep="\t", index=False)
        print(f"Saved task summary to: {summary_file}")

        # Collect detailed information for each task
        successful_details = 0
        failed_details = 0

        for idx, row in summary_df.iterrows():
            task_id = row["id"]
            task_name = row["name"]

            if not task_id:  # Skip if no ID
                print(f"Skipping task with no ID: {task_name}")
                continue

            # Get detailed information
            task_details = self.get_task_details(task_id, task_name)

            if task_details:
                self.save_task_details(task_details, task_id)
                successful_details += 1
            else:
                failed_details += 1

            # Pause between requests to be respectful to the API
            if (
                cast(int, idx) < len(summary_df) - 1
            ):  # Don't pause after the last request
                print(f"Waiting {self.delay_seconds} seconds before next request...")
                time.sleep(self.delay_seconds)

        print("\nCollection complete!")
        print(f"Successfully collected details for {successful_details} tasks")
        print(f"Failed to collect details for {failed_details} tasks")
        print(f"Results saved in: {self.output_dir}")

        return summary_df

    def collect_specific_tasks(self, task_ids: list[str]) -> pd.DataFrame:
        """Collect data for specific tasks only.

        This method allows you to collect detailed information for a subset
        of tasks rather than all available tasks. Useful when you only need
        data for specific experiments or when testing the collector.

        Args:
            task_ids: List of task IDs to collect. Task IDs should be in the
                     format used by Cognitive Atlas (e.g., "trm_4f24126c8c83a")

        Returns:
            DataFrame with collected task information (filtered subset of summary)

        Example:
            >>> collector = CognitiveAtlasCollector()
            >>> # Collect data for just two specific tasks
            >>> task_ids = ["trm_4f24126c8c83a", "trm_4cacee4a1d875"]
            >>> filtered_df = collector.collect_specific_tasks(task_ids)
            Collecting data for 2 specific tasks...
            Found 2 matching tasks
            Saved filtered task summary to: H:\\CogTaskResults\task_summary_filtered.tsv
            ...
            Collection complete!
            Successfully collected details for 2 tasks
            Failed to collect details for 0 tasks
        """
        print(f"Collecting data for {len(task_ids)} specific tasks...")

        # Get full task list to get names
        all_tasks_df = self.get_all_tasks_summary()

        # Filter to requested tasks
        filtered_df = all_tasks_df[all_tasks_df["id"].isin(task_ids)].copy()

        if len(filtered_df) == 0:
            print("No matching tasks found!")
            return pd.DataFrame()

        print(f"Found {len(filtered_df)} matching tasks")

        # Save filtered summary
        summary_file = self.output_dir / "task_summary_filtered.tsv"
        filtered_df.to_csv(summary_file, sep="\t", index=False)
        print(f"Saved filtered task summary to: {summary_file}")

        # Collect detailed information
        successful_details = 0
        failed_details = 0

        for idx, row in filtered_df.iterrows():
            task_id = row["id"]
            task_name = row["name"]

            # Get detailed information
            task_details = self.get_task_details(task_id, task_name)

            if task_details:
                self.save_task_details(task_details, task_id)
                successful_details += 1
            else:
                failed_details += 1

            # Pause between requests
            if cast(int, idx) < len(filtered_df) - 1:
                print(f"Waiting {self.delay_seconds} seconds before next request...")
                time.sleep(self.delay_seconds)

        print("\nCollection complete!")
        print(f"Successfully collected details for {successful_details} tasks")
        print(f"Failed to collect details for {failed_details} tasks")

        return filtered_df


def main() -> None:
    """Main function for command-line usage.

    When run as a script, this function creates a CognitiveAtlasCollector
    with default settings and collects data for all available tasks.

    Example:
        $ python cognitive_atlas_collector.py
        Starting Cognitive Atlas data collection...
        Found 854 tasks
        Saved task summary to: H:\\CogTaskResults\task_summary.tsv
        ...
        Collection complete!
        Successfully collected details for 849 tasks
        Failed to collect details for 5 tasks

        Collected data for 854 tasks
    """
    collector = CognitiveAtlasCollector()
    summary_df = collector.collect_all_task_data()
    if summary_df is not None:
        print(f"\nCollected data for {len(summary_df)} tasks")


if __name__ == "__main__":
    main()
