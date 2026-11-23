from collections.abc import Callable, Iterable
from typing import TypeVar

T = TypeVar("T")


def reduce_balanced(function: Callable[[T, T], T], iterable: Iterable[T]) -> T: ...
