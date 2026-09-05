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


def test_interval_mul() -> None:
    interval_i = pd.Interval(0, 1, closed="left")
    interval_f = pd.Interval(0.0, 1.0, closed="right")
    interval_td = pd.Interval(
        pd.Timedelta("1 days"), pd.Timedelta("2 days"), closed="neither"
    )

    check(assert_type(interval_i * 3, "pd.Interval[int]"), pd.Interval, int)
    check(assert_type(interval_f * 3, "pd.Interval[float]"), pd.Interval, float)
    check(
        assert_type(interval_td * 3, "pd.Interval[pd.Timedelta]"),
        pd.Interval,
        pd.Timedelta,
    )

    check(assert_type(interval_i * 3.5, "pd.Interval[float]"), pd.Interval, float)
    check(assert_type(interval_f * 3.5, "pd.Interval[float]"), pd.Interval, float)
    check(
        assert_type(interval_td * 3.5, "pd.Interval[pd.Timedelta]"),
        pd.Interval,
        pd.Timedelta,
    )

    check(assert_type(3 * interval_i, "pd.Interval[int]"), pd.Interval, int)
    check(assert_type(3 * interval_f, "pd.Interval[float]"), pd.Interval, float)
    check(
        assert_type(3 * interval_td, "pd.Interval[pd.Timedelta]"),
        pd.Interval,
        pd.Timedelta,
    )

    check(assert_type(3.5 * interval_i, "pd.Interval[float]"), pd.Interval, float)
    check(assert_type(3.5 * interval_f, "pd.Interval[float]"), pd.Interval, float)
    check(
        assert_type(3.5 * interval_td, "pd.Interval[pd.Timedelta]"),
        pd.Interval,
        pd.Timedelta,
    )


def test_timedelta_mul() -> None:
    td = pd.Timedelta("1 day")

    np_intp_arr: np_ndarray_anyint = np.array([1, 2, 3])
    np_float_arr: np_ndarray_float = np.array([1.2, 2.2, 3.4])

    md_int = 3
    md_float = 3.5
    md_ndarray_intp = np_intp_arr
    md_ndarray_float = np_float_arr

    check(assert_type(td * md_int, pd.Timedelta), pd.Timedelta)
    check(assert_type(td * md_float, pd.Timedelta), pd.Timedelta)
    check(assert_type(td * md_ndarray_intp, np_ndarray_td), np_ndarray, np.timedelta64)
    check(assert_type(td * md_ndarray_float, np_ndarray_td), np_ndarray, np.timedelta64)

    check(assert_type(md_int * td, pd.Timedelta), pd.Timedelta)
    check(assert_type(md_float * td, pd.Timedelta), pd.Timedelta)
    check(assert_type(md_ndarray_intp * td, np_ndarray_td), np_ndarray, np.timedelta64)
    check(assert_type(md_ndarray_float * td, np_ndarray_td), np_ndarray, np.timedelta64)


def test_mul() -> None:
    """Test checking that pd.Timedelta * int / float."""
    a = pd.Timedelta("1 day")
    b = True
    c = 1.0
    d = 5
    e = 1 + 3.0j

    check(assert_type(a * c, pd.Timedelta), pd.Timedelta)
    check(assert_type(c * a, pd.Timedelta), pd.Timedelta)
    check(assert_type(a * d, pd.Timedelta), pd.Timedelta)
    check(assert_type(d * a, pd.Timedelta), pd.Timedelta)

    if TYPE_CHECKING_INVALID_USAGE:
        # pd.Timedelta * bool is not allowed, see GH1418
        _0 = a * b  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _1 = b * a  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _2 = a * e  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _3 = e * a  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
