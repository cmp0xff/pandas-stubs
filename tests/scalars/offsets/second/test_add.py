import datetime as dt
from typing import assert_type

import numpy as np
import pandas as pd
from pandas.api.typing import NaTType
import pytest

from tests import check

from pandas.tseries.offsets import (
    Hour,
    Milli,
    Minute,
    Second,
    Tick,
)


@pytest.fixture
def left() -> Second:
    """Left operand."""
    return Second()


def test_second_python_scalars(left: Second) -> None:
    """Second scalar addition returns Timestamp, NaT, or Timedelta."""
    check(assert_type(left + dt.date(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.date(2026, 1, 1) + left, pd.Timestamp), pd.Timestamp)
    check(assert_type(left + dt.datetime(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.datetime(2026, 1, 1) + left, pd.Timestamp), pd.Timestamp)
    check(assert_type(left + dt.timedelta(hours=2), pd.Timedelta), pd.Timedelta)
    check(assert_type(dt.timedelta(hours=2) + left, pd.Timedelta), pd.Timedelta)


def test_second_numpy_scalars(left: Second) -> None:
    """Second scalar addition returns Timestamp, NaT, or Timedelta."""
    check(assert_type(left + np.datetime64("2026-01-01"), pd.Timestamp), pd.Timestamp)
    check(assert_type(np.datetime64("2026-01-01") + left, pd.Timestamp), pd.Timestamp)
    check(assert_type(left + np.timedelta64(2, "h"), pd.Timedelta), pd.Timedelta)
    check(assert_type(np.timedelta64(2, "h") + left, pd.Timedelta), pd.Timedelta)


def test_second_pandas_scalars(left: Second) -> None:
    """Second scalar addition returns Timestamp, NaT, or Timedelta."""
    check(assert_type(left + pd.Timestamp("2026-01-01"), pd.Timestamp), pd.Timestamp)
    check(assert_type(pd.Timestamp("2026-01-01") + left, pd.Timestamp), pd.Timestamp)
    check(assert_type(left + pd.NaT, NaTType), NaTType)
    check(assert_type(pd.NaT + left, NaTType), NaTType)
    check(assert_type(left + pd.Timedelta("2h"), pd.Timedelta), pd.Timedelta)
    check(assert_type(pd.Timedelta("2h") + left, pd.Timedelta), pd.Timedelta)


def test_homogeneous_second() -> None:
    """Homogeneous concrete ticks preserve their class."""
    check(assert_type(Second(1) + Second(2), Second), Second)
    check(assert_type(Second(2) + Second(1), Second), Second)


def test_mixed_ticks() -> None:
    """Mixed ticks normalize by value, including cancellation."""
    check(assert_type(Minute(60) + Second(3600), Tick), Hour)
    check(assert_type(Second(3600) + Minute(60), Tick), Hour)


class SpecialSecond(Second):
    """Second subclass for normalization and cancellation."""


def test_second_subclass() -> None:
    """Second subclasses use Tick results even with homogeneous operands."""
    check(assert_type(SpecialSecond(30) + Second(30), Tick), Minute)
    check(assert_type(Second(30) + SpecialSecond(30), Tick), Minute)
    check(assert_type(SpecialSecond(30) + Second(-30), Tick), Hour)
    check(assert_type(Second(-30) + SpecialSecond(30), Tick), Hour)


def test_finer_mixed_ticks(left: Second) -> None:
    """Finer mixed ticks retain the broad Tick result."""
    check(assert_type(left + Milli(), Tick), Milli)
    check(assert_type(Milli() + left, Tick), Milli)
