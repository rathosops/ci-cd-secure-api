"""Application entrypoint.

This module exposes the FastAPI application instance used by ASGI servers
such as Uvicorn.

The factory function exists to make the application easier to test and
extend without adding side effects at import time.
"""

from fastapi import FastAPI

from secure_api import __version__
from secure_api.api.routes import router
from secure_api.core.config import settings


def create_app() -> FastAPI:
    """Create and configure the FastAPI application.

    Returns:
        A configured FastAPI application instance.
    """
    app = FastAPI(
        title=settings.app_name,
        version=__version__,
        description=settings.app_description,
    )

    app.include_router(router)

    return app


app = create_app()