import datetime as dt
from typing import assert_type

import numpy as np
import pandas as pd
from pandas.api.typing import NaTType
import pytest

from tests import check

from pandas.tseries.offsets import (
    BusinessDay,
    Day,
    Hour,
    Week,
)


@pytest.fixture
def left() -> Week:
    """Left operand."""
    return Week()


def test_week_python_scalars(left: Week) -> None:
    """Week handles python scalars in both directions."""
    check(assert_type(left + dt.date(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.date(2026, 1, 1) + left, pd.Timestamp), pd.Timestamp)
    check(assert_type(left + dt.datetime(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.datetime(2026, 1, 1) + left, pd.Timestamp), pd.Timestamp)


def test_week_durations_python() -> None:
    """Python durations follow the concrete offset result family."""
    check(
        assert_type(Week(weekday=None) + dt.timedelta(hours=1), dt.timedelta),
        dt.timedelta,
    )
    check(
        assert_type(dt.timedelta(hours=1) + Week(weekday=None), dt.timedelta),
        dt.timedelta,
    )


def test_week_numpy_scalars(left: Week) -> None:
    """Week handles numpy scalars in both directions."""
    check(assert_type(left + np.datetime64("2026-01-01"), pd.Timestamp), pd.Timestamp)
    check(assert_type(np.datetime64("2026-01-01") + left, pd.Timestamp), pd.Timestamp)


def test_week_durations_numpy() -> None:
    """Numpy durations follow the concrete offset result family."""
    check(
        assert_type(Week(weekday=None) + np.timedelta64(1, "h"), dt.timedelta),
        dt.timedelta,
    )
    check(
        assert_type(np.timedelta64(1, "h") + Week(weekday=None), dt.timedelta),
        dt.timedelta,
    )


def test_week_pandas_scalars(left: Week) -> None:
    """Week handles pandas scalars in both directions."""
    check(assert_type(left + pd.Timestamp("2026-01-01"), pd.Timestamp), pd.Timestamp)
    check(assert_type(pd.Timestamp("2026-01-01") + left, pd.Timestamp), pd.Timestamp)
    check(assert_type(left + pd.NaT, NaTType), NaTType)
    check(assert_type(pd.NaT + left, NaTType), NaTType)


def test_week_durations_pandas() -> None:
    """Pandas durations follow the concrete offset result family."""
    check(
        assert_type(Week(weekday=None) + pd.Timedelta("1h"), pd.Timedelta), pd.Timedelta
    )
    check(
        assert_type(pd.Timedelta("1h") + Week(weekday=None), pd.Timedelta), pd.Timedelta
    )


def test_week_offsets() -> None:
    """Week offset combinations require weekday=None."""
    check(assert_type(Week(weekday=None) + Day(), dt.timedelta), dt.timedelta)
    check(assert_type(Day() + Week(weekday=None), dt.timedelta), dt.timedelta)
    check(
        assert_type(Week(1, weekday=None) + Week(2, weekday=None), dt.timedelta),
        dt.timedelta,
    )
    check(
        assert_type(Week(2, weekday=None) + Week(1, weekday=None), dt.timedelta),
        dt.timedelta,
    )
    check(assert_type(Week(weekday=None) + Hour(), pd.Timedelta), pd.Timedelta)
    check(assert_type(Hour() + Week(weekday=None), pd.Timedelta), pd.Timedelta)
    check(assert_type(Week(weekday=None) + BusinessDay(), BusinessDay), BusinessDay)
    check(assert_type(BusinessDay() + Week(weekday=None), BusinessDay), BusinessDay)


def test_week_numpy_arrays(left: Week) -> None:
    """Week supports object arrays, including empty arrays."""
    values = np.array([dt.datetime(2026, 1, 1)], dtype=object)
    empty = np.array([], dtype=object)
    check(left + values, np.ndarray)
    check(values + left, np.ndarray)
    check(left + empty, np.ndarray)
    check(empty + left, np.ndarray)
    # NumPy expressions can hide the offset's declared array result.
    check(
        assert_type(
            left.__add__(values), np.ndarray[tuple[int, ...], np.dtype[np.generic]]
        ),
        np.ndarray,
    )
    check(
        assert_type(
            left.__radd__(values), np.ndarray[tuple[int, ...], np.dtype[np.generic]]
        ),
        np.ndarray,
    )
