from __future__ import annotations
import contextlib
from typing import TYPE_CHECKING, Final
from polars.lazyframe.engine import (
    Engine,
    GPUEngine,
    InMemoryEngine,
    StreamingEngine,
    _AutoEngine,
)
from polars._typing import EngineType, EngineTypeName

SUPPORTED_ENGINE_NAMES: Final[tuple[str, ...]]


def get_engine_affinity_override() -> Engine | None: ...


def set_engine_affinity_override(engine: Engine | None) -> None: ...


__all__ = ([
    "GPUEngine",
    "SUPPORTED_ENGINE_NAMES",
    "get_engine_affinity_override",
    "set_engine_affinity_override",
])
