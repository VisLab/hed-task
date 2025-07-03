"""Download citation information from PubMed for citations processed by the HED task pipeline."""

import argparse
import csv
import json
import logging
import time
from pathlib import Path
from typing import Any, Optional

from Bio import Entrez


def setup_logging(log_level: str = "INFO", log_file: Optional[str] = None) -> None:
    """Set up logging configuration."""
    # Clear any existing handlers
    logging.getLogger().handlers.clear()

    handlers: list[logging.Handler] = []
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    handlers.append(console_handler)

    # File handler (if log_file is specified)
    if log_file:
        file_handler = logging.FileHandler(
            log_file, mode="w", encoding="utf-8"
        )  # Use 'w' to overwrite
        file_handler.setFormatter(formatter)
        handlers.append(file_handler)

    logging.basicConfig(
        level=getattr(logging, log_level.upper()),
        handlers=handlers,
        force=True,  # Force reconfiguration
    )


def get_args() -> argparse.Namespace:
    """Gets the command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Download citation information from PubMed based on citation_summary.tsv"
    )
    parser.add_argument(
        "--email", required=True, help="Email address for NCBI Entrez API."
    )
    parser.add_argument(
        "--cogat-data-dir", required=True, help="Path to the cogat_data directory."
    )
    parser.add_argument(
        "--limit", type=int, help="Limit the number of records to process."
    )
    parser.add_argument(
        "--request-rate",
        type=float,
        default=1.0,
        help="Delay between NCBI API requests in seconds.",
    )
    parser.add_argument(
        "--log-level",
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        help="Set the logging level",
    )
    parser.add_argument(
        "--log-file", help="Path to log file (logs to console only if not specified)"
    )
    return parser.parse_args()


def fetch_pubmed_details(
    pmid: str, email: str, request_rate: float
) -> Optional[dict[str, Any]]:
    """Fetches details for a given PubMed ID."""
    Entrez.email = email
    try:
        logging.debug(f"Fetching PubMed record for PMID: {pmid}")
        handle = Entrez.efetch(db="pubmed", id=pmid, rettype="abstract", retmode="xml")
        records = Entrez.read(handle)
        handle.close()
        time.sleep(request_rate)  # Be nice to NCBI servers
        return records  # type: ignore[no-any-return]
    except Exception as e:
        logging.error(f"Error fetching pmid {pmid}: {e}")
        return None


def parse_article_ids(article_id_list: list[str]) -> tuple[str, str, str, list[str]]:
    """
    Parse ArticleIdList to extract pmid, pmcid, doi, and other IDs.

    Args:
        article_id_list: List of article IDs from PubMed record

    Returns:
        Tuple of (pmid, pmcid, doi, other_ids)
    """
    pmid = ""
    pmcid = ""
    doi = ""
    other_ids = []

    for article_id in article_id_list:
        article_id_str = str(article_id)

        # Check if it's a DOI (starts with 10.)
        if article_id_str.startswith("10."):
            doi = article_id_str
        # Check if it's a PMC ID (starts with PMC or is all digits as PMID)
        elif article_id_str.startswith("PMC"):
            pmcid = article_id_str
        # Check if it's likely a PMID (all digits)
        elif article_id_str.isdigit():
            pmid = article_id_str
        else:
            # Everything else goes to other_ids
            other_ids.append(article_id_str)

    return pmid, pmcid, doi, other_ids


def save_pubmed_record(
    cit_id: str, pmid: str, record: dict[str, Any], citation_dir: Path
) -> None:
    """Saves the PubMed record to a JSON file in the citation directory."""
    try:
        pubmed_file = citation_dir / f"{cit_id}_pubmed.json"
        with open(pubmed_file, "w", encoding="utf-8") as f:
            json.dump(record, f, ensure_ascii=False, indent=2)
        logging.debug(f"Saved PubMed record to {pubmed_file}")
    except Exception as e:
        logging.error(f"Error saving PubMed record for {cit_id}: {e}")


def extract_and_save_abstract(
    cit_id: str, record: dict[str, Any], citation_dir: Path
) -> None:
    """Extracts and saves abstract as markdown if available."""
    try:
        article = record["PubmedArticle"][0]["MedlineCitation"]["Article"]
        abstract_parts = article.get("Abstract", {}).get("AbstractText", [])

        if abstract_parts:
            # Join abstract parts and create markdown
            abstract_text = " ".join(str(part) for part in abstract_parts)

            # Create markdown content
            title = article.get("ArticleTitle", "No title available")
            markdown_content = f"# {title}\n\n## Abstract\n\n{abstract_text}\n"

            # Save as markdown file
            abstract_file = citation_dir / f"{cit_id}_abstract.md"
            with open(abstract_file, "w", encoding="utf-8") as f:
                f.write(markdown_content)
            logging.debug(f"Saved abstract to {abstract_file}")
    except Exception as e:
        logging.error(f"Error extracting/saving abstract for {cit_id}: {e}")


def process_citations(
    cogat_data_dir: Path, email: str, request_rate: float, limit: Optional[int] = None
) -> list[dict[str, str]]:
    """Process citations from citation_summary.tsv and download PubMed records."""
    citation_summary_file = cogat_data_dir / "citation_summary.tsv"
    citation_data_dir = cogat_data_dir / "citation_data"

    if not citation_summary_file.exists():
        raise FileNotFoundError(
            f"Citation summary file not found: {citation_summary_file}"
        )

    summary_data = []
    missing_pmids = []
    processed_count = 0

    logging.info(f"Reading citation summary from {citation_summary_file}")

    with open(citation_summary_file, newline="", encoding="utf-8") as tsvfile:
        reader = csv.DictReader(tsvfile, delimiter="\t")

        rows = list(reader)
        if limit:
            rows = rows[:limit]
            logging.info(f"Processing limited to {limit} citations")

        total_rows = len(rows)
        logging.info(f"Processing {total_rows} citations")

        for row in rows:
            cit_id = row.get("cit_id", "").strip()
            citation_pmid = row.get("citation_pmid", "").strip()
            doi = row.get("doi", "").strip()

            processed_count += 1

            if not cit_id:
                logging.warning(f"Row {processed_count}: Missing cit_id, skipping")
                continue

            logging.info(f"Processing {processed_count}/{total_rows}: {cit_id}")

            # Initialize summary entry
            summary_entry = {
                "citation_id": cit_id,
                "citation_pmid": citation_pmid,
                "pmid": "",
                "pmcid": "",
                "doi": doi,  # Use existing DOI from citation_summary
                "other": "",
            }

            if citation_pmid:
                logging.info(f"  Fetching PubMed record for PMID: {citation_pmid}")

                # Fetch PubMed record
                record = fetch_pubmed_details(citation_pmid, email, request_rate)

                if record:
                    try:
                        # Get citation directory
                        citation_dir = citation_data_dir / cit_id
                        citation_dir.mkdir(exist_ok=True)

                        # Save PubMed record
                        save_pubmed_record(cit_id, citation_pmid, record, citation_dir)

                        # Extract and save abstract if available
                        extract_and_save_abstract(cit_id, record, citation_dir)

                        # Parse ArticleIdList from PubmedData section
                        pubmed_data = record["PubmedArticle"][0].get("PubmedData", {})
                        article_id_list = pubmed_data.get("ArticleIdList", [])

                        if article_id_list:
                            pmid, pmcid, fetched_doi, other_ids = parse_article_ids(
                                article_id_list
                            )

                            summary_entry.update(
                                {
                                    "pmid": pmid,
                                    "pmcid": pmcid,
                                    "other": "; ".join(other_ids) if other_ids else "",
                                }
                            )

                            # Use fetched DOI if we don't have one already
                            if not summary_entry["doi"] and fetched_doi:
                                summary_entry["doi"] = fetched_doi

                        logging.info(f"  Successfully processed PMID: {citation_pmid}")

                    except Exception as e:
                        logging.error(
                            f"  Error processing PubMed record for {cit_id}: {e}"
                        )
                else:
                    logging.warning(
                        f"  Failed to fetch PubMed record for PMID: {citation_pmid}"
                    )
            else:
                logging.info(f"  No PMID available for {cit_id}")
                missing_pmids.append(cit_id)

            summary_data.append(summary_entry)

    if missing_pmids:
        logging.info(f"Citations without PMIDs: {len(missing_pmids)}")
        logging.debug(f"Missing PMID citations: {missing_pmids}")

    logging.info(
        f"Processed {processed_count} citations, {len(summary_data)} summary entries created"
    )

    return summary_data


def save_pubmed_summary(
    summary_data: list[dict[str, str]], cogat_data_dir: Path
) -> None:
    """Save the PubMed summary to TSV file."""
    if not summary_data:
        logging.warning("No summary data to save")
        return

    output_file = cogat_data_dir / "pubmed_summary.tsv"

    # Define the expected field order
    fieldnames = ["citation_id", "citation_pmid", "pmid", "pmcid", "doi", "other"]

    try:
        with open(output_file, "w", newline="", encoding="utf-8") as tsvfile:
            writer = csv.DictWriter(tsvfile, fieldnames=fieldnames, delimiter="\t")
            writer.writeheader()
            writer.writerows(summary_data)

        logging.info(f"PubMed summary saved to {output_file}")
        logging.info(f"Summary contains {len(summary_data)} entries")
    except Exception as e:
        logging.error(f"Error saving PubMed summary: {e}")


def main() -> None:
    """Main function to download PubMed data based on citation_summary.tsv."""
    args = get_args()
    setup_logging(args.log_level, args.log_file)

    cogat_data_dir = Path(args.cogat_data_dir)

    if not cogat_data_dir.exists():
        logging.error(f"Cogat data directory not found: {cogat_data_dir}")
        return

    logging.info("Starting PubMed download process")
    logging.info(f"Cogat data directory: {cogat_data_dir}")
    logging.info(f"Request rate: {args.request_rate} seconds")
    if args.limit:
        logging.info(f"Processing limited to {args.limit} citations")

    try:
        # Process citations and download PubMed records
        summary_data = process_citations(
            cogat_data_dir=cogat_data_dir,
            email=args.email,
            request_rate=args.request_rate,
            limit=args.limit,
        )

        # Save summary
        save_pubmed_summary(summary_data, cogat_data_dir)

        logging.info("PubMed download process completed successfully")

    except Exception as e:
        logging.error(f"Error in main process: {e}")
        raise


if __name__ == "__main__":
    main()
