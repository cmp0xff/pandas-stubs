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
    Nano,
    Tick,
)


@pytest.fixture
def left() -> Nano:
    """Left operand."""
    return Nano()


def test_nano_python_scalars(left: Nano) -> None:
    """Nano scalar addition returns Timestamp, NaT, or Timedelta."""
    check(assert_type(left + dt.date(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.date(2026, 1, 1) + left, pd.Timestamp), pd.Timestamp)
    check(assert_type(left + dt.datetime(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.datetime(2026, 1, 1) + left, pd.Timestamp), pd.Timestamp)
    check(assert_type(left + dt.timedelta(hours=2), pd.Timedelta), pd.Timedelta)
    check(assert_type(dt.timedelta(hours=2) + left, pd.Timedelta), pd.Timedelta)


def test_nano_numpy_scalars(left: Nano) -> None:
    """Nano scalar addition returns Timestamp, NaT, or Timedelta."""
    check(assert_type(left + np.datetime64("2026-01-01"), pd.Timestamp), pd.Timestamp)
    check(assert_type(np.datetime64("2026-01-01") + left, pd.Timestamp), pd.Timestamp)
    check(assert_type(left + np.timedelta64(2, "h"), pd.Timedelta), pd.Timedelta)
    check(assert_type(np.timedelta64(2, "h") + left, pd.Timedelta), pd.Timedelta)


def test_nano_pandas_scalars(left: Nano) -> None:
    """Nano scalar addition returns Timestamp, NaT, or Timedelta."""
    check(assert_type(left + pd.Timestamp("2026-01-01"), pd.Timestamp), pd.Timestamp)
    check(assert_type(pd.Timestamp("2026-01-01") + left, pd.Timestamp), pd.Timestamp)
    check(assert_type(left + pd.NaT, NaTType), NaTType)
    check(assert_type(pd.NaT + left, NaTType), NaTType)
    check(assert_type(left + pd.Timedelta("2h"), pd.Timedelta), pd.Timedelta)
    check(assert_type(pd.Timedelta("2h") + left, pd.Timedelta), pd.Timedelta)


def test_homogeneous_nano() -> None:
    """Homogeneous concrete ticks preserve their class."""
    check(assert_type(Nano(1) + Nano(2), Nano), Nano)
    check(assert_type(Nano(2) + Nano(1), Nano), Nano)


class SpecialNano(Nano):
    """Nano subclass for normalization and cancellation."""


def test_nano_subclass() -> None:
    """Nano subclasses use Tick results even with homogeneous operands."""
    check(assert_type(SpecialNano(500) + Nano(500), Tick), Micro)
    check(assert_type(Nano(500) + SpecialNano(500), Tick), Micro)
    check(assert_type(SpecialNano(500) + Nano(-500), Tick), Hour)
    check(assert_type(Nano(-500) + SpecialNano(500), Tick), Hour)


def test_finer_mixed_ticks(left: Nano) -> None:
    """Finer mixed ticks retain the broad Tick result."""
    check(assert_type(Micro() + left, Tick), Nano)
    check(assert_type(left + Micro(), Tick), Nano)
