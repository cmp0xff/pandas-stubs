from typing import assert_type

import numpy as np
import pandas as pd

from tests import check


def test_mod_fill_value() -> None:
    s = pd.Series([0, 1, -10])
    s2 = pd.Series([7, -5, 10])

    check(assert_type(s % s2, "pd.Series[int]"), pd.Series, np.integer)
    check(assert_type(s.mod(s2, fill_value=0), "pd.Series[int]"), pd.Series, np.integer)


def test_mod_scalar_fill_value() -> None:
    s = pd.Series([0, 1, -10])

    check(assert_type(s % 2, "pd.Series[int]"), pd.Series, np.integer)
    check(assert_type(s.mod(2, fill_value=0), "pd.Series[int]"), pd.Series, np.integer)
