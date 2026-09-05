from typing import assert_type

import pandas as pd

from tests import check


def test_timedelta_abs() -> None:
    td = pd.Timedelta("1 day")

    check(assert_type(abs(td), pd.Timedelta), pd.Timedelta)

    check(assert_type(td.__abs__(), pd.Timedelta), pd.Timedelta)
