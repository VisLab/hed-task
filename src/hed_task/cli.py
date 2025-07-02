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


if __name__ == "__main__":
    app()
