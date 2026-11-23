from __future__ import annotations
import os
from typing import Final

MONITORING_ENV_VAR: Final[str] = "POLARS_QUERY_MONITORING"
MONITORING_WORKSPACE_ENV_VAR: Final[str] = "POLARS_QUERY_MONITORING_WORKSPACE"
MONITORING_ORGANIZATION_ENV_VAR: Final[str] = "POLARS_QUERY_MONITORING_ORGANIZATION"


def monitoring_enabled_globally() -> bool: ...


def monitoring_workspace() -> str | None: ...


def monitoring_organization() -> str | None: ...


def activate_monitoring() -> None: ...
