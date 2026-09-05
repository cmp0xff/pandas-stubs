from typing import assert_type

import numpy as np
import pandas as pd

from tests import (
    TYPE_CHECKING_INVALID_USAGE,
    check,
)


def test_bitwise_operators() -> None:
    s = pd.Series([1, 2, 3, 4], dtype=int)
    s2 = pd.Series([9, 10, 11, 12], dtype=int)
    # for issue #348 (bitwise operators on Series should support int)
    # The bitwise integers return platform-dependent numpy integers in the Series
    check(assert_type(s & 3, "pd.Series[int]"), pd.Series, np.integer)
    check(assert_type(3 & s, "pd.Series[int]"), pd.Series, np.integer)

    check(assert_type(s | 3, "pd.Series[int]"), pd.Series, np.integer)
    check(assert_type(3 | s, "pd.Series[int]"), pd.Series, np.integer)

    check(assert_type(s ^ 3, "pd.Series[int]"), pd.Series, np.integer)
    check(assert_type(3 ^ s, "pd.Series[int]"), pd.Series, np.integer)

    check(assert_type(s & s2, "pd.Series[int]"), pd.Series, np.integer)
    check(assert_type(s2 & s, "pd.Series[int]"), pd.Series, np.integer)

    check(assert_type(s | s2, "pd.Series[int]"), pd.Series, np.integer)
    check(assert_type(s2 | s, "pd.Series[int]"), pd.Series, np.integer)

    check(assert_type(s ^ s2, "pd.Series[int]"), pd.Series, np.integer)
    check(assert_type(s2 ^ s, "pd.Series[int]"), pd.Series, np.integer)

    if TYPE_CHECKING_INVALID_USAGE:
        _0 = s & [1, 2, 3, 4]  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _1 = [1, 2, 3, 4] & s  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]

        _2 = s | [1, 2, 3, 4]  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _3 = [1, 2, 3, 4] | s  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]

        _4 = s ^ [1, 2, 3, 4]  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _5 = [1, 2, 3, 4] ^ s  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
