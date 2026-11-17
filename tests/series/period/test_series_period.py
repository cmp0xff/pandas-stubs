"""Test module for shift operation on Series[Period]."""

from typing import assert_type

import pandas as pd

from tests import (
    TYPE_CHECKING_INVALID_USAGE,
    check,
)


def test_types_shift_fill_value() -> None:
    """Test fill_value of pd.Series[pd.Period].shift."""
    s = pd.Series(pd.period_range("2020", periods=3, freq="D"))
    per = pd.Period("2020", "D")

    check(assert_type(s.shift(1, fill_value=per), pd.Series), pd.Series, pd.Period)
    check(assert_type(s.shift(1, fill_value=pd.NaT), pd.Series), pd.Series)
    check(assert_type(s.shift(1, fill_value=None), pd.Series), pd.Series)

    if TYPE_CHECKING_INVALID_USAGE:
        s.shift(1, fill_value=True)  # type: ignore[call-overload] # pyright: ignore[reportCallIssue,reportArgumentType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
