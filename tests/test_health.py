"""Tests for the health endpoint."""

from fastapi.testclient import TestClient

from secure_api.main import create_app


def test_health_check_returns_success_status() -> None:
    """Health endpoint should return HTTP 200 and status ok."""
    client = TestClient(create_app())

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}