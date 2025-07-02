#!/usr/bin/env python3
"""Script to start the HED Task API server."""

import uvicorn

from hed_task.config import settings

if __name__ == "__main__":
    uvicorn.run(
        "hed_task.api:app",
        host=settings.api_host,
        port=settings.api_port,
        reload=True,
        log_level=settings.log_level.lower(),
    )
