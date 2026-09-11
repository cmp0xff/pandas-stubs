from typing import assert_type

import pandas as pd
import pytest

from tests import (
    TYPE_CHECKING_INVALID_USAGE,
    check,
)

from pandas.tseries.offsets import (
    BaseOffset,
    BusinessDay,
    CustomBusinessDay,
    Day,
    Hour,
    Micro,
    Milli,
    Minute,
    Nano,
    Second,
    Tick,
)


def test_add_same_tick_class() -> None:
    """Adding ticks of the same concrete class preserves that class."""
    check(assert_type(Hour(1) + Hour(2), Hour), Hour)
    check(assert_type(Minute(1) + Minute(2), Minute), Minute)
    check(assert_type(Second(1) + Second(2), Second), Second)
    check(assert_type(Milli(1) + Milli(2), Milli), Milli)
    check(assert_type(Micro(1) + Micro(2), Micro), Micro)
    check(assert_type(Nano(1) + Nano(2), Nano), Nano)

    check(assert_type(Hour(1).__radd__(Hour(2)), Hour), Hour)
    check(assert_type(Minute(1).__radd__(Minute(2)), Minute), Minute)
    check(assert_type(Second(1).__radd__(Second(2)), Second), Second)
    check(assert_type(Milli(1).__radd__(Milli(2)), Milli), Milli)
    check(assert_type(Micro(1).__radd__(Micro(2)), Micro), Micro)
    check(assert_type(Nano(1).__radd__(Nano(2)), Nano), Nano)


def test_add_mixed_ticks() -> None:
    """Mixed tick results depend on values, including cancellation."""
    check(assert_type(Hour(1) + Minute(30), Tick), Minute)
    check(assert_type(Minute(30) + Hour(1), Tick), Minute)
    check(assert_type(Hour(1).__radd__(Minute(30)), Tick), Minute)
    check(assert_type(Minute(30).__radd__(Hour(1)), Tick), Minute)

    check(assert_type(Hour(1) + Minute(60), Tick), Hour)
    check(assert_type(Minute(60) + Hour(1), Tick), Hour)
    result = check(assert_type(Hour(1) + Minute(-60), Tick), Hour)
    assert result.n == 0
    check(assert_type(Minute(-60) + Hour(1), Tick), Hour)

    # Normalization can produce a class different from either operand's class.
    result = check(assert_type(Minute(60) + Second(3600), Tick), Hour)
    assert result == Hour(2)
    check(assert_type(Second(3600) + Minute(60), Tick), Hour)
    check(assert_type(Milli(1000) + Micro(1_000_000), Tick), Second)


@pytest.mark.parametrize("left, right", [(Hour(), Hour()), (Hour(), Minute())])
def test_add_broad_ticks(left: Tick, right: Tick) -> None:
    check(assert_type(left + right, Tick), Tick)
    check(assert_type(right + left, Tick), Tick)
    check(assert_type(left.__radd__(right), Tick), Tick)
    check(assert_type(right.__radd__(left), Tick), Tick)


class SpecialHour(Hour): ...


class SpecialMinute(Minute): ...


def test_add_tick_subclass() -> None:
    """Known subclasses do not receive the exact homogeneous-tick guarantee."""
    special = SpecialHour()
    check(assert_type(special + Hour(), Tick), Tick)
    check(assert_type(Hour() + special, Tick), Tick)
    check(assert_type(special + SpecialHour(), Tick), Tick)
    check(assert_type(special.__radd__(Hour()), Tick), Tick)
    check(assert_type(Hour().__radd__(special), Tick), Tick)
    check(assert_type(special.__radd__(SpecialHour()), Tick), Tick)


def test_add_tick_subclass_normalization() -> None:
    special = SpecialMinute(30)
    check(assert_type(special + Minute(30), Tick), Hour)
    check(assert_type(Minute(30) + special, Tick), Hour)
    check(assert_type(special.__radd__(Minute(30)), Tick), Hour)
    check(assert_type(Minute(30).__radd__(special), Tick), Hour)
    check(assert_type(special + SpecialMinute(30), Tick), SpecialMinute)


def test_add_day() -> None:
    check(assert_type(Day(1) + Day(2), Day), Day)
    check(assert_type(Day(1).__radd__(Day(2)), Day), Day)
    check(assert_type(Day() + Hour(), pd.Timedelta), pd.Timedelta)
    check(assert_type(Hour() + Day(), pd.Timedelta), pd.Timedelta)
    check(assert_type(Day().__radd__(Hour()), pd.Timedelta), pd.Timedelta)
    assert Day() + Hour() == pd.Timedelta(days=1, hours=1)


@pytest.mark.parametrize("business", [BusinessDay(), CustomBusinessDay()])
@pytest.mark.parametrize("duration", [Day(), Hour()])
def test_add_business_day(business: BusinessDay, duration: Day | Tick) -> None:
    left = check(assert_type(business + duration, BusinessDay), BusinessDay)
    right = check(assert_type(duration + business, BusinessDay), BusinessDay)
    assert type(left) is BusinessDay
    assert type(right) is BusinessDay


@pytest.mark.parametrize("business", [BusinessDay(), CustomBusinessDay()])
def test_radd_business_day(business: BusinessDay) -> None:
    reflected_left = check(
        assert_type(business.__radd__(Hour()), BusinessDay), BusinessDay
    )
    reflected_right = check(
        assert_type(Day().__radd__(business), BusinessDay), BusinessDay
    )
    assert type(reflected_left) is BusinessDay
    assert type(reflected_right) is BusinessDay


def test_add_custom_business_day() -> None:
    """CustomBusinessDay arithmetic returns a plain BusinessDay."""
    check(assert_type(CustomBusinessDay() + Day(), BusinessDay), BusinessDay)
    check(assert_type(Day() + CustomBusinessDay(), BusinessDay), BusinessDay)
    check(assert_type(CustomBusinessDay() + Hour(), BusinessDay), BusinessDay)
    check(assert_type(Hour() + CustomBusinessDay(), BusinessDay), BusinessDay)


@pytest.mark.parametrize(
    "left, right, expected",
    [(Day(), Hour(), pd.Timedelta), (Hour(), Minute(), Tick)],
)
def test_add_broad_offsets(
    left: BaseOffset, right: BaseOffset, expected: type[BaseOffset] | type[pd.Timedelta]
) -> None:
    check(assert_type(left + right, BaseOffset | pd.Timedelta), expected)
    check(assert_type(right + left, BaseOffset | pd.Timedelta), expected)
    check(
        assert_type(left.__radd__(right), BaseOffset | pd.Timedelta),
        expected,
    )


def test_day_hierarchy() -> None:
    day = Day()
    timestamp = pd.Timestamp("2026-01-01")
    check(assert_type(timestamp + day, pd.Timestamp), pd.Timestamp)
    check(assert_type(day + timestamp, pd.Timestamp), pd.Timestamp)
    check(assert_type(timestamp - day, pd.Timestamp), pd.Timestamp)
    check(assert_type(day.__rsub__(timestamp), pd.Timestamp), pd.Timestamp)
    if TYPE_CHECKING_INVALID_USAGE:
        pd.Timedelta(day)  # type: ignore[arg-type] # pyright: ignore[reportArgumentType] # pyrefly: ignore[bad-argument-type] # ty: ignore[invalid-argument-type]
