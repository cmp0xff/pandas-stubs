from __future__ import annotations

from datetime import (
    timedelta,
)
from typing import assert_type

import numpy as np
import pandas as pd
import pytest

from tests import (
    TYPE_CHECKING_INVALID_USAGE,
    check,
)


@pytest.fixture
def left() -> pd.Series[pd.Timedelta]:
    """Left operand"""
    lo = pd.Series([pd.Timedelta(1, "D")])
    return check(assert_type(lo, "pd.Series[pd.Timedelta]"), pd.Series, pd.Timedelta)


def test_relops_py_scalar(left: pd.Series[pd.Timedelta]) -> None:
    """Test pd.Series[pd.Timedelta] <comparison> py scalar"""
    t = pd.Timedelta(2, "D")

    check(assert_type(left < t, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left <= t, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left > t, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left >= t, "pd.Series[bool]"), pd.Series, np.bool_)


def test_relops_py_sequence(left: pd.Series[pd.Timedelta]) -> None:
    """Test pd.Series[pd.Timedelta] <comparison> py sequence"""
    t = [timedelta(days=2)]

    check(assert_type(left < t, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left <= t, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left > t, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left >= t, "pd.Series[bool]"), pd.Series, np.bool_)


def test_relops_numpy_array(left: pd.Series[pd.Timedelta]) -> None:
    """Test pd.Series[pd.Timedelta] <comparison> numpy array"""
    t = np.array([2], dtype="timedelta64[D]")

    check(assert_type(left < t, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left <= t, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left > t, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left >= t, "pd.Series[bool]"), pd.Series, np.bool_)


def test_relops_pd_index(left: pd.Series[pd.Timedelta]) -> None:
    """Test pd.Series[pd.Timedelta] <comparison> pd index"""
    t = pd.TimedeltaIndex(["2D"])

    check(assert_type(left < t, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left <= t, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left > t, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left >= t, "pd.Series[bool]"), pd.Series, np.bool_)


def test_relops_pd_series(left: pd.Series[pd.Timedelta]) -> None:
    """Test pd.Series[pd.Timedelta] <comparison> pd series"""
    t = pd.Series([pd.Timedelta(2, "D")])

    check(assert_type(left < t, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left <= t, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left > t, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left >= t, "pd.Series[bool]"), pd.Series, np.bool_)


def test_relops_invalid(left: pd.Series[pd.Timedelta]) -> None:
    """Test invalid pd.Series[pd.Timedelta] comparisons"""
    i: list[int] = [1, 2]
    idx: pd.Index[int] = pd.Index([1, 2])
    ser: pd.Series[int] = pd.Series([1, 2])

    if TYPE_CHECKING_INVALID_USAGE:
        _0 = left < i  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _1 = left <= i  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _2 = left > i  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _3 = left >= i  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _4 = left < idx  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _5 = left <= idx  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _6 = left > idx  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _7 = left >= idx  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _8 = left < ser  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _9 = left <= ser  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _10 = left > ser  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _11 = left >= ser  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
