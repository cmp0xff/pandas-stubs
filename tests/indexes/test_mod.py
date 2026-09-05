from typing import assert_type

import numpy as np
import pandas as pd
import pytest

from tests import check


@pytest.fixture
def left_i() -> pd.Index:
    """Left operand"""
    lo = pd.MultiIndex.from_arrays([[1, 2, 3]]).levels[0]
    return check(assert_type(lo, pd.Index), pd.Index, np.integer)


def test_mod_py_scalar(left_i: pd.Index) -> None:
    """Test pd.Index[Any] % Python native scalars"""
    # GH 405
    check(assert_type(left_i % 10, pd.Index), pd.Index, np.integer)
    check(assert_type(10 % left_i, pd.Index), pd.Index, np.integer)


def test_mod_pd_index(left_i: pd.Index) -> None:
    """Test pd.Index[Any] % pandas Indexes"""
    i2 = pd.Index([4, 5, 6])

    check(assert_type(left_i % i2, pd.Index), pd.Index, np.integer)
