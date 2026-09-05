from typing import assert_type

import numpy as np
import pandas as pd

from tests import check


def test_pow_fill_value() -> None:
    s = pd.Series([0, 1, -10])
    s2 = pd.Series([7, -5, 10])

    check(assert_type(s ** s2.abs(), "pd.Series[int]"), pd.Series, np.integer)
    check(
        assert_type(s.pow(s2.abs(), fill_value=0), "pd.Series[int]"),
        pd.Series,
        np.integer,
    )


def test_pow_scalar_fill_value() -> None:
    s = pd.Series([0, 1, -10])

    check(assert_type(s**2, "pd.Series[int]"), pd.Series, np.integer)
    check(assert_type(s**0, "pd.Series[int]"), pd.Series, np.integer)
    # The stubs type `__pow__`/`pow` as returning the same element type as `self`
    # (`int`), while pandas produces `float` for fractional exponents at runtime.
    check(assert_type(s**0.213, "pd.Series[int]"), pd.Series, np.floating)
    check(assert_type(s.pow(0.5), "pd.Series[int]"), pd.Series, np.floating)
