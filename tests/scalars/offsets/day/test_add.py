import datetime as dt
from typing import (
    Any,
    assert_type,
)

import numpy as np
import pandas as pd
from pandas.api.typing import NaTType
import pytest

from tests import check

from pandas.tseries.offsets import (
    Day,
    Hour,
    Week,
)


@pytest.fixture
def left() -> Day:
    """Left operand."""
    return Day()


def test_day_python_scalars(left: Day) -> None:
    """Python dates become Timestamp; durations follow the offset family."""
    check(assert_type(left + dt.date(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.date(2026, 1, 1) + left, pd.Timestamp), pd.Timestamp)
    check(assert_type(left + dt.datetime(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.datetime(2026, 1, 1) + left, pd.Timestamp), pd.Timestamp)
    check(assert_type(left + dt.timedelta(hours=2), dt.timedelta), dt.timedelta)
    check(assert_type(dt.timedelta(hours=2) + left, dt.timedelta), dt.timedelta)


def test_day_numpy_scalars(left: Day) -> None:
    """NumPy temporal scalars use the supported scalar results."""
    check(assert_type(left + np.datetime64("2026-01-01"), pd.Timestamp), pd.Timestamp)
    check(assert_type(np.datetime64("2026-01-01") + left, pd.Timestamp), pd.Timestamp)
    check(assert_type(left + np.timedelta64(2, "h"), np.timedelta64), np.timedelta64)
    check(assert_type(np.timedelta64(2, "h") + left, np.timedelta64), np.timedelta64)


def test_day_pandas_scalars(left: Day) -> None:
    """Timestamp and NaT retain pandas scalar results."""
    check(assert_type(left + pd.Timestamp("2026-01-01"), pd.Timestamp), pd.Timestamp)
    check(assert_type(pd.Timestamp("2026-01-01") + left, pd.Timestamp), pd.Timestamp)
    check(assert_type(left + pd.NaT, NaTType), NaTType)
    check(assert_type(pd.NaT + left, NaTType), NaTType)
    check(assert_type(left + pd.Timedelta("2h"), pd.Timedelta), pd.Timedelta)
    check(assert_type(pd.Timedelta("2h") + left, pd.Timedelta), pd.Timedelta)


def test_day_offsets(left: Day) -> None:
    """Day combines with days, ticks, and unanchored weeks."""
    check(assert_type(Day(1) + Day(2), Day), Day)
    check(assert_type(Day(2) + Day(1), Day), Day)
    check(assert_type(left + Hour(), pd.Timedelta), pd.Timedelta)
    check(assert_type(Hour() + left, pd.Timedelta), pd.Timedelta)
    check(assert_type(left + Week(), dt.timedelta), dt.timedelta)
    check(assert_type(Week() + left, dt.timedelta), dt.timedelta)


def test_day_numpy_arrays(left: Day) -> None:
    """Object-array results do not promise shape or dtype preservation."""
    # NumPy returns Any for array + Day, masking the reflected contract.
    values = np.array([dt.datetime(2026, 1, 1)], dtype=object)
    check(
        assert_type(
            left.__radd__(values), np.ndarray[tuple[int, ...], np.dtype[np.generic]]
        ),
        np.ndarray,
    )
    check(
        assert_type(left + values, np.ndarray[tuple[int, ...], np.dtype[np.generic]]),
        np.ndarray,
    )
    check(assert_type(values + left, Any), np.ndarray)
    empty = np.array([], dtype=object)
    check(
        assert_type(left + empty, np.ndarray[tuple[int, ...], np.dtype[np.generic]]),
        np.ndarray,
    )
    check(assert_type(empty + left, Any), np.ndarray)
    check(
        assert_type(
            left.__radd__(empty), np.ndarray[tuple[int, ...], np.dtype[np.generic]]
        ),
        np.ndarray,
    )


def test_day_array_dtype(left: Day) -> None:
    """Day can change an object array to timedelta64 dtype."""
    values = np.array([np.timedelta64(1, "h")], dtype=object)
    result = check(
        assert_type(left + values, np.ndarray[tuple[int, ...], np.dtype[np.generic]]),
        np.ndarray,
    )
    assert result.dtype.kind == "m"
