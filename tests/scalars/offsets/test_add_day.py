import datetime as dt
from typing import assert_type

import numpy as np
import pandas as pd
from pandas.api.typing import NaTType

from tests import (
    TYPE_CHECKING_INVALID_USAGE,
    check,
)

from pandas.tseries.offsets import (
    Day,
    Hour,
    Week,
)


def test_day_python_scalars() -> None:
    """Python dates become Timestamp; durations follow the offset family."""
    check(assert_type(Day() + dt.date(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.date(2026, 1, 1) + Day(), pd.Timestamp), pd.Timestamp)
    check(assert_type(Day() + dt.datetime(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.datetime(2026, 1, 1) + Day(), pd.Timestamp), pd.Timestamp)
    check(assert_type(Day() + dt.timedelta(hours=2), dt.timedelta), dt.timedelta)
    check(assert_type(dt.timedelta(hours=2) + Day(), dt.timedelta), dt.timedelta)


def test_day_numpy_scalars() -> None:
    """NumPy temporal scalars use the supported scalar results."""
    check(assert_type(Day() + np.datetime64("2026-01-01"), pd.Timestamp), pd.Timestamp)
    check(assert_type(np.datetime64("2026-01-01") + Day(), pd.Timestamp), pd.Timestamp)
    check(assert_type(Day() + np.timedelta64(2, "h"), np.timedelta64), np.timedelta64)
    check(assert_type(np.timedelta64(2, "h") + Day(), np.timedelta64), np.timedelta64)


def test_day_pandas_scalars() -> None:
    """Timestamp and NaT retain pandas scalar results."""
    check(assert_type(Day() + pd.Timestamp("2026-01-01"), pd.Timestamp), pd.Timestamp)
    check(assert_type(pd.Timestamp("2026-01-01") + Day(), pd.Timestamp), pd.Timestamp)
    check(assert_type(Day() + pd.NaT, NaTType), NaTType)
    check(assert_type(pd.NaT + Day(), NaTType), NaTType)
    check(assert_type(Day() + pd.Timedelta("2h"), pd.Timedelta), pd.Timedelta)
    check(assert_type(pd.Timedelta("2h") + Day(), pd.Timedelta), pd.Timedelta)


def test_day_offsets() -> None:
    """Day combines with days, ticks, and unanchored weeks."""
    check(assert_type(Day(1) + Day(2), Day), Day)
    check(assert_type(Day(2) + Day(1), Day), Day)
    check(assert_type(Day() + Hour(), pd.Timedelta), pd.Timedelta)
    check(assert_type(Hour() + Day(), pd.Timedelta), pd.Timedelta)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = Hour().__add__(Day())  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = Hour().__radd__(Day())  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
    check(assert_type(Day() + Week(), dt.timedelta), dt.timedelta)
    check(assert_type(Week() + Day(), dt.timedelta), dt.timedelta)

    check(assert_type(Day().__add__(Hour()), pd.Timedelta), pd.Timedelta)
    check(assert_type(Day().__radd__(Hour()), pd.Timedelta), pd.Timedelta)


def test_day_numpy_arrays() -> None:
    """Object-array results do not promise shape or dtype preservation."""
    values = np.array([dt.datetime(2026, 1, 1)], dtype=object)
    check(
        assert_type(
            Day().__add__(values), np.ndarray[tuple[int, ...], np.dtype[np.generic]]
        ),
        np.ndarray,
    )
    check(
        assert_type(
            Day().__radd__(values), np.ndarray[tuple[int, ...], np.dtype[np.generic]]
        ),
        np.ndarray,
    )
    check(Day() + values, np.ndarray)
    check(values + Day(), np.ndarray)
    empty = np.array([], dtype=object)
    check(Day() + empty, np.ndarray)
    check(empty + Day(), np.ndarray)
    check(
        assert_type(
            Day().__add__(empty), np.ndarray[tuple[int, ...], np.dtype[np.generic]]
        ),
        np.ndarray,
    )
    check(
        assert_type(
            Day().__radd__(empty), np.ndarray[tuple[int, ...], np.dtype[np.generic]]
        ),
        np.ndarray,
    )


def test_day_array_dtype() -> None:
    """Day can change an object array to timedelta64 dtype."""
    values = np.array([np.timedelta64(1, "h")], dtype=object)
    result = check(
        assert_type(
            Day().__add__(values), np.ndarray[tuple[int, ...], np.dtype[np.generic]]
        ),
        np.ndarray,
    )
    assert result.dtype.kind == "m"


def test_day_index() -> None:
    """Containers support expressions through their own dispatch."""
    values = pd.date_range("2026-01-01", periods=2)
    check(assert_type(Day() + values, pd.DatetimeIndex), pd.DatetimeIndex)
    check(assert_type(values + Day(), pd.DatetimeIndex), pd.DatetimeIndex)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = Day().__add__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = Day().__radd__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]


def test_day_series() -> None:
    """Containers support expressions through their own dispatch."""
    values = pd.Series(pd.date_range("2026-01-01", periods=2))
    check(assert_type(Day() + values, "pd.Series[pd.Timestamp]"), pd.Series)
    check(assert_type(values + Day(), "pd.Series[pd.Timestamp]"), pd.Series)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = Day().__add__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = Day().__radd__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
