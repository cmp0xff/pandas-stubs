from pandas.core.arraylike import OpsMixin

from pandas.core.arrays.base import ExtensionArray


class ArrowExtensionArray(OpsMixin, ExtensionArray): ...
