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
    BusinessDay,
    CustomBusinessDay,
    Day,
    Hour,
)


@pytest.fixture
def left() -> CustomBusinessDay:
    """Left operand."""
    return CustomBusinessDay()


def test_custombusinessday_python_scalars(left: CustomBusinessDay) -> None:
    """CustomBusinessDay handles python scalars through supported dispatch."""
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
    check(
        assert_type(left + dt.timedelta(hours=2), BusinessDay),
        BusinessDay,
    )
    check(
        assert_type(dt.timedelta(hours=2) + left, BusinessDay),
        BusinessDay,
    )


def test_custombusinessday_numpy_scalars(left: CustomBusinessDay) -> None:
    """CustomBusinessDay handles numpy scalars through supported dispatch."""
    check(
        assert_type(left + np.datetime64("2026-01-01"), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(np.datetime64("2026-01-01") + left, pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(left + np.timedelta64(2, "h"), BusinessDay),
        BusinessDay,
    )
    check(
        assert_type(np.timedelta64(2, "h") + left, BusinessDay),
        BusinessDay,
    )


def test_custombusinessday_pandas_scalars(left: CustomBusinessDay) -> None:
    """CustomBusinessDay handles pandas scalars through supported dispatch."""
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


def test_custombusinessday_offsets(left: CustomBusinessDay) -> None:
    """Business-day combinations return BusinessDay through supported dispatch."""
    check(assert_type(Day() + left, BusinessDay), BusinessDay)
    check(assert_type(left + Day(), BusinessDay), BusinessDay)
    check(assert_type(left + Hour(), BusinessDay), BusinessDay)
    check(assert_type(Hour() + left, BusinessDay), BusinessDay)


def test_custombusinessday_numpy_arrays(left: CustomBusinessDay) -> None:
    """CustomBusinessDay handles numpy arrays through supported dispatch."""
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
