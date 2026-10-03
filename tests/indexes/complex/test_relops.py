from __future__ import annotations

from typing import assert_type

import numpy as np
import pandas as pd
import pytest

from tests import (
    TYPE_CHECKING_INVALID_USAGE,
    check,
)
from tests._typing import (
    np_1darray_bool,
    np_ndarray_bool,
)


@pytest.fixture
def left() -> pd.Index[complex]:
    """Left operand"""
    lo = pd.Index([1j, 2j, 4j])
    return check(assert_type(lo, "pd.Index[complex]"), pd.Index, np.complexfloating)


def test_relops_py_scalar(left: pd.Index[complex]) -> None:
    """Test pd.Index[complex] <comparison> py scalar"""
    i, f = 2, 2.0

    check(assert_type(left < i, np_1darray_bool), np_1darray_bool)
    check(assert_type(left < f, np_1darray_bool), np_1darray_bool)

    check(assert_type(left <= i, np_1darray_bool), np_1darray_bool)
    check(assert_type(left <= f, np_1darray_bool), np_1darray_bool)

    check(assert_type(left > i, np_1darray_bool), np_1darray_bool)
    check(assert_type(left > f, np_1darray_bool), np_1darray_bool)

    check(assert_type(left >= i, np_1darray_bool), np_1darray_bool)
    check(assert_type(left >= f, np_1darray_bool), np_1darray_bool)


def test_relops_py_sequence(left: pd.Index[complex]) -> None:
    """Test pd.Index[complex] <comparison> py sequence"""
    i, f = [2, 3, 5], [1.0, 2.0, 3.0]

    check(assert_type(left < i, np_1darray_bool), np_1darray_bool)
    check(assert_type(left < f, np_1darray_bool), np_1darray_bool)

    check(assert_type(left <= i, np_1darray_bool), np_1darray_bool)
    check(assert_type(left <= f, np_1darray_bool), np_1darray_bool)

    check(assert_type(left > i, np_1darray_bool), np_1darray_bool)
    check(assert_type(left > f, np_1darray_bool), np_1darray_bool)

    check(assert_type(left >= i, np_1darray_bool), np_1darray_bool)
    check(assert_type(left >= f, np_1darray_bool), np_1darray_bool)


def test_relops_numpy_array(left: pd.Index[complex]) -> None:
    """Test pd.Index[complex] <comparison> numpy array"""
    i = np.array([2, 3, 5], np.int64)
    f = np.array([1.0, 2.0, 3.0], np.float64)

    check(assert_type(left < i, np_ndarray_bool), np_1darray_bool)
    check(assert_type(left < f, np_ndarray_bool), np_1darray_bool)

    check(assert_type(left <= i, np_ndarray_bool), np_1darray_bool)
    check(assert_type(left <= f, np_ndarray_bool), np_1darray_bool)

    check(assert_type(left > i, np_ndarray_bool), np_1darray_bool)
    check(assert_type(left > f, np_ndarray_bool), np_1darray_bool)

    check(assert_type(left >= i, np_ndarray_bool), np_1darray_bool)
    check(assert_type(left >= f, np_ndarray_bool), np_1darray_bool)


def test_relops_pd_index(left: pd.Index[complex]) -> None:
    """Test pd.Index[complex] <comparison> pd index"""
    i = pd.Index([2, 3, 5])
    f = pd.Index([1.0, 2.0, 3.0])

    check(assert_type(left < i, np_1darray_bool), np_1darray_bool)
    check(assert_type(left < f, np_1darray_bool), np_1darray_bool)

    check(assert_type(left <= i, np_1darray_bool), np_1darray_bool)
    check(assert_type(left <= f, np_1darray_bool), np_1darray_bool)

    check(assert_type(left > i, np_1darray_bool), np_1darray_bool)
    check(assert_type(left > f, np_1darray_bool), np_1darray_bool)

    check(assert_type(left >= i, np_1darray_bool), np_1darray_bool)
    check(assert_type(left >= f, np_1darray_bool), np_1darray_bool)


def test_relops_invalid(left: pd.Index[complex]) -> None:
    """Test invalid pd.Index[complex] comparisons"""
    s: list[str] = ["a", "b"]
    idx: pd.Index[str] = pd.Index(["a", "b"])

    if TYPE_CHECKING_INVALID_USAGE:
        _0 = left < s  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _1 = left <= s  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _2 = left > s  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _3 = left >= s  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _4 = left < idx  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _5 = left <= idx  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _6 = left > idx  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _7 = left >= idx  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
