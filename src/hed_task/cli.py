"""Command-line interface for hed-task using Typer."""

from pathlib import Path

import typer

app = typer.Typer(
    help="HED Task - Exploration of task structure and its annotation with HED"
)


@app.command()
def version() -> None:
    """Show version information."""
    from hed_task import __version__

    typer.echo(f"hed-task version: {__version__}")


@app.command()
def collect_tasks(
    output_dir: str = typer.Option(
        "task_data", "--output-dir", "-o", help="Directory to save task data"
    ),
) -> None:
    """Collect all task data from Cognitive Atlas API."""
    from hed_task.task_collector import process_all_tasks

    typer.echo("Starting Cognitive Atlas data collection...")
    typer.echo(f"Output directory: {output_dir}")

    try:
        summary_df = process_all_tasks(output_dir)

        if summary_df is not None:
            typer.echo("\n" + "=" * 50)
            typer.echo("SUCCESS: Task collection completed!")
            typer.echo(f"Collected {len(summary_df)} tasks")
            typer.echo(f"Data saved to: {Path(output_dir).absolute()}")
            typer.echo("=" * 50)
        else:
            typer.echo("\n" + "=" * 50)
            typer.echo("WARNING: No tasks were successfully collected")
            typer.echo("=" * 50)
            raise typer.Exit(1)

    except KeyboardInterrupt:
        typer.echo("\nCollection interrupted by user.")
        raise typer.Exit(1) from None
    except Exception as e:
        typer.echo(f"ERROR: {e}")
        raise typer.Exit(1) from e


@app.command()
def generate_citations(
    cogat_data_dir: str = typer.Option(
        "src/cogat_data",
        "--cogat-data",
        "-c",
        help="Directory containing cogat_data (with task_data and citation_data subdirs)",
    ),
    verbose: bool = typer.Option(
        False, "--verbose", "-v", help="Enable verbose logging"
    ),
) -> None:
    """Generate citation summary from collected task data."""
    import logging

    from hed_task.summarize_citations import summarize_citations

    if verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    typer.echo("Generating citation summary...")
    typer.echo(f"Cogat data directory: {cogat_data_dir}")

    try:
        success, num_tasks, num_citations = summarize_citations(cogat_data_dir)

        if success:
            typer.echo("\n" + "=" * 50)
            typer.echo("SUCCESS: Citation summary generated!")
            typer.echo(f"Processed {num_tasks} tasks with {num_citations} citations")
            typer.echo(
                f"Output saved to: {Path(cogat_data_dir) / 'citation_summary.tsv'}"
            )
            typer.echo(
                f"Citation details created in: {Path(cogat_data_dir) / 'citation_data'}"
            )
            typer.echo("=" * 50)
        else:
            typer.echo("\n" + "=" * 50)
            typer.echo("WARNING: Citation summary generation failed")
            typer.echo("=" * 50)
            raise typer.Exit(1)

    except Exception as e:
        typer.echo(f"ERROR: {e}")
        raise typer.Exit(1) from e


