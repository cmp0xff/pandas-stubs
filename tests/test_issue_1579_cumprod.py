from typing import (
    TYPE_CHECKING,
    Never,
)

import pandas as pd


def test_series_cumprod_timedelta_restriction() -> None:
    s = pd.Series([pd.Timedelta("1D")])
    if TYPE_CHECKING:
        # This should return Never now
        _0: Never = s.cumprod()
