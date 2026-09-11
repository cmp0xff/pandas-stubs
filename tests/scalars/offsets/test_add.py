from typing import cast

from tests import TYPE_CHECKING_INVALID_USAGE

from pandas.tseries.offsets import (
    BaseOffset,
    Day,
    Hour,
)


def test_base_offset_rejection() -> None:
    """BaseOffset itself does not implement scalar addition."""
    left = BaseOffset()
    right = BaseOffset()
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = left + right  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _1 = right + left  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _2 = left.__add__(right)  # type: ignore[operator] # pyright: ignore[reportAttributeAccessIssue,reportUnknownVariableType,reportUnknownMemberType] # pyrefly: ignore[missing-attribute] # ty: ignore[unresolved-attribute]
        _3 = left.__radd__(right)  # type: ignore[attr-defined] # pyright: ignore[reportAttributeAccessIssue,reportUnknownVariableType,reportUnknownMemberType] # pyrefly: ignore[missing-attribute] # ty: ignore[unresolved-attribute]


def test_broad_offset_rejection() -> None:
    """Broad operands require narrowing to an implementing family."""
    left = cast(BaseOffset, Day())
    right = cast(BaseOffset, Hour())
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = left + right  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _1 = right + left  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _2 = left.__add__(right)  # type: ignore[operator] # pyright: ignore[reportAttributeAccessIssue,reportUnknownVariableType,reportUnknownMemberType] # pyrefly: ignore[missing-attribute] # ty: ignore[unresolved-attribute]
        _3 = left.__radd__(right)  # type: ignore[attr-defined] # pyright: ignore[reportAttributeAccessIssue,reportUnknownVariableType,reportUnknownMemberType] # pyrefly: ignore[missing-attribute] # ty: ignore[unresolved-attribute]
