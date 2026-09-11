import datetime as dt
from typing import assert_type

import pandas as pd
import pytest

from tests import check

from pandas.tseries.offsets import HalfYearBegin


@pytest.fixture
def left() -> HalfYearBegin:
    """Left operand."""
    return HalfYearBegin()


def test_halfyearbegin_date(left: HalfYearBegin) -> None:
    """HalfYearBegin inherits calendar date addition."""
    check(assert_type(left + dt.date(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.date(2026, 1, 1) + left, pd.Timestamp), pd.Timestamp)


def test_pandas_scalar_regression(left: HalfYearBegin) -> None:
    """Test half-year offsets introduced in pandas 3.0 GH1654."""
    ts = pd.Timestamp(2024, 2, 1)
    check(assert_type(left + ts, pd.Timestamp), pd.Timestamp)
    check(assert_type(ts + left, pd.Timestamp), pd.Timestamp)
