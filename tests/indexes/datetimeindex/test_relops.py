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
from tests._typing import (
    np_1darray_bool,
)


@pytest.fixture
def left() -> pd.DatetimeIndex:
    """Left operand"""
    lo = pd.DatetimeIndex(["2022-01-01", "2022-01-02"])
    return check(assert_type(lo, "pd.DatetimeIndex"), pd.Index, pd.Timestamp)


def test_relops_py_scalar(left: pd.DatetimeIndex) -> None:
    """Test pd.DatetimeIndex <comparison> py scalar"""
    t = pd.Timestamp(2022, 1, 2)

    check(assert_type(left < t, np_1darray_bool), np_1darray_bool)

    check(assert_type(left <= t, np_1darray_bool), np_1darray_bool)

    check(assert_type(left > t, np_1darray_bool), np_1darray_bool)

    check(assert_type(left >= t, np_1darray_bool), np_1darray_bool)


def test_relops_py_sequence(left: pd.DatetimeIndex) -> None:
    """Test pd.DatetimeIndex <comparison> py sequence"""
    t = [datetime(2022, 1, 2), datetime(2022, 1, 3)]

    check(assert_type(left < t, np_1darray_bool), np_1darray_bool)

    check(assert_type(left <= t, np_1darray_bool), np_1darray_bool)

    check(assert_type(left > t, np_1darray_bool), np_1darray_bool)

    check(assert_type(left >= t, np_1darray_bool), np_1darray_bool)


def test_relops_numpy_array(left: pd.DatetimeIndex) -> None:
    """Test pd.DatetimeIndex <comparison> numpy array"""
    t = np.array(["2022-01-02", "2022-01-03"], dtype="datetime64[ns]")

    check(assert_type(left < t, np_1darray_bool), np_1darray_bool)

    check(assert_type(left <= t, np_1darray_bool), np_1darray_bool)

    check(assert_type(left > t, np_1darray_bool), np_1darray_bool)

    check(assert_type(left >= t, np_1darray_bool), np_1darray_bool)


def test_relops_pd_index(left: pd.DatetimeIndex) -> None:
    """Test pd.DatetimeIndex <comparison> pd index"""
    t = pd.DatetimeIndex(["2022-01-02", "2022-01-03"])

    check(assert_type(left < t, np_1darray_bool), np_1darray_bool)

    check(assert_type(left <= t, np_1darray_bool), np_1darray_bool)

    check(assert_type(left > t, np_1darray_bool), np_1darray_bool)

    check(assert_type(left >= t, np_1darray_bool), np_1darray_bool)


def test_relops_invalid(left: pd.DatetimeIndex) -> None:
    """Test invalid pd.DatetimeIndex comparisons"""
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
