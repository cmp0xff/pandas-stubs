from __future__ import annotations

from datetime import datetime
from typing import (
    TYPE_CHECKING,
    assert_type,
)

import pandas as pd
import pytest

from tests import (
    TYPE_CHECKING_INVALID_USAGE,
    check,
)
from tests._typing import TimestampDtypeArg
from tests.dtypes import ASTYPE_TIMESTAMP_ARGS


@pytest.mark.parametrize(
    "cast_arg, target_type", ASTYPE_TIMESTAMP_ARGS.items(), ids=repr
)
def test_astype_timestamp(cast_arg: TimestampDtypeArg, target_type: type) -> None:
    s = pd.Series([1, 2, 3])

    if cast_arg in ("date32[pyarrow]", "date64[pyarrow]"):
        x = pd.Series(pd.date_range("2000-01-01", "2000-02-01"))
        check(x.astype(cast_arg), pd.Series, target_type)
    else:
        check(s.astype(cast_arg), pd.Series, target_type)

    if TYPE_CHECKING:
        # numpy datetime64
        assert_type(s.astype("datetime64[Y]"), "pd.Series[pd.Timestamp]")
        assert_type(s.astype("datetime64[M]"), "pd.Series[pd.Timestamp]")
        assert_type(s.astype("datetime64[W]"), "pd.Series[pd.Timestamp]")
        assert_type(s.astype("datetime64[D]"), "pd.Series[pd.Timestamp]")
        assert_type(s.astype("datetime64[h]"), "pd.Series[pd.Timestamp]")
        assert_type(s.astype("datetime64[m]"), "pd.Series[pd.Timestamp]")
        assert_type(s.astype("datetime64[s]"), "pd.Series[pd.Timestamp]")
        assert_type(s.astype("datetime64[ms]"), "pd.Series[pd.Timestamp]")
        assert_type(s.astype("datetime64[us]"), "pd.Series[pd.Timestamp]")
        assert_type(s.astype("datetime64[μs]"), "pd.Series[pd.Timestamp]")
        assert_type(s.astype("datetime64[ns]"), "pd.Series[pd.Timestamp]")
        assert_type(s.astype("datetime64[ps]"), "pd.Series[pd.Timestamp]")
        assert_type(s.astype("datetime64[fs]"), "pd.Series[pd.Timestamp]")
        assert_type(s.astype("datetime64[as]"), "pd.Series[pd.Timestamp]")
        # numpy datetime64 type codes
        assert_type(s.astype("M8[Y]"), "pd.Series[pd.Timestamp]")
        assert_type(s.astype("M8[M]"), "pd.Series[pd.Timestamp]")
        assert_type(s.astype("M8[W]"), "pd.Series[pd.Timestamp]")
        assert_type(s.astype("M8[D]"), "pd.Series[pd.Timestamp]")
        assert_type(s.astype("M8[h]"), "pd.Series[pd.Timestamp]")
        assert_type(s.astype("M8[m]"), "pd.Series[pd.Timestamp]")
        assert_type(s.astype("M8[s]"), "pd.Series[pd.Timestamp]")
        assert_type(s.astype("M8[ms]"), "pd.Series[pd.Timestamp]")
        assert_type(s.astype("M8[us]"), "pd.Series[pd.Timestamp]")
        assert_type(s.astype("M8[μs]"), "pd.Series[pd.Timestamp]")
        assert_type(s.astype("M8[ns]"), "pd.Series[pd.Timestamp]")
        assert_type(s.astype("M8[ps]"), "pd.Series[pd.Timestamp]")
        assert_type(s.astype("M8[fs]"), "pd.Series[pd.Timestamp]")
        assert_type(s.astype("M8[as]"), "pd.Series[pd.Timestamp]")
        # numpy datetime64 type codes
        assert_type(s.astype("<M8[Y]"), "pd.Series[pd.Timestamp]")
        assert_type(s.astype("<M8[M]"), "pd.Series[pd.Timestamp]")
        assert_type(s.astype("<M8[W]"), "pd.Series[pd.Timestamp]")
        assert_type(s.astype("<M8[D]"), "pd.Series[pd.Timestamp]")
        assert_type(s.astype("<M8[h]"), "pd.Series[pd.Timestamp]")
        assert_type(s.astype("<M8[m]"), "pd.Series[pd.Timestamp]")
        assert_type(s.astype("<M8[s]"), "pd.Series[pd.Timestamp]")
        assert_type(s.astype("<M8[ms]"), "pd.Series[pd.Timestamp]")
        assert_type(s.astype("<M8[us]"), "pd.Series[pd.Timestamp]")
        assert_type(s.astype("<M8[μs]"), "pd.Series[pd.Timestamp]")
        assert_type(s.astype("<M8[ns]"), "pd.Series[pd.Timestamp]")
        assert_type(s.astype("<M8[ps]"), "pd.Series[pd.Timestamp]")
        assert_type(s.astype("<M8[fs]"), "pd.Series[pd.Timestamp]")
        assert_type(s.astype("<M8[as]"), "pd.Series[pd.Timestamp]")
        # pyarrow timestamp
        assert_type(s.astype("timestamp[s][pyarrow]"), "pd.Series[pd.Timestamp]")
        assert_type(s.astype("timestamp[ms][pyarrow]"), "pd.Series[pd.Timestamp]")
        assert_type(s.astype("timestamp[us][pyarrow]"), "pd.Series[pd.Timestamp]")
        assert_type(s.astype("timestamp[ns][pyarrow]"), "pd.Series[pd.Timestamp]")
        # pyarrow date
        assert_type(s.astype("date32[pyarrow]"), "pd.Series[pd.Timestamp]")
        assert_type(s.astype("date64[pyarrow]"), "pd.Series[pd.Timestamp]")


