from typing import assert_type

import pandas as pd


def test_to_datetime_numeric_mixed() -> None:
    # Now allows sequences with mixed numeric and datetime objects
    data: list[pd.Timestamp | int] = [pd.Timestamp("2023-01-01"), 1234567890]
    res = pd.to_datetime(data)
    assert_type(res, pd.DatetimeIndex)


def test_datetime_index_numeric_mixed() -> None:
    # Now allows sequences with mixed numeric and datetime objects
    data: list[pd.Timestamp | int] = [pd.Timestamp("2023-01-01"), 1234567890]
    res = pd.DatetimeIndex(data)
    assert_type(res, pd.DatetimeIndex)
