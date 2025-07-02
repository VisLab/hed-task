"""FastAPI application for hed-task."""

from fastapi import FastAPI

app = FastAPI(
    title="HED Task API",
    description="API for exploring task structure and its annotation with HED",
    version="0.1.0",
)


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
