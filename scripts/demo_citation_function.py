#!/usr/bin/env python3
"""Direct test of the summarize_citations function.

This script demonstrates how to use the summarize_citations function
directly in Python code.
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
    """Demonstrate direct usage of summarize_citations function."""
    print("Direct Citation Processing Demo")
    print("=" * 40)

    # Path to cogat_data directory
    cogat_data_path = project_root / "src" / "cogat_data"

    print(f"Processing citations from: {cogat_data_path}")

    # Call the function directly
    success, num_tasks, num_citations = summarize_citations(cogat_data_path)

    if success:
        print(
            f"✓ Success! Processed {num_tasks} tasks and found {num_citations} citations"
        )

        # Check output files
        summary_file = cogat_data_path / "citation_summary.tsv"
        citation_data_dir = cogat_data_path / "citation_data"

        print(f"  Summary file: {summary_file}")
        print(
            f"  Citation directories: {len(list(citation_data_dir.iterdir()))} created"
        )

    else:
        print("✗ Processing failed")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
