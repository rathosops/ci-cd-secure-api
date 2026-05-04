"""Application configuration.

The project intentionally keeps configuration simple. For this initial
version, static values are enough and avoid unnecessary complexity.

If the API grows, this module can evolve to read environment variables,
feature flags, or deployment-specific settings.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Settings:
    """Application settings.

    Attributes:
        app_name: Public application name shown in the API documentation.
        app_description: Short description shown in the API documentation.
        health_status: Default status returned by the health endpoint.
    """

    app_name: str = "CI/CD Secure API"
    app_description: str = (
        "A small Python API used to demonstrate CI/CD, Docker, testing, "
        "and security automation."
    )
    health_status: str = "ok"


settings = Settings()