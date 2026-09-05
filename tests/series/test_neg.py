from typing import assert_type

import numpy as np
import pandas as pd
import pytest

from tests import check


@pytest.fixture
def left_i() -> pd.Series:
    """Left operand"""
    lo = pd.DataFrame({"a": [1, 2, 3]})["a"]
    return check(assert_type(lo, pd.Series), pd.Series, np.integer)


def test_neg(left_i: pd.Series) -> None:
    # GH 253
    check(assert_type(-left_i, pd.Series), pd.Series, np.integer)
