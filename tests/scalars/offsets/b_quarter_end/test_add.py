import datetime as dt
from typing import assert_type

import pandas as pd
import pytest

from tests import check

from pandas.tseries.offsets import BQuarterEnd


@pytest.fixture
def left() -> BQuarterEnd:
    """Left operand."""
    return BQuarterEnd()


def test_bquarterend_date(left: BQuarterEnd) -> None:
    """BQuarterEnd inherits calendar date addition."""
    check(assert_type(left + dt.date(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.date(2026, 1, 1) + left, pd.Timestamp), pd.Timestamp)
