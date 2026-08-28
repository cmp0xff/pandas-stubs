# Private types that are not used in tests

from collections.abc import (
    Callable,
    Hashable,
    Mapping,
    Sequence,
)
from datetime import timedelta
from typing import (
    Any,
    Generic,
    Literal,
    TypeAlias,
    overload,
    type_check_only,
)

import numpy as np
from pandas.core.arrays.arrow.array import ArrowExtensionArray
from pandas.core.arrays.arrow.dtype import ArrowDtype
from pandas.core.arrays.base import ExtensionArray
from pandas.core.arrays.boolean import (
    BooleanArray,
    BooleanDtype,
)
from pandas.core.arrays.categorical import (
    Categorical,
    CategoricalAccessor,
)
from pandas.core.arrays.datetimes import DatetimeArray
from pandas.core.arrays.floating import (
    FloatingArray,
    FloatingDtype,
)
from pandas.core.arrays.integer import (
    IntegerArray,
    IntegerDtype,
)
from pandas.core.arrays.interval import IntervalArray
from pandas.core.arrays.numpy_ import NumpyExtensionArray
from pandas.core.arrays.period import PeriodArray
from pandas.core.arrays.string_ import (
    BaseStringArray,
    StringArray,
    StringDtype,
)
from pandas.core.arrays.string_arrow import ArrowStringArray
from pandas.core.arrays.timedeltas import TimedeltaArray
from pandas.core.base import T_INTERVAL_NP
from pandas.core.groupby.base import ReductionKernelType
from pandas.core.groupby.grouper import Grouper
from pandas.core.indexes.base import Index
from pandas.core.series import Series
from typing_extensions import (
    TypeVar,
    override,
)

from pandas._libs.interval import Interval
from pandas._libs.tslibs.offsets import BaseOffset
from pandas._libs.tslibs.timedeltas import Timedelta
from pandas._libs.tslibs.timestamps import Timestamp
from pandas._typing import (
    S1,
    ArrayT_co,
    DTypeLike,
    DtypeObj,
    GenericT,
    GenericT_co,
    Label,
    Scalar,
    ScalarT,
    SupportsDType,
    np_1darray,
)

from pandas.core.dtypes.dtypes import (
    CategoricalDtype,
    CategoricalValueT,
    CategoricalValueT1,
    DatetimeTZDtype,
    IntervalDtype,
    PeriodDtype,
)

T_co = TypeVar("T_co", covariant=True)
T_contra = TypeVar("T_contra", contravariant=True)

PivotAggCallable: TypeAlias = Callable[[Series], ScalarT]
PivotAggFunc: TypeAlias = (
    PivotAggCallable[ScalarT]
    | np.ufunc
    | ReductionKernelType
    | Literal[
        "ohlc",
        "quantile",
        "bfill",
        "cummax",
        "cummin",
        "cumprod",
        "cumsum",
        "diff",
        "ffill",
        "pct_change",
        "rank",
        "shift",
    ]
)
PivotAggFuncTypes: TypeAlias = (
    PivotAggFunc[ScalarT]
    | Sequence[PivotAggFunc[ScalarT]]
    | Mapping[Any, PivotAggFunc[ScalarT]]
)

PivotTableIndexTypes: TypeAlias = Label | Sequence[Hashable] | Series | Grouper | None
PivotTableColumnsTypes: TypeAlias = Label | Sequence[Hashable] | Series | Grouper | None
PivotTableValuesTypes: TypeAlias = Label | Sequence[Hashable] | None

PeriodAddSub: TypeAlias = (
    Timedelta | timedelta | np.timedelta64 | np.int64 | int | BaseOffset
)

OrderableScalars: TypeAlias = int | float
OrderableTimes: TypeAlias = Timestamp | Timedelta
Orderables: TypeAlias = OrderableScalars | OrderableTimes
OrderableScalarT = TypeVar("OrderableScalarT", bound=OrderableScalars)
OrderableTimesT = TypeVar("OrderableTimesT", bound=OrderableTimes)
OrderableT = TypeVar("OrderableT", bound=Orderables, default=Any)

_CategoricalSeries: TypeAlias = Series[  # pyrefly: ignore[bad-specialization]
    CategoricalValueT,  # pyright: ignore[reportInvalidTypeArguments] # ty: ignore[invalid-type-arguments]
    Categorical[CategoricalValueT],
]

_RetainedArrayT = TypeVar(
    "_RetainedArrayT",
    bound=(
        BooleanArray
        | IntegerArray
        | FloatingArray
        | ArrowExtensionArray
        | BaseStringArray
        | Categorical
        | IntervalArray
    ),
)

@type_check_only
class _SeriesValuesDescriptor:
    @overload
    def __get__(
        self,
        instance: Series[
            Any,
            NumpyExtensionArray | DatetimeArray | TimedeltaArray | PeriodArray,
        ],
        owner: Any,
    ) -> np_1darray: ...
    @overload
    def __get__(
        self,
        instance: Series[CategoricalValueT1, Categorical[CategoricalValueT1]],
        owner: Any,
    ) -> Categorical[CategoricalValueT1]: ...
    @overload
    def __get__(
        self, instance: Series[Any, _RetainedArrayT], owner: Any
    ) -> _RetainedArrayT: ...
    @overload
    def __get__(
        self, instance: Series, owner: Any
    ) -> np_1darray | ExtensionArray | Categorical: ...

