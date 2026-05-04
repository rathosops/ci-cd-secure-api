"""Schemas used by the version endpoint."""

from pydantic import BaseModel, ConfigDict


class VersionResponse(BaseModel):
    """Response model for the version endpoint.

    Attributes:
        name: Application name.
        version: Current application version.
    """

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "CI/CD Secure API",
                "version": "0.1.0",
            },
        },
    )

    name: str
    version: str