from typing import assert_type

import pandas as pd
import pytest

from tests import (
    TYPE_CHECKING_INVALID_USAGE,
    check,
)

from pandas.tseries.offsets import (
    BaseOffset,
    Day,
    Hour,
    Minute,
    Tick,
)


@pytest.mark.parametrize("left, right", [(Day(), Hour()), (Hour(), Minute())])
def test_add_broad_offsets(left: BaseOffset, right: BaseOffset) -> None:
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = left + right  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _1 = right + left  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _2 = left.__add__(right)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _3 = left.__radd__(right)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]

    if isinstance(left, Day) and isinstance(right, Tick):
        check(assert_type(left + right, pd.Timedelta), pd.Timedelta)
        check(assert_type(right + left, pd.Timedelta), pd.Timedelta)
    elif isinstance(left, Tick) and isinstance(right, Tick):
        check(assert_type(left + right, Tick), Tick)
        check(assert_type(left.__add__(right), Tick), Tick)
        check(assert_type(left.__radd__(right), Tick), Tick)
