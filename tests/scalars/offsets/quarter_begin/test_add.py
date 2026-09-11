import datetime as dt
from typing import assert_type

import pandas as pd
import pytest

from tests import check

from pandas.tseries.offsets import QuarterBegin


@pytest.fixture
def left() -> QuarterBegin:
    """Left operand."""
    return QuarterBegin()


def test_quarterbegin_date(left: QuarterBegin) -> None:
    """QuarterBegin inherits calendar date addition."""
    check(assert_type(left + dt.date(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.date(2026, 1, 1) + left, pd.Timestamp), pd.Timestamp)
