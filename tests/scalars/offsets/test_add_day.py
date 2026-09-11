from typing import assert_type

import pandas as pd
import pytest

from tests import (
    TYPE_CHECKING_INVALID_USAGE,
    check,
)

from pandas.tseries.offsets import (
    BusinessDay,
    CustomBusinessDay,
    Day,
    Hour,
)


def test_add_day() -> None:
    check(assert_type(Day(1) + Day(2), Day), Day)
    check(assert_type(Day(1).__radd__(Day(2)), Day), Day)
    check(assert_type(Day() + Hour(), pd.Timedelta), pd.Timedelta)
    check(assert_type(Hour() + Day(), pd.Timedelta), pd.Timedelta)
    check(assert_type(Day().__radd__(Hour()), pd.Timedelta), pd.Timedelta)
    assert Day() + Hour() == pd.Timedelta(days=1, hours=1)


def test_day_hierarchy() -> None:
    day = Day()
    timestamp = pd.Timestamp("2026-01-01")
    check(assert_type(timestamp + day, pd.Timestamp), pd.Timestamp)
    check(assert_type(day + timestamp, pd.Timestamp), pd.Timestamp)
    check(assert_type(timestamp - day, pd.Timestamp), pd.Timestamp)
    check(assert_type(day.__rsub__(timestamp), pd.Timestamp), pd.Timestamp)
    if TYPE_CHECKING_INVALID_USAGE:
        pd.Timedelta(day)  # type: ignore[arg-type] # pyright: ignore[reportArgumentType] # pyrefly: ignore[bad-argument-type] # ty: ignore[invalid-argument-type]


def test_day_direct_dispatch() -> None:
    check(assert_type(Day().__add__(Day()), Day), Day)
    check(assert_type(Day().__add__(Hour()), pd.Timedelta), pd.Timedelta)
    check(assert_type(Day().__add__(BusinessDay()), BusinessDay), BusinessDay)
    check(assert_type(Day().__radd__(BusinessDay()), BusinessDay), BusinessDay)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = Hour().__add__(Day())  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = Hour().__radd__(Day())  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _2 = BusinessDay().__add__(Day())  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _3 = BusinessDay().__radd__(Day())  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]


@pytest.mark.parametrize("left", [Hour(), BusinessDay(), CustomBusinessDay()])
@pytest.mark.parametrize("method", ["__add__", "__radd__"])
def test_day_runtime_dispatch(left: object, method: str) -> None:
    """Probe runtime dispatch without advertising unsupported direct calls."""
    assert getattr(left, method)(Day()) is NotImplemented
