"""Tests for the API module."""


def test_root_endpoint(client):
    """Test the root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to HED Task API"}


def test_health_check(client):
    """Test the health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_version_endpoint(client):
    """Test that version endpoint doesn't exist (returns 404)."""
    response = client.get("/version")
    assert response.status_code == 404
