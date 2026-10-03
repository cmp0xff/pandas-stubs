from __future__ import annotations

from typing import assert_type

import pandas as pd
import pytest

from tests import (
    TYPE_CHECKING_INVALID_USAGE,
    check,
)
from tests._typing import (
    np_1darray_bool,
)


@pytest.fixture
def left() -> pd.PeriodIndex:
    """Left operand"""
    lo = pd.period_range("2022-01", periods=2, freq="M")
    return check(assert_type(lo, "pd.PeriodIndex"), pd.Index, pd.Period)


def test_relops_py_scalar(left: pd.PeriodIndex) -> None:
    """Test pd.PeriodIndex <comparison> py scalar"""
    t = pd.Period("2022-02", "M")

    check(assert_type(left < t, np_1darray_bool), np_1darray_bool)

    check(assert_type(left <= t, np_1darray_bool), np_1darray_bool)

    check(assert_type(left > t, np_1darray_bool), np_1darray_bool)

    check(assert_type(left >= t, np_1darray_bool), np_1darray_bool)


def test_relops_py_sequence(left: pd.PeriodIndex) -> None:
    """Test pd.PeriodIndex <comparison> py sequence"""
    t = [pd.Period("2022-02", "M"), pd.Period("2022-03", "M")]

    check(assert_type(left < t, np_1darray_bool), np_1darray_bool)

    check(assert_type(left <= t, np_1darray_bool), np_1darray_bool)

    check(assert_type(left > t, np_1darray_bool), np_1darray_bool)

    check(assert_type(left >= t, np_1darray_bool), np_1darray_bool)


def test_relops_pd_index(left: pd.PeriodIndex) -> None:
    """Test pd.PeriodIndex <comparison> pd index"""
    t = pd.period_range("2022-02", periods=2, freq="M")

    check(assert_type(left < t, np_1darray_bool), np_1darray_bool)

    check(assert_type(left <= t, np_1darray_bool), np_1darray_bool)

    check(assert_type(left > t, np_1darray_bool), np_1darray_bool)

    check(assert_type(left >= t, np_1darray_bool), np_1darray_bool)


def test_relops_invalid(left: pd.PeriodIndex) -> None:
    """Test invalid pd.PeriodIndex comparisons"""
    i: list[int] = [1, 2]

    if TYPE_CHECKING_INVALID_USAGE:
        _0 = left < i  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _1 = left <= i  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _2 = left > i  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _3 = left >= i  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
