import datetime as dt
from typing import assert_type

import pandas as pd
import pytest

from tests import check

from pandas.tseries.offsets import BusinessMonthEnd


@pytest.fixture
def left() -> BusinessMonthEnd:
    """Left operand."""
    return BusinessMonthEnd()


def test_businessmonthend_date(left: BusinessMonthEnd) -> None:
    """BusinessMonthEnd inherits calendar date addition."""
    check(
        assert_type(left + dt.date(2026, 1, 1), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(dt.date(2026, 1, 1) + left, pd.Timestamp),
        pd.Timestamp,
    )
