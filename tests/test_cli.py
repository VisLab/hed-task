"""Tests for the CLI module."""

from typer.testing import CliRunner

from hed_task.cli import app

runner = CliRunner()


def test_hello_default():
    """Test hello command with default name."""
    result = runner.invoke(app, ["hello"])
    assert result.exit_code == 0
    assert "Hello World!" in result.stdout


def test_hello_with_name():
    """Test hello command with custom name."""
    result = runner.invoke(app, ["hello", "Alice"])
    assert result.exit_code == 0
    assert "Hello Alice!" in result.stdout


def test_version():
    """Test version command."""
    result = runner.invoke(app, ["version"])
    assert result.exit_code == 0
    assert "hed-task version:" in result.stdout
