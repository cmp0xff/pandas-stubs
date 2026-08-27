from typing import assert_type

import numpy as np  # noqa: F401
import pandas as pd
from pandas.core.arrays.arrow.array import ArrowExtensionArray
from pandas.core.arrays.boolean import BooleanArray  # noqa: F401
from pandas.core.arrays.boolean import BooleanDtype
from pandas.core.arrays.categorical import Categorical  # noqa: F401
from pandas.core.arrays.datetimes import DatetimeArray
from pandas.core.arrays.floating import FloatingArray  # noqa: F401
from pandas.core.arrays.floating import FloatingDtype
from pandas.core.arrays.integer import (
    IntegerArray,
    IntegerDtype,
)
from pandas.core.arrays.interval import IntervalArray
from pandas.core.arrays.numpy_ import NumpyExtensionArray
from pandas.core.arrays.period import PeriodArray
from pandas.core.arrays.string_ import (
    BaseStringArray,
    StringDtype,
)
from pandas.core.arrays.string_ import StringArray  # noqa: F401
from pandas.core.arrays.string_arrow import ArrowStringArray  # noqa: F401
from pandas.core.arrays.timedeltas import TimedeltaArray


def test_constructor_backing_array() -> None:
    numpy_index = assert_type(pd.Index([1, 2]), "pd.Index[int, NumpyExtensionArray]")
    assert_type(numpy_index.array, NumpyExtensionArray)
    assert_type(numpy_index.dtype, "np.dtype[np.generic]")

    nullable_index = assert_type(
        pd.Index([1, 2], dtype="Int64"), "pd.Index[int, IntegerArray]"
    )
    assert_type(nullable_index.array, IntegerArray)
    assert_type(nullable_index.dtype, IntegerDtype)

    arrow_index = assert_type(
        pd.Index([1, 2], dtype="int64[pyarrow]"),
        "pd.Index[int, ArrowExtensionArray]",
    )
    assert_type(arrow_index.array, ArrowExtensionArray)
    assert_type(arrow_index.dtype, pd.ArrowDtype)


def test_astype_backing_array() -> None:
    index = pd.Index([0, 1])

    nullable_bool = assert_type(index.astype("boolean"), "pd.Index[bool, BooleanArray]")
    assert_type(nullable_bool.dtype, BooleanDtype)

    nullable_float = assert_type(
        index.astype("Float64"), "pd.Index[float, FloatingArray]"
    )
    assert_type(nullable_float.dtype, FloatingDtype)

    arrow_float = assert_type(
        index.astype("float64[pyarrow]"), "pd.Index[float, ArrowExtensionArray]"
    )
    assert_type(arrow_float.dtype, pd.ArrowDtype)

    python_string = assert_type(
        index.astype("string[python]"), "pd.Index[str, StringArray]"
    )
    assert_type(python_string.dtype, StringDtype)

    arrow_string = assert_type(
        index.astype("string[pyarrow]"), "pd.Index[str, ArrowStringArray]"
    )
    assert_type(arrow_string.dtype, StringDtype)


def test_storage_propagation() -> None:
    nullable = pd.Index([1, 2], dtype="Int64")
    assert_type(nullable[:1], "pd.Index[int, IntegerArray]")
    assert_type(nullable.diff(), "pd.Index[int, IntegerArray]")
    assert_type(nullable.to_series(), "pd.Series[int, IntegerArray]")

    numpy_index = pd.Index([1, 2])
    assert_type(numpy_index.diff(), "pd.Index[float, NumpyExtensionArray]")
    assert_type(numpy_index.to_series(), "pd.Series[int, NumpyExtensionArray]")

    arrow = pd.Index([1, 2], dtype="int64[pyarrow]")
    assert_type(arrow[:1], "pd.Index[int, ArrowExtensionArray]")
    assert_type(arrow.diff(), "pd.Index[int, ArrowExtensionArray]")
    assert_type(arrow.to_series(), "pd.Series[int, ArrowExtensionArray]")


def test_string_and_semantic_indexes() -> None:
    strings = assert_type(pd.Index(["a", "b"]), "pd.Index[str, BaseStringArray]")
    assert_type(strings.array, BaseStringArray)
    assert_type(strings.dtype, StringDtype)

    datetimes = pd.date_range("2020", periods=2)
    assert_type(datetimes.array, DatetimeArray)
    assert_type(datetimes.to_series(), "pd.Series[pd.Timestamp, DatetimeArray]")
    assert_type(datetimes.diff(), pd.TimedeltaIndex)

    timedeltas = pd.timedelta_range("1 day", periods=2)
    assert_type(timedeltas.array, TimedeltaArray)
    assert_type(timedeltas.to_series(), "pd.Series[pd.Timedelta, TimedeltaArray]")

    periods = pd.period_range("2020", periods=2, freq="D")
    assert_type(periods.array, PeriodArray)

    intervals = pd.interval_range(0, 2)
    assert_type(intervals.array, IntervalArray)

    categorical = pd.CategoricalIndex(["a", "b"])
    assert_type(categorical.array, "Categorical[object]")
