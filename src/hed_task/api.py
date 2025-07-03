"""FastAPI application for hed-task."""

from pathlib import Path
from typing import Optional

from fastapi import BackgroundTasks, FastAPI, HTTPException
from pydantic import BaseModel

from .citation_summary import save_citation_summary
from .task_collector import process_all_tasks

app = FastAPI(
    title="HED Task API",
    description="API for collecting task structure and annotation data from Cognitive Atlas",
    version="0.1.0",
)


class CollectionRequest(BaseModel):
    """Request model for task collection."""

    output_dir: str = "task_data"


class SpecificTasksRequest(BaseModel):
    """Request model for collecting specific tasks."""

    task_ids: list[str]
    output_dir: str = "task_data"


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


@app.post("/tasks/collect-all", response_model=CollectionStatus)
async def collect_all_tasks(
    request: CollectionRequest, background_tasks: BackgroundTasks
) -> CollectionStatus:
    """Start collection of all tasks from Cognitive Atlas."""
    try:

        def run_collection() -> None:
            process_all_tasks(output_dir=request.output_dir)

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


@app.post("/tasks/collect-specific", response_model=CollectionStatus)
async def collect_specific_tasks(
    request: SpecificTasksRequest, background_tasks: BackgroundTasks
) -> CollectionStatus:
    """Start collection of specific tasks from Cognitive Atlas."""
    # This is a placeholder as process_specific_tasks is not implemented
    raise HTTPException(
        status_code=501, detail="Specific task collection not implemented"
    )


@app.post("/generate-citations", response_model=CollectionStatus)
async def generate_citations(request: CollectionRequest) -> CollectionStatus:
    """Generate citation summary from collected task data."""
    try:
        output_path = Path(request.output_dir)
        if not output_path.exists():
            raise HTTPException(
                status_code=400,
                detail=f"Task data directory {request.output_dir} does not exist",
            )

        success = save_citation_summary(request.output_dir, "citation_summary.tsv")

        if success:
            return CollectionStatus(
                status="success",
                message="Citation summary generated successfully",
                output_dir=request.output_dir,
            )
        else:
            raise HTTPException(
                status_code=500, detail="Failed to generate citation summary"
            )

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error generating citations: {e}"
        ) from e


async def run_task_collection(output_dir: str) -> None:
    """Background task to run the complete task collection."""
    try:
        summary_df = process_all_tasks(output_dir)
        if summary_df is not None:
            print(f"Successfully collected {len(summary_df)} tasks to {output_dir}")
        else:
            print("Task collection failed")
    except Exception as e:
        print(f"Error during task collection: {e}")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
