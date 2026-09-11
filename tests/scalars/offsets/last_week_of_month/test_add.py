import datetime as dt
from typing import assert_type

import pandas as pd
import pytest

from tests import check

from pandas.tseries.offsets import LastWeekOfMonth


@pytest.fixture
def left() -> LastWeekOfMonth:
    """Left operand."""
    return LastWeekOfMonth()


def test_lastweekofmonth_date(left: LastWeekOfMonth) -> None:
    """LastWeekOfMonth inherits calendar date addition."""
    check(assert_type(left + dt.date(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.date(2026, 1, 1) + left, pd.Timestamp), pd.Timestamp)


def test_pandas_scalar_regression() -> None:
    """Preserve WeekOfMonth constructor cases from GH 320."""
    check(
        assert_type(LastWeekOfMonth(2, 3) + pd.Timestamp("9/23/2022"), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(pd.Timestamp("9/23/2022") + LastWeekOfMonth(2, 3), pd.Timestamp),
        pd.Timestamp,
    )
