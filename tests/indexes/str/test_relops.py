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
)


@pytest.fixture
def left() -> pd.Index[str]:
    """Left operand"""
    lo = pd.Index(["1", "2", "3"])
    return check(assert_type(lo, "pd.Index[str]"), pd.Index, str)


def test_relops_py_scalar(left: pd.Index[str]) -> None:
    """Test pd.Index[str] <comparison> py scalar"""
    s = "b"

    check(assert_type(left < s, np_1darray_bool), np_1darray_bool)

    check(assert_type(left <= s, np_1darray_bool), np_1darray_bool)

    check(assert_type(left > s, np_1darray_bool), np_1darray_bool)

    check(assert_type(left >= s, np_1darray_bool), np_1darray_bool)


def test_relops_py_sequence(left: pd.Index[str]) -> None:
    """Test pd.Index[str] <comparison> py sequence"""
    s = ["b", "c", "d"]

    check(assert_type(left < s, np_1darray_bool), np_1darray_bool)

    check(assert_type(left <= s, np_1darray_bool), np_1darray_bool)

    check(assert_type(left > s, np_1darray_bool), np_1darray_bool)

    check(assert_type(left >= s, np_1darray_bool), np_1darray_bool)


def test_relops_numpy_array(left: pd.Index[str]) -> None:
    """Test pd.Index[str] <comparison> numpy array"""
    s = np.array(["b", "c", "d"])

    check(assert_type(left < s, np_1darray_bool), np_1darray_bool)

    check(assert_type(left <= s, np_1darray_bool), np_1darray_bool)

    check(assert_type(left > s, np_1darray_bool), np_1darray_bool)

    check(assert_type(left >= s, np_1darray_bool), np_1darray_bool)


def test_relops_pd_index(left: pd.Index[str]) -> None:
    """Test pd.Index[str] <comparison> pd index"""
    s = pd.Index(["b", "c", "d"])

    check(assert_type(left < s, np_1darray_bool), np_1darray_bool)

    check(assert_type(left <= s, np_1darray_bool), np_1darray_bool)

    check(assert_type(left > s, np_1darray_bool), np_1darray_bool)

    check(assert_type(left >= s, np_1darray_bool), np_1darray_bool)


def test_relops_invalid(left: pd.Index[str]) -> None:
    """Test invalid pd.Index[str] comparisons"""
    i: list[int] = [1, 2]
    idx: pd.Index[int] = pd.Index([1, 2])

    if TYPE_CHECKING_INVALID_USAGE:
        _0 = left < i  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _1 = left <= i  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _2 = left > i  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _3 = left >= i  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _4 = left < idx  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _5 = left <= idx  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _6 = left > idx  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _7 = left >= idx  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
