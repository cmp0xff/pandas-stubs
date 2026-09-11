import datetime as dt
from typing import assert_type

import numpy as np
import pandas as pd
from pandas.api.typing import NaTType
import pytest

from tests import check

from pandas.tseries.offsets import (
    Hour,
    Micro,
    Milli,
    Second,
    Tick,
)


@pytest.fixture
def left() -> Milli:
    """Left operand."""
    return Milli()


def test_milli_python_scalars(left: Milli) -> None:
    """Milli scalar addition returns Timestamp, NaT, or Timedelta."""
    check(assert_type(left + dt.date(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.date(2026, 1, 1) + left, pd.Timestamp), pd.Timestamp)
    check(assert_type(left + dt.datetime(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.datetime(2026, 1, 1) + left, pd.Timestamp), pd.Timestamp)
    check(assert_type(left + dt.timedelta(hours=2), pd.Timedelta), pd.Timedelta)
    check(assert_type(dt.timedelta(hours=2) + left, pd.Timedelta), pd.Timedelta)


def test_milli_numpy_scalars(left: Milli) -> None:
    """Milli scalar addition returns Timestamp, NaT, or Timedelta."""
    check(assert_type(left + np.datetime64("2026-01-01"), pd.Timestamp), pd.Timestamp)
    check(assert_type(np.datetime64("2026-01-01") + left, pd.Timestamp), pd.Timestamp)
    check(assert_type(left + np.timedelta64(2, "h"), pd.Timedelta), pd.Timedelta)
    check(assert_type(np.timedelta64(2, "h") + left, pd.Timedelta), pd.Timedelta)


def test_milli_pandas_scalars(left: Milli) -> None:
    """Milli scalar addition returns Timestamp, NaT, or Timedelta."""
    check(assert_type(left + pd.Timestamp("2026-01-01"), pd.Timestamp), pd.Timestamp)
    check(assert_type(pd.Timestamp("2026-01-01") + left, pd.Timestamp), pd.Timestamp)
    check(assert_type(left + pd.NaT, NaTType), NaTType)
    check(assert_type(pd.NaT + left, NaTType), NaTType)
    check(assert_type(left + pd.Timedelta("2h"), pd.Timedelta), pd.Timedelta)
    check(assert_type(pd.Timedelta("2h") + left, pd.Timedelta), pd.Timedelta)


def test_homogeneous_milli() -> None:
    """Homogeneous concrete ticks preserve their class."""
    check(assert_type(Milli(1) + Milli(2), Milli), Milli)
    check(assert_type(Milli(2) + Milli(1), Milli), Milli)


class SpecialMilli(Milli):
    """Milli subclass for normalization and cancellation."""


def test_milli_subclass() -> None:
    """Milli subclasses use Tick results even with homogeneous operands."""
    check(assert_type(SpecialMilli(500) + Milli(500), Tick), Second)
    check(assert_type(Milli(500) + SpecialMilli(500), Tick), Second)
    check(assert_type(SpecialMilli(500) + Milli(-500), Tick), Hour)
    check(assert_type(Milli(-500) + SpecialMilli(500), Tick), Hour)


def test_finer_mixed_ticks(left: Milli) -> None:
    """Finer mixed ticks retain the broad Tick result."""
    check(assert_type(Second() + left, Tick), Milli)
    check(assert_type(left + Second(), Tick), Milli)
    check(assert_type(left + Micro(), Tick), Micro)
    check(assert_type(Micro() + left, Tick), Micro)
