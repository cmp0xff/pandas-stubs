from typing import (
    Any,
    overload,
)

from pandas import (
    DataFrame,
    Series,
)
from pandas._stubs_only import SupportsArray
from typing_extensions import TypeIs

from pandas._libs.missing import NAType
from pandas._libs.tslibs import NaTType
from pandas._typing import (
    Scalar,
    ScalarT,
    ScalarT0,
    ShapeT,
    np_1darray_bool,
    np_ndarray_bool,
)

@overload
def isna(obj: DataFrame) -> DataFrame: ...  # type: ignore[overload-overlap] # pyright: ignore[reportOverlappingOverload]
@overload
def isna(obj: Series) -> Series[bool]: ...  # type: ignore[overload-overlap]
@overload
def isna(obj: list[ScalarT]) -> np_1darray_bool: ...
@overload
def isna(obj: list[Any]) -> np_ndarray_bool: ...
@overload
def isna(obj: Scalar | NaTType | NAType | None) -> TypeIs[NaTType | NAType | None]: ...
@overload
def isna(obj: SupportsArray[ShapeT]) -> np_ndarray_bool[ShapeT]: ...
@overload
def isna(obj: Any) -> TypeIs[NaTType | NAType | None]: ...

isnull = isna

@overload
def notna(obj: DataFrame) -> DataFrame: ...  # type: ignore[overload-overlap] # pyright: ignore[reportOverlappingOverload]
@overload
def notna(obj: Series) -> Series[bool]: ...  # type: ignore[overload-overlap]
@overload
def notna(obj: list[ScalarT]) -> np_1darray_bool: ...
@overload
def notna(obj: list[Any]) -> np_ndarray_bool: ...
@overload
def notna(obj: ScalarT0 | NaTType | NAType | None) -> TypeIs[ScalarT0]: ...
@overload
def notna(obj: SupportsArray[ShapeT]) -> np_ndarray_bool[ShapeT]: ...
@overload
def notna(obj: Any) -> bool: ...

notnull = notna
