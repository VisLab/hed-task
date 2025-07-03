"""Command-line interface for hed-task using Typer."""

from typing import Optional

import typer

app = typer.Typer(
    help="HED Task - Exploration of task structure and its annotation with HED"
)


@app.command()
def hello(
    name: Optional[str] = typer.Argument(None, help="Name to greet"),
) -> None:
    """Say hello to someone."""
    if name is None:
        name = "World"
    typer.echo(f"Hello {name}!")


@app.command()
def version() -> None:
    """Show version information."""
    from hed_task import __version__

    typer.echo(f"hed-task version: {__version__}")


@app.command()
def collect_tasks(
    output_dir: str = typer.Option(
        "H:\\CogTaskResults", "--output-dir", "-o", help="Directory to save results"
    ),
    delay: float = typer.Option(
        5.0, "--delay", "-d", help="Delay between API requests in seconds"
    ),
) -> None:
    """Collect all task data from Cognitive Atlas."""
    from hed_task.cognitive_atlas_collector import CognitiveAtlasCollector

    typer.echo("Starting Cognitive Atlas data collection...")
    typer.echo(f"Output directory: {output_dir}")
    typer.echo(f"Delay between requests: {delay} seconds")

    try:
        collector = CognitiveAtlasCollector(output_dir=output_dir, delay_seconds=delay)
        summary_df = collector.collect_all_task_data()

        if summary_df is not None:
            typer.echo(f"✅ Successfully collected data for {len(summary_df)} tasks!")
            typer.echo(f"📁 Results saved in: {output_dir}")

    except Exception as e:
        typer.echo(f"❌ Error during collection: {e}", err=True)
        raise typer.Exit(1) from e


@app.command()
def collect_specific(
    task_ids: list[str] = typer.Argument(..., help="Task IDs to collect"),
    output_dir: str = typer.Option(
        "H:\\CogTaskResults", "--output-dir", "-o", help="Directory to save results"
    ),
    delay: float = typer.Option(
        5.0, "--delay", "-d", help="Delay between API requests in seconds"
    ),
) -> None:
    """Collect data for specific tasks from Cognitive Atlas."""
    from hed_task.cognitive_atlas_collector import CognitiveAtlasCollector

    typer.echo(f"Collecting data for specific tasks: {', '.join(task_ids)}")
    typer.echo(f"Output directory: {output_dir}")
    typer.echo(f"Delay between requests: {delay} seconds")

    try:
        collector = CognitiveAtlasCollector(output_dir=output_dir, delay_seconds=delay)
        summary_df = collector.collect_specific_tasks(task_ids)

        if summary_df is not None and len(summary_df) > 0:
            typer.echo(f"✅ Successfully collected data for {len(summary_df)} tasks!")
            typer.echo(f"📁 Results saved in: {output_dir}")
        else:
            typer.echo("❌ No matching tasks found!")
            raise typer.Exit(1)

    except Exception as e:
        typer.echo(f"❌ Error during collection: {e}", err=True)
        raise typer.Exit(1) from None


@app.command()
def list_tasks(
    limit: int = typer.Option(10, "--limit", "-l", help="Number of tasks to display"),
) -> None:
    """List available tasks from Cognitive Atlas."""
    from hed_task.cognitive_atlas_collector import CognitiveAtlasCollector

    try:
        collector = CognitiveAtlasCollector()
        summary_df = collector.get_all_tasks_summary()

        typer.echo(f"Found {len(summary_df)} total tasks in Cognitive Atlas")
        typer.echo(f"\nShowing first {min(limit, len(summary_df))} tasks:")
        typer.echo("-" * 80)

        for _idx, row in summary_df.head(limit).iterrows():
            typer.echo(f"ID: {row['id']}")
            typer.echo(f"Name: {row['name']}")
            typer.echo(f"Class: {row['concept_class']}")
            typer.echo(
                f"Definition: {row['definition_text'][:100]}{'...' if len(row['definition_text']) > 100 else ''}"
            )
            typer.echo("-" * 80)

        if len(summary_df) > limit:
            typer.echo(f"... and {len(summary_df) - limit} more tasks")

    except Exception as e:
        typer.echo(f"Error fetching task list: {e}", err=True)
        raise typer.Exit(1) from e


if __name__ == "__main__":
    app()
