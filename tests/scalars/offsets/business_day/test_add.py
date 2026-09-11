import datetime as dt
from typing import assert_type

import numpy as np
import pandas as pd
from pandas.api.typing import NaTType
import pytest

from tests import (
    TYPE_CHECKING_INVALID_USAGE,
    check,
)

from pandas.tseries.offsets import (
    BusinessDay,
    Day,
    Hour,
)


@pytest.fixture
def left() -> BusinessDay:
    """Left operand."""
    return BusinessDay()


def test_businessday_python_scalars(left: BusinessDay) -> None:
    """BusinessDay handles python scalars through supported dispatch."""
    check(assert_type(left + dt.date(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.date(2026, 1, 1) + left, pd.Timestamp), pd.Timestamp)
    check(assert_type(left + dt.datetime(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.datetime(2026, 1, 1) + left, pd.Timestamp), pd.Timestamp)
    check(assert_type(left + dt.timedelta(hours=2), BusinessDay), BusinessDay)
    check(assert_type(dt.timedelta(hours=2) + left, BusinessDay), BusinessDay)


def test_businessday_numpy_scalars(left: BusinessDay) -> None:
    """BusinessDay handles numpy scalars through supported dispatch."""
    check(
        assert_type(left + np.datetime64("2026-01-01"), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(np.datetime64("2026-01-01") + left, pd.Timestamp),
        pd.Timestamp,
    )
    check(assert_type(left + np.timedelta64(2, "h"), BusinessDay), BusinessDay)
    check(assert_type(np.timedelta64(2, "h") + left, BusinessDay), BusinessDay)


def test_businessday_pandas_scalars(left: BusinessDay) -> None:
    """BusinessDay handles pandas scalars through supported dispatch."""
    check(
        assert_type(left + pd.Timestamp("2026-01-01"), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(pd.Timestamp("2026-01-01") + left, pd.Timestamp),
        pd.Timestamp,
    )
    check(assert_type(left + pd.NaT, NaTType), NaTType)
    check(assert_type(pd.NaT + left, NaTType), NaTType)
    check(assert_type(left + pd.Timedelta("2h"), BusinessDay), BusinessDay)
    check(assert_type(pd.Timedelta("2h") + left, BusinessDay), BusinessDay)


def test_businessday_offsets(left: BusinessDay) -> None:
    """Business-day combinations return BusinessDay through supported dispatch."""
    check(assert_type(Day() + left, BusinessDay), BusinessDay)
    check(assert_type(left + Day(), BusinessDay), BusinessDay)
    check(assert_type(Day().__add__(left), BusinessDay), BusinessDay)
    check(assert_type(Day().__radd__(left), BusinessDay), BusinessDay)
    check(assert_type(left + Hour(), BusinessDay), BusinessDay)
    check(assert_type(Hour() + left, BusinessDay), BusinessDay)
    check(assert_type(left.__add__(Hour()), BusinessDay), BusinessDay)
    check(assert_type(left.__radd__(Hour()), BusinessDay), BusinessDay)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = Hour().__add__(left)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = Hour().__radd__(left)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _2 = left.__add__(Day())  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _3 = left.__radd__(Day())  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]


def test_businessday_numpy_arrays(left: BusinessDay) -> None:
    """BusinessDay handles numpy arrays through supported dispatch."""
    values = np.array([dt.datetime(2026, 1, 1)], dtype=object)
    empty = np.array([], dtype=object)
    check(left + values, np.ndarray)
    check(values + left, np.ndarray)
    check(left + empty, np.ndarray)
    check(empty + left, np.ndarray)
    # NumPy expressions can hide the offset's declared array result.
    check(
        assert_type(
            left.__add__(values),
            np.ndarray[tuple[int, ...], np.dtype[np.generic]],
        ),
        np.ndarray,
    )
    check(
        assert_type(
            left.__radd__(values),
            np.ndarray[tuple[int, ...], np.dtype[np.generic]],
        ),
        np.ndarray,
    )
