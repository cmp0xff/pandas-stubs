from __future__ import annotations

from typing import assert_type

import numpy as np  # noqa: F401
import pandas as pd
from pandas.api.extensions import ExtensionArray
from pandas.core.arrays.arrow import ArrowExtensionArray
from pandas.core.arrays.categorical import Categorical  # noqa: F401
from pandas.core.arrays.datetimes import DatetimeArray
from pandas.core.arrays.integer import (
    IntegerArray,
    IntegerDtype,
)
from pandas.core.arrays.numpy_ import NumpyExtensionArray
from pandas.core.base import IndexOpsMixin

from tests._typing import np_1darray


def test_constructor_backing_arrays() -> None:
    numpy_series = assert_type(pd.Series([1, 2]), "pd.Series[int, NumpyExtensionArray]")
    nullable_series = assert_type(
        pd.Series([1, 2], dtype="Int64"), "pd.Series[int, IntegerArray]"
    )
    arrow_series = assert_type(
        pd.Series([1, 2], dtype="int64[pyarrow]"),
        "pd.Series[int, ArrowExtensionArray]",
    )
    categorical_series = assert_type(
        pd.Series([1, 2], dtype="category"), "pd.Series[int, Categorical[int]]"
    )
    datetime_series = assert_type(
        pd.Series([pd.Timestamp("2020-01-01")]),
        "pd.Series[pd.Timestamp, DatetimeArray]",
    )

    assert_type(numpy_series.array, NumpyExtensionArray)
    assert_type(numpy_series.values, np_1darray)
    assert_type(numpy_series.dtype, "np.dtype[np.generic]")
    assert_type(numpy_series.unique(), np_1darray)

    assert_type(nullable_series.array, IntegerArray)
    assert_type(nullable_series.values, IntegerArray)
    assert_type(nullable_series.dtype, IntegerDtype)
    assert_type(nullable_series.unique(), IntegerArray)

    assert_type(arrow_series.array, ArrowExtensionArray)
    assert_type(arrow_series.values, ArrowExtensionArray)
    assert_type(arrow_series.dtype, pd.ArrowDtype)
    assert_type(arrow_series.unique(), ArrowExtensionArray)

    assert_type(categorical_series.array, "Categorical[int]")
    assert_type(categorical_series.values, "Categorical[int]")
    assert_type(categorical_series.dtype, "pd.CategoricalDtype[int]")
    assert_type(categorical_series.unique(), "Categorical[int]")

    assert_type(datetime_series.array, DatetimeArray)
    assert_type(datetime_series.values, np_1darray)
    assert_type(datetime_series.dtype, "np.dtypes.DateTime64DType | pd.DatetimeTZDtype")
    assert_type(datetime_series.unique(), DatetimeArray)


def test_index_ops_mixin_array() -> None:
    def read_array(obj: IndexOpsMixin[int, IntegerArray]) -> IntegerArray:
        return obj.array

    assert_type(read_array(pd.Series([1, 2], dtype="Int64")), IntegerArray)


def test_backing_array_covariance() -> None:
    concrete: pd.Series[int, NumpyExtensionArray] = pd.Series([1, 2])
    unspecified: pd.Series[int] = concrete

    def accept_unspecified(series: pd.Series[int]) -> None:
        assert_type(series.array, ExtensionArray)

    accept_unspecified(unspecified)


def test_storage_preserving_operations() -> None:
    series = pd.Series([1, 2, 3])

    assert_type(series.copy(), "pd.Series[int, NumpyExtensionArray]")
    assert_type(series.head(), "pd.Series[int, NumpyExtensionArray]")
    assert_type(series.tail(), "pd.Series[int, NumpyExtensionArray]")
    assert_type(series.sample(n=1), "pd.Series[int, NumpyExtensionArray]")
    assert_type(series.drop(0), "pd.Series[int, NumpyExtensionArray]")
    assert_type(series.dropna(), "pd.Series[int, NumpyExtensionArray]")
    assert_type(series.drop_duplicates(), "pd.Series[int, NumpyExtensionArray]")
    assert_type(series.sort_index(), "pd.Series[int, NumpyExtensionArray]")
    assert_type(series.sort_values(), "pd.Series[int, NumpyExtensionArray]")
    assert_type(series.take([0]), "pd.Series[int, NumpyExtensionArray]")
    assert_type(series.rename("values"), "pd.Series[int, NumpyExtensionArray]")
    assert_type(series.round(), "pd.Series[int, NumpyExtensionArray]")
    assert_type(series[1:], "pd.Series[int, NumpyExtensionArray]")
    assert_type(series[series > 1], "pd.Series[int, NumpyExtensionArray]")
    assert_type(series.loc[[0]], "pd.Series[int, NumpyExtensionArray]")
    assert_type(series.iloc[:1], "pd.Series[int, NumpyExtensionArray]")

    assert_type(pd.Series([1, 2], dtype="Int64").head(), "pd.Series[int, IntegerArray]")
    assert_type(
        pd.Series([1, 2], dtype="int64[pyarrow]").dropna(),
        "pd.Series[int, ArrowExtensionArray]",
    )
    assert_type(
        pd.Series([1, 2], dtype="category").sort_values(),
        "pd.Series[int, Categorical[int]]",
    )
    assert_type(
        pd.Series([pd.Timestamp("2020-01-01")]).tail(),
        "pd.Series[pd.Timestamp, DatetimeArray]",
    )


def test_storage_unspecified_boundaries() -> None:
    series = pd.Series([1, 2, 3])

    assert_type(pd.concat([series, series]), "pd.Series[int]")
    assert_type(series.groupby([0, 0, 1]).sum(), "pd.Series[int]")
    assert_type(series.map(str), "pd.Series[str]")
    assert_type(series.rolling(2).sum(), pd.Series)
    assert_type(series.set_flags(allows_duplicate_labels=True), "pd.Series[int]")
    assert_type(-series, "pd.Series[int]")
    assert_type(+series, "pd.Series[int]")
    assert_type(series.T, "pd.Series[int]")
    assert_type(series.quantile([0.5]), "pd.Series[float]")
    assert_type(series.clip(), "pd.Series[int]")
    assert_type(series.replace(1, 2), "pd.Series[int]")
    assert_type(series.where(series > 1), "pd.Series[int]")
