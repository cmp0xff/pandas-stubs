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
def left() -> pd.Series[bytes]:
    """Left operand"""
    lo = pd.Series([b"1", b"2", b"3"])
    return check(assert_type(lo, "pd.Series[bytes]"), pd.Series, bytes)


def test_relops_py_scalar(left: pd.Series[bytes]) -> None:
    """Test pd.Series[bytes] <comparison> py scalar"""
    y = b"b"

    check(assert_type(left < y, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left <= y, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left > y, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left >= y, "pd.Series[bool]"), pd.Series, np.bool_)


def test_relops_py_sequence(left: pd.Series[bytes]) -> None:
    """Test pd.Series[bytes] <comparison> py sequence"""
    y = [b"b", b"c", b"d"]

    check(assert_type(left < y, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left <= y, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left > y, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left >= y, "pd.Series[bool]"), pd.Series, np.bool_)


def test_relops_numpy_array(left: pd.Series[bytes]) -> None:
    """Test pd.Series[bytes] <comparison> numpy array"""
    y = np.array([b"b", b"c", b"d"])

    check(assert_type(left < y, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left <= y, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left > y, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left >= y, "pd.Series[bool]"), pd.Series, np.bool_)


def test_relops_pd_index(left: pd.Series[bytes]) -> None:
    """Test pd.Series[bytes] <comparison> pd index"""
    y = pd.Index([b"b", b"c", b"d"])

    check(assert_type(left < y, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left <= y, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left > y, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left >= y, "pd.Series[bool]"), pd.Series, np.bool_)


def test_relops_pd_series(left: pd.Series[bytes]) -> None:
    """Test pd.Series[bytes] <comparison> pd series"""
    y = pd.Series([b"b", b"c", b"d"])

    check(assert_type(left < y, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left <= y, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left > y, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left >= y, "pd.Series[bool]"), pd.Series, np.bool_)


def test_relops_invalid(left: pd.Series[bytes]) -> None:
    """Test invalid pd.Series[bytes] comparisons"""
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
