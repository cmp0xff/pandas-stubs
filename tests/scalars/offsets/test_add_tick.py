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


def test_tick_python_scalars() -> None:
    """Python dates become Timestamp; durations follow the offset family."""
    check(assert_type(Hour() + dt.date(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.date(2026, 1, 1) + Hour(), pd.Timestamp), pd.Timestamp)
    check(assert_type(Hour().__add__(dt.date(2026, 1, 1)), pd.Timestamp), pd.Timestamp)
    check(assert_type(Hour().__radd__(dt.date(2026, 1, 1)), pd.Timestamp), pd.Timestamp)
    check(assert_type(Hour() + dt.datetime(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.datetime(2026, 1, 1) + Hour(), pd.Timestamp), pd.Timestamp)
    check(
        assert_type(Hour().__add__(dt.datetime(2026, 1, 1)), pd.Timestamp), pd.Timestamp
    )
    check(
        assert_type(Hour().__radd__(dt.datetime(2026, 1, 1)), pd.Timestamp),
        pd.Timestamp,
    )
    check(assert_type(Hour() + dt.timedelta(hours=2), pd.Timedelta), pd.Timedelta)
    check(assert_type(dt.timedelta(hours=2) + Hour(), pd.Timedelta), pd.Timedelta)
    check(
        assert_type(Hour().__add__(dt.timedelta(hours=2)), pd.Timedelta), pd.Timedelta
    )
    check(
        assert_type(Hour().__radd__(dt.timedelta(hours=2)), pd.Timedelta), pd.Timedelta
    )


def test_tick_numpy_scalars() -> None:
    """NumPy temporal scalars use the supported scalar results."""
    check(assert_type(Hour() + np.datetime64("2026-01-01"), pd.Timestamp), pd.Timestamp)
    check(assert_type(np.datetime64("2026-01-01") + Hour(), pd.Timestamp), pd.Timestamp)
    check(
        assert_type(Hour().__add__(np.datetime64("2026-01-01")), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(Hour().__radd__(np.datetime64("2026-01-01")), pd.Timestamp),
        pd.Timestamp,
    )
    check(assert_type(Hour() + np.timedelta64(2, "h"), pd.Timedelta), pd.Timedelta)
    check(assert_type(np.timedelta64(2, "h") + Hour(), pd.Timedelta), pd.Timedelta)
    check(
        assert_type(Hour().__add__(np.timedelta64(2, "h")), pd.Timedelta), pd.Timedelta
    )
    check(
        assert_type(Hour().__radd__(np.timedelta64(2, "h")), pd.Timedelta), pd.Timedelta
    )


def test_tick_pandas_scalars() -> None:
    """Timestamp and NaT retain pandas scalar results."""
    check(assert_type(Hour() + pd.Timestamp("2026-01-01"), pd.Timestamp), pd.Timestamp)
    check(assert_type(pd.Timestamp("2026-01-01") + Hour(), pd.Timestamp), pd.Timestamp)
    check(
        assert_type(Hour().__add__(pd.Timestamp("2026-01-01")), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(Hour().__radd__(pd.Timestamp("2026-01-01")), pd.Timestamp),
        pd.Timestamp,
    )
    check(assert_type(Hour() + pd.NaT, NaTType), NaTType)
    check(assert_type(pd.NaT + Hour(), NaTType), NaTType)
    check(assert_type(Hour().__add__(pd.NaT), NaTType), NaTType)
    check(assert_type(Hour().__radd__(pd.NaT), NaTType), NaTType)
    check(assert_type(Hour() + pd.Timedelta("2h"), pd.Timedelta), pd.Timedelta)
    check(assert_type(pd.Timedelta("2h") + Hour(), pd.Timedelta), pd.Timedelta)
    check(assert_type(Hour().__add__(pd.Timedelta("2h")), pd.Timedelta), pd.Timedelta)
    check(assert_type(Hour().__radd__(pd.Timedelta("2h")), pd.Timedelta), pd.Timedelta)


def test_homogeneous_hour() -> None:
    """Homogeneous concrete ticks preserve their class."""
    check(assert_type(Hour(1) + Hour(2), Hour), Hour)
    check(assert_type(Hour(2) + Hour(1), Hour), Hour)
    check(assert_type(Hour(1).__add__(Hour(2)), Hour), Hour)
    check(assert_type(Hour(1).__radd__(Hour(2)), Hour), Hour)


def test_homogeneous_minute() -> None:
    """Homogeneous concrete ticks preserve their class."""
    check(assert_type(Minute(1) + Minute(2), Minute), Minute)
    check(assert_type(Minute(2) + Minute(1), Minute), Minute)
    check(assert_type(Minute(1).__add__(Minute(2)), Minute), Minute)
    check(assert_type(Minute(1).__radd__(Minute(2)), Minute), Minute)


def test_homogeneous_second() -> None:
    """Homogeneous concrete ticks preserve their class."""
    check(assert_type(Second(1) + Second(2), Second), Second)
    check(assert_type(Second(2) + Second(1), Second), Second)
    check(assert_type(Second(1).__add__(Second(2)), Second), Second)
    check(assert_type(Second(1).__radd__(Second(2)), Second), Second)


def test_homogeneous_milli() -> None:
    """Homogeneous concrete ticks preserve their class."""
    check(assert_type(Milli(1) + Milli(2), Milli), Milli)
    check(assert_type(Milli(2) + Milli(1), Milli), Milli)
    check(assert_type(Milli(1).__add__(Milli(2)), Milli), Milli)
    check(assert_type(Milli(1).__radd__(Milli(2)), Milli), Milli)


def test_homogeneous_micro() -> None:
    """Homogeneous concrete ticks preserve their class."""
    check(assert_type(Micro(1) + Micro(2), Micro), Micro)
    check(assert_type(Micro(2) + Micro(1), Micro), Micro)
    check(assert_type(Micro(1).__add__(Micro(2)), Micro), Micro)
    check(assert_type(Micro(1).__radd__(Micro(2)), Micro), Micro)


def test_homogeneous_nano() -> None:
    """Homogeneous concrete ticks preserve their class."""
    check(assert_type(Nano(1) + Nano(2), Nano), Nano)
    check(assert_type(Nano(2) + Nano(1), Nano), Nano)
    check(assert_type(Nano(1).__add__(Nano(2)), Nano), Nano)
    check(assert_type(Nano(1).__radd__(Nano(2)), Nano), Nano)


def test_mixed_ticks() -> None:
    """Mixed ticks normalize by value, including cancellation."""
    check(assert_type(Hour(1) + Minute(30), Tick), Minute)
    check(assert_type(Minute(30) + Hour(1), Tick), Minute)
    check(assert_type(Hour(1).__add__(Minute(30)), Tick), Minute)
    check(assert_type(Hour(1).__radd__(Minute(30)), Tick), Minute)
    check(assert_type(Hour(1) + Minute(-60), Tick), Hour)
    check(assert_type(Minute(-60) + Hour(1), Tick), Hour)
    check(assert_type(Hour(1).__add__(Minute(-60)), Tick), Hour)
    check(assert_type(Hour(1).__radd__(Minute(-60)), Tick), Hour)
    check(assert_type(Minute(60) + Second(3600), Tick), Hour)
    check(assert_type(Second(3600) + Minute(60), Tick), Hour)
    check(assert_type(Minute(60).__add__(Second(3600)), Tick), Hour)
    check(assert_type(Minute(60).__radd__(Second(3600)), Tick), Hour)
    assert Hour(1) + Minute(-60) == Hour(0)


def test_broad_ticks() -> None:
    """Broad Tick operands retain the Tick result."""
    left = cast(Tick, Hour())
    right = cast(Tick, Minute())
    check(assert_type(left + right, Tick), Tick)
    check(assert_type(right + left, Tick), Tick)
    check(assert_type(left.__add__(right), Tick), Tick)
    check(assert_type(left.__radd__(right), Tick), Tick)


class SpecialHour(Hour):
    """Hour subclass for homogeneous arithmetic."""


class SpecialMinute(Minute):
    """Minute subclass that can normalize to Hour."""


def test_tick_subclasses() -> None:
    """Hour subclasses stay hourly; minute subclasses can normalize."""
    check(assert_type(SpecialHour() + Hour(), Hour), Hour)
    check(assert_type(Hour() + SpecialHour(), Hour), Hour)
    check(assert_type(SpecialHour().__add__(Hour()), Hour), Hour)
    check(assert_type(SpecialHour().__radd__(Hour()), Hour), Hour)
    check(assert_type(SpecialMinute(30) + Minute(30), Tick), Hour)
    check(assert_type(Minute(30) + SpecialMinute(30), Tick), Hour)
    check(assert_type(SpecialMinute(30).__add__(Minute(30)), Tick), Hour)
    check(assert_type(SpecialMinute(30).__radd__(Minute(30)), Tick), Hour)
    check(assert_type(SpecialMinute(30) + Minute(-30), Tick), Hour)
    check(assert_type(Minute(-30) + SpecialMinute(30), Tick), Hour)
    check(assert_type(SpecialMinute(30).__add__(Minute(-30)), Tick), Hour)
    check(assert_type(SpecialMinute(30).__radd__(Minute(-30)), Tick), Hour)


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
