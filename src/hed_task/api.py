"""FastAPI application for hed-task."""

from pathlib import Path
from typing import Optional

from fastapi import BackgroundTasks, FastAPI, HTTPException
from pydantic import BaseModel

from .summarize_citations import summarize_citations
from .task_collector import process_all_tasks

app = FastAPI(
    title="HED Task API",
    description="API for collecting task structure and annotation data from Cognitive Atlas",
    version="0.1.0",
)


class CollectionRequest(BaseModel):
    """Request model for task collection."""

    cogat_data_dir: str = "src/cogat_data"


class CitationRequest(BaseModel):
    """Request model for citation processing."""

    cogat_data_dir: str = "src/cogat_data"
    verbose: bool = False


class SpecificTasksRequest(BaseModel):
    """Request model for collecting specific tasks."""

    task_ids: list[str]
    output_dir: str = "task_data"


class CollectionStatus(BaseModel):
    """Response model for collection status."""

    status: str
    message: str
    task_count: Optional[int] = None
    citation_count: Optional[int] = None
    cogat_data_dir: Optional[str] = None


class PubMedRequest(BaseModel):
    """Request model for PubMed download."""

    email: str
    cogat_data_dir: str = "src/cogat_data"
    limit: Optional[int] = None
    request_rate: float = 1.0
    log_level: str = "INFO"


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
        # Create task_data directory path from cogat_data_dir
        cogat_data_path = Path(request.cogat_data_dir)
        task_data_dir = cogat_data_path / "task_data"
        task_data_dir.mkdir(parents=True, exist_ok=True)

        def run_collection() -> None:
            process_all_tasks(output_dir=str(task_data_dir))

        # Run collection in background
        background_tasks.add_task(run_collection)

        return CollectionStatus(
            status="started",
            message="Task collection started in background",
            cogat_data_dir=request.cogat_data_dir,
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
async def generate_citations_endpoint(request: CitationRequest) -> CollectionStatus:
    """Generate citation summary from collected task data."""
    try:
        cogat_data_path = Path(request.cogat_data_dir)
        if not cogat_data_path.exists():
            raise HTTPException(
                status_code=400,
                detail=f"Cogat data directory {request.cogat_data_dir} does not exist",
            )

        task_data_path = cogat_data_path / "task_data"
        if not task_data_path.exists():
            raise HTTPException(
                status_code=400,
                detail=f"Task data directory {task_data_path} does not exist",
            )

        success, num_tasks, num_citations = summarize_citations(request.cogat_data_dir)

        if success:
            return CollectionStatus(
                status="success",
                message="Citation summary generated successfully",
                task_count=num_tasks,
                citation_count=num_citations,
                cogat_data_dir=request.cogat_data_dir,
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


@app.post("/download-pubmed", response_model=CollectionStatus)
async def download_pubmed_endpoint(
    request: PubMedRequest, background_tasks: BackgroundTasks
) -> CollectionStatus:
    """Download PubMed records for citations in citation_summary.tsv."""
    try:
        cogat_data_path = Path(request.cogat_data_dir)
        if not cogat_data_path.exists():
            raise HTTPException(
                status_code=400,
                detail=f"Cogat data directory {request.cogat_data_dir} does not exist",
            )

        citation_summary_file = cogat_data_path / "citation_summary.tsv"
        if not citation_summary_file.exists():
            raise HTTPException(
                status_code=400,
                detail=f"Citation summary file not found: {citation_summary_file}. Please run citation generation first.",
            )

        def run_pubmed_download() -> None:
            from .download_pubmed import (
                process_citations,
                save_pubmed_summary,
                setup_logging,
            )

            try:
                setup_logging(request.log_level)

                # Process citations and download PubMed records
                summary_data = process_citations(
                    cogat_data_dir=cogat_data_path,
                    email=request.email,
                    request_rate=request.request_rate,
                    limit=request.limit,
                )

                # Save summary
                save_pubmed_summary(summary_data, cogat_data_path)
                print(
                    f"PubMed download completed. Processed {len(summary_data)} citations."
                )

            except Exception as e:
                print(f"Error during PubMed download: {e}")

        # Run PubMed download in background
        background_tasks.add_task(run_pubmed_download)

        return CollectionStatus(
            status="started",
            message="PubMed download started in background",
            cogat_data_dir=request.cogat_data_dir,
        )

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error starting PubMed download: {e}"
        ) from e


async def run_task_collection(cogat_data_dir: str) -> None:
    """Background task to run the complete task collection."""
    try:
        # Create task_data directory
        cogat_data_path = Path(cogat_data_dir)
        task_data_dir = cogat_data_path / "task_data"
        task_data_dir.mkdir(parents=True, exist_ok=True)

        summary_df = process_all_tasks(str(task_data_dir))
        if summary_df is not None:
            print(f"Successfully collected {len(summary_df)} tasks to {task_data_dir}")
        else:
            print("Task collection failed")
    except Exception as e:
        print(f"Error during task collection: {e}")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
