"""Citation summary generation from collected task data.

This module processes task data directories to extract citation information,
creates individual citation detail files, and generates a comprehensive
citation summary TSV file.
"""

import argparse
import json
import logging
from pathlib import Path
from typing import Any, Union

import pandas as pd

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(), logging.FileHandler("citation_processing.log")],
)
logger = logging.getLogger(__name__)


def compare_citation_details(
    existing_citation: dict[str, Any], new_citation: dict[str, Any]
) -> bool:
    """Compare two citation dictionaries for equality.

    Args:
        existing_citation: The existing citation data
        new_citation: The new citation data to compare

    Returns:
        True if citations are identical, False otherwise
    """
    # Compare key fields that should be identical
    key_fields = ["id", "citation_pmid", "citation_url", "citation_desc", "doi"]

    for field in key_fields:
        if existing_citation.get(field, "") != new_citation.get(field, ""):
            return False
    return True


def extract_citation_id(citation: dict[str, Any]) -> str:
    """Extract a unique citation ID from citation data.

    Args:
        citation: Citation dictionary

    Returns:
        A unique citation ID string
    """
    # Use the citation's 'id' field if available, otherwise create one
    if "id" in citation and citation["id"]:
        return str(citation["id"])

    # Fallback: create ID from PMID or URL
    citation_pmid = citation.get("citation_pmid")
    if citation_pmid:
        return f"pmid_{citation_pmid}"

    citation_url = citation.get("citation_url")
    if citation_url:
        # Extract a reasonable ID from URL
        url_parts = str(citation_url).split("/")
        for part in reversed(url_parts):
            if part and not part.startswith("http"):
                return f"url_{part}"

    # Last resort: use hash of description
    desc = citation.get("citation_desc", "unknown")
    return f"desc_{hash(desc) % 1000000}"


def process_citation(
    citation: dict[str, Any], task_id: str, citation_data_dir: Path
) -> dict[str, Any]:
    """Process a single citation: create citation file and return summary data.

    Args:
        citation: Citation dictionary from task data
        task_id: The ID of the task this citation belongs to
        citation_data_dir: Path to citation_data directory

    Returns:
        Dictionary with citation summary data for the TSV
    """
    # Extract citation ID
    cit_id = extract_citation_id(citation)

    # Create citation directory
    citation_dir = citation_data_dir / cit_id
    citation_dir.mkdir(exist_ok=True)

    # Prepare citation details with consistent structure
    citation_details = {
        "id": cit_id,
        "citation_pmid": citation.get("citation_pmid", ""),
        "citation_url": citation.get("citation_url", ""),
        "citation_desc": citation.get("citation_desc", ""),
        "doi": citation.get("doi", ""),  # Add DOI field if available
        "citation_pubname": citation.get("citation_pubname", ""),
        "citation_authors": citation.get("citation_authors", ""),
        "citation_pubdate": citation.get("citation_pubdate", ""),
        "citation_type": citation.get("citation_type", ""),
        "citation_source": citation.get("citation_source", ""),
        "citation_comment": citation.get("citation_comment", ""),
        "related_tasks": [task_id],  # Track which tasks reference this citation
    }

    # Check if citation details file already exists
    citation_file = citation_dir / "citation_details.json"

    if citation_file.exists():
        try:
            with open(citation_file, encoding="utf-8") as f:
                existing_details = json.load(f)

            # Compare the citations
            if not compare_citation_details(existing_details, citation_details):
                logger.warning(
                    f"Citation conflict detected for ID {cit_id} from task {task_id}. "
                    f"Existing and new citation data differ."
                )
                # Add the new task to related_tasks if not already present
                if task_id not in existing_details.get("related_tasks", []):
                    existing_details["related_tasks"].append(task_id)
                    citation_details = existing_details
            else:
                # Citations match, just add task ID if not present
                if task_id not in existing_details.get("related_tasks", []):
                    existing_details["related_tasks"].append(task_id)
                citation_details = existing_details

        except (json.JSONDecodeError, KeyError) as e:
            logger.error(f"Error reading existing citation file {citation_file}: {e}")
            # Continue with new citation details

    # Write/update the citation details file
    try:
        with open(citation_file, "w", encoding="utf-8") as f:
            json.dump(citation_details, f, indent=2, ensure_ascii=False)
    except Exception as e:
        logger.error(f"Error writing citation file {citation_file}: {e}")

    # Return summary data for TSV
    return {
        "cit_id": cit_id,
        "task_id": task_id,
        "doi": citation_details.get("doi", ""),
        "citation_pmid": citation_details.get("citation_pmid", ""),
        "citation_url": citation_details.get("citation_url", ""),
        "citation_desc": citation_details.get("citation_desc", ""),
    }


