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

from pandas.tseries.offsets import CustomBusinessMonthEnd


@pytest.fixture
def left() -> CustomBusinessMonthEnd:
    """Left operand."""
    return CustomBusinessMonthEnd()


def test_custombusinessmonthend_python_scalars(left: CustomBusinessMonthEnd) -> None:
    """CustomBusinessMonthEnd handles python scalars in both directions."""
    check(
        assert_type(left + dt.date(2026, 1, 1), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(dt.date(2026, 1, 1) + left, pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(left + dt.datetime(2026, 1, 1), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(dt.datetime(2026, 1, 1) + left, pd.Timestamp),
        pd.Timestamp,
    )
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = left + dt.timedelta(hours=2)  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _1 = dt.timedelta(hours=2) + left  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]


def test_custombusinessmonthend_numpy_scalars(left: CustomBusinessMonthEnd) -> None:
    """CustomBusinessMonthEnd handles numpy scalars in both directions."""
    check(
        assert_type(left + np.datetime64("2026-01-01"), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(np.datetime64("2026-01-01") + left, pd.Timestamp),
        pd.Timestamp,
    )
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = left.__add__(np.timedelta64(2, "h"))  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = left.__radd__(np.timedelta64(2, "h"))  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]


def test_custombusinessmonthend_pandas_scalars(left: CustomBusinessMonthEnd) -> None:
    """CustomBusinessMonthEnd handles pandas scalars in both directions."""
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
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = left + pd.Timedelta("2h")  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _1 = pd.Timedelta("2h") + left  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]


def test_custombusinessmonthend_numpy_arrays(left: CustomBusinessMonthEnd) -> None:
    """CustomBusinessMonthEnd supports object arrays, including empty arrays."""
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
