# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --frozen --no-cache

# Copy source code
COPY src/ ./src/

# Expose port
EXPOSE 8000

# Command to run the application
CMD ["uv", "run", "uvicorn", "hed_task.api:app", "--host", "0.0.0.0", "--port", "8000"]
