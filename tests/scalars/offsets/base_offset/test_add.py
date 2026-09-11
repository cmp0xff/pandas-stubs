import pytest

from tests import TYPE_CHECKING_INVALID_USAGE

from pandas.tseries.offsets import BaseOffset


@pytest.fixture
def left() -> BaseOffset:
    """Left operand."""
    return BaseOffset()


def test_base_offset_rejection(left: BaseOffset) -> None:
    """BaseOffset operands require narrowing to an implementing family."""
    right = BaseOffset()
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = left + right  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
