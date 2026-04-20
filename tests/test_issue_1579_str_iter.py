from typing import TYPE_CHECKING

import pandas as pd


def test_str_accessor_not_iterable() -> None:
    s = pd.Series(["a", "b"])
    # This should be a type error now
    if TYPE_CHECKING:
        for _ in s.str:  # type: ignore[attr-defined]
            pass
