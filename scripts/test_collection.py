"""Quick test script for Cognitive Atlas collection using the existing task_details1.json."""

import json
from pathlib import Path

import pandas as pd


def test_with_existing_data():
    """Test the data structure with the existing task_details1.json file."""

    # Load the existing task details
    task_file = Path("h:/task_details1.json")

    if not task_file.exists():
        print(f"Task file not found: {task_file}")
        return

    with open(task_file, encoding="utf-8") as f:
        task_details = json.load(f)

    print("=== Analyzing existing task data ===")
    print(f"Task ID: {task_details.get('id', 'N/A')}")
    print(f"Task Name: {task_details.get('name', 'N/A')}")
    print(f"Task Type: {task_details.get('type', 'N/A')}")
    print(f"Concept Class: {task_details.get('id_concept_class', 'N/A')}")
    print(f"Definition: {task_details.get('definition_text', 'N/A')}")

    # Create a sample DataFrame entry
    summary_data = {
        "id": task_details.get("id", ""),
        "name": task_details.get("name", ""),
        "concept_class": task_details.get("id_concept_class", ""),
        "definition_text": task_details.get("definition_text", ""),
    }

    # Create DataFrame
    df = pd.DataFrame([summary_data])
    print("\n=== Sample DataFrame ===")
    print(df.to_string(index=False))

    # Create output directory structure as would be done by collector
    output_dir = Path("H:/CogTaskResults")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Save sample TSV
    tsv_file = output_dir / "task_summary_sample.tsv"
    df.to_csv(tsv_file, sep="\t", index=False)
    print(f"\n=== Sample TSV saved to: {tsv_file} ===")

    # Create task subdirectory and save JSON
    task_id = task_details.get("id", "unknown_task")
    task_dir = output_dir / task_id
    task_dir.mkdir(exist_ok=True)

    json_file = task_dir / f"{task_id}_details.json"
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(task_details, f, indent=4, ensure_ascii=False)

    print(f"=== Task details saved to: {json_file} ===")

    # Analyze the task structure
    print("\n=== Task Structure Analysis ===")
    for key, value in task_details.items():
        if isinstance(value, list):
            print(f"{key}: {len(value)} items")
            if value and len(value) > 0:
                print(f"  First item type: {type(value[0]).__name__}")
                if isinstance(value[0], dict) and value[0]:
                    print(f"  First item keys: {list(value[0].keys())[:5]}...")
        elif isinstance(value, dict):
            print(f"{key}: dict with {len(value)} keys")
        else:
            print(f"{key}: {type(value).__name__}")

    print("\n=== Directory structure created ===")
    print(f"Output directory: {output_dir}")
    print(f"Task subdirectory: {task_dir}")
    print("Files created:")
    print(f"  - {tsv_file}")
    print(f"  - {json_file}")

    return df, task_details


if __name__ == "__main__":
    test_with_existing_data()
