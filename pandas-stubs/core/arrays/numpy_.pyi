import numpy as np
from numpy.lib.mixins import NDArrayOperatorsMixin
from pandas.core.arraylike import OpsMixin
from pandas.core.arrays.base import (
    ExtensionArray,
    ExtensionOpsMixin,
)

from pandas.core.dtypes.dtypes import ExtensionDtype

class NumpyExtensionArray(OpsMixin, ExtensionArray): ...

class PandasDtype(ExtensionDtype):
    @property
    def numpy_dtype(self) -> np.dtype: ...
    @property
    def itemsize(self) -> int: ...

class PandasArray(ExtensionArray, ExtensionOpsMixin, NDArrayOperatorsMixin): ...
