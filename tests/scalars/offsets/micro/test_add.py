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
    Nano,
    Tick,
)


@pytest.fixture
def left() -> Micro:
    """Left operand."""
    return Micro()


def test_micro_python_scalars(left: Micro) -> None:
    """Micro scalar addition returns Timestamp, NaT, or Timedelta."""
    check(assert_type(left + dt.date(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.date(2026, 1, 1) + left, pd.Timestamp), pd.Timestamp)
    check(assert_type(left + dt.datetime(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.datetime(2026, 1, 1) + left, pd.Timestamp), pd.Timestamp)
    check(assert_type(left + dt.timedelta(hours=2), pd.Timedelta), pd.Timedelta)
    check(assert_type(dt.timedelta(hours=2) + left, pd.Timedelta), pd.Timedelta)


def test_micro_numpy_scalars(left: Micro) -> None:
    """Micro scalar addition returns Timestamp, NaT, or Timedelta."""
    check(assert_type(left + np.datetime64("2026-01-01"), pd.Timestamp), pd.Timestamp)
    check(assert_type(np.datetime64("2026-01-01") + left, pd.Timestamp), pd.Timestamp)
    check(assert_type(left + np.timedelta64(2, "h"), pd.Timedelta), pd.Timedelta)
    check(assert_type(np.timedelta64(2, "h") + left, pd.Timedelta), pd.Timedelta)


def test_micro_pandas_scalars(left: Micro) -> None:
    """Micro scalar addition returns Timestamp, NaT, or Timedelta."""
    check(assert_type(left + pd.Timestamp("2026-01-01"), pd.Timestamp), pd.Timestamp)
    check(assert_type(pd.Timestamp("2026-01-01") + left, pd.Timestamp), pd.Timestamp)
    check(assert_type(left + pd.NaT, NaTType), NaTType)
    check(assert_type(pd.NaT + left, NaTType), NaTType)
    check(assert_type(left + pd.Timedelta("2h"), pd.Timedelta), pd.Timedelta)
    check(assert_type(pd.Timedelta("2h") + left, pd.Timedelta), pd.Timedelta)


def test_homogeneous_micro() -> None:
    """Homogeneous concrete ticks preserve their class."""
    check(assert_type(Micro(1) + Micro(2), Micro), Micro)
    check(assert_type(Micro(2) + Micro(1), Micro), Micro)


class SpecialMicro(Micro):
    """Micro subclass for normalization and cancellation."""


def test_micro_subclass() -> None:
    """Micro subclasses use Tick results even with homogeneous operands."""
    check(assert_type(SpecialMicro(500) + Micro(500), Tick), Milli)
    check(assert_type(Micro(500) + SpecialMicro(500), Tick), Milli)
    check(assert_type(SpecialMicro(500) + Micro(-500), Tick), Hour)
    check(assert_type(Micro(-500) + SpecialMicro(500), Tick), Hour)


def test_finer_mixed_ticks(left: Micro) -> None:
    """Finer mixed ticks retain the broad Tick result."""
    check(assert_type(Milli() + left, Tick), Micro)
    check(assert_type(left + Milli(), Tick), Micro)
    check(assert_type(left + Nano(), Tick), Nano)
    check(assert_type(Nano() + left, Tick), Nano)
