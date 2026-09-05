import datetime as dt
from datetime import (
    datetime,
    timedelta,
)
from typing import assert_type

import numpy as np
import pandas as pd
from pandas.api.typing import NaTType
import pytest

from tests import (
    TYPE_CHECKING_INVALID_USAGE,
    check,
)
from tests._typing import (
    np_ndarray,
    np_ndarray_dt,
    np_ndarray_td,
)

from pandas.tseries.offsets import (
    BaseOffset,
    Day,
)


def test_interval_sub() -> None:
    interval_i = pd.Interval(0, 1, closed="left")
    interval_f = pd.Interval(0.0, 1.0, closed="right")
    interval_ts = pd.Interval(
        pd.Timestamp("2017-01-01"), pd.Timestamp("2017-01-02"), closed="both"
    )
    interval_td = pd.Interval(
        pd.Timedelta("1 days"), pd.Timedelta("2 days"), closed="neither"
    )

    check(assert_type(interval_i - 1, "pd.Interval[int]"), pd.Interval, int)
    check(assert_type(interval_f - 1, "pd.Interval[float]"), pd.Interval, float)
    check(
        assert_type(interval_ts - pd.Timedelta(days=1), "pd.Interval[pd.Timestamp]"),
        pd.Interval,
        pd.Timestamp,
    )
    check(
        assert_type(interval_td - pd.Timedelta(days=1), "pd.Interval[pd.Timedelta]"),
        pd.Interval,
        pd.Timedelta,
    )

    check(assert_type(interval_i - 1.5, "pd.Interval[float]"), pd.Interval, float)
    check(assert_type(interval_f - 1.5, "pd.Interval[float]"), pd.Interval, float)
    check(
        assert_type(interval_ts - pd.Timedelta(days=1), "pd.Interval[pd.Timestamp]"),
        pd.Interval,
    )
    check(
        assert_type(interval_td - pd.Timedelta(days=1), "pd.Interval[pd.Timedelta]"),
        pd.Interval,
    )

    if TYPE_CHECKING_INVALID_USAGE:
        _i = interval_i - pd.Interval(1, 2)  # type: ignore[type-var] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _f = interval_f - pd.Interval(1.0, 2.0)  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _ts = interval_ts - pd.Interval(pd.Timestamp(2025, 9, 29), pd.Timestamp(2025, 9, 30), closed="both")  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _td = interval_td - pd.Interval(pd.Timedelta(1, "ns"), pd.Timedelta(2, "ns"))  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]


def test_timedelta_sub() -> None:
    td = pd.Timedelta("1 day")

    ndarray_td64: np_ndarray_td = np.array([1, 2, 3], dtype="timedelta64[D]")
    ndarray_dt64: np_ndarray_dt = np.array([1, 2, 3], dtype="datetime64[D]")
    as_timestamp = pd.Timestamp("2012-01-01")
    as_datetime = dt.datetime(2012, 1, 1)
    as_date = dt.date(2012, 1, 1)
    as_datetime64 = np.datetime64(1, "ns")
    as_dt_timedelta = dt.timedelta(days=1)
    as_timedelta64 = np.timedelta64(1, "D")
    as_timedelta_index = pd.TimedeltaIndex([td])
    as_period_index = pd.period_range("2012-01-01", periods=3, freq="D")
    as_datetime_index = pd.date_range("2012-01-01", periods=3)
    as_ndarray_td64 = ndarray_td64
    as_ndarray_dt64 = ndarray_dt64
    as_nat = pd.NaT

    # sub is not symmetric with dates. In general date_like - timedelta is
    # sensible, while timedelta - date_like is not
    # TypeError: as_timestamp, as_datetime, as_date, as_datetime64,
    #            as_period_index, as_datetime_index, as_ndarray_dt64
    if TYPE_CHECKING_INVALID_USAGE:
        _1 = td - as_timestamp  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _2 = td - as_datetime  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _3 = td - as_date  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _4 = td - as_datetime64  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _5 = td - as_period_index  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _6 = td - as_datetime_index  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _7 = td - as_ndarray_dt64  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]

    check(assert_type(td - td, pd.Timedelta), pd.Timedelta)
    check(assert_type(td - as_dt_timedelta, pd.Timedelta), pd.Timedelta)
    check(assert_type(td - as_timedelta64, pd.Timedelta), pd.Timedelta)
    check(assert_type(td - as_timedelta_index, pd.TimedeltaIndex), pd.TimedeltaIndex)
    check(assert_type(td - as_ndarray_td64, np_ndarray_td), np_ndarray, np.timedelta64)
    check(assert_type(td - as_nat, NaTType), NaTType)
    check(assert_type(as_timestamp - td, pd.Timestamp), pd.Timestamp)
    check(assert_type(as_datetime - td, dt.datetime), dt.datetime)
    check(assert_type(as_date - td, dt.date), dt.date)
    check(assert_type(as_datetime64 - td, pd.Timestamp), pd.Timestamp)
    # pyright, pyrefly and ty can't know that as_dt_timedelta - td calls
    # td.__rsub__(as_dt_timedelta), not as_dt_timedelta.__sub__(td)
    # https://github.com/microsoft/pyright/issues/4088
    check(
        assert_type(  # pyrefly: ignore[assert-type] # ty: ignore[type-assertion-failure]
            as_dt_timedelta - td,  # pyright: ignore[reportAssertTypeFailure]
            pd.Timedelta,
        ),
        pd.Timedelta,
    )
    # TODO: reduce the double unused-ignore-comment when astral-sh/ty#2681 is resolved
    check(assert_type(as_timedelta64 - td, pd.Timedelta), pd.Timedelta)  # type: ignore[assert-type] # pyright: ignore[reportAssertTypeFailure] # pyrefly: ignore[assert-type] # ty: ignore[type-assertion-failure,unused-ignore-comment,unused-ignore-comment]
    check(assert_type(as_timedelta_index - td, pd.TimedeltaIndex), pd.TimedeltaIndex)
    check(assert_type(as_period_index - td, pd.PeriodIndex), pd.PeriodIndex)
    check(assert_type(as_datetime_index - td, pd.DatetimeIndex), pd.DatetimeIndex)
    check(assert_type(as_ndarray_td64 - td, np_ndarray_td), np_ndarray, np.timedelta64)
    check(assert_type(as_ndarray_dt64 - td, np_ndarray_dt), np_ndarray, np.datetime64)
    check(assert_type(as_nat - td, NaTType), NaTType)


