from typing import Callable

from __future__ import annotations
from concurrent.futures import ThreadPoolExecutor
from typing import TYPE_CHECKING, Generic, ParamSpec, TypeVar
from collections.abc import Callable

P = ParamSpec("P")

T = TypeVar("T")


class FnPoolWrap(Generic[P, T]):
    f: Callable[..., T]
    pool_wrap: PyThreadPool

    def __init__(self, f: Callable[P, T], pool_wrap: PyThreadPool) -> None: ...

    def __call__(self, *a: P.args, **kw: P.kwargs) -> T: ...


class PyThreadPool:
    last_exception: BaseException | None
    pool: ThreadPoolExecutor

    def __init__(self, num_threads: int) -> None: ...
