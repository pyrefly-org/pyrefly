from typing import Callable, ClassVar
from _typeshed import Incomplete

from __future__ import annotations
import inspect
from typing import TYPE_CHECKING
from polars._dependencies import altair as alt
from collections.abc import Callable
from typing import TypeAlias, Unpack
from altair.typing import ChannelColor as Color
from altair.typing import ChannelOrder as Order
from altair.typing import ChannelSize as Size
from altair.typing import ChannelTooltip as Tooltip
from altair.typing import ChannelX as X
from altair.typing import ChannelY as Y
from altair.typing import EncodeKwds
from polars import DataFrame

Encoding: TypeAlias = X | Y | Color | Order | Size | Tooltip
Encodings: TypeAlias = dict[str, Encoding]


class DataFramePlot:
    def __init__(self, df: DataFrame) -> None: ...

    def bar(self, x: X | None = None, y: Y | None = None, color: Color | None = None, /, **kwargs: Unpack[EncodeKwds]) -> alt.Chart: ...

    def line(self, x: X | None = None, y: Y | None = None, color: Color | None = None, order: Order | None = None, /, **kwargs: Unpack[EncodeKwds]) -> alt.Chart: ...

    def point(self, x: X | None = None, y: Y | None = None, color: Color | None = None, size: Size | None = None, /, **kwargs: Unpack[EncodeKwds]) -> alt.Chart: ...

    scatter: ClassVar[Callable[..., Incomplete]]

    def __getattr__(self, attr: str) -> Callable[..., alt.Chart]: ...
