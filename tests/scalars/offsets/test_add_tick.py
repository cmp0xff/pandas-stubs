from typing import assert_type

import pytest

from tests import (
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


def test_add_same_tick_class() -> None:
    """Adding ticks of the same concrete class preserves that class."""
    check(assert_type(Hour(1) + Hour(2), Hour), Hour)
    check(assert_type(Minute(1) + Minute(2), Minute), Minute)
    check(assert_type(Second(1) + Second(2), Second), Second)
    check(assert_type(Milli(1) + Milli(2), Milli), Milli)
    check(assert_type(Micro(1) + Micro(2), Micro), Micro)
    check(assert_type(Nano(1) + Nano(2), Nano), Nano)

    check(assert_type(Hour(1).__radd__(Hour(2)), Hour), Hour)
    check(assert_type(Hour(1).__add__(Hour(2)), Hour), Hour)
    check(assert_type(Minute(1).__radd__(Minute(2)), Minute), Minute)
    check(assert_type(Minute(1).__add__(Minute(2)), Minute), Minute)
    check(assert_type(Second(1).__radd__(Second(2)), Second), Second)
    check(assert_type(Second(1).__add__(Second(2)), Second), Second)
    check(assert_type(Milli(1).__radd__(Milli(2)), Milli), Milli)
    check(assert_type(Milli(1).__add__(Milli(2)), Milli), Milli)
    check(assert_type(Micro(1).__radd__(Micro(2)), Micro), Micro)
    check(assert_type(Micro(1).__add__(Micro(2)), Micro), Micro)
    check(assert_type(Nano(1).__radd__(Nano(2)), Nano), Nano)
    check(assert_type(Nano(1).__add__(Nano(2)), Nano), Nano)


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
