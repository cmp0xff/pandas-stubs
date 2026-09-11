import datetime as dt
from typing import assert_type

import pandas as pd
import pytest

from tests import check

from pandas.tseries.offsets import YearBegin


@pytest.fixture
def left() -> YearBegin:
    """Left operand."""
    return YearBegin()


def test_yearbegin_date(left: YearBegin) -> None:
    """YearBegin inherits calendar date addition."""
    check(assert_type(left + dt.date(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.date(2026, 1, 1) + left, pd.Timestamp), pd.Timestamp)
