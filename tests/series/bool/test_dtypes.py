from __future__ import annotations

from typing import (
    TYPE_CHECKING,
    assert_type,
)

import numpy as np
import pandas as pd
import pytest

from tests import check
from tests._typing import BooleanDtypeArg
from tests.dtypes import ASTYPE_BOOL_ARGS


@pytest.mark.parametrize("cast_arg, target_type", ASTYPE_BOOL_ARGS.items(), ids=repr)
def test_astype_bool(cast_arg: BooleanDtypeArg, target_type: type) -> None:
    s = pd.Series([0, 1])
    check(s.astype(cast_arg), pd.Series, target_type)

    if TYPE_CHECKING:
        # python boolean
        assert_type(s.astype(bool), "pd.Series[bool, pd.arrays.NumpyExtensionArray]")
        assert_type(s.astype("bool"), "pd.Series[bool, pd.arrays.NumpyExtensionArray]")
        # pandas boolean
        assert_type(
            s.astype(pd.BooleanDtype()), "pd.Series[bool, pd.arrays.BooleanArray]"
        )
        assert_type(s.astype("boolean"), "pd.Series[bool, pd.arrays.BooleanArray]")
        # numpy boolean type
        assert_type(
            s.astype(np.bool_), "pd.Series[bool, pd.arrays.NumpyExtensionArray]"
        )
        assert_type(s.astype("bool_"), "pd.Series[bool, pd.arrays.NumpyExtensionArray]")
        assert_type(s.astype("?"), "pd.Series[bool, pd.arrays.NumpyExtensionArray]")
        # pyarrow boolean type
        assert_type(
            s.astype("bool[pyarrow]"), "pd.Series[bool, pd.arrays.ArrowExtensionArray]"
        )
        assert_type(
            s.astype("boolean[pyarrow]"),
            "pd.Series[bool, pd.arrays.ArrowExtensionArray]",
        )
