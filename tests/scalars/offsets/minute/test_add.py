import datetime as dt
from typing import assert_type

import numpy as np
import pandas as pd
from pandas.api.typing import NaTType
import pytest

from tests import check

from pandas.tseries.offsets import (
    Hour,
    Minute,
    Second,
    Tick,
)


@pytest.fixture
def left() -> Minute:
    """Left operand."""
    return Minute()


def test_minute_python_scalars(left: Minute) -> None:
    """Minute scalar addition returns Timestamp, NaT, or Timedelta."""
    check(assert_type(left + dt.date(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.date(2026, 1, 1) + left, pd.Timestamp), pd.Timestamp)
    check(assert_type(left + dt.datetime(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.datetime(2026, 1, 1) + left, pd.Timestamp), pd.Timestamp)
    check(assert_type(left + dt.timedelta(hours=2), pd.Timedelta), pd.Timedelta)
    check(assert_type(dt.timedelta(hours=2) + left, pd.Timedelta), pd.Timedelta)


def test_minute_numpy_scalars(left: Minute) -> None:
    """Minute scalar addition returns Timestamp, NaT, or Timedelta."""
    check(assert_type(left + np.datetime64("2026-01-01"), pd.Timestamp), pd.Timestamp)
    check(assert_type(np.datetime64("2026-01-01") + left, pd.Timestamp), pd.Timestamp)
    check(assert_type(left + np.timedelta64(2, "h"), pd.Timedelta), pd.Timedelta)
    check(assert_type(np.timedelta64(2, "h") + left, pd.Timedelta), pd.Timedelta)


def test_minute_pandas_scalars(left: Minute) -> None:
    """Minute scalar addition returns Timestamp, NaT, or Timedelta."""
    check(assert_type(left + pd.Timestamp("2026-01-01"), pd.Timestamp), pd.Timestamp)
    check(assert_type(pd.Timestamp("2026-01-01") + left, pd.Timestamp), pd.Timestamp)
    check(assert_type(left + pd.NaT, NaTType), NaTType)
    check(assert_type(pd.NaT + left, NaTType), NaTType)
    check(assert_type(left + pd.Timedelta("2h"), pd.Timedelta), pd.Timedelta)
    check(assert_type(pd.Timedelta("2h") + left, pd.Timedelta), pd.Timedelta)


def test_homogeneous_minute() -> None:
    """Homogeneous concrete ticks preserve their class."""
    check(assert_type(Minute(1) + Minute(2), Minute), Minute)
    check(assert_type(Minute(2) + Minute(1), Minute), Minute)


def test_mixed_ticks() -> None:
    """Mixed ticks normalize by value, including cancellation."""
    check(assert_type(Hour(1) + Minute(30), Tick), Minute)
    check(assert_type(Minute(30) + Hour(1), Tick), Minute)
    check(assert_type(Hour(1) + Minute(-60), Tick), Hour)
    check(assert_type(Minute(-60) + Hour(1), Tick), Hour)
    check(assert_type(Minute(60) + Second(3600), Tick), Hour)
    check(assert_type(Second(3600) + Minute(60), Tick), Hour)
    assert Hour(1) + Minute(-60) == Hour(0)


class SpecialMinute(Minute):
    """Minute subclass that can normalize to Hour."""


def test_subclass() -> None:
    """Hour subclasses stay hourly; minute subclasses can normalize."""
    check(assert_type(SpecialMinute(30) + Minute(30), Tick), Hour)
    check(assert_type(Minute(30) + SpecialMinute(30), Tick), Hour)
    check(assert_type(SpecialMinute(30) + Minute(-30), Tick), Hour)
    check(assert_type(Minute(-30) + SpecialMinute(30), Tick), Hour)
