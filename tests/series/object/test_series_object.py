from __future__ import annotations

import datetime
from typing import assert_type

import pandas as pd

from tests import check


def test_types_shift_fill_value() -> None:
    """Test fill_value of pd.Series[datetime.date] and pd.Series[datetime.time].shift."""
    s = pd.Series(pd.date_range("2020", periods=3))
    s_date = check(
        assert_type(s.dt.date, "pd.Series[datetime.date]"), pd.Series, datetime.date
    )
    s_time = s.dt.time
    check(assert_type(s_time, "pd.Series[datetime.time]"), pd.Series, datetime.time)
    check(
        assert_type(s_date.shift(1, fill_value=datetime.date(2020, 1, 2)), pd.Series),
        pd.Series,
        datetime.date,
    )
    check(
        assert_type(s_time.shift(1, fill_value=datetime.time(1)), pd.Series),
        pd.Series,
        datetime.time,
    )
