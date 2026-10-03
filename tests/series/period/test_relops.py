from __future__ import annotations

from typing import assert_type

import numpy as np
import pandas as pd
import pytest

from tests import (
    TYPE_CHECKING_INVALID_USAGE,
    check,
)


@pytest.fixture
def left() -> pd.Series[pd.Period]:
    """Left operand"""
    lo = pd.Series(pd.period_range("2022-01", periods=2, freq="M"))
    return check(assert_type(lo, "pd.Series[pd.Period]"), pd.Series, pd.Period)


def test_relops_py_scalar(left: pd.Series[pd.Period]) -> None:
    """Test pd.Series[pd.Period] <comparison> py scalar"""
    t = pd.Period("2022-02", "M")

    check(assert_type(left < t, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left <= t, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left > t, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left >= t, "pd.Series[bool]"), pd.Series, np.bool_)


def test_relops_py_sequence(left: pd.Series[pd.Period]) -> None:
    """Test pd.Series[pd.Period] <comparison> py sequence"""
    t = [pd.Period("2022-02", "M"), pd.Period("2022-03", "M")]

    check(assert_type(left < t, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left <= t, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left > t, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left >= t, "pd.Series[bool]"), pd.Series, np.bool_)


def test_relops_pd_index(left: pd.Series[pd.Period]) -> None:
    """Test pd.Series[pd.Period] <comparison> pd index"""
    t = pd.period_range("2022-02", periods=2, freq="M")

    check(assert_type(left < t, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left <= t, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left > t, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left >= t, "pd.Series[bool]"), pd.Series, np.bool_)


def test_relops_pd_series(left: pd.Series[pd.Period]) -> None:
    """Test pd.Series[pd.Period] <comparison> pd series"""
    t = pd.Series(pd.period_range("2022-02", periods=2, freq="M"))

    check(assert_type(left < t, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left <= t, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left > t, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left >= t, "pd.Series[bool]"), pd.Series, np.bool_)


def test_relops_invalid(left: pd.Series[pd.Period]) -> None:
    """Test invalid pd.Series[pd.Period] comparisons"""
    i: list[int] = [1, 2]

    if TYPE_CHECKING_INVALID_USAGE:
        _0 = left < i  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _1 = left <= i  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _2 = left > i  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _3 = left >= i  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