@type_check_only
class _SeriesDtypeDescriptor:
    @overload
    def __get__(
        self, instance: Series[Any, StringArray], owner: Any
    ) -> StringDtype: ...
    @overload
    def __get__(
        self, instance: Series[Any, BaseStringArray[Any]], owner: Any
    ) -> StringDtype: ...
    @overload
    def __get__(
        self, instance: Series[Any, BooleanArray], owner: Any
    ) -> BooleanDtype: ...
    @overload
    def __get__(
        self, instance: Series[Any, IntegerArray], owner: Any
    ) -> IntegerDtype: ...
    @overload
    def __get__(
        self, instance: Series[Any, FloatingArray], owner: Any
    ) -> FloatingDtype: ...
    @overload
    def __get__(
        self, instance: Series[Any, ArrowExtensionArray], owner: Any
    ) -> ArrowDtype: ...
    @overload
    def __get__(
        self, instance: Series[Any, NumpyExtensionArray], owner: Any
    ) -> np.dtype[np.generic]: ...
    @overload
    def __get__(
        self,
        instance: _CategoricalSeries[CategoricalValueT],  # type: ignore[type-var]
        owner: Any,
    ) -> CategoricalDtype[CategoricalValueT]: ...
    @overload
    def __get__(
        self, instance: Series[Any, DatetimeArray], owner: Any
    ) -> np.dtypes.DateTime64DType | DatetimeTZDtype: ...
    @overload
    def __get__(
        self, instance: Series[Any, TimedeltaArray], owner: Any
    ) -> np.dtypes.TimeDelta64DType: ...
    @overload
    def __get__(
        self, instance: Series[Any, PeriodArray], owner: Any
    ) -> PeriodDtype: ...
    @overload
    def __get__(
        self, instance: Series[Any, IntervalArray], owner: Any
    ) -> IntervalDtype: ...
    @overload
    def __get__(self, instance: Series, owner: Any) -> DtypeObj: ...

@type_check_only
class _IndexDtypeDescriptor:
    @overload
    def __get__(
        self, instance: Index[Any, ArrowStringArray], owner: Any
    ) -> StringDtype: ...
    @overload
    def __get__(self, instance: Index[Any, StringArray], owner: Any) -> StringDtype: ...
    @overload
    def __get__(
        self, instance: Index[Any, BaseStringArray[Any]], owner: Any
    ) -> StringDtype: ...
    @overload
    def __get__(
        self, instance: Index[Any, BooleanArray], owner: Any
    ) -> BooleanDtype: ...
    @overload
    def __get__(
        self, instance: Index[Any, IntegerArray], owner: Any
    ) -> IntegerDtype: ...
    @overload
    def __get__(
        self, instance: Index[Any, FloatingArray], owner: Any
    ) -> FloatingDtype: ...
    @overload
    def __get__(
        self, instance: Index[Any, ArrowExtensionArray], owner: Any
    ) -> ArrowDtype: ...
    @overload
    def __get__(
        self, instance: Index[Any, NumpyExtensionArray], owner: Any
    ) -> np.dtype[np.generic]: ...
    @overload
    def __get__(
        self, instance: Index[Any, Categorical[Any]], owner: Any
    ) -> CategoricalDtype[Any]: ...
    @overload
    def __get__(
        self, instance: Index[Any, DatetimeArray], owner: Any
    ) -> np.dtypes.DateTime64DType | DatetimeTZDtype: ...
    @overload
    def __get__(
        self, instance: Index[Any, TimedeltaArray], owner: Any
    ) -> np.dtypes.TimeDelta64DType: ...
    @overload
    def __get__(self, instance: Index[Any, PeriodArray], owner: Any) -> PeriodDtype: ...
    @overload
    def __get__(
        self, instance: Index[Any, IntervalArray], owner: Any
    ) -> IntervalDtype: ...
    @overload
    def __get__(self, instance: Index, owner: Any) -> DtypeObj: ...

@type_check_only
class _CatDescriptor:
    @overload
    def __get__(
        self,
        instance: _CategoricalSeries[CategoricalValueT],  # type: ignore[type-var]
        owner: Any,
    ) -> CategoricalAccessor[CategoricalValueT]: ...
    @overload
    def __get__(self, instance: Series, owner: Any) -> CategoricalAccessor[Any]: ...

@type_check_only
class IndexSubclassBase(Index[S1, ArrayT_co], Generic[S1, ArrayT_co, GenericT_co]):
    @overload
    @override
    def to_numpy(
        self: IndexSubclassBase[Interval],
        dtype: type[T_INTERVAL_NP],
        copy: bool = False,
        na_value: Scalar = ...,
        **kwargs: Any,
    ) -> np_1darray: ...
    @overload
    def to_numpy(
        self,
        dtype: None = None,
        copy: bool = False,
        na_value: Scalar = ...,
        **kwargs: Any,
    ) -> np_1darray[GenericT_co]: ...
    @overload
    def to_numpy(
        self,
        dtype: np.dtype[GenericT] | SupportsDType[GenericT] | type[GenericT],
        copy: bool = False,
        na_value: Scalar = ...,
        **kwargs: Any,
    ) -> np_1darray[GenericT]: ...
    @overload
    def to_numpy(  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        dtype: DTypeLike,
        copy: bool = False,
        na_value: Scalar = ...,
        **kwargs: Any,
    ) -> np_1darray: ...
