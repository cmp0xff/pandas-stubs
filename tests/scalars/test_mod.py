from typing import assert_type

import numpy as np
import pandas as pd

from tests import check
from tests._typing import (
    np_ndarray,
    np_ndarray_td,
)


def test_timedelta_mod() -> None:
    td = pd.Timedelta("1 day")

    i_idx = pd.Index([1, 2, 3], dtype=int)
    f_idx = pd.Index([1.2, 2.2, 3.4], dtype=float)

    check(assert_type(td % 3, pd.Timedelta), pd.Timedelta)
    check(assert_type(td % 3.5, pd.Timedelta), pd.Timedelta)
    check(assert_type(td % td, pd.Timedelta), pd.Timedelta)
    check(
        assert_type(td % np.array([1, 2, 3]), np_ndarray_td), np_ndarray, np.timedelta64
    )
    check(
        assert_type(td % np.array([1.2, 2.2, 3.4]), np_ndarray_td),
        np_ndarray,
        np.timedelta64,
    )
    int_series = pd.Series([1, 2, 3], dtype=int)
    float_series = pd.Series([1.2, 2.2, 3.4], dtype=float)
    check(
        assert_type(td % int_series, "pd.Series[pd.Timedelta]"), pd.Series, pd.Timedelta
    )
    check(
        assert_type(td % float_series, "pd.Series[pd.Timedelta]"),
        pd.Series,
        pd.Timedelta,
    )
    check(assert_type(td % i_idx, pd.TimedeltaIndex), pd.TimedeltaIndex)

    check(
        assert_type(td % f_idx, pd.TimedeltaIndex),
        pd.TimedeltaIndex,
    )
