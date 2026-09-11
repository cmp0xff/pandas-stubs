import datetime as dt
from typing import (
    assert_type,
    cast,
)

import numpy as np
import pandas as pd
from pandas.api.typing import NaTType

from tests import (
    TYPE_CHECKING_INVALID_USAGE,
    check,
)

from pandas.tseries.offsets import (
    Hour,
    Micro,
    Milli,
    Minute,
    Nano,
    Second,
    Tick,
)


def test_hour_python_scalars() -> None:
    """Hour scalar addition returns Timestamp, NaT, or Timedelta."""
    check(assert_type(Hour() + dt.date(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.date(2026, 1, 1) + Hour(), pd.Timestamp), pd.Timestamp)
    check(assert_type(Hour() + dt.datetime(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.datetime(2026, 1, 1) + Hour(), pd.Timestamp), pd.Timestamp)
    check(assert_type(Hour() + dt.timedelta(hours=2), pd.Timedelta), pd.Timedelta)
    check(assert_type(dt.timedelta(hours=2) + Hour(), pd.Timedelta), pd.Timedelta)


def test_minute_python_scalars() -> None:
    """Minute scalar addition returns Timestamp, NaT, or Timedelta."""
    check(assert_type(Minute() + dt.date(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.date(2026, 1, 1) + Minute(), pd.Timestamp), pd.Timestamp)
    check(assert_type(Minute() + dt.datetime(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.datetime(2026, 1, 1) + Minute(), pd.Timestamp), pd.Timestamp)
    check(assert_type(Minute() + dt.timedelta(hours=2), pd.Timedelta), pd.Timedelta)
    check(assert_type(dt.timedelta(hours=2) + Minute(), pd.Timedelta), pd.Timedelta)


def test_second_python_scalars() -> None:
    """Second scalar addition returns Timestamp, NaT, or Timedelta."""
    check(assert_type(Second() + dt.date(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.date(2026, 1, 1) + Second(), pd.Timestamp), pd.Timestamp)
    check(assert_type(Second() + dt.datetime(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.datetime(2026, 1, 1) + Second(), pd.Timestamp), pd.Timestamp)
    check(assert_type(Second() + dt.timedelta(hours=2), pd.Timedelta), pd.Timedelta)
    check(assert_type(dt.timedelta(hours=2) + Second(), pd.Timedelta), pd.Timedelta)


def test_milli_python_scalars() -> None:
    """Milli scalar addition returns Timestamp, NaT, or Timedelta."""
    check(assert_type(Milli() + dt.date(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.date(2026, 1, 1) + Milli(), pd.Timestamp), pd.Timestamp)
    check(assert_type(Milli() + dt.datetime(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.datetime(2026, 1, 1) + Milli(), pd.Timestamp), pd.Timestamp)
    check(assert_type(Milli() + dt.timedelta(hours=2), pd.Timedelta), pd.Timedelta)
    check(assert_type(dt.timedelta(hours=2) + Milli(), pd.Timedelta), pd.Timedelta)


def test_micro_python_scalars() -> None:
    """Micro scalar addition returns Timestamp, NaT, or Timedelta."""
    check(assert_type(Micro() + dt.date(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.date(2026, 1, 1) + Micro(), pd.Timestamp), pd.Timestamp)
    check(assert_type(Micro() + dt.datetime(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.datetime(2026, 1, 1) + Micro(), pd.Timestamp), pd.Timestamp)
    check(assert_type(Micro() + dt.timedelta(hours=2), pd.Timedelta), pd.Timedelta)
    check(assert_type(dt.timedelta(hours=2) + Micro(), pd.Timedelta), pd.Timedelta)


def test_nano_python_scalars() -> None:
    """Nano scalar addition returns Timestamp, NaT, or Timedelta."""
    check(assert_type(Nano() + dt.date(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.date(2026, 1, 1) + Nano(), pd.Timestamp), pd.Timestamp)
    check(assert_type(Nano() + dt.datetime(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.datetime(2026, 1, 1) + Nano(), pd.Timestamp), pd.Timestamp)
    check(assert_type(Nano() + dt.timedelta(hours=2), pd.Timedelta), pd.Timedelta)
    check(assert_type(dt.timedelta(hours=2) + Nano(), pd.Timedelta), pd.Timedelta)


def test_tick_python_scalars() -> None:
    """Tick scalar addition returns Timestamp, NaT, or Timedelta."""
    offset = cast(Tick, Hour())
    check(assert_type(offset + dt.date(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.date(2026, 1, 1) + offset, pd.Timestamp), pd.Timestamp)
    check(assert_type(offset + dt.datetime(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.datetime(2026, 1, 1) + offset, pd.Timestamp), pd.Timestamp)
    check(assert_type(offset + dt.timedelta(hours=2), pd.Timedelta), pd.Timedelta)
    check(assert_type(dt.timedelta(hours=2) + offset, pd.Timedelta), pd.Timedelta)


def test_hour_numpy_scalars() -> None:
    """Hour scalar addition returns Timestamp, NaT, or Timedelta."""
    check(assert_type(Hour() + np.datetime64("2026-01-01"), pd.Timestamp), pd.Timestamp)
    check(assert_type(np.datetime64("2026-01-01") + Hour(), pd.Timestamp), pd.Timestamp)
    check(assert_type(Hour() + np.timedelta64(2, "h"), pd.Timedelta), pd.Timedelta)
    check(assert_type(np.timedelta64(2, "h") + Hour(), pd.Timedelta), pd.Timedelta)


def test_minute_numpy_scalars() -> None:
    """Minute scalar addition returns Timestamp, NaT, or Timedelta."""
    check(
        assert_type(Minute() + np.datetime64("2026-01-01"), pd.Timestamp), pd.Timestamp
    )
    check(
        assert_type(np.datetime64("2026-01-01") + Minute(), pd.Timestamp), pd.Timestamp
    )
    check(assert_type(Minute() + np.timedelta64(2, "h"), pd.Timedelta), pd.Timedelta)
    check(assert_type(np.timedelta64(2, "h") + Minute(), pd.Timedelta), pd.Timedelta)


def test_second_numpy_scalars() -> None:
    """Second scalar addition returns Timestamp, NaT, or Timedelta."""
    check(
        assert_type(Second() + np.datetime64("2026-01-01"), pd.Timestamp), pd.Timestamp
    )
    check(
        assert_type(np.datetime64("2026-01-01") + Second(), pd.Timestamp), pd.Timestamp
    )
    check(assert_type(Second() + np.timedelta64(2, "h"), pd.Timedelta), pd.Timedelta)
    check(assert_type(np.timedelta64(2, "h") + Second(), pd.Timedelta), pd.Timedelta)


def test_milli_numpy_scalars() -> None:
    """Milli scalar addition returns Timestamp, NaT, or Timedelta."""
    check(
        assert_type(Milli() + np.datetime64("2026-01-01"), pd.Timestamp), pd.Timestamp
    )
    check(
        assert_type(np.datetime64("2026-01-01") + Milli(), pd.Timestamp), pd.Timestamp
    )
    check(assert_type(Milli() + np.timedelta64(2, "h"), pd.Timedelta), pd.Timedelta)
    check(assert_type(np.timedelta64(2, "h") + Milli(), pd.Timedelta), pd.Timedelta)


def test_micro_numpy_scalars() -> None:
    """Micro scalar addition returns Timestamp, NaT, or Timedelta."""
    check(
        assert_type(Micro() + np.datetime64("2026-01-01"), pd.Timestamp), pd.Timestamp
    )
    check(
        assert_type(np.datetime64("2026-01-01") + Micro(), pd.Timestamp), pd.Timestamp
    )
    check(assert_type(Micro() + np.timedelta64(2, "h"), pd.Timedelta), pd.Timedelta)
    check(assert_type(np.timedelta64(2, "h") + Micro(), pd.Timedelta), pd.Timedelta)


def test_nano_numpy_scalars() -> None:
    """Nano scalar addition returns Timestamp, NaT, or Timedelta."""
    check(assert_type(Nano() + np.datetime64("2026-01-01"), pd.Timestamp), pd.Timestamp)
    check(assert_type(np.datetime64("2026-01-01") + Nano(), pd.Timestamp), pd.Timestamp)
    check(assert_type(Nano() + np.timedelta64(2, "h"), pd.Timedelta), pd.Timedelta)
    check(assert_type(np.timedelta64(2, "h") + Nano(), pd.Timedelta), pd.Timedelta)


def test_tick_numpy_scalars() -> None:
    """Tick scalar addition returns Timestamp, NaT, or Timedelta."""
    offset = cast(Tick, Hour())
    check(assert_type(offset + np.datetime64("2026-01-01"), pd.Timestamp), pd.Timestamp)
    check(assert_type(np.datetime64("2026-01-01") + offset, pd.Timestamp), pd.Timestamp)
    check(assert_type(offset + np.timedelta64(2, "h"), pd.Timedelta), pd.Timedelta)
    check(assert_type(np.timedelta64(2, "h") + offset, pd.Timedelta), pd.Timedelta)


def test_hour_pandas_scalars() -> None:
    """Hour scalar addition returns Timestamp, NaT, or Timedelta."""
    check(assert_type(Hour() + pd.Timestamp("2026-01-01"), pd.Timestamp), pd.Timestamp)
    check(assert_type(pd.Timestamp("2026-01-01") + Hour(), pd.Timestamp), pd.Timestamp)
    check(assert_type(Hour() + pd.NaT, NaTType), NaTType)
    check(assert_type(pd.NaT + Hour(), NaTType), NaTType)
    check(assert_type(Hour() + pd.Timedelta("2h"), pd.Timedelta), pd.Timedelta)
    check(assert_type(pd.Timedelta("2h") + Hour(), pd.Timedelta), pd.Timedelta)


def test_minute_pandas_scalars() -> None:
    """Minute scalar addition returns Timestamp, NaT, or Timedelta."""
    check(
        assert_type(Minute() + pd.Timestamp("2026-01-01"), pd.Timestamp), pd.Timestamp
    )
    check(
        assert_type(pd.Timestamp("2026-01-01") + Minute(), pd.Timestamp), pd.Timestamp
    )
    check(assert_type(Minute() + pd.NaT, NaTType), NaTType)
    check(assert_type(pd.NaT + Minute(), NaTType), NaTType)
    check(assert_type(Minute() + pd.Timedelta("2h"), pd.Timedelta), pd.Timedelta)
    check(assert_type(pd.Timedelta("2h") + Minute(), pd.Timedelta), pd.Timedelta)


def test_second_pandas_scalars() -> None:
    """Second scalar addition returns Timestamp, NaT, or Timedelta."""
    check(
        assert_type(Second() + pd.Timestamp("2026-01-01"), pd.Timestamp), pd.Timestamp
    )
    check(
        assert_type(pd.Timestamp("2026-01-01") + Second(), pd.Timestamp), pd.Timestamp
    )
    check(assert_type(Second() + pd.NaT, NaTType), NaTType)
    check(assert_type(pd.NaT + Second(), NaTType), NaTType)
    check(assert_type(Second() + pd.Timedelta("2h"), pd.Timedelta), pd.Timedelta)
    check(assert_type(pd.Timedelta("2h") + Second(), pd.Timedelta), pd.Timedelta)


def test_milli_pandas_scalars() -> None:
    """Milli scalar addition returns Timestamp, NaT, or Timedelta."""
    check(assert_type(Milli() + pd.Timestamp("2026-01-01"), pd.Timestamp), pd.Timestamp)
    check(assert_type(pd.Timestamp("2026-01-01") + Milli(), pd.Timestamp), pd.Timestamp)
    check(assert_type(Milli() + pd.NaT, NaTType), NaTType)
    check(assert_type(pd.NaT + Milli(), NaTType), NaTType)
    check(assert_type(Milli() + pd.Timedelta("2h"), pd.Timedelta), pd.Timedelta)
    check(assert_type(pd.Timedelta("2h") + Milli(), pd.Timedelta), pd.Timedelta)


def test_micro_pandas_scalars() -> None:
    """Micro scalar addition returns Timestamp, NaT, or Timedelta."""
    check(assert_type(Micro() + pd.Timestamp("2026-01-01"), pd.Timestamp), pd.Timestamp)
    check(assert_type(pd.Timestamp("2026-01-01") + Micro(), pd.Timestamp), pd.Timestamp)
    check(assert_type(Micro() + pd.NaT, NaTType), NaTType)
    check(assert_type(pd.NaT + Micro(), NaTType), NaTType)
    check(assert_type(Micro() + pd.Timedelta("2h"), pd.Timedelta), pd.Timedelta)
    check(assert_type(pd.Timedelta("2h") + Micro(), pd.Timedelta), pd.Timedelta)


def test_nano_pandas_scalars() -> None:
    """Nano scalar addition returns Timestamp, NaT, or Timedelta."""
    check(assert_type(Nano() + pd.Timestamp("2026-01-01"), pd.Timestamp), pd.Timestamp)
    check(assert_type(pd.Timestamp("2026-01-01") + Nano(), pd.Timestamp), pd.Timestamp)
    check(assert_type(Nano() + pd.NaT, NaTType), NaTType)
    check(assert_type(pd.NaT + Nano(), NaTType), NaTType)
    check(assert_type(Nano() + pd.Timedelta("2h"), pd.Timedelta), pd.Timedelta)
    check(assert_type(pd.Timedelta("2h") + Nano(), pd.Timedelta), pd.Timedelta)


def test_tick_pandas_scalars() -> None:
    """Tick scalar addition returns Timestamp, NaT, or Timedelta."""
    offset = cast(Tick, Hour())
    check(assert_type(offset + pd.Timestamp("2026-01-01"), pd.Timestamp), pd.Timestamp)
    check(assert_type(pd.Timestamp("2026-01-01") + offset, pd.Timestamp), pd.Timestamp)
    check(assert_type(offset + pd.NaT, NaTType), NaTType)
    check(assert_type(pd.NaT + offset, NaTType), NaTType)
    check(assert_type(offset + pd.Timedelta("2h"), pd.Timedelta), pd.Timedelta)
    check(assert_type(pd.Timedelta("2h") + offset, pd.Timedelta), pd.Timedelta)


def test_homogeneous_hour() -> None:
    """Homogeneous concrete ticks preserve their class."""
    check(assert_type(Hour(1) + Hour(2), Hour), Hour)
    check(assert_type(Hour(2) + Hour(1), Hour), Hour)


def test_homogeneous_minute() -> None:
    """Homogeneous concrete ticks preserve their class."""
    check(assert_type(Minute(1) + Minute(2), Minute), Minute)
    check(assert_type(Minute(2) + Minute(1), Minute), Minute)


def test_homogeneous_second() -> None:
    """Homogeneous concrete ticks preserve their class."""
    check(assert_type(Second(1) + Second(2), Second), Second)
    check(assert_type(Second(2) + Second(1), Second), Second)


def test_homogeneous_milli() -> None:
    """Homogeneous concrete ticks preserve their class."""
    check(assert_type(Milli(1) + Milli(2), Milli), Milli)
    check(assert_type(Milli(2) + Milli(1), Milli), Milli)


def test_homogeneous_micro() -> None:
    """Homogeneous concrete ticks preserve their class."""
    check(assert_type(Micro(1) + Micro(2), Micro), Micro)
    check(assert_type(Micro(2) + Micro(1), Micro), Micro)


def test_homogeneous_nano() -> None:
    """Homogeneous concrete ticks preserve their class."""
    check(assert_type(Nano(1) + Nano(2), Nano), Nano)
    check(assert_type(Nano(2) + Nano(1), Nano), Nano)


def test_mixed_ticks() -> None:
    """Mixed ticks normalize by value, including cancellation."""
    check(assert_type(Hour(1) + Minute(30), Tick), Minute)
    check(assert_type(Minute(30) + Hour(1), Tick), Minute)
    check(assert_type(Hour(1) + Minute(-60), Tick), Hour)
    check(assert_type(Minute(-60) + Hour(1), Tick), Hour)
    check(assert_type(Minute(60) + Second(3600), Tick), Hour)
    check(assert_type(Second(3600) + Minute(60), Tick), Hour)
    assert Hour(1) + Minute(-60) == Hour(0)


def test_broad_ticks() -> None:
    """Broad Tick operands retain the Tick result."""
    left = cast(Tick, Hour())
    right = cast(Tick, Minute())
    check(assert_type(left + right, Tick), Tick)
    check(assert_type(right + left, Tick), Tick)


class SpecialHour(Hour):
    """Hour subclass for homogeneous arithmetic."""


class SpecialMinute(Minute):
    """Minute subclass that can normalize to Hour."""


def test_tick_subclasses() -> None:
    """Hour subclasses stay hourly; minute subclasses can normalize."""
    check(assert_type(SpecialHour() + Hour(), Hour), Hour)
    check(assert_type(Hour() + SpecialHour(), Hour), Hour)
    check(assert_type(SpecialMinute(30) + Minute(30), Tick), Hour)
    check(assert_type(Minute(30) + SpecialMinute(30), Tick), Hour)
    check(assert_type(SpecialMinute(30) + Minute(-30), Tick), Hour)
    check(assert_type(Minute(-30) + SpecialMinute(30), Tick), Hour)


class SpecialSecond(Second):
    """Second subclass for normalization and cancellation."""


def test_second_subclass() -> None:
    """Second subclasses use Tick results even with homogeneous operands."""
    check(assert_type(SpecialSecond(30) + Second(30), Tick), Minute)
    check(assert_type(Second(30) + SpecialSecond(30), Tick), Minute)
    check(assert_type(SpecialSecond(30) + Second(-30), Tick), Hour)
    check(assert_type(Second(-30) + SpecialSecond(30), Tick), Hour)


class SpecialMilli(Milli):
    """Milli subclass for normalization and cancellation."""


def test_milli_subclass() -> None:
    """Milli subclasses use Tick results even with homogeneous operands."""
    check(assert_type(SpecialMilli(500) + Milli(500), Tick), Second)
    check(assert_type(Milli(500) + SpecialMilli(500), Tick), Second)
    check(assert_type(SpecialMilli(500) + Milli(-500), Tick), Hour)
    check(assert_type(Milli(-500) + SpecialMilli(500), Tick), Hour)


class SpecialMicro(Micro):
    """Micro subclass for normalization and cancellation."""


def test_micro_subclass() -> None:
    """Micro subclasses use Tick results even with homogeneous operands."""
    check(assert_type(SpecialMicro(500) + Micro(500), Tick), Milli)
    check(assert_type(Micro(500) + SpecialMicro(500), Tick), Milli)
    check(assert_type(SpecialMicro(500) + Micro(-500), Tick), Hour)
    check(assert_type(Micro(-500) + SpecialMicro(500), Tick), Hour)


class SpecialNano(Nano):
    """Nano subclass for normalization and cancellation."""


def test_nano_subclass() -> None:
    """Nano subclasses use Tick results even with homogeneous operands."""
    check(assert_type(SpecialNano(500) + Nano(500), Tick), Micro)
    check(assert_type(Nano(500) + SpecialNano(500), Tick), Micro)
    check(assert_type(SpecialNano(500) + Nano(-500), Tick), Hour)
    check(assert_type(Nano(-500) + SpecialNano(500), Tick), Hour)


def test_finer_mixed_ticks() -> None:
    """Finer mixed ticks retain the broad Tick result."""
    check(assert_type(Second() + Milli(), Tick), Milli)
    check(assert_type(Milli() + Second(), Tick), Milli)
    check(assert_type(Milli() + Micro(), Tick), Micro)
    check(assert_type(Micro() + Milli(), Tick), Micro)
    check(assert_type(Micro() + Nano(), Tick), Nano)
    check(assert_type(Nano() + Micro(), Tick), Nano)


def test_tick_numpy_arrays() -> None:
    """Object-array results do not promise shape or dtype preservation."""
    values = np.array([dt.datetime(2026, 1, 1)], dtype=object)
    # NumPy accepts broad object operations; it cannot enforce direct-call rejection.
    check(Hour() + values, np.ndarray)


def test_tick_index() -> None:
    """Containers support expressions through their own dispatch."""
    values = pd.date_range("2026-01-01", periods=2)
    check(assert_type(Hour() + values, pd.DatetimeIndex), pd.DatetimeIndex)
    check(assert_type(values + Hour(), pd.DatetimeIndex), pd.DatetimeIndex)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = Hour().__add__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = Hour().__radd__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]


def test_tick_series() -> None:
    """Containers support expressions through their own dispatch."""
    values = pd.Series(pd.date_range("2026-01-01", periods=2))
    check(assert_type(Hour() + values, "pd.Series[pd.Timestamp]"), pd.Series)
    check(assert_type(values + Hour(), "pd.Series[pd.Timestamp]"), pd.Series)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = Hour().__add__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = Hour().__radd__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
