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
def left() -> pd.Series[complex]:
    """Left operand"""
    lo = pd.Series([1j, 2j, 4j])
    return check(assert_type(lo, "pd.Series[complex]"), pd.Series, np.complexfloating)


def test_relops_py_scalar(left: pd.Series[complex]) -> None:
    """Test pd.Series[complex] <comparison> py scalar"""
    i, f = 1, 1.0

    check(assert_type(left < i, "pd.Series[bool]"), pd.Series, np.bool_)
    check(assert_type(left < f, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left <= i, "pd.Series[bool]"), pd.Series, np.bool_)
    check(assert_type(left <= f, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left > i, "pd.Series[bool]"), pd.Series, np.bool_)
    check(assert_type(left > f, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left >= i, "pd.Series[bool]"), pd.Series, np.bool_)
    check(assert_type(left >= f, "pd.Series[bool]"), pd.Series, np.bool_)


def test_relops_py_sequence(left: pd.Series[complex]) -> None:
    """Test pd.Series[complex] <comparison> py sequence"""
    i, f = [2, 3, 5], [1.0, 2.0, 3.0]

    check(assert_type(left < i, "pd.Series[bool]"), pd.Series, np.bool_)
    check(assert_type(left < f, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left <= i, "pd.Series[bool]"), pd.Series, np.bool_)
    check(assert_type(left <= f, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left > i, "pd.Series[bool]"), pd.Series, np.bool_)
    check(assert_type(left > f, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left >= i, "pd.Series[bool]"), pd.Series, np.bool_)
    check(assert_type(left >= f, "pd.Series[bool]"), pd.Series, np.bool_)


def test_relops_numpy_array(left: pd.Series[complex]) -> None:
    """Test pd.Series[complex] <comparison> numpy array"""
    i = np.array([2, 3, 5], np.int64)
    f = np.array([1.0, 2.0, 3.0], np.float64)

    check(assert_type(left < i, "pd.Series[bool]"), pd.Series, np.bool_)
    check(assert_type(left < f, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left <= i, "pd.Series[bool]"), pd.Series, np.bool_)
    check(assert_type(left <= f, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left > i, "pd.Series[bool]"), pd.Series, np.bool_)
    check(assert_type(left > f, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left >= i, "pd.Series[bool]"), pd.Series, np.bool_)
    check(assert_type(left >= f, "pd.Series[bool]"), pd.Series, np.bool_)


def test_relops_pd_index(left: pd.Series[complex]) -> None:
    """Test pd.Series[complex] <comparison> pd index"""
    i = pd.Index([2, 3, 5])
    f = pd.Index([1.0, 2.0, 3.0])

    check(assert_type(left < i, "pd.Series[bool]"), pd.Series, np.bool_)
    check(assert_type(left < f, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left <= i, "pd.Series[bool]"), pd.Series, np.bool_)
    check(assert_type(left <= f, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left > i, "pd.Series[bool]"), pd.Series, np.bool_)
    check(assert_type(left > f, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left >= i, "pd.Series[bool]"), pd.Series, np.bool_)
    check(assert_type(left >= f, "pd.Series[bool]"), pd.Series, np.bool_)


def test_relops_pd_series(left: pd.Series[complex]) -> None:
    """Test pd.Series[complex] <comparison> pd series"""
    i = pd.Series([2, 3, 5])
    f = pd.Series([1.0, 2.0, 3.0])

    check(assert_type(left < i, "pd.Series[bool]"), pd.Series, np.bool_)
    check(assert_type(left < f, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left <= i, "pd.Series[bool]"), pd.Series, np.bool_)
    check(assert_type(left <= f, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left > i, "pd.Series[bool]"), pd.Series, np.bool_)
    check(assert_type(left > f, "pd.Series[bool]"), pd.Series, np.bool_)

    check(assert_type(left >= i, "pd.Series[bool]"), pd.Series, np.bool_)
    check(assert_type(left >= f, "pd.Series[bool]"), pd.Series, np.bool_)


def test_relops_invalid(left: pd.Series[complex]) -> None:
    """Test invalid pd.Series[complex] comparisons"""
    s: list[str] = ["a", "b"]
    idx: pd.Index[str] = pd.Index(["a", "b"])
    ser: pd.Series[str] = pd.Series(["a", "b"])

    if TYPE_CHECKING_INVALID_USAGE:
        _0 = left < s  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _1 = left <= s  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _2 = left > s  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _3 = left >= s  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _4 = left < idx  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _5 = left <= idx  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _6 = left > idx  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _7 = left >= idx  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _8 = left < ser  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _9 = left <= ser  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _10 = left > ser  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _11 = left >= ser  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
