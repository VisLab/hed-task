#!/usr/bin/env python3
"""Test script for the new PubMed download functionality."""

import sys
from pathlib import Path

# Add the src directory to Python path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from hed_task.download_pubmed import (
    process_citations,
    save_pubmed_summary,
    setup_logging,
)


def test_pubmed_download():
    """Test the PubMed download functionality with a small subset."""

    # Set up logging
    setup_logging("INFO")

    # Configuration
    cogat_data_dir = Path("src/cogat_data")
    email = "test@example.com"  # Replace with a real email for actual testing
    request_rate = 1.0
    limit = 3  # Process only first 3 citations for testing

    print(f"Testing PubMed download with {limit} citations...")
    print(f"Cogat data directory: {cogat_data_dir.absolute()}")

    # Check if required files exist
    citation_summary_file = cogat_data_dir / "citation_summary.tsv"
    if not citation_summary_file.exists():
        print(f"ERROR: Citation summary file not found: {citation_summary_file}")
        print("Please run 'python -m hed_task.cli generate-citations' first.")
        return False

    try:
        # Process citations (with limit for testing)
        print("\nProcessing citations...")
        summary_data = process_citations(
            cogat_data_dir=cogat_data_dir,
            email=email,
            request_rate=request_rate,
            limit=limit,
        )

        print(f"✓ Processed {len(summary_data)} citations")

        # Save summary
        print("\nSaving PubMed summary...")
        save_pubmed_summary(summary_data, cogat_data_dir)

        # Check results
        pubmed_summary_file = cogat_data_dir / "pubmed_summary.tsv"
        if pubmed_summary_file.exists():
            print(f"✓ PubMed summary saved to: {pubmed_summary_file}")

            # Show sample results
            print("\nSample results:")
            with open(pubmed_summary_file, encoding="utf-8") as f:
                lines = f.readlines()
                for line in lines[:4]:  # Show header + first 3 rows
                    print(f"  {line.strip()}")

        # Check for created files in citation directories
        citation_data_dir = cogat_data_dir / "citation_data"
        if citation_data_dir.exists():
            created_files = []
            for cit_dir in citation_data_dir.iterdir():
                if cit_dir.is_dir():
                    pubmed_file = cit_dir / f"{cit_dir.name}_pubmed.json"
                    abstract_file = cit_dir / f"{cit_dir.name}_abstract.md"
                    if pubmed_file.exists():
                        created_files.append(f"PubMed: {pubmed_file}")
                    if abstract_file.exists():
                        created_files.append(f"Abstract: {abstract_file}")

            if created_files:
                print(
                    f"\n✓ Created {len(created_files)} files in citation directories:"
                )
                for file_info in created_files[:5]:  # Show first 5
                    print(f"  {file_info}")
                if len(created_files) > 5:
                    print(f"  ... and {len(created_files) - 5} more")

        print("\n" + "=" * 50)
        print("SUCCESS: PubMed download test completed!")
        print("=" * 50)
        return True

    except Exception as e:
        print(f"\nERROR during testing: {e}")
        import traceback

        traceback.print_exc()
        return False


if __name__ == "__main__":
    print("HED Task - PubMed Download Test")
    print("=" * 40)

    # Note about email requirement
    print(
        "\nNOTE: For actual PubMed API calls, you need to provide a real email address."
    )
    print(
        "This test uses a placeholder email and may fail if PubMed records are fetched."
    )
    print("To test with real API calls, update the 'email' variable in the script.\n")

    # Check if we're in the right directory
    if not Path("src/cogat_data").exists():
        print("ERROR: Please run this script from the hed-task project root directory.")
        sys.exit(1)

    success = test_pubmed_download()
    sys.exit(0 if success else 1)
