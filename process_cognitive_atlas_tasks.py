#!/usr/bin/env python3
"""
Cognitive Atlas Task Processing Script

This script processes all tasks from the Cognitive Atlas API by:
1. Retrieving the full list of tasks
2. Creating directories for each task ID
3. Downloading detailed task information and saving as JSON files
4. Creating a summary DataFrame with all task information

Usage:
    python process_cognitive_atlas_tasks.py [output_directory]

Example:
    python process_cognitive_atlas_tasks.py cognitive_atlas_data
"""

import argparse
import sys
from pathlib import Path

# Add src directory to path to import our module
sys.path.insert(0, str(Path(__file__).parent / "src"))

from get_task_info import process_all_tasks


def main():
    parser = argparse.ArgumentParser(
        description="Process all tasks from Cognitive Atlas API",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )

    parser.add_argument(
        "output_dir",
        nargs="?",
        default="cognitive_atlas_tasks",
        help="Output directory for task data (default: cognitive_atlas_tasks)",
    )

    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable verbose output"
    )

    args = parser.parse_args()

    print("=" * 60)
    print("Cognitive Atlas Task Processing")
    print("=" * 60)
    print(f"Output directory: {args.output_dir}")
    print()

    try:
        # Check if cognitiveatlas package is available
        import cognitiveatlas

        print(f"Using cognitiveatlas package version: {cognitiveatlas.__version__}")
    except ImportError:
        print("ERROR: cognitiveatlas package not found!")
        print("Please install it using: pip install cognitiveatlas")
        return 1
    except AttributeError:
        print("Using cognitiveatlas package (version not available)")

    # Run the processing workflow
    try:
        summary_df = process_all_tasks(args.output_dir)

        if summary_df is not None:
            print("\n" + "=" * 60)
            print("SUCCESS: All tasks processed successfully!")
            print("=" * 60)
            return 0
        else:
            print("\n" + "=" * 60)
            print("WARNING: No tasks were successfully processed")
            print("=" * 60)
            return 1

    except KeyboardInterrupt:
        print("\n\nProcessing interrupted by user.")
        return 1
    except Exception as e:
        print(f"\n\nERROR: An unexpected error occurred: {e}")
        import traceback

        traceback.print_exc()
        return 1


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
