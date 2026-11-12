from typing import Self

import numpy as np
from pandas.core.arraylike import OpsMixin
from pandas.core.arrays._mixins import NDArrayBackedExtensionArray

from pandas._typing import (
    np_1darray,
    np_ndarray,
)

class NumpyExtensionArray(OpsMixin, NDArrayBackedExtensionArray):
    def __new__(cls, values: np_ndarray | Self, copy: bool = False) -> Self: ...
    def __array__(
        self, dtype: np.dtype | None = None, copy: bool | None = None
    ) -> np_1darray: ...
