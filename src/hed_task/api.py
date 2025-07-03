"""FastAPI application for hed-task."""

from pathlib import Path
from typing import Optional

from fastapi import BackgroundTasks, FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="HED Task API",
    description="API for exploring task structure and its annotation with HED",
    version="0.1.0",
)


class CollectionRequest(BaseModel):
    """Request model for task collection."""

    output_dir: str = "H:\\CogTaskResults"
    delay_seconds: float = 5.0


class SpecificTasksRequest(BaseModel):
    """Request model for collecting specific tasks."""

    task_ids: list[str]
    output_dir: str = "H:\\CogTaskResults"
    delay_seconds: float = 5.0


class CollectionStatus(BaseModel):
    """Response model for collection status."""

    status: str
    message: str
    task_count: Optional[int] = None
    output_dir: Optional[str] = None


@app.get("/")
async def root() -> dict[str, str]:
    """Root endpoint."""
    return {"message": "Welcome to HED Task API"}


@app.get("/health")
async def health_check() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "healthy"}


@app.get("/version")
async def get_version() -> dict[str, str]:
    """Get version information."""
    from hed_task import __version__

    return {"version": __version__}


@app.get("/tasks/list")
async def list_tasks(limit: int = 10) -> dict:
    """List available tasks from Cognitive Atlas."""
    try:
        from hed_task.cognitive_atlas_collector import CognitiveAtlasCollector

        collector = CognitiveAtlasCollector()
        summary_df = collector.get_all_tasks_summary()

        # Convert to list of dictionaries
        tasks = summary_df.head(limit).to_dict("records")

        return {"total_tasks": len(summary_df), "showing": len(tasks), "tasks": tasks}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching tasks: {e}") from e


@app.post("/tasks/collect-all")
async def collect_all_tasks(
    request: CollectionRequest, background_tasks: BackgroundTasks
) -> CollectionStatus:
    """Start collection of all tasks from Cognitive Atlas."""
    try:
        from hed_task.cognitive_atlas_collector import CognitiveAtlasCollector

        def run_collection() -> None:
            collector = CognitiveAtlasCollector(
                output_dir=request.output_dir, delay_seconds=request.delay_seconds
            )
            collector.collect_all_task_data()

        # Run collection in background
        background_tasks.add_task(run_collection)

        return CollectionStatus(
            status="started",
            message="Task collection started in background",
            output_dir=request.output_dir,
        )
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error starting collection: {e}"
        ) from e


@app.post("/tasks/collect-specific")
async def collect_specific_tasks(
    request: SpecificTasksRequest, background_tasks: BackgroundTasks
) -> CollectionStatus:
    """Start collection of specific tasks from Cognitive Atlas."""
    try:
        from hed_task.cognitive_atlas_collector import CognitiveAtlasCollector

        def run_specific_collection() -> None:
            collector = CognitiveAtlasCollector(
                output_dir=request.output_dir, delay_seconds=request.delay_seconds
            )
            collector.collect_specific_tasks(request.task_ids)

        # Run collection in background
        background_tasks.add_task(run_specific_collection)

        return CollectionStatus(
            status="started",
            message=f"Collection started for {len(request.task_ids)} specific tasks",
            task_count=len(request.task_ids),
            output_dir=request.output_dir,
        )
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error starting collection: {e}"
        ) from e


@app.get("/tasks/collection-status")
async def get_collection_status(output_dir: str = "H:\\CogTaskResults") -> dict:
    """Check the status of task collection in a directory."""
    try:
        output_path = Path(output_dir)

        if not output_path.exists():
            return {
                "status": "not_started",
                "message": "Output directory does not exist",
                "output_dir": output_dir,
            }

        # Check for summary file
        summary_file = output_path / "task_summary.tsv"
        has_summary = summary_file.exists()

        # Count subdirectories (task details)
        task_dirs = [d for d in output_path.iterdir() if d.is_dir()]
        task_count = len(task_dirs)

        # Count JSON detail files
        detail_files = list(output_path.glob("*/*_details.json"))
        detail_count = len(detail_files)

        return {
            "status": "completed" if has_summary else "in_progress",
            "output_dir": output_dir,
            "has_summary": has_summary,
            "task_directories": task_count,
            "detail_files": detail_count,
            "summary_file": str(summary_file) if has_summary else None,
        }
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error checking status: {e}"
        ) from e
