from __future__ import annotations

from datetime import (
    datetime,
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
def left() -> pd.Series[pd.Timestamp]:
    """Left operand"""
    lo = pd.Series([pd.Timestamp(2022, 1, 1)])
    return check(assert_type(lo, "pd.Series[pd.Timestamp]"), pd.Series, pd.Timestamp)


def test_relops_py_scalar(left: pd.Series[pd.Timestamp]) -> None:
    """Test pd.Series[pd.Timestamp] <comparison> py scalar"""
    t = pd.Timestamp(2022, 1, 2)

    check(assert_type(left < t, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left <= t, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left > t, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left >= t, "pd.Series[bool]"), pd.Series, np.bool_)


def test_relops_py_sequence(left: pd.Series[pd.Timestamp]) -> None:
    """Test pd.Series[pd.Timestamp] <comparison> py sequence"""
    t = [datetime(2022, 1, 2)]

    check(assert_type(left < t, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left <= t, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left > t, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left >= t, "pd.Series[bool]"), pd.Series, np.bool_)


def test_relops_numpy_array(left: pd.Series[pd.Timestamp]) -> None:
    """Test pd.Series[pd.Timestamp] <comparison> numpy array"""
    t = np.array(["2022-01-02"], dtype="datetime64[ns]")

    check(assert_type(left < t, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left <= t, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left > t, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left >= t, "pd.Series[bool]"), pd.Series, np.bool_)


def test_relops_pd_index(left: pd.Series[pd.Timestamp]) -> None:
    """Test pd.Series[pd.Timestamp] <comparison> pd index"""
    t = pd.DatetimeIndex(["2022-01-02"])

    check(assert_type(left < t, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left <= t, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left > t, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left >= t, "pd.Series[bool]"), pd.Series, np.bool_)


def test_relops_pd_series(left: pd.Series[pd.Timestamp]) -> None:
    """Test pd.Series[pd.Timestamp] <comparison> pd series"""
    t = pd.Series([pd.Timestamp(2022, 1, 2)])

    check(assert_type(left < t, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left <= t, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left > t, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left >= t, "pd.Series[bool]"), pd.Series, np.bool_)


def test_relops_invalid(left: pd.Series[pd.Timestamp]) -> None:
    """Test invalid pd.Series[pd.Timestamp] comparisons"""
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
