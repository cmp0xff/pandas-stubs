from typing import assert_type

import numpy as np
import pandas as pd

from tests import (
    TYPE_CHECKING_INVALID_USAGE,
    check,
)
from tests._typing import (
    np_ndarray,
    np_ndarray_anyint,
    np_ndarray_float,
    np_ndarray_td,
)


def test_interval_truediv() -> None:
    interval_i = pd.Interval(0, 1, closed="left")
    interval_f = pd.Interval(0.0, 1.0, closed="right")
    interval_td = pd.Interval(
        pd.Timedelta("1 days"), pd.Timedelta("2 days"), closed="neither"
    )

    check(assert_type(interval_i / 3, "pd.Interval[float]"), pd.Interval, float)
    check(assert_type(interval_f / 3, "pd.Interval[float]"), pd.Interval, float)
    check(
        assert_type(interval_td / 3, "pd.Interval[pd.Timedelta]"),
        pd.Interval,
        pd.Timedelta,
    )

    check(assert_type(interval_i / 3.5, "pd.Interval[float]"), pd.Interval, float)
    check(assert_type(interval_f / 3.5, "pd.Interval[float]"), pd.Interval, float)
    check(
        assert_type(interval_td / 3.5, "pd.Interval[pd.Timedelta]"),
        pd.Interval,
        pd.Timedelta,
    )


def test_timedelta_truediv() -> None:
    td = pd.Timedelta("1 day")

    np_intp_arr: np_ndarray_anyint = np.array([1, 2, 3])
    np_float_arr: np_ndarray_float = np.array([1.2, 2.2, 3.4])

    md_int = 3
    md_float = 3.5
    md_ndarray_intp = np_intp_arr
    md_ndarray_float = np_float_arr

    check(assert_type(td / td, float), float)
    check(assert_type(td / pd.NaT, float), float)
    check(assert_type(td / md_int, pd.Timedelta), pd.Timedelta)
    check(assert_type(td / md_float, pd.Timedelta), pd.Timedelta)
    check(assert_type(td / md_ndarray_intp, np_ndarray_td), np_ndarray, np.timedelta64)
    check(assert_type(td / md_ndarray_float, np_ndarray_td), np_ndarray, np.timedelta64)

    check(assert_type(pd.NaT / td, float), float)
    # Note: None of the reverse truediv work
    # TypeError: md_int, md_float, md_ndarray_intp, md_ndarray_float, mp_series_int,
    #            mp_series_float, md_int64_index, md_float_index
    if TYPE_CHECKING_INVALID_USAGE:
        _10 = md_int / td  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _11 = md_float / td  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _12 = md_ndarray_intp / td  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _13 = md_ndarray_float / td  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