def test_timestamp_sub() -> None:
    ts = pd.Timestamp("2000-1-1")
    np_td64_arr: np_ndarray_td = np.array([1, 2], dtype="timedelta64[ns]")

    as_pd_timedelta = pd.Timedelta(days=1)
    as_dt_timedelta = dt.timedelta(days=1)
    as_offset = 3 * Day()

    as_timedelta_index = pd.to_timedelta([1, 2, 3], unit="D")
    as_timedelta_series = pd.Series(as_timedelta_index)
    check(
        assert_type(as_timedelta_series, "pd.Series[pd.Timedelta]"),
        pd.Series,
        pd.Timedelta,
    )
    as_np_ndarray_td64 = np_td64_arr

    # Reverse order is not possible for all of these
    check(assert_type(ts - as_pd_timedelta, pd.Timestamp), pd.Timestamp)
    check(assert_type(ts - as_dt_timedelta, pd.Timestamp), pd.Timestamp)
    check(assert_type(ts - as_offset, pd.Timestamp), pd.Timestamp)
    check(assert_type(ts - as_timedelta_index, pd.DatetimeIndex), pd.DatetimeIndex)
    check(
        assert_type(ts - as_timedelta_series, "pd.Series[pd.Timestamp]"),
        pd.Series,
        pd.Timestamp,
    )
    check(
        assert_type(ts - as_np_ndarray_td64, np_ndarray_dt), np_ndarray, np.datetime64
    )


def test_timestamp_types_sub() -> None:
    ts: pd.Timestamp = pd.to_datetime("2021-03-01")
    ts2: pd.Timestamp = pd.to_datetime("2021-01-01")
    delta: pd.Timedelta = pd.to_timedelta("1 day")

    check(assert_type(ts - ts2, pd.Timedelta), pd.Timedelta)
    check(assert_type(ts - delta, pd.Timestamp), pd.Timestamp)
    check(assert_type(ts - dt.datetime(2021, 1, 3), pd.Timedelta), pd.Timedelta)


def test_period_sub() -> None:
    p = pd.Period("2012-1-1", freq="D")

    as_period_index = pd.period_range("2012-1-1", periods=10, freq="D")
    check(assert_type(as_period_index, pd.PeriodIndex), pd.PeriodIndex)
    scale = 24 * 60 * 60 * 10**9
    as_td_series = pd.Series(pd.timedelta_range(scale, scale, freq="D"))
    check(assert_type(as_td_series, "pd.Series[pd.Timedelta]"), pd.Series, pd.Timedelta)
    as_period_series = pd.Series(as_period_index)
    check(assert_type(as_period_series, "pd.Series[pd.Period]"), pd.Series, pd.Period)
    offset_index = p - as_period_index
    check(assert_type(offset_index, pd.Index), pd.Index)
    offset_series = as_period_series - as_period_series
    check(assert_type(offset_series, "pd.Series[BaseOffset]"), pd.Series)
    check(assert_type(p - as_td_series, "pd.Series[pd.Period]"), pd.Series, pd.Period)


@pytest.fixture
def left() -> pd.Period:
    """Left operand"""
    return pd.Period("2025-08-20", freq="D")


def test_sub_py_scalar(left: pd.Period) -> None:
    """Test pd.Period - Python native scalars"""
    d = timedelta(days=1)
    i = 1
    f = 1.5
    s = datetime(2025, 8, 20)
    st = "str"

    check(assert_type(left - d, pd.Period), pd.Period)
    check(assert_type(left - i, pd.Period), pd.Period)

    if TYPE_CHECKING_INVALID_USAGE:
        _0 = left - f  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _1 = left - s  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _2 = left - st  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]

    if TYPE_CHECKING_INVALID_USAGE:
        _3 = d - left  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _4 = i - left  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _5 = f - left  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _6 = s - left  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _7 = st - left  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]


def test_sub_numpy_scalar(left: pd.Period) -> None:
    """Test pd.Period - numpy scalars"""
    d = np.timedelta64(1, "D")
    i = np.int64(1)
    s = np.datetime64("2025-08-20")

    check(assert_type(left - d, pd.Period), pd.Period)
    check(assert_type(left - i, pd.Period), pd.Period)

    if TYPE_CHECKING_INVALID_USAGE:
        _0 = left - s  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]

    if TYPE_CHECKING_INVALID_USAGE:
        _1 = d - left  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _2 = i - left  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _3 = s - left  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]


def test_sub_pd_scalar(left: pd.Period) -> None:
    """Test pd.Period - pandas scalars"""
    d = pd.Timedelta(days=1)
    off = pd.offsets.Day(1)
    p = pd.Period("2025-08-20", freq="D")
    nat = pd.NaT

    check(assert_type(left - d, pd.Period), pd.Period)
    check(assert_type(left - off, pd.Period), pd.Period)
    check(assert_type(left - p, BaseOffset), Day)
    check(assert_type(left - nat, NaTType), NaTType)

    if TYPE_CHECKING_INVALID_USAGE:
        _0 = d - left  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _1 = off - left  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
