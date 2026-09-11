from typing import assert_type

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


def test_add_business_day() -> None:
    check(assert_type(BusinessDay() + Day(), BusinessDay), BusinessDay)
    check(assert_type(Day() + BusinessDay(), BusinessDay), BusinessDay)
    check(assert_type(BusinessDay() + Hour(), BusinessDay), BusinessDay)
    check(assert_type(Hour() + BusinessDay(), BusinessDay), BusinessDay)
    check(assert_type(BusinessDay().__add__(Hour()), BusinessDay), BusinessDay)
    check(assert_type(BusinessDay().__radd__(Hour()), BusinessDay), BusinessDay)
    check(assert_type(Day().__add__(BusinessDay()), BusinessDay), BusinessDay)
    check(assert_type(Day().__radd__(BusinessDay()), BusinessDay), BusinessDay)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = Hour().__add__(BusinessDay())  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = Hour().__radd__(BusinessDay())  # type: ignore[arg-type] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]


def test_add_custom_business_day() -> None:
    check(assert_type(CustomBusinessDay() + Day(), BusinessDay), BusinessDay)
    check(assert_type(Day() + CustomBusinessDay(), BusinessDay), BusinessDay)
    check(assert_type(CustomBusinessDay() + Hour(), BusinessDay), BusinessDay)
    check(assert_type(Hour() + CustomBusinessDay(), BusinessDay), BusinessDay)
    check(assert_type(CustomBusinessDay().__add__(Hour()), BusinessDay), BusinessDay)
    check(assert_type(CustomBusinessDay().__radd__(Hour()), BusinessDay), BusinessDay)
    check(assert_type(Day().__add__(CustomBusinessDay()), BusinessDay), BusinessDay)
    check(assert_type(Day().__radd__(CustomBusinessDay()), BusinessDay), BusinessDay)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = Hour().__add__(CustomBusinessDay())  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = Hour().__radd__(CustomBusinessDay())  # type: ignore[arg-type] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _2 = CustomBusinessDay().__add__(Day())  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _3 = CustomBusinessDay().__radd__(Day())  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
