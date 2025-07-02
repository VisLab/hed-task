#!/usr/bin/env python3
"""Example script demonstrating hed-task usage."""

import asyncio

import pandas as pd

from hed_task.config import settings


async def main():
    """Main example function."""
    print(f"Welcome to {settings.app_name} v{settings.app_version}")

    # Example pandas usage
    data = {
        "task_id": [1, 2, 3],
        "task_name": ["Task A", "Task B", "Task C"],
        "duration": [10.5, 15.2, 8.7],
    }
    df = pd.DataFrame(data)
    print("\nExample task data:")
    print(df)

    # Example with cognitiveatlas (when available)
    try:
        import cognitiveatlas

        print(f"\nCognitiveAtlas package available: {cognitiveatlas.__version__}")
    except ImportError:
        print("\nCognitiveAtlas package not yet installed")

    print("\nSetup complete! You can now:")
    print("1. Run CLI: uv run hed-task --help")
    print("2. Start API: uv run uvicorn hed_task.api:app --reload")
    print("3. Run tests: uv run pytest")


if __name__ == "__main__":
    asyncio.run(main())
