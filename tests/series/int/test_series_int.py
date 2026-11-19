from __future__ import annotations

from typing import assert_type

import numpy as np
import pandas as pd

from tests import (
    TYPE_CHECKING_INVALID_USAGE,
    check,
)

from pandas.tseries.offsets import (
    BDay,
    BQuarterEnd,
    MonthEnd,
    Week,
    YearEnd,
)


def test_types_ffill() -> None:
    s1 = pd.Series([1, 2, 3])
    check(assert_type(s1.ffill(), "pd.Series[int]"), pd.Series, np.integer)
    check(assert_type(s1.ffill(inplace=False), "pd.Series[int]"), pd.Series, np.integer)
    check(
        assert_type(s1.ffill(inplace=False, limit_area="inside"), "pd.Series[int]"),
        pd.Series,
        np.integer,
    )
    check(assert_type(s1.ffill(inplace=True), "pd.Series[int]"), pd.Series, np.integer)
    check(
        assert_type(s1.ffill(inplace=True, limit_area="outside"), "pd.Series[int]"),
        pd.Series,
        np.integer,
    )


def test_types_bfill() -> None:
    s1 = pd.Series([1, 2, 3])
    check(assert_type(s1.bfill(), "pd.Series[int]"), pd.Series, np.integer)
    check(assert_type(s1.bfill(inplace=False), "pd.Series[int]"), pd.Series, np.integer)
    check(
        assert_type(s1.bfill(inplace=False, limit_area="inside"), "pd.Series[int]"),
        pd.Series,
        np.integer,
    )
    check(assert_type(s1.bfill(inplace=True), "pd.Series[int]"), pd.Series, np.integer)
    check(
        assert_type(s1.bfill(inplace=True, limit_area="outside"), "pd.Series[int]"),
        pd.Series,
        np.integer,
    )


def test_types_shift() -> None:
    """Test shift operator on series with different arguments."""
    s = pd.Series([1, 2, 3], index=pd.date_range("2020", periods=3))
    check(assert_type(s.shift(), pd.Series), pd.Series, np.floating)
    check(assert_type(s.shift(axis=0, periods=1), pd.Series), pd.Series, np.floating)
    check(assert_type(s.shift(-1, fill_value=0), pd.Series), pd.Series, np.integer)
    check(assert_type(s.shift(freq="1D"), pd.Series), pd.Series, np.integer)
    check(assert_type(s.shift(freq=BDay(1)), pd.Series), pd.Series, np.integer)
    check(assert_type(s.shift(freq=BQuarterEnd(5)), pd.Series), pd.Series, np.integer)
    check(assert_type(s.shift(freq=MonthEnd(3)), pd.Series), pd.Series, np.integer)
    check(assert_type(s.shift(freq=Week(4)), pd.Series), pd.Series, np.integer)
    check(assert_type(s.shift(freq=YearEnd(2)), pd.Series), pd.Series, np.integer)
    check(
        assert_type(s.shift(freq=None, fill_value=None), pd.Series),
        pd.Series,
        np.floating,
    )

    if TYPE_CHECKING_INVALID_USAGE:
        s.shift(freq="1D", fill_value=4)  # type: ignore[call-overload] # pyright: ignore[reportArgumentType] # pyrefly: ignore[no-matching-overload] # ty: ignore[invalid-argument-type]
