"""Schemas used by the health endpoint."""

from pydantic import BaseModel, ConfigDict


class HealthResponse(BaseModel):
    """Response model for the health check endpoint.

    Attributes:
        status: Current API health status.
    """

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "status": "ok",
            },
        },
    )

    status: str