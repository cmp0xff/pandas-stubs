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

from pandas.tseries.offsets import BHalfYearBegin


@pytest.fixture
def left() -> BHalfYearBegin:
    """Left operand."""
    return BHalfYearBegin()


def test_bhalfyearbegin_python_scalars(left: BHalfYearBegin) -> None:
    """BHalfYearBegin handles python scalars in both directions."""
    check(assert_type(left + dt.date(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.date(2026, 1, 1) + left, pd.Timestamp), pd.Timestamp)
    check(assert_type(left + dt.datetime(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.datetime(2026, 1, 1) + left, pd.Timestamp), pd.Timestamp)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = left + dt.timedelta(hours=2)  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _1 = dt.timedelta(hours=2) + left  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]


def test_bhalfyearbegin_numpy_scalars(left: BHalfYearBegin) -> None:
    """BHalfYearBegin handles numpy scalars in both directions."""
    check(assert_type(left + np.datetime64("2026-01-01"), pd.Timestamp), pd.Timestamp)
    check(assert_type(np.datetime64("2026-01-01") + left, pd.Timestamp), pd.Timestamp)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = left + np.timedelta64(2, "h")  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _1 = np.timedelta64(2, "h") + left  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]


def test_bhalfyearbegin_pandas_scalars(left: BHalfYearBegin) -> None:
    """BHalfYearBegin handles pandas scalars in both directions."""
    check(assert_type(left + pd.Timestamp("2026-01-01"), pd.Timestamp), pd.Timestamp)
    check(assert_type(pd.Timestamp("2026-01-01") + left, pd.Timestamp), pd.Timestamp)
    check(assert_type(left + pd.NaT, NaTType), NaTType)
    check(assert_type(pd.NaT + left, NaTType), NaTType)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = left + pd.Timedelta("2h")  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _1 = pd.Timedelta("2h") + left  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]


def test_bhalfyearbegin_numpy_arrays(left: BHalfYearBegin) -> None:
    """BHalfYearBegin supports object arrays, including empty arrays."""
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


def test_pandas_scalar_regression(left: BHalfYearBegin) -> None:
    """Test half-year offsets introduced in pandas 3.0 GH1654."""
    ts = pd.Timestamp(2024, 2, 1)
    check(assert_type(left + ts, pd.Timestamp), pd.Timestamp)
    check(assert_type(ts + left, pd.Timestamp), pd.Timestamp)
