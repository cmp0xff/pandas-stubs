from typing import assert_type

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
    Tick,
)


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


@pytest.mark.parametrize("business", [BusinessDay(), CustomBusinessDay()])
def test_business_day_direct_dispatch(business: BusinessDay) -> None:
    result = check(assert_type(business.__add__(Hour()), BusinessDay), BusinessDay)
    assert type(result) is BusinessDay
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = Hour().__add__(business)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = Hour().__radd__(business)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]


@pytest.mark.parametrize("business", [BusinessDay(), CustomBusinessDay()])
@pytest.mark.parametrize("method", ["__add__", "__radd__"])
def test_business_day_runtime_dispatch(business: object, method: str) -> None:
    assert getattr(Hour(), method)(business) is NotImplemented
