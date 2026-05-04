"""HTTP routes for the API.

Routes are kept in this module because the initial project is intentionally
small. If the API grows, routes can be split by domain, for example:

- health.py
- users.py
- items.py

For now, keeping one routes module makes the code easier to read and explain.
"""

from fastapi import APIRouter

from secure_api import __version__
from secure_api.core.config import settings
from secure_api.schemas.health import HealthResponse
from secure_api.schemas.version import VersionResponse

router = APIRouter()


@router.get(
    "/health",
    response_model=HealthResponse,
    summary="Check API health",
    tags=["health"],
)
def health_check() -> HealthResponse:
    """Return the current API health status.

    This endpoint is intentionally simple. It is useful for:

    - validating that the API is running;
    - testing the application with pytest;
    - demonstrating CI/CD checks in a small and clear way.

    Returns:
        A health response containing the current API status.
    """
    return HealthResponse(status=settings.health_status)


@router.get(
    "/version",
    response_model=VersionResponse,
    summary="Get API version",
    tags=["metadata"],
)
def get_version() -> VersionResponse:
    """Return application name and version.

    This endpoint is useful for checking which application version is
    currently running, especially in Docker images and CI/CD environments.

    Returns:
        A version response containing the application name and version.
    """
    return VersionResponse(
        name=settings.app_name,
        version=__version__,
    )