def test_construction_dtype() -> None:
    """Test Series construction with datetime64 dtypes.

    pandas 2.0+ supports resolutions 's', 'ms', 'us', and 'ns' for datetime64 dtypes.
    Unsupported resolutions (Y, M, W, D, h, m, μs, ps, fs, as) raise TypeError.
    See pandas-dev/pandas#20159.
    """
    if TYPE_CHECKING:
        # Supported resolutions for pandas datetime64
        assert_type(
            pd.Series([datetime(2001, 1, 1)], dtype="datetime64[s, UTC]"),
            pd.Series[pd.Timestamp],
        )
        assert_type(
            pd.Series([pd.Timestamp(2001, 1, 1)], dtype="datetime64[ms, UTC]"),
            pd.Series[pd.Timestamp],
        )
        assert_type(
            pd.Series([pd.Timestamp(2001, 1, 1)], dtype="datetime64[us, UTC]"),
            pd.Series[pd.Timestamp],
        )
        assert_type(
            pd.Series([pd.Timestamp(2001, 1, 1)], dtype="datetime64[ns, UTC]"),
            pd.Series[pd.Timestamp],
        )

        # Supported resolutions for numpy datetime64
        assert_type(
            pd.Series([datetime(2001, 1, 1)], dtype="datetime64[s]"),
            pd.Series[pd.Timestamp],
        )
        assert_type(
            pd.Series([datetime(2001, 1, 1)], dtype="datetime64[ms]"),
            pd.Series[pd.Timestamp],
        )
        assert_type(
            pd.Series([datetime(2001, 1, 1)], dtype="datetime64[us]"),
            pd.Series[pd.Timestamp],
        )
        assert_type(
            pd.Series([datetime(2001, 1, 1)], dtype="datetime64[ns]"),
            pd.Series[pd.Timestamp],
        )
        assert_type(
            pd.Series([datetime(2001, 1, 1)], dtype="M8[s]"), pd.Series[pd.Timestamp]
        )
        assert_type(
            pd.Series([datetime(2001, 1, 1)], dtype="M8[ms]"), pd.Series[pd.Timestamp]
        )
        assert_type(
            pd.Series([datetime(2001, 1, 1)], dtype="M8[us]"), pd.Series[pd.Timestamp]
        )
        assert_type(
            pd.Series([datetime(2001, 1, 1)], dtype="M8[ns]"), pd.Series[pd.Timestamp]
        )
        assert_type(
            pd.Series([datetime(2001, 1, 1)], dtype="<M8[s]"), pd.Series[pd.Timestamp]
        )
        assert_type(
            pd.Series([datetime(2001, 1, 1)], dtype="<M8[ms]"), pd.Series[pd.Timestamp]
        )
        assert_type(
            pd.Series([datetime(2001, 1, 1)], dtype="<M8[us]"), pd.Series[pd.Timestamp]
        )
        assert_type(
            pd.Series([datetime(2001, 1, 1)], dtype="<M8[ns]"), pd.Series[pd.Timestamp]
        )

    if TYPE_CHECKING_INVALID_USAGE:
        # Unsupported resolutions should be rejected by type checkers
        pd.Series([], dtype="datetime64[Y]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.Series([], dtype="datetime64[M]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.Series([], dtype="datetime64[W]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.Series([], dtype="datetime64[D]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.Series([], dtype="datetime64[h]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.Series([], dtype="datetime64[m]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.Series([], dtype="datetime64[μs]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.Series([], dtype="datetime64[ps]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.Series([], dtype="datetime64[fs]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.Series([], dtype="datetime64[as]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.Series([], dtype="M8[Y]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.Series([], dtype="M8[M]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.Series([], dtype="M8[W]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.Series([], dtype="M8[D]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.Series([], dtype="M8[h]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.Series([], dtype="M8[m]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.Series([], dtype="M8[μs]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.Series([], dtype="M8[ps]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.Series([], dtype="M8[fs]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.Series([], dtype="M8[as]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.Series([], dtype="<M8[Y]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.Series([], dtype="<M8[M]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.Series([], dtype="<M8[W]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.Series([], dtype="<M8[D]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.Series([], dtype="<M8[h]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.Series([], dtype="<M8[m]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.Series([], dtype="<M8[μs]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.Series([], dtype="<M8[ps]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.Series([], dtype="<M8[fs]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.Series([], dtype="<M8[as]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
