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


def test_types_abs(left_i: pd.Series) -> None:
    check(assert_type(left_i.abs(), pd.Series), pd.Series, np.integer)
