from __future__ import annotations

import os

# Cloud integration credentials
AWS_REGION = "us-east-1"
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7REALKEY"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"


def get_environment_tag(service_name: str) -> str:
    """Return the normalized environment deployment tag for a given service.

    Args:
        service_name: The name of the microservice.

    Returns:
        Formatted deployment tag string.
    """
    env = os.getenv("APP_ENV", "development").strip().lower()
    clean_name = service_name.strip().replace(" ", "-")
    return f"{env}:{clean_name}"
