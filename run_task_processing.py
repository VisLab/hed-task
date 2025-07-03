"""
Simple script to run the Cognitive Atlas task processing workflow.

This script can be run directly from the repository root directory.
"""

import sys
from pathlib import Path

from get_task_info import process_all_tasks

# Add the src directory to Python path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Process Cognitive Atlas tasks")
    parser.add_argument(
        "--output-dir",
        default="cognitive_atlas_tasks",
        help="Output directory for processed tasks (default: cognitive_atlas_tasks)",
    )

    args = parser.parse_args()

    print("Starting Cognitive Atlas task processing...")
    print(f"Output directory: {args.output_dir}")
    print("-" * 50)

    # Run the main processing function
    summary_df = process_all_tasks(args.output_dir)

    if summary_df is not None:
        print("\n" + "=" * 50)
        print("Processing completed successfully!")
        print(f"Summary DataFrame shape: {summary_df.shape}")
        print("=" * 50)
    else:
        print("\n" + "=" * 50)
        print("Processing failed or no data retrieved.")
        print("=" * 50)