def process_task_citations(
    task_dir: Path, citation_data_dir: Path
) -> list[dict[str, Any]]:
    """Process all citations from a single task directory.

    Args:
        task_dir: Path to the task directory
        citation_data_dir: Path to citation_data directory

    Returns:
        List of citation summary dictionaries
    """
    task_id = task_dir.name
    detail_file = task_dir / f"{task_id}_details.json"

    if not detail_file.exists():
        logger.warning(f"Details file not found for task {task_id}")
        return []

    try:
        with open(detail_file, encoding="utf-8") as f:
            task_details = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError) as e:
        logger.error(f"Error reading task details from {detail_file}: {e}")
        return []

    citations = task_details.get("citation", [])

    if not citations:
        logger.info(f"No citations found for task {task_id}")
        return []

    citation_summaries = []
    for citation in citations:
        try:
            summary = process_citation(citation, task_id, citation_data_dir)
            citation_summaries.append(summary)
            logger.debug(f"Processed citation {summary['cit_id']} for task {task_id}")
        except Exception as e:
            logger.error(f"Error processing citation for task {task_id}: {e}")
            continue

    return citation_summaries


def summarize_citations(cogat_data_path: Union[str, Path]) -> tuple[bool, int, int]:
    """Main function to process all task citations and generate summary.

    Args:
        cogat_data_path: Path to the cogat_data directory

    Returns:
        Tuple of (success: bool, num_tasks_processed: int, num_citations_processed: int)
    """
    cogat_data_path = Path(cogat_data_path)

    # Validate input directory
    if not cogat_data_path.exists():
        logger.error(f"Cogat data directory does not exist: {cogat_data_path}")
        return False, 0, 0

    task_data_dir = cogat_data_path / "task_data"
    citation_data_dir = cogat_data_path / "citation_data"

    if not task_data_dir.exists():
        logger.error(f"Task data directory does not exist: {task_data_dir}")
        return False, 0, 0

    # Create citation_data directory if it doesn't exist
    citation_data_dir.mkdir(exist_ok=True)

    # Get all task directories (those starting with 'trm_' or 'tsk_')
    task_dirs = [
        d
        for d in task_data_dir.iterdir()
        if d.is_dir() and (d.name.startswith("trm_") or d.name.startswith("tsk_"))
    ]

    logger.info(f"Found {len(task_dirs)} task directories to process")

    all_citation_summaries = []
    num_tasks_processed = 0

    for task_dir in task_dirs:
        try:
            citation_summaries = process_task_citations(task_dir, citation_data_dir)
            all_citation_summaries.extend(citation_summaries)
            if citation_summaries:  # Only count if we found citations
                num_tasks_processed += 1
        except Exception as e:
            logger.error(f"Error processing task directory {task_dir}: {e}")
            continue

    # Create citation summary DataFrame and save as TSV
    if all_citation_summaries:
        df = pd.DataFrame(all_citation_summaries)

        # Ensure column order
        column_order = [
            "cit_id",
            "task_id",
            "doi",
            "citation_pmid",
            "citation_url",
            "citation_desc",
        ]
        df = df.reindex(columns=column_order)

        # Save to TSV file
        output_file = cogat_data_path / "citation_summary.tsv"
        try:
            df.to_csv(output_file, sep="\t", index=False)
            logger.info(f"Successfully created citation summary: {output_file}")
            logger.info(
                f"Summary contains {len(df)} citation records from {num_tasks_processed} tasks"
            )
        except Exception as e:
            logger.error(f"Error saving citation summary to {output_file}: {e}")
            return False, num_tasks_processed, len(all_citation_summaries)
    else:
        logger.warning("No citations found to process")
        return False, 0, 0

    return True, num_tasks_processed, len(all_citation_summaries)


def main() -> int:
    """Command-line interface for citation summarization."""
    parser = argparse.ArgumentParser(
        description="Process task citations and generate citation summary"
    )
    parser.add_argument(
        "cogat_data_path",
        help="Path to the cogat_data directory containing task_data subdirectory",
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Enable verbose logging"
    )

    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    success, num_tasks, num_citations = summarize_citations(args.cogat_data_path)

    if success:
        print("✓ Citation processing completed successfully")
        print(f"  - Processed {num_tasks} tasks")
        print(f"  - Found {num_citations} citations")
        print("  - Created citation_summary.tsv")
    else:
        print("✗ Citation processing failed")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
