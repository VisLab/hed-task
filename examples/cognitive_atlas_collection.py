"""Example script demonstrating Cognitive Atlas data collection."""

import json
from pathlib import Path

from hed_task.cognitive_atlas_collector import CognitiveAtlasCollector


def example_collect_all_tasks():
    """Example: Collect all tasks from Cognitive Atlas."""
    print("=== Example: Collecting All Tasks ===")

    # Initialize collector with custom output directory
    collector = CognitiveAtlasCollector(
        output_dir="H:\\CogTaskResults", delay_seconds=5.0
    )

    # Collect all task data
    summary_df = collector.collect_all_task_data()

    print("\nSummary:")
    print(f"- Total tasks collected: {len(summary_df)}")
    print(f"- Results saved in: {collector.output_dir}")
    print(f"- Task summary file: {collector.output_dir / 'task_summary.tsv'}")

    # Show first few tasks
    print("\nFirst 5 tasks:")
    print(summary_df.head().to_string(index=False))

    return summary_df


def example_collect_specific_tasks():
    """Example: Collect specific tasks only."""
    print("\n=== Example: Collecting Specific Tasks ===")

    # Example task IDs (you would replace these with actual IDs)
    task_ids = ["trm_4fba85a597ca9", "trm_another_task_id"]

    collector = CognitiveAtlasCollector(
        output_dir="H:\\CogTaskResults\\specific", delay_seconds=3.0
    )

    # Collect specific tasks
    summary_df = collector.collect_specific_tasks(task_ids)

    print(f"\nCollected {len(summary_df)} specific tasks")
    return summary_df


def example_examine_task_details():
    """Example: Examine the structure of collected task details."""
    print("\n=== Example: Examining Task Details Structure ===")

    # Look for existing task detail files
    results_dir = Path("H:\\CogTaskResults")

    if not results_dir.exists():
        print("No results directory found. Run collection first.")
        return

    # Find a task detail file
    detail_files = list(results_dir.glob("*/*_details.json"))

    if not detail_files:
        print("No task detail files found. Run collection first.")
        return

    # Examine the first detail file
    detail_file = detail_files[0]
    print(f"Examining: {detail_file}")

    with open(detail_file, encoding="utf-8") as f:
        task_details = json.load(f)

    print("\nTask detail structure:")
    print(f"- ID: {task_details.get('id', 'N/A')}")
    print(f"- Name: {task_details.get('name', 'N/A')}")
    print(f"- Type: {task_details.get('type', 'N/A')}")
    print(f"- Definition: {task_details.get('definition_text', 'N/A')[:100]}...")

    # Show main sections
    print("\nMain sections in task details:")
    for key in task_details.keys():
        if isinstance(task_details[key], list):
            print(f"- {key}: {len(task_details[key])} items")
        elif isinstance(task_details[key], dict):
            print(f"- {key}: dictionary with {len(task_details[key])} keys")
        else:
            print(f"- {key}: {type(task_details[key]).__name__}")

    # Show conditions if present
    if "conditions" in task_details and task_details["conditions"]:
        print(f"\nConditions ({len(task_details['conditions'])}):")
        for condition in task_details["conditions"][:3]:  # Show first 3
            print(
                f"- {condition.get('name', 'N/A')}: {condition.get('condition_description', 'N/A')}"
            )

    # Show concepts if present
    if "concepts" in task_details and task_details["concepts"]:
        print(f"\nConcepts ({len(task_details['concepts'])}):")
        for concept in task_details["concepts"][:3]:  # Show first 3
            print(
                f"- {concept.get('name', 'N/A')}: {concept.get('definition_text', 'N/A')[:50]}..."
            )


def main():
    """Run all examples."""
    try:
        # Example 1: Collect all tasks (commented out to avoid long runtime)
        # summary_df = example_collect_all_tasks()

        # Example 2: Collect specific tasks (commented out to avoid API calls)
        # example_collect_specific_tasks()

        # Example 3: Examine existing task details
        example_examine_task_details()

        print("\n=== Examples Complete ===")
        print("To run the full collection, uncomment the relevant lines in main()")
        print("or use the CLI commands:")
        print("  uv run hed-task collect-tasks")
        print("  uv run hed-task collect-specific TASK_ID1 TASK_ID2")
        print("  uv run hed-task list-tasks")

    except Exception as e:
        print(f"Error running examples: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    main()
