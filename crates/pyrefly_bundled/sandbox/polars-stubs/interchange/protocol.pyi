from __future__ import annotations
from polars._utils.unstable import issue_unstable_warning


class CompatLevel:
    def __init__(self) -> None: ...

    @staticmethod
    def newest() -> CompatLevel: ...

    @staticmethod
    def oldest() -> CompatLevel: ...

    def __repr__(self) -> str: ...
