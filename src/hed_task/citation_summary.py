"""Citation summary generation from collected task data.

This module processes task data directories to extract citation information
and create a comprehensive citation summary spreadsheet.
"""

import json
from pathlib import Path
from typing import Union

import pandas as pd


def extract_citations_from_task(task_details: dict) -> list[dict[str, str]]:
    """Extract citation information from a task details dictionary.

    Args:
        task_details: The task details dictionary loaded from JSON

    Returns:
        List of citation dictionaries with pmid, url, and description
    """
    citations = []
    task_id = task_details.get("id", "")
    citation_data = task_details.get("citation", [])

    if citation_data:
        for citation in citation_data:
            citations.append(
                {
                    "id": task_id,
                    "citation_pmid": citation.get("citation_pmid", ""),
                    "citation_url": citation.get("citation_url", ""),
                    "citation_desc": citation.get("citation_desc", ""),
                }
            )
    else:
        # Add empty citation row for tasks with no citations
        citations.append(
            {
                "id": task_id,
                "citation_pmid": "",
                "citation_url": "",
                "citation_desc": "",
            }
        )

    return citations


def get_citation_summary(
    task_data_path: Union[str, Path] = "src/task_data",
) -> pd.DataFrame:
    """Process task data to create a citation summary.

    This function scans the task data directory for task-specific JSON files,
    extracts citation information from each, and compiles it into a single
    DataFrame.

    Args:
        task_data_path: Path to the directory containing task data subdirectories

    Returns:
        DataFrame with columns:
        - id: The task ID
        - citation_pmid: The PubMed ID of the citation
        - citation_url: The URL for the citation
        - citation_desc: The description of the citation

    Note:
        If a task has no citations, it will still be included in the summary with
        empty values for the citation-related columns.
    """
    task_data_path = Path(task_data_path)

    if not task_data_path.exists():
        print(f"Warning: Task data path {task_data_path} does not exist")
        return pd.DataFrame()

    all_citations = []

    # Get all task directories
    task_dirs = [
        d for d in task_data_path.iterdir() if d.is_dir() and d.name.startswith("trm_")
    ]

    print(f"Found {len(task_dirs)} task directories to process")

    for task_dir in task_dirs:
        task_id = task_dir.name
        detail_file_path = task_dir / f"{task_id}_details.json"

        if detail_file_path.exists():
            try:
                with open(detail_file_path, encoding="utf-8") as f:
                    task_details = json.load(f)

                # Extract citations for this task
                task_citations = extract_citations_from_task(task_details)
                all_citations.extend(task_citations)

            except json.JSONDecodeError:
                print(f"Warning: Could not decode JSON from {detail_file_path}")
                # Add empty citation row for failed JSON decode
                all_citations.append(
                    {
                        "id": task_id,
                        "citation_pmid": "",
                        "citation_url": "",
                        "citation_desc": "",
                    }
                )
            except Exception as e:
                print(f"Warning: Error processing {detail_file_path}: {e}")
                # Add empty citation row for other errors
                all_citations.append(
                    {
                        "id": task_id,
                        "citation_pmid": "",
                        "citation_url": "",
                        "citation_desc": "",
                    }
                )
        else:
            print(f"Warning: Details file not found for task {task_id}")
            # Add empty citation row for missing details file
            all_citations.append(
                {
                    "id": task_id,
                    "citation_pmid": "",
                    "citation_url": "",
                    "citation_desc": "",
                }
            )

    if all_citations:
        df = pd.DataFrame(all_citations)
        print(f"Successfully processed {len(df)} citation records")
        return df
    else:
        print("No citation data found to process.")
        return pd.DataFrame()


def save_citation_summary(
    task_data_path: Union[str, Path] = "src/task_data",
    output_filename: str = "citation_summary.tsv",
) -> bool:
    """Generate and save citation summary to a TSV file.

    Args:
        task_data_path: Path to the directory containing task data
        output_filename: Name of the output file (will be saved in task_data_path)

    Returns:
        True if successful, False otherwise
    """
    try:
        df = get_citation_summary(task_data_path)

        if df.empty:
            print("No citation data to save.")
            return False

        output_path = Path(task_data_path) / output_filename
        df.to_csv(output_path, sep="\t", index=False)
        print(f"Successfully created {output_path}")
        return True

    except Exception as e:
        print(f"Error saving citation summary: {e}")
        return False


if __name__ == "__main__":
    # Run with default settings
    success = save_citation_summary()
    if success:
        print("Citation summary generation completed successfully.")
    else:
        print("Citation summary generation failed.")
