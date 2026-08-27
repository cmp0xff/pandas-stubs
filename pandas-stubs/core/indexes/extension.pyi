from pandas._stubs_only import IndexSubclassBase

from pandas._typing import (
    S1,
    ArrayT_co,
    GenericT_co,
)

class ExtensionIndex(IndexSubclassBase[S1, GenericT_co, ArrayT_co]): ...
