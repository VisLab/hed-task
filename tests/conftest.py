"""Test configuration and fixtures."""

import pytest
from fastapi.testclient import TestClient

from hed_task.api import app


@pytest.fixture
def client():
    """Create a test client for the FastAPI app."""
    return TestClient(app)
