from __future__ import annotations
from typing import Final, TypedDict


class ArrowDriverProperties(TypedDict):
    fetch_all: str
    fetch_batches: str | None
    exact_batch_size: bool | None
    repeat_batch_calls: bool
    minimum_version: str | None


ARROW_DRIVER_REGISTRY: Final[dict[str, list[ArrowDriverProperties]]]
