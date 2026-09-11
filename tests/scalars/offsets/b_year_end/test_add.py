import datetime as dt
from typing import assert_type

import pandas as pd
import pytest

from tests import check

from pandas.tseries.offsets import BYearEnd


@pytest.fixture
def left() -> BYearEnd:
    """Left operand."""
    return BYearEnd()


def test_byearend_date(left: BYearEnd) -> None:
    """BYearEnd inherits calendar date addition."""
    check(assert_type(left + dt.date(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.date(2026, 1, 1) + left, pd.Timestamp), pd.Timestamp)
