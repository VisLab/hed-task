#!/usr/bin/env python3
"""Test script for citation processing functionality.

This script tests the new citation processing functionality to ensure
it works correctly with the reorganized data structure.
"""

import sys
from pathlib import Path

# Add the src directory to Python path
script_dir = Path(__file__).parent
project_root = script_dir.parent
src_dir = project_root / "src"
sys.path.insert(0, str(src_dir))

from hed_task.summarize_citations import summarize_citations  # noqa: E402


def main():
    """Test citation processing with the current data structure."""
    print("Testing Citation Processing")
    print("=" * 50)

    # Path to cogat_data directory
    cogat_data_path = project_root / "src" / "cogat_data"

    print(f"Cogat data path: {cogat_data_path}")
    print(f"Path exists: {cogat_data_path.exists()}")

    if not cogat_data_path.exists():
        print("ERROR: Cogat data path does not exist!")
        return 1

    # Check subdirectories
    task_data_path = cogat_data_path / "task_data"
    citation_data_path = cogat_data_path / "citation_data"

    print(f"Task data path: {task_data_path} (exists: {task_data_path.exists()})")
    print(
        f"Citation data path: {citation_data_path} (exists: {citation_data_path.exists()})"
    )

    if not task_data_path.exists():
        print("ERROR: Task data directory does not exist!")
        return 1

    # Count task directories
    task_dirs = [
        d
        for d in task_data_path.iterdir()
        if d.is_dir() and (d.name.startswith("trm_") or d.name.startswith("tsk_"))
    ]
    print(f"Found {len(task_dirs)} task directories")

    # Run citation processing
    print("\nRunning citation processing...")
    try:
        success, num_tasks, num_citations = summarize_citations(cogat_data_path)

        if success:
            print("✓ Citation processing completed successfully!")
            print(f"  - Processed {num_tasks} tasks")
            print(f"  - Found {num_citations} citations")

            # Check output files
            citation_summary_file = cogat_data_path / "citation_summary.tsv"
            print(
                f"  - Citation summary file: {citation_summary_file} (exists: {citation_summary_file.exists()})"
            )

            if citation_summary_file.exists():
                print(f"  - File size: {citation_summary_file.stat().st_size} bytes")

            # Check citation_data directory
            citation_dirs = [d for d in citation_data_path.iterdir() if d.is_dir()]
            print(f"  - Created {len(citation_dirs)} citation directories")

        else:
            print("✗ Citation processing failed!")
            return 1

    except Exception as e:
        print(f"✗ Error during citation processing: {e}")
        return 1

    print("\nTest completed successfully!")
    return 0


if __name__ == "__main__":
    exit(main())
