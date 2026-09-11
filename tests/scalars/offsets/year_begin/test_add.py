import datetime as dt
from typing import (
    Any,
    assert_type,
)

import numpy as np
import pandas as pd
from pandas.api.typing import NaTType
import pytest

from tests import (
    TYPE_CHECKING_INVALID_USAGE,
    check,
)

from pandas.tseries.offsets import YearBegin


@pytest.fixture
def left() -> YearBegin:
    """Left operand."""
    return YearBegin()


def test_yearbegin_python_scalars(left: YearBegin) -> None:
    """YearBegin handles python scalars in both directions."""
    check(assert_type(left + dt.date(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.date(2026, 1, 1) + left, pd.Timestamp), pd.Timestamp)
    check(assert_type(left + dt.datetime(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.datetime(2026, 1, 1) + left, pd.Timestamp), pd.Timestamp)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = left + dt.timedelta(hours=2)  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _1 = dt.timedelta(hours=2) + left  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]


def test_yearbegin_numpy_scalars(left: YearBegin) -> None:
    """YearBegin handles numpy scalars in both directions."""
    check(assert_type(left + np.datetime64("2026-01-01"), pd.Timestamp), pd.Timestamp)
    check(assert_type(np.datetime64("2026-01-01") + left, pd.Timestamp), pd.Timestamp)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = left + np.timedelta64(2, "h")  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _1 = np.timedelta64(2, "h") + left  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]


def test_yearbegin_pandas_scalars(left: YearBegin) -> None:
    """YearBegin handles pandas scalars in both directions."""
    check(assert_type(left + pd.Timestamp("2026-01-01"), pd.Timestamp), pd.Timestamp)
    check(assert_type(pd.Timestamp("2026-01-01") + left, pd.Timestamp), pd.Timestamp)
    check(assert_type(left + pd.NaT, NaTType), NaTType)
    check(assert_type(pd.NaT + left, NaTType), NaTType)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = left + pd.Timedelta("2h")  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _1 = pd.Timedelta("2h") + left  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]


def test_yearbegin_numpy_arrays(left: YearBegin) -> None:
    """YearBegin supports object arrays, including empty arrays."""
    values = np.array([dt.datetime(2026, 1, 1)], dtype=object)
    empty = np.array([], dtype=object)
    check(
        assert_type(left + values, np.ndarray[tuple[int, ...], np.dtype[np.generic]]),
        np.ndarray,
    )
    check(assert_type(values + left, Any), np.ndarray)
    check(
        assert_type(left + empty, np.ndarray[tuple[int, ...], np.dtype[np.generic]]),
        np.ndarray,
    )
    check(assert_type(empty + left, Any), np.ndarray)
    # NumPy's forward array operator returns Any, masking offset.__radd__.
    # Check the reflected contract directly as well as the expression above.
    check(
        assert_type(
            left.__radd__(values),
            np.ndarray[tuple[int, ...], np.dtype[np.generic]],
        ),
        np.ndarray,
    )
