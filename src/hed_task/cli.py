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
    task_data_dir: str = typer.Option(
        "task_data", "--task-data", "-t", help="Directory containing task data"
    ),
    output_file: str = typer.Option(
        "citation_summary.tsv",
        "--output",
        "-o",
        help="Output filename for citation summary",
    ),
) -> None:
    """Generate citation summary from collected task data."""
    from hed_task.citation_summary import save_citation_summary

    typer.echo("Generating citation summary...")
    typer.echo(f"Task data directory: {task_data_dir}")
    typer.echo(f"Output file: {output_file}")

    try:
        success = save_citation_summary(task_data_dir, output_file)

        if success:
            typer.echo("\n" + "=" * 50)
            typer.echo("SUCCESS: Citation summary generated!")
            typer.echo(f"Output saved to: {Path(task_data_dir) / output_file}")
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
        "task_data", "--output-dir", "-o", help="Directory to save all data"
    ),
) -> None:
    """Run the complete workflow: collect tasks and generate citation summary."""
    from hed_task.citation_summary import save_citation_summary
    from hed_task.task_collector import process_all_tasks

    typer.echo("Starting complete HED Task workflow...")
    typer.echo(f"Output directory: {output_dir}")

    try:
        # Step 1: Collect task data
        typer.echo("\nStep 1: Collecting task data from Cognitive Atlas...")
        summary_df = process_all_tasks(output_dir)

        if summary_df is None:
            typer.echo("Failed to collect task data. Aborting workflow.")
            raise typer.Exit(1)

        typer.echo(f"✓ Successfully collected {len(summary_df)} tasks")

        # Step 2: Generate citation summary
        typer.echo("\nStep 2: Generating citation summary...")
        citation_success = save_citation_summary(output_dir, "citation_summary.tsv")

        if not citation_success:
            typer.echo("Warning: Citation summary generation failed")

        typer.echo("\n" + "=" * 60)
        typer.echo("WORKFLOW COMPLETE!")
        typer.echo(
            f"Task data and citation summary saved to: {Path(output_dir).absolute()}"
        )
        typer.echo("=" * 60)

    except KeyboardInterrupt:
        typer.echo("\nWorkflow interrupted by user.")
        raise typer.Exit(1) from None
    except Exception as e:
        typer.echo(f"ERROR: {e}")
        raise typer.Exit(1) from e


if __name__ == "__main__":
    app()
