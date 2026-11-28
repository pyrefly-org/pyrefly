from __future__ import annotations
from typing import TYPE_CHECKING
from polars._utils.unstable import issue_unstable_warning
from polars.dataframe import DataFrame
from polars.expr import Expr
from polars.selectors import exclude
from collections.abc import Sequence
from typing import Self
from torch import Tensor, memory_format
import torch
from torch.utils.data import TensorDataset

__all__ = ["PolarsDataset"]


class PolarsDataset(TensorDataset):
    tensors: tuple[Tensor, ...]
    labels: Tensor | None
    features: Tensor

    def __init__(self, frame: DataFrame, *, label: str | Expr | Sequence[str | Expr] | None = None, features: str | Expr | Sequence[str | Expr] | None = None) -> None: ...

    def __copy__(self) -> Self: ...

    def __repr__(self) -> str: ...

    def half(self, *, features: bool = True, labels: bool = True, memory_format: memory_format = ...) -> Self: ...

    @property
    def schema(self) -> dict[str, torch.dtype | None]: ...
