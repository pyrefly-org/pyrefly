from __future__ import annotations
import inspect
from typing import TYPE_CHECKING
from polars._dependencies import altair as alt
from collections.abc import Callable
from typing import Unpack
from altair.typing import EncodeKwds
from polars import Series
from polars.dataframe.plotting import Encodings


class SeriesPlot:
    def __init__(self, s: Series) -> None: ...

    def hist(self, /, **kwargs: Unpack[EncodeKwds]) -> alt.Chart: ...

    def kde(self, /, **kwargs: Unpack[EncodeKwds]) -> alt.Chart: ...

    def line(self, /, **kwargs: Unpack[EncodeKwds]) -> alt.Chart: ...

    def __getattr__(self, attr: str) -> Callable[..., alt.Chart]: ...
