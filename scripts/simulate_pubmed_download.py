#!/usr/bin/env python3
"""Test script that simulates PubMed download using existing local data."""

import json
import shutil
import sys
from pathlib import Path

# Add the src directory to Python path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from hed_task.download_pubmed import (
    extract_and_save_abstract,
    parse_article_ids,
    save_pubmed_summary,
)


def simulate_pubmed_download():
    """Simulate PubMed download using existing local PubMed files."""

    print("HED Task - Simulated PubMed Download Test")
    print("=" * 50)

    # Configuration
    cogat_data_dir = Path("src/cogat_data")
    citation_data_dir = cogat_data_dir / "citation_data"
    task_data_dir = cogat_data_dir / "task_data"

    print(f"Cogat data directory: {cogat_data_dir.absolute()}")

    # Check if required files exist
    citation_summary_file = cogat_data_dir / "citation_summary.tsv"
    if not citation_summary_file.exists():
        print(f"ERROR: Citation summary file not found: {citation_summary_file}")
        print("Please run 'python -m hed_task.cli generate-citations' first.")
        return False

    # Find existing PubMed files in task_data
    existing_pubmed_files = []
    if task_data_dir.exists():
        for task_dir in task_data_dir.iterdir():
            if task_dir.is_dir():
                for pubmed_file in task_dir.glob("*_pubmed.json"):
                    existing_pubmed_files.append(pubmed_file)

    if not existing_pubmed_files:
        print("No existing PubMed files found in task_data for simulation.")
        return False

    print(f"Found {len(existing_pubmed_files)} existing PubMed files for simulation")

    try:
        # Read citation summary to get citation mappings
        summary_data = []
        citation_pmid_map = {}

        with open(citation_summary_file, encoding="utf-8") as f:
            f.readline()  # Skip header
            for line in f:
                parts = line.strip().split("\t")
                if len(parts) >= 4:
                    cit_id = parts[0]
                    citation_pmid = parts[3] if len(parts) > 3 and parts[3] else ""
                    if citation_pmid:
                        citation_pmid_map[citation_pmid] = cit_id

        print(f"Found {len(citation_pmid_map)} citations with PMIDs")

        # Process a few existing PubMed files
        processed_count = 0
        for pubmed_file in existing_pubmed_files[:3]:  # Process first 3 for demo
            pmid = pubmed_file.stem.replace("_pubmed", "")

            # Find corresponding citation
            cit_id = citation_pmid_map.get(pmid)
            if not cit_id:
                print(f"  Skipping {pmid} - no corresponding citation found")
                continue

            print(f"\nProcessing PMID {pmid} → Citation {cit_id}")

            # Load the PubMed record
            with open(pubmed_file, encoding="utf-8") as f:
                record = json.load(f)

            # Get citation directory
            cit_dir = citation_data_dir / cit_id
            if not cit_dir.exists():
                print(f"  Warning: Citation directory not found: {cit_dir}")
                continue

            # Copy PubMed record to citation directory
            dest_pubmed_file = cit_dir / f"{cit_id}_pubmed.json"
            shutil.copy2(pubmed_file, dest_pubmed_file)
            print(f"  ✓ Copied PubMed record to: {dest_pubmed_file}")

            # Extract and save abstract
            try:
                extract_and_save_abstract(cit_id, record, cit_dir)
                abstract_file = cit_dir / f"{cit_id}_abstract.md"
                if abstract_file.exists():
                    print(f"  ✓ Created abstract: {abstract_file}")
            except Exception as e:
                print(f"  Warning: Could not extract abstract: {e}")

            # Parse ArticleIdList
            try:
                pubmed_data = record["PubmedArticle"][0].get("PubmedData", {})
                article_id_list = pubmed_data.get("ArticleIdList", [])

                if article_id_list:
                    parsed_pmid, pmcid, doi, other_ids = parse_article_ids(
                        article_id_list
                    )
                    print(
                        f"  ✓ Parsed IDs - PMID: {parsed_pmid}, PMCID: {pmcid}, DOI: {doi}"
                    )

                    # Create summary entry
                    summary_data.append(
                        {
                            "citation_id": cit_id,
                            "citation_pmid": pmid,
                            "pmid": parsed_pmid,
                            "pmcid": pmcid,
                            "doi": doi,
                            "other": "; ".join(other_ids) if other_ids else "",
                        }
                    )
                else:
                    print("  Warning: No ArticleIdList found")
                    summary_data.append(
                        {
                            "citation_id": cit_id,
                            "citation_pmid": pmid,
                            "pmid": pmid,
                            "pmcid": "",
                            "doi": "",
                            "other": "",
                        }
                    )
            except Exception as e:
                print(f"  Warning: Could not parse article IDs: {e}")

            processed_count += 1

        # Save summary
        if summary_data:
            print(f"\nSaving PubMed summary with {len(summary_data)} entries...")
            save_pubmed_summary(summary_data, cogat_data_dir)

            pubmed_summary_file = cogat_data_dir / "pubmed_summary.tsv"
            if pubmed_summary_file.exists():
                print(f"✓ PubMed summary saved to: {pubmed_summary_file}")

                # Show sample results
                print("\nSample PubMed summary:")
                with open(pubmed_summary_file, encoding="utf-8") as f:
                    lines = f.readlines()
                    for line in lines[:4]:  # Show header + first 3 rows
                        print(f"  {line.strip()}")

        print("\n" + "=" * 50)
        print("SUCCESS: Simulated PubMed download completed!")
        print(f"Processed {processed_count} citations")
        print("=" * 50)
        return True

    except Exception as e:
        print(f"\nERROR during simulation: {e}")
        import traceback

        traceback.print_exc()
        return False


if __name__ == "__main__":
    # Check if we're in the right directory
    if not Path("src/cogat_data").exists():
        print("ERROR: Please run this script from the hed-task project root directory.")
        sys.exit(1)

    success = simulate_pubmed_download()
    sys.exit(0 if success else 1)
