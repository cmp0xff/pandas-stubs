from typing import assert_type

import pandas as pd

from tests import (
    TYPE_CHECKING_INVALID_USAGE,
    check,
)


def test_divmod() -> None:
    s = pd.Series([0, 1, -10])
    s2 = pd.Series([7, -5, 10])

    check(assert_type(divmod(s, s2), tuple["pd.Series[int]", "pd.Series[int]"]), tuple)


def test_divmod_frame_invalid() -> None:
    """Test that the flex method does not allow passing a frame as other."""
    df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    s = pd.Series([0, 1, -10])

    if TYPE_CHECKING_INVALID_USAGE:
        _0 = s.divmod(df)  # type: ignore[arg-type] # pyright: ignore[reportArgumentType] # pyrefly: ignore[bad-argument-type] # ty: ignore[invalid-argument-type]
