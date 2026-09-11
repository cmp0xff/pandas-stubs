import datetime as dt
from typing import assert_type

import numpy as np
import pandas as pd
from pandas.api.typing import NaTType
import pytest

from pandas.errors import PerformanceWarning

from tests import (
    TYPE_CHECKING_INVALID_USAGE,
    check,
)

from pandas.tseries.offsets import (
    BusinessDay,
    CustomBusinessDay,
    Day,
    Hour,
)


def test_businessday_python_scalars() -> None:
    """BusinessDay handles python scalars through supported dispatch."""
    check(assert_type(BusinessDay() + dt.date(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.date(2026, 1, 1) + BusinessDay(), pd.Timestamp), pd.Timestamp)
    check(
        assert_type(BusinessDay() + dt.datetime(2026, 1, 1), pd.Timestamp), pd.Timestamp
    )
    check(
        assert_type(dt.datetime(2026, 1, 1) + BusinessDay(), pd.Timestamp), pd.Timestamp
    )
    check(assert_type(BusinessDay() + dt.timedelta(hours=2), BusinessDay), BusinessDay)
    check(assert_type(dt.timedelta(hours=2) + BusinessDay(), BusinessDay), BusinessDay)


def test_custombusinessday_python_scalars() -> None:
    """CustomBusinessDay handles python scalars through supported dispatch."""
    check(
        assert_type(CustomBusinessDay() + dt.date(2026, 1, 1), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(dt.date(2026, 1, 1) + CustomBusinessDay(), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(CustomBusinessDay() + dt.datetime(2026, 1, 1), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(dt.datetime(2026, 1, 1) + CustomBusinessDay(), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(CustomBusinessDay() + dt.timedelta(hours=2), BusinessDay),
        BusinessDay,
    )
    check(
        assert_type(dt.timedelta(hours=2) + CustomBusinessDay(), BusinessDay),
        BusinessDay,
    )


def test_businessday_numpy_scalars() -> None:
    """BusinessDay handles numpy scalars through supported dispatch."""
    check(
        assert_type(BusinessDay() + np.datetime64("2026-01-01"), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(np.datetime64("2026-01-01") + BusinessDay(), pd.Timestamp),
        pd.Timestamp,
    )
    check(assert_type(BusinessDay() + np.timedelta64(2, "h"), BusinessDay), BusinessDay)
    check(assert_type(np.timedelta64(2, "h") + BusinessDay(), BusinessDay), BusinessDay)


def test_custombusinessday_numpy_scalars() -> None:
    """CustomBusinessDay handles numpy scalars through supported dispatch."""
    check(
        assert_type(CustomBusinessDay() + np.datetime64("2026-01-01"), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(np.datetime64("2026-01-01") + CustomBusinessDay(), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(CustomBusinessDay() + np.timedelta64(2, "h"), BusinessDay),
        BusinessDay,
    )
    check(
        assert_type(np.timedelta64(2, "h") + CustomBusinessDay(), BusinessDay),
        BusinessDay,
    )


def test_businessday_pandas_scalars() -> None:
    """BusinessDay handles pandas scalars through supported dispatch."""
    check(
        assert_type(BusinessDay() + pd.Timestamp("2026-01-01"), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(pd.Timestamp("2026-01-01") + BusinessDay(), pd.Timestamp),
        pd.Timestamp,
    )
    check(assert_type(BusinessDay() + pd.NaT, NaTType), NaTType)
    check(assert_type(pd.NaT + BusinessDay(), NaTType), NaTType)
    check(assert_type(BusinessDay() + pd.Timedelta("2h"), BusinessDay), BusinessDay)
    check(assert_type(pd.Timedelta("2h") + BusinessDay(), BusinessDay), BusinessDay)


def test_custombusinessday_pandas_scalars() -> None:
    """CustomBusinessDay handles pandas scalars through supported dispatch."""
    check(
        assert_type(CustomBusinessDay() + pd.Timestamp("2026-01-01"), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(pd.Timestamp("2026-01-01") + CustomBusinessDay(), pd.Timestamp),
        pd.Timestamp,
    )
    check(assert_type(CustomBusinessDay() + pd.NaT, NaTType), NaTType)
    check(assert_type(pd.NaT + CustomBusinessDay(), NaTType), NaTType)
    check(
        assert_type(CustomBusinessDay() + pd.Timedelta("2h"), BusinessDay), BusinessDay
    )
    check(
        assert_type(pd.Timedelta("2h") + CustomBusinessDay(), BusinessDay), BusinessDay
    )


def test_businessday_offsets() -> None:
    """Business-day combinations return BusinessDay through supported dispatch."""
    check(assert_type(Day() + BusinessDay(), BusinessDay), BusinessDay)
    check(assert_type(BusinessDay() + Day(), BusinessDay), BusinessDay)
    check(assert_type(Day().__add__(BusinessDay()), BusinessDay), BusinessDay)
    check(assert_type(Day().__radd__(BusinessDay()), BusinessDay), BusinessDay)
    check(assert_type(BusinessDay() + Hour(), BusinessDay), BusinessDay)
    check(assert_type(Hour() + BusinessDay(), BusinessDay), BusinessDay)
    check(assert_type(BusinessDay().__add__(Hour()), BusinessDay), BusinessDay)
    check(assert_type(BusinessDay().__radd__(Hour()), BusinessDay), BusinessDay)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = Hour().__add__(BusinessDay())  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = Hour().__radd__(BusinessDay())  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _2 = BusinessDay().__add__(Day())  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _3 = BusinessDay().__radd__(Day())  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]


def test_custombusinessday_offsets() -> None:
    """Business-day combinations return BusinessDay through supported dispatch."""
    check(assert_type(Day() + CustomBusinessDay(), BusinessDay), BusinessDay)
    check(assert_type(CustomBusinessDay() + Day(), BusinessDay), BusinessDay)
    check(assert_type(Day().__add__(CustomBusinessDay()), BusinessDay), BusinessDay)
    check(assert_type(Day().__radd__(CustomBusinessDay()), BusinessDay), BusinessDay)
    check(assert_type(CustomBusinessDay() + Hour(), BusinessDay), BusinessDay)
    check(assert_type(Hour() + CustomBusinessDay(), BusinessDay), BusinessDay)
    check(assert_type(CustomBusinessDay().__add__(Hour()), BusinessDay), BusinessDay)
    check(assert_type(CustomBusinessDay().__radd__(Hour()), BusinessDay), BusinessDay)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = Hour().__add__(CustomBusinessDay())  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = Hour().__radd__(CustomBusinessDay())  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _2 = CustomBusinessDay().__add__(Day())  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _3 = CustomBusinessDay().__radd__(Day())  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]


def test_businessday_numpy_arrays() -> None:
    """BusinessDay handles numpy arrays through supported dispatch."""
    values = np.array([dt.datetime(2026, 1, 1)], dtype=object)
    empty = np.array([], dtype=object)
    check(BusinessDay() + values, np.ndarray)
    check(values + BusinessDay(), np.ndarray)
    check(BusinessDay() + empty, np.ndarray)
    check(empty + BusinessDay(), np.ndarray)
    # NumPy expressions can hide the offset's declared array result.
    check(
        assert_type(
            BusinessDay().__add__(values),
            np.ndarray[tuple[int, ...], np.dtype[np.generic]],
        ),
        np.ndarray,
    )
    check(
        assert_type(
            BusinessDay().__radd__(values),
            np.ndarray[tuple[int, ...], np.dtype[np.generic]],
        ),
        np.ndarray,
    )


def test_custombusinessday_numpy_arrays() -> None:
    """CustomBusinessDay handles numpy arrays through supported dispatch."""
    values = np.array([dt.datetime(2026, 1, 1)], dtype=object)
    empty = np.array([], dtype=object)
    check(CustomBusinessDay() + values, np.ndarray)
    check(values + CustomBusinessDay(), np.ndarray)
    check(CustomBusinessDay() + empty, np.ndarray)
    check(empty + CustomBusinessDay(), np.ndarray)
    # NumPy expressions can hide the offset's declared array result.
    check(
        assert_type(
            CustomBusinessDay().__add__(values),
            np.ndarray[tuple[int, ...], np.dtype[np.generic]],
        ),
        np.ndarray,
    )
    check(
        assert_type(
            CustomBusinessDay().__radd__(values),
            np.ndarray[tuple[int, ...], np.dtype[np.generic]],
        ),
        np.ndarray,
    )


def test_businessday_index() -> None:
    """BusinessDay handles index through supported dispatch."""
    values = pd.date_range("2026-01-01", periods=2)
    check(assert_type(BusinessDay() + values, pd.DatetimeIndex), pd.DatetimeIndex)
    check(assert_type(values + BusinessDay(), pd.DatetimeIndex), pd.DatetimeIndex)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = BusinessDay().__add__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = BusinessDay().__radd__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]


def test_custombusinessday_index() -> None:
    """CustomBusinessDay handles index through supported dispatch."""
    values = pd.date_range("2026-01-01", periods=2)
    with pytest.warns(PerformanceWarning, match="Non-vectorized DateOffset"):
        check(
            assert_type(CustomBusinessDay() + values, pd.DatetimeIndex),
            pd.DatetimeIndex,
        )
        check(
            assert_type(values + CustomBusinessDay(), pd.DatetimeIndex),
            pd.DatetimeIndex,
        )
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = CustomBusinessDay().__add__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = CustomBusinessDay().__radd__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]


def test_businessday_series() -> None:
    """BusinessDay handles series through supported dispatch."""
    values = pd.Series(pd.date_range("2026-01-01", periods=2))
    check(assert_type(BusinessDay() + values, "pd.Series[pd.Timestamp]"), pd.Series)
    check(assert_type(values + BusinessDay(), "pd.Series[pd.Timestamp]"), pd.Series)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = BusinessDay().__add__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = BusinessDay().__radd__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]


def test_custombusinessday_series() -> None:
    """CustomBusinessDay handles series through supported dispatch."""
    values = pd.Series(pd.date_range("2026-01-01", periods=2))
    with pytest.warns(PerformanceWarning, match="Non-vectorized DateOffset"):
        check(
            assert_type(CustomBusinessDay() + values, "pd.Series[pd.Timestamp]"),
            pd.Series,
        )
        check(
            assert_type(values + CustomBusinessDay(), "pd.Series[pd.Timestamp]"),
            pd.Series,
        )
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = CustomBusinessDay().__add__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = CustomBusinessDay().__radd__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
