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
from tests._typing import (
    np_1darray_bool,
)


@pytest.fixture
def left() -> pd.TimedeltaIndex:
    """Left operand"""
    lo = pd.TimedeltaIndex(["1D", "2D"])
    return check(assert_type(lo, "pd.TimedeltaIndex"), pd.Index, pd.Timedelta)


def test_relops_py_scalar(left: pd.TimedeltaIndex) -> None:
    """Test pd.TimedeltaIndex <comparison> py scalar"""
    t = pd.Timedelta(2, "D")

    check(assert_type(left < t, np_1darray_bool), np_1darray_bool)

    check(assert_type(left <= t, np_1darray_bool), np_1darray_bool)

    check(assert_type(left > t, np_1darray_bool), np_1darray_bool)

    check(assert_type(left >= t, np_1darray_bool), np_1darray_bool)


def test_relops_py_sequence(left: pd.TimedeltaIndex) -> None:
    """Test pd.TimedeltaIndex <comparison> py sequence"""
    t = [timedelta(days=2), timedelta(days=3)]

    check(assert_type(left < t, np_1darray_bool), np_1darray_bool)

    check(assert_type(left <= t, np_1darray_bool), np_1darray_bool)

    check(assert_type(left > t, np_1darray_bool), np_1darray_bool)

    check(assert_type(left >= t, np_1darray_bool), np_1darray_bool)


def test_relops_numpy_array(left: pd.TimedeltaIndex) -> None:
    """Test pd.TimedeltaIndex <comparison> numpy array"""
    t = np.array([2, 3], dtype="timedelta64[D]")

    check(assert_type(left < t, np_1darray_bool), np_1darray_bool)

    check(assert_type(left <= t, np_1darray_bool), np_1darray_bool)

    check(assert_type(left > t, np_1darray_bool), np_1darray_bool)

    check(assert_type(left >= t, np_1darray_bool), np_1darray_bool)


def test_relops_pd_index(left: pd.TimedeltaIndex) -> None:
    """Test pd.TimedeltaIndex <comparison> pd index"""
    t = pd.TimedeltaIndex(["2D", "3D"])

    check(assert_type(left < t, np_1darray_bool), np_1darray_bool)

    check(assert_type(left <= t, np_1darray_bool), np_1darray_bool)

    check(assert_type(left > t, np_1darray_bool), np_1darray_bool)

    check(assert_type(left >= t, np_1darray_bool), np_1darray_bool)


def test_relops_invalid(left: pd.TimedeltaIndex) -> None:
    """Test invalid pd.TimedeltaIndex comparisons"""
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
