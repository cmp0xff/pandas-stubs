from typing import (
    Any,
    overload,
)

from pandas import (
    DataFrame,
    Series,
)
from pandas.core.arrays import ExtensionArray
from typing_extensions import (
    TypeIs,
    TypeVar,
)

from pandas._libs.missing import NAType
from pandas._libs.tslibs import NaTType
from pandas._typing import (
    Scalar,
    ScalarT,
    ScalarT0,
    ShapeT,
    SupportsArray,
    np_1darray_bool,
    np_ndarray_bool,
)

# Bind the input type to preserve mypy's ndarray overload selection with Any.
_ObjectT = TypeVar("_ObjectT", bound=object)

@overload
def isna(obj: DataFrame) -> DataFrame: ...  # type: ignore[overload-overlap] # pyright: ignore[reportOverlappingOverload]
@overload
def isna(obj: Series) -> Series[bool]: ...  # type: ignore[overload-overlap]
@overload
def isna(obj: ExtensionArray | list[ScalarT]) -> np_1darray_bool: ...  # type: ignore[overload-overlap]
@overload
def isna(obj: list[Any]) -> np_ndarray_bool: ...  # type: ignore[overload-overlap]
@overload
def isna(obj: Scalar | NaTType | NAType | None) -> TypeIs[NaTType | NAType | None]: ...
@overload
def isna(obj: SupportsArray[ShapeT]) -> np_ndarray_bool[ShapeT]: ...  # type: ignore[overload-overlap]
@overload
def isna(
    obj: _ObjectT,  # pyright: ignore[reportInvalidTypeVarUse]
) -> bool: ...

isnull = isna

@overload
def notna(obj: DataFrame) -> DataFrame: ...  # type: ignore[overload-overlap] # pyright: ignore[reportOverlappingOverload]
@overload
def notna(obj: Series) -> Series[bool]: ...  # type: ignore[overload-overlap]
@overload
def notna(obj: ExtensionArray | list[ScalarT]) -> np_1darray_bool: ...  # type: ignore[overload-overlap]
@overload
def notna(obj: list[Any]) -> np_ndarray_bool: ...  # type: ignore[overload-overlap]
@overload
def notna(obj: ScalarT0 | NaTType | NAType | None) -> TypeIs[ScalarT0]: ...
@overload
def notna(obj: SupportsArray[ShapeT]) -> np_ndarray_bool[ShapeT]: ...  # type: ignore[overload-overlap]
@overload
def notna(
    obj: _ObjectT,  # pyright: ignore[reportInvalidTypeVarUse]
) -> bool: ...

notnull = notna
