"""Task information collection from Cognitive Atlas API.

This module provides functions to collect and organize task data from the
Cognitive Atlas API, creating structured directories and files for each task.
"""

import json
from pathlib import Path
from typing import Any, Optional, cast

import pandas as pd
from cognitiveatlas.api import get_task


def retrieve_task_info(
    task_id: str, task_name: Optional[str] = None
) -> Optional[dict[str, Any]]:
    """Retrieve detailed task information for a specific task ID.

    Args:
        task_id: The task identifier
        task_name: Optional task name for the API call

    Returns:
        Task details as dictionary, or None if retrieval failed
    """
    try:
        task = get_task(id=task_id, name=task_name)
        return task.json if task else None
    except Exception as e:
        print(f"Error retrieving task info for {task_id}: {e}")
        return None


def retrieve_tasks() -> pd.DataFrame:
    """Retrieve the full list of tasks from Cognitive Atlas API.

    Returns:
        DataFrame containing all available tasks, or empty DataFrame on error
    """
    try:
        task_list = get_task().json
        # Convert the task list to a DataFrame for easier manipulation
        task_df = pd.DataFrame(task_list)
        return task_df if not task_df.empty else pd.DataFrame()
    except Exception as e:
        print(f"Error retrieving tasks: {e}")
        return pd.DataFrame()


def process_all_tasks(output_dir: str = "task_data") -> Optional[pd.DataFrame]:
    """Complete workflow to process all tasks from Cognitive Atlas API.

    This function:
    1. Retrieves the full list of tasks
    2. Creates directories for each task
    3. Gets detailed task info and saves to individual JSON files
    4. Creates and saves summary DataFrame as TSV

    Args:
        output_dir: Directory where task data will be saved

    Returns:
        Summary DataFrame if successful, None otherwise
    """
    # Create main output directory
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)

    print("Retrieving task list from Cognitive Atlas API...")
    task_df = retrieve_tasks()

    if task_df.empty:
        print("No tasks retrieved. Exiting.")
        return None

    print(f"Found {len(task_df)} tasks. Processing...")

    # Initialize summary data
    summary_data = []
    successful_tasks = 0
    failed_tasks = 0

    # Process each task
    for idx, task_row in task_df.iterrows():
        task_id = task_row.get("id")
        task_name = task_row.get("name")

        if not task_id:
            print(f"Skipping task at index {idx}: No ID found")
            failed_tasks += 1
            continue

        print(
            f"Processing task {cast(int, idx) + 1}/{len(task_df)}: {task_id} - {task_name}"
        )

        # Create directory for this task
        task_dir = output_path / str(task_id)
        task_dir.mkdir(exist_ok=True)

        # Get detailed task information
        detailed_info = retrieve_task_info(task_id, task_name)

        if detailed_info:
            # Save detailed info to JSON file
            details_file = task_dir / f"{task_id}_details.json"
            try:
                with open(details_file, "w", encoding="utf-8") as f:
                    json.dump(detailed_info, f, indent=2, ensure_ascii=False)
                print(f"  ✓ Saved detailed info to {details_file}")
                successful_tasks += 1
            except Exception as e:
                print(f"  ✗ Error saving detailed info for {task_id}: {e}")
                failed_tasks += 1
                continue
        else:
            print(f"  ✗ Failed to retrieve detailed info for {task_id}")
            failed_tasks += 1
            continue

        # Add row to summary data (using top-level info from task list)
        summary_row = {
            "id": task_id,
            "name": task_name,
            "definition": task_row.get("definition", ""),
            "alias": task_row.get("alias", ""),
            "event_stamp": task_row.get("event_stamp", ""),
            "type": task_row.get("type", ""),
            "uri": task_row.get("uri", ""),
            "has_detailed_info": True,
        }
        summary_data.append(summary_row)

    # Create summary DataFrame
    if summary_data:
        summary_df = pd.DataFrame(summary_data)

        # Save summary DataFrame as TSV (tab-separated values)
        summary_tsv = output_path / "task_summary.tsv"
        summary_df.to_csv(summary_tsv, sep="\t", index=False)
        print(f"\n✓ Saved summary DataFrame to {summary_tsv}")

        # Also save as JSON for convenience
        summary_json = output_path / "task_summary.json"
        summary_df.to_json(summary_json, orient="records", indent=2)
        print(f"✓ Saved summary DataFrame to {summary_json}")

        print("\nProcessing complete!")
        print(f"  Total tasks processed: {len(task_df)}")
        print(f"  Successful: {successful_tasks}")
        print(f"  Failed: {failed_tasks}")
        print(f"  Output directory: {output_path.absolute()}")

        return summary_df
    else:
        print("\nNo successful tasks processed.")
        return None


if __name__ == "__main__":
    # Run the complete workflow with default settings
    summary = process_all_tasks()
    if summary is not None:
        print(f"\nSummary DataFrame shape: {summary.shape}")
        print("\nFirst few rows:")
        print(summary.head())
