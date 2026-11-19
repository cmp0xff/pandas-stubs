"""Test module for shift operation on Series[Timestamp]."""

from typing import assert_type

import numpy as np
import pandas as pd

from tests import (
    TYPE_CHECKING_INVALID_USAGE,
    check,
)


def test_types_shift_fill_value() -> None:
    """Test fill_value of pd.Series[pd.Timestamp].shift."""
    s = pd.Series(pd.date_range("2020", periods=3))
    ts = pd.Timestamp("2020")

    check(assert_type(s.shift(1, fill_value=ts), pd.Series), pd.Series, pd.Timestamp)
    check(assert_type(s.shift(1, fill_value=pd.NaT), pd.Series), pd.Series)
    check(assert_type(s.shift(1, fill_value=None), pd.Series), pd.Series)
    check(
        assert_type(s.shift(1, fill_value=np.datetime64("2020-01-02")), pd.Series),
        pd.Series,
        pd.Timestamp,
    )

    if TYPE_CHECKING_INVALID_USAGE:
        s.shift(1, fill_value=1)  # type: ignore[call-overload] # pyright: ignore[reportCallIssue,reportArgumentType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        s.shift(1, fill_value=1.5)  # type: ignore[call-overload] # pyright: ignore[reportCallIssue,reportArgumentType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        s.shift(1, fill_value=np.int64(1))  # type: ignore[call-overload] # pyright: ignore[reportCallIssue,reportArgumentType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        s.shift(1, fill_value="a")  # type: ignore[call-overload] # pyright: ignore[reportCallIssue,reportArgumentType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
