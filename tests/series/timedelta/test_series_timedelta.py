"""Test module for shift operation on Series[Timedelta]."""

from typing import assert_type

import numpy as np
import pandas as pd

from tests import (
    TYPE_CHECKING_INVALID_USAGE,
    check,
)


def test_types_shift_fill_value() -> None:
    """Test fill_value of pd.Series[pd.Timedelta].shift."""
    s = pd.Series(pd.to_timedelta([1, 2, 3], unit="D"))
    td = pd.Timedelta(1, "D")

    check(assert_type(s.shift(1, fill_value=td), pd.Series), pd.Series, pd.Timedelta)
    check(assert_type(s.shift(1, fill_value=pd.NaT), pd.Series), pd.Series)
    check(assert_type(s.shift(1, fill_value=None), pd.Series), pd.Series)
    check(
        assert_type(s.shift(1, fill_value=np.timedelta64(1, "D")), pd.Series),
        pd.Series,
        pd.Timedelta,
    )

    if TYPE_CHECKING_INVALID_USAGE:
        s.shift(1, fill_value=1)  # type: ignore[call-overload] # pyright: ignore[reportCallIssue,reportArgumentType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
