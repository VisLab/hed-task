"""Tests for the CLI module."""

from typer.testing import CliRunner

from hed_task.cli import app

runner = CliRunner()


def test_collect_tasks_help():
    """Test collect-tasks command help."""
    result = runner.invoke(app, ["collect-tasks", "--help"])
    assert result.exit_code == 0
    assert "Collect all task data from Cognitive Atlas API" in result.stdout


def test_generate_citations_help():
    """Test generate-citations command help."""
    result = runner.invoke(app, ["generate-citations", "--help"])
    assert result.exit_code == 0
    assert "Generate citation summary from collected task data" in result.stdout


def test_version():
    """Test version command."""
    result = runner.invoke(app, ["version"])
    assert result.exit_code == 0
    assert "hed-task version:" in result.stdout
