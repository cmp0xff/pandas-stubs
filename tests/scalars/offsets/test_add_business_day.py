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
    BusinessDay,
    CustomBusinessDay,
    Day,
    Hour,
)


def test_business_day_python_scalars() -> None:
    """Python dates become Timestamp; durations follow the offset family."""
    check(assert_type(BusinessDay() + dt.date(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.date(2026, 1, 1) + BusinessDay(), pd.Timestamp), pd.Timestamp)
    check(
        assert_type(BusinessDay().__add__(dt.date(2026, 1, 1)), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(BusinessDay().__radd__(dt.date(2026, 1, 1)), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(BusinessDay() + dt.datetime(2026, 1, 1), pd.Timestamp), pd.Timestamp
    )
    check(
        assert_type(dt.datetime(2026, 1, 1) + BusinessDay(), pd.Timestamp), pd.Timestamp
    )
    check(
        assert_type(BusinessDay().__add__(dt.datetime(2026, 1, 1)), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(BusinessDay().__radd__(dt.datetime(2026, 1, 1)), pd.Timestamp),
        pd.Timestamp,
    )
    check(assert_type(BusinessDay() + dt.timedelta(hours=2), BusinessDay), BusinessDay)
    check(assert_type(dt.timedelta(hours=2) + BusinessDay(), BusinessDay), BusinessDay)
    check(
        assert_type(BusinessDay().__add__(dt.timedelta(hours=2)), BusinessDay),
        BusinessDay,
    )
    check(
        assert_type(BusinessDay().__radd__(dt.timedelta(hours=2)), BusinessDay),
        BusinessDay,
    )


def test_businessday_durations_python() -> None:
    """Python durations follow the concrete offset result family."""
    check(assert_type(BusinessDay() + dt.timedelta(hours=2), BusinessDay), BusinessDay)
    check(assert_type(dt.timedelta(hours=2) + BusinessDay(), BusinessDay), BusinessDay)
    check(
        assert_type(BusinessDay().__add__(dt.timedelta(hours=2)), BusinessDay),
        BusinessDay,
    )
    check(
        assert_type(BusinessDay().__radd__(dt.timedelta(hours=2)), BusinessDay),
        BusinessDay,
    )


def test_custombusinessday_durations_python() -> None:
    """Python durations follow the concrete offset result family."""
    check(
        assert_type(CustomBusinessDay() + dt.timedelta(hours=2), BusinessDay),
        BusinessDay,
    )
    check(
        assert_type(dt.timedelta(hours=2) + CustomBusinessDay(), BusinessDay),
        BusinessDay,
    )
    check(
        assert_type(CustomBusinessDay().__add__(dt.timedelta(hours=2)), BusinessDay),
        BusinessDay,
    )
    check(
        assert_type(CustomBusinessDay().__radd__(dt.timedelta(hours=2)), BusinessDay),
        BusinessDay,
    )


def test_business_day_numpy_scalars() -> None:
    """NumPy temporal scalars use the supported scalar results."""
    check(
        assert_type(BusinessDay() + np.datetime64("2026-01-01"), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(np.datetime64("2026-01-01") + BusinessDay(), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(BusinessDay().__add__(np.datetime64("2026-01-01")), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(BusinessDay().__radd__(np.datetime64("2026-01-01")), pd.Timestamp),
        pd.Timestamp,
    )
    check(assert_type(BusinessDay() + np.timedelta64(2, "h"), BusinessDay), BusinessDay)
    check(assert_type(np.timedelta64(2, "h") + BusinessDay(), BusinessDay), BusinessDay)
    check(
        assert_type(BusinessDay().__add__(np.timedelta64(2, "h")), BusinessDay),
        BusinessDay,
    )
    check(
        assert_type(BusinessDay().__radd__(np.timedelta64(2, "h")), BusinessDay),
        BusinessDay,
    )


def test_businessday_durations_numpy() -> None:
    """Numpy durations follow the concrete offset result family."""
    check(assert_type(BusinessDay() + np.timedelta64(2, "h"), BusinessDay), BusinessDay)
    check(assert_type(np.timedelta64(2, "h") + BusinessDay(), BusinessDay), BusinessDay)
    check(
        assert_type(BusinessDay().__add__(np.timedelta64(2, "h")), BusinessDay),
        BusinessDay,
    )
    check(
        assert_type(BusinessDay().__radd__(np.timedelta64(2, "h")), BusinessDay),
        BusinessDay,
    )


def test_custombusinessday_durations_numpy() -> None:
    """Numpy durations follow the concrete offset result family."""
    check(
        assert_type(CustomBusinessDay() + np.timedelta64(2, "h"), BusinessDay),
        BusinessDay,
    )
    check(
        assert_type(np.timedelta64(2, "h") + CustomBusinessDay(), BusinessDay),
        BusinessDay,
    )
    check(
        assert_type(CustomBusinessDay().__add__(np.timedelta64(2, "h")), BusinessDay),
        BusinessDay,
    )
    check(
        assert_type(CustomBusinessDay().__radd__(np.timedelta64(2, "h")), BusinessDay),
        BusinessDay,
    )


def test_business_day_pandas_scalars() -> None:
    """Timestamp and NaT retain pandas scalar results."""
    check(
        assert_type(BusinessDay() + pd.Timestamp("2026-01-01"), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(pd.Timestamp("2026-01-01") + BusinessDay(), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(BusinessDay().__add__(pd.Timestamp("2026-01-01")), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(BusinessDay().__radd__(pd.Timestamp("2026-01-01")), pd.Timestamp),
        pd.Timestamp,
    )
    check(assert_type(BusinessDay() + pd.NaT, NaTType), NaTType)
    check(assert_type(pd.NaT + BusinessDay(), NaTType), NaTType)
    check(assert_type(BusinessDay().__add__(pd.NaT), NaTType), NaTType)
    check(assert_type(BusinessDay().__radd__(pd.NaT), NaTType), NaTType)
    check(assert_type(BusinessDay() + pd.Timedelta("2h"), BusinessDay), BusinessDay)
    check(assert_type(pd.Timedelta("2h") + BusinessDay(), BusinessDay), BusinessDay)
    check(
        assert_type(BusinessDay().__add__(pd.Timedelta("2h")), BusinessDay), BusinessDay
    )
    check(
        assert_type(BusinessDay().__radd__(pd.Timedelta("2h")), BusinessDay),
        BusinessDay,
    )


def test_businessday_durations_pandas() -> None:
    """Pandas durations follow the concrete offset result family."""
    check(assert_type(BusinessDay() + pd.Timedelta("2h"), BusinessDay), BusinessDay)
    check(assert_type(pd.Timedelta("2h") + BusinessDay(), BusinessDay), BusinessDay)
    check(
        assert_type(BusinessDay().__add__(pd.Timedelta("2h")), BusinessDay), BusinessDay
    )
    check(
        assert_type(BusinessDay().__radd__(pd.Timedelta("2h")), BusinessDay),
        BusinessDay,
    )


def test_custombusinessday_durations_pandas() -> None:
    """Pandas durations follow the concrete offset result family."""
    check(
        assert_type(CustomBusinessDay() + pd.Timedelta("2h"), BusinessDay), BusinessDay
    )
    check(
        assert_type(pd.Timedelta("2h") + CustomBusinessDay(), BusinessDay), BusinessDay
    )
    check(
        assert_type(CustomBusinessDay().__add__(pd.Timedelta("2h")), BusinessDay),
        BusinessDay,
    )
    check(
        assert_type(CustomBusinessDay().__radd__(pd.Timedelta("2h")), BusinessDay),
        BusinessDay,
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


def test_business_day_numpy_arrays() -> None:
    """Object-array results do not promise shape or dtype preservation."""
    values = np.array([dt.datetime(2026, 1, 1)], dtype=object)
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
    empty = np.array([], dtype=object)
    check(
        assert_type(
            BusinessDay().__add__(empty),
            np.ndarray[tuple[int, ...], np.dtype[np.generic]],
        ),
        np.ndarray,
    )
    check(
        assert_type(
            BusinessDay().__radd__(empty),
            np.ndarray[tuple[int, ...], np.dtype[np.generic]],
        ),
        np.ndarray,
    )


def test_business_day_index() -> None:
    """Containers support expressions through their own dispatch."""
    values = pd.date_range("2026-01-01", periods=2)
    check(assert_type(BusinessDay() + values, pd.DatetimeIndex), pd.DatetimeIndex)
    check(assert_type(values + BusinessDay(), pd.DatetimeIndex), pd.DatetimeIndex)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = BusinessDay().__add__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = BusinessDay().__radd__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]


def test_business_day_series() -> None:
    """Containers support expressions through their own dispatch."""
    values = pd.Series(pd.date_range("2026-01-01", periods=2))
    check(assert_type(BusinessDay() + values, "pd.Series[pd.Timestamp]"), pd.Series)
    check(assert_type(values + BusinessDay(), "pd.Series[pd.Timestamp]"), pd.Series)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = BusinessDay().__add__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = BusinessDay().__radd__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
