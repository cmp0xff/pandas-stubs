import datetime as dt
from typing import assert_type

import pandas as pd
import pytest

from tests import check

from pandas.tseries.offsets import BusinessMonthBegin


@pytest.fixture
def left() -> BusinessMonthBegin:
    """Left operand."""
    return BusinessMonthBegin()


def test_businessmonthbegin_date(left: BusinessMonthBegin) -> None:
    """BusinessMonthBegin inherits calendar date addition."""
    check(
        assert_type(left + dt.date(2026, 1, 1), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(dt.date(2026, 1, 1) + left, pd.Timestamp),
        pd.Timestamp,
    )
