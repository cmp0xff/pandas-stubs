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


def test_divmod_py_scalar(left_i: pd.Index) -> None:
    """Test pd.Index[Any] divmod Python native scalars"""
    # GH 405
    check(assert_type(divmod(left_i, 10), tuple[pd.Index, pd.Index]), tuple)
    check(assert_type(divmod(10, left_i), tuple[pd.Index, pd.Index]), tuple)


def test_divmod_pd_index(left_i: pd.Index) -> None:
    """Test pd.Index[Any] divmod pandas Indexes"""
    i2 = pd.Index([4, 5, 6])

    check(assert_type(divmod(left_i, i2), tuple[pd.Index, pd.Index]), tuple)
