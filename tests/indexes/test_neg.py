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


def test_neg(left_i: pd.Index) -> None:
    """Test -pd.Index[Any]"""
    # GH 253
    check(assert_type(-left_i, pd.Index), pd.Index, np.integer)