@app.command()
def full_workflow(
    output_dir: str = typer.Option(
        "src/cogat_data",
        "--output-dir",
        "-o",
        help="Directory to save all data (will create task_data and citation_data subdirs)",
    ),
    email: str = typer.Option(
        None,
        "--email",
        "-e",
        help="Email address for NCBI Entrez API (for PubMed download)",
    ),
    request_rate: float = typer.Option(
        1.0, "--request-rate", "-r", help="Delay between NCBI API requests in seconds"
    ),
    verbose: bool = typer.Option(
        False, "--verbose", "-v", help="Enable verbose logging"
    ),
) -> None:
    """Run the complete workflow: collect tasks, generate citation summary, and optionally download PubMed records."""
    import logging

    from hed_task.summarize_citations import summarize_citations
    from hed_task.task_collector import process_all_tasks

    if verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    typer.echo("Starting complete HED Task workflow...")
    typer.echo(f"Output directory: {output_dir}")

    try:
        # Ensure output directory exists
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        # Create task_data subdirectory for collection
        task_data_dir = output_path / "task_data"
        task_data_dir.mkdir(exist_ok=True)

        # Step 1: Collect task data
        typer.echo("\nStep 1: Collecting task data from Cognitive Atlas...")
        summary_df = process_all_tasks(str(task_data_dir))

        if summary_df is None:
            typer.echo("Failed to collect task data. Aborting workflow.")
            raise typer.Exit(1)

        typer.echo(f"✓ Successfully collected {len(summary_df)} tasks")

        # Step 2: Generate citation summary
        typer.echo("\nStep 2: Generating citation summary...")
        success, num_tasks, num_citations = summarize_citations(output_dir)

        if not success:
            typer.echo("Warning: Citation summary generation failed")
        else:
            typer.echo(
                f"✓ Successfully generated citation summary ({num_tasks} tasks, {num_citations} citations)"
            )

        # Step 3: Download PubMed records (if email provided)
        if email and success:
            typer.echo("\nStep 3: Downloading PubMed records...")
            try:
                from hed_task.download_pubmed import (
                    process_citations,
                    save_pubmed_summary,
                    setup_logging,
                )

                if verbose:
                    setup_logging("DEBUG")
                else:
                    setup_logging("INFO")

                # Process citations and download PubMed records
                summary_data = process_citations(
                    cogat_data_dir=output_path,
                    email=email,
                    request_rate=request_rate,
                    limit=None,
                )

                # Save summary
                save_pubmed_summary(summary_data, output_path)
                typer.echo(
                    f"✓ Successfully downloaded PubMed records for {len(summary_data)} citations"
                )

            except Exception as e:
                typer.echo(f"Warning: PubMed download failed: {e}")
        elif not email:
            typer.echo("\nStep 3: Skipping PubMed download (no email provided)")
            typer.echo(
                "To download PubMed records, use: hed-task download-pubmed --email <your-email>"
            )

        typer.echo("\n" + "=" * 60)
        typer.echo("WORKFLOW COMPLETE!")
        typer.echo(f"Task data saved to: {task_data_dir.absolute()}")
        if success:
            typer.echo(
                f"Citation data saved to: {(output_path / 'citation_data').absolute()}"
            )
            typer.echo(
                f"Citation summary: {(output_path / 'citation_summary.tsv').absolute()}"
            )
            typer.echo(f"Processed {num_tasks} tasks with {num_citations} citations")
            if email:
                typer.echo(
                    f"PubMed summary: {(output_path / 'pubmed_summary.tsv').absolute()}"
                )
        typer.echo("=" * 60)

    except KeyboardInterrupt:
        typer.echo("\nWorkflow interrupted by user.")
        raise typer.Exit(1) from None
    except Exception as e:
        typer.echo(f"ERROR: {e}")
        raise typer.Exit(1) from e


@app.command()
def download_pubmed(
    email: str = typer.Option(
        ..., "--email", "-e", help="Email address for NCBI Entrez API (required)"
    ),
    cogat_data_dir: str = typer.Option(
        "src/cogat_data",
        "--cogat-data",
        "-c",
        help="Directory containing cogat_data with citation_summary.tsv",
    ),
    limit: int = typer.Option(
        None, "--limit", "-l", help="Limit the number of citations to process"
    ),
    request_rate: float = typer.Option(
        1.0, "--request-rate", "-r", help="Delay between NCBI API requests in seconds"
    ),
    log_level: str = typer.Option("INFO", "--log-level", help="Set the logging level"),
) -> None:
    """Download PubMed records for citations in citation_summary.tsv."""
    from pathlib import Path

    from hed_task.download_pubmed import (
        process_citations,
        save_pubmed_summary,
        setup_logging,
    )

    setup_logging(log_level)

    typer.echo("Starting PubMed download process...")
    typer.echo(f"Cogat data directory: {cogat_data_dir}")
    typer.echo(f"Request rate: {request_rate} seconds")
    if limit:
        typer.echo(f"Processing limited to {limit} citations")

    try:
        cogat_data_path = Path(cogat_data_dir)

        if not cogat_data_path.exists():
            typer.echo(f"ERROR: Cogat data directory not found: {cogat_data_path}")
            raise typer.Exit(1)

        citation_summary_file = cogat_data_path / "citation_summary.tsv"
        if not citation_summary_file.exists():
            typer.echo(
                f"ERROR: Citation summary file not found: {citation_summary_file}"
            )
            typer.echo("Please run 'hed-task generate-citations' first.")
            raise typer.Exit(1)

        # Process citations and download PubMed records
        summary_data = process_citations(
            cogat_data_dir=cogat_data_path,
            email=email,
            request_rate=request_rate,
            limit=limit,
        )

        # Save summary
        save_pubmed_summary(summary_data, cogat_data_path)

        typer.echo("\n" + "=" * 50)
        typer.echo("SUCCESS: PubMed download completed!")
        typer.echo(f"Processed {len(summary_data)} citations")
        typer.echo(f"PubMed summary saved to: {cogat_data_path / 'pubmed_summary.tsv'}")
        typer.echo("PubMed records and abstracts saved to citation directories")
        typer.echo("=" * 50)

    except Exception as e:
        typer.echo(f"ERROR: {e}")
        raise typer.Exit(1) from e


if __name__ == "__main__":
    app()
