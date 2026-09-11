from typing import cast

from tests import TYPE_CHECKING_INVALID_USAGE

from pandas.tseries.offsets import (
    BaseOffset,
    Day,
    Hour,
    Minute,
)


def test_add_broad_offsets() -> None:
    left = cast(BaseOffset, Day())
    right = cast(BaseOffset, Hour())
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = left + right  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _1 = right + left  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _2 = left.__add__(right)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _3 = left.__radd__(right)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]

    left = cast(BaseOffset, Hour())
    right = cast(BaseOffset, Minute())
    if TYPE_CHECKING_INVALID_USAGE:
        _4 = left + right  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _5 = right + left  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _6 = left.__add__(right)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _7 = left.__radd__(right)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
