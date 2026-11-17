from __future__ import annotations

from typing import assert_type

import pandas as pd

from tests import check


def test_types_shift_fill_value() -> None:
    """Test fill_value of pd.Series[str].shift."""
    s = pd.Series(["a", "b", "c"])
    check(assert_type(s.shift(1, fill_value="x"), pd.Series), pd.Series, str)
