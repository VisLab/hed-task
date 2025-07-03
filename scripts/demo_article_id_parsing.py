#!/usr/bin/env python3
"""Demonstrate the ArticleIdList parsing functionality."""

import json
import sys
from pathlib import Path

# Add the src directory to Python path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from hed_task.download_pubmed import parse_article_ids


def demo_article_id_parsing():
    """Demonstrate parsing of ArticleIdList from a sample PubMed record."""

    print("HED Task - Article ID Parsing Demo")
    print("=" * 40)

    # Load the sample PubMed record
    sample_file = Path(
        "src/cogat_data/task_data/trm_4af89b3a925ca/15708213_pubmed.json"
    )

    if not sample_file.exists():
        print(f"ERROR: Sample PubMed file not found: {sample_file}")
        return False

    try:
        with open(sample_file, encoding="utf-8") as f:
            record = json.load(f)

        # Extract ArticleIdList
        pubmed_data = record["PubmedArticle"][0].get("PubmedData", {})
        article_id_list = pubmed_data.get("ArticleIdList", [])

        print(f"Sample PubMed record: {sample_file.name}")
        print(f"ArticleIdList: {article_id_list}")
        print()

        # Parse the IDs
        pmid, pmcid, doi, other_ids = parse_article_ids(article_id_list)

        print("Parsed results:")
        print(f"  PMID: '{pmid}'")
        print(f"  PMCID: '{pmcid}'")
        print(f"  DOI: '{doi}'")
        print(f"  Other IDs: {other_ids}")
        print()

        # Test with additional sample data to show different ID types
        print("Testing with additional sample data:")

        test_cases = [
            [
                "12345678",
                "10.1016/j.example.2023.01.001",
                "PMC1234567",
                "S1234-5678(23)00001-2",
            ],
            ["10.1038/nature12345", "PMC987654", "23456789"],
            ["34567890", "unknown-id-format", "10.1126/science.abc123"],
        ]

        for i, test_ids in enumerate(test_cases, 1):
            print(f"\nTest case {i}: {test_ids}")
            pmid, pmcid, doi, other_ids = parse_article_ids(test_ids)
            print(
                f"  → PMID: '{pmid}', PMCID: '{pmcid}', DOI: '{doi}', Other: {other_ids}"
            )

        print("\n" + "=" * 50)
        print("Article ID parsing demo completed!")
        print("=" * 50)
        return True

    except Exception as e:
        print(f"ERROR: {e}")
        import traceback

        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = demo_article_id_parsing()
    sys.exit(0 if success else 1)
