from __future__ import annotations

from typing import (
    TYPE_CHECKING,
    assert_type,
)

import pandas as pd

from tests import TYPE_CHECKING_INVALID_USAGE


def test_construction_dtype() -> None:
    """Test DatetimeIndex construction with datetime64 dtypes.

    pandas 2.0+ supports resolutions 's', 'ms', 'us', and 'ns' for datetime64 dtypes.
    Unsupported resolutions (Y, M, W, D, h, m, μs, ps, fs, as) raise TypeError.
    See pandas-dev/pandas#20159.
    """
    if TYPE_CHECKING:
        # Supported resolutions for pandas datetime64
        assert_type(pd.DatetimeIndex(["2001-01-01"], dtype="datetime64[s, UTC]"), pd.DatetimeIndex)
        assert_type(pd.DatetimeIndex([], dtype="datetime64[ms, UTC]"), pd.DatetimeIndex)
        assert_type(pd.DatetimeIndex([], dtype="datetime64[us, UTC]"), pd.DatetimeIndex)
        assert_type(pd.DatetimeIndex([], dtype="datetime64[ns, UTC]"), pd.DatetimeIndex)

        # Supported resolutions for numpy datetime64
        assert_type(pd.DatetimeIndex([], dtype="datetime64[s]"), pd.DatetimeIndex)
        assert_type(pd.DatetimeIndex([], dtype="datetime64[ms]"), pd.DatetimeIndex)
        assert_type(pd.DatetimeIndex([], dtype="datetime64[us]"), pd.DatetimeIndex)
        assert_type(pd.DatetimeIndex([], dtype="datetime64[ns]"), pd.DatetimeIndex)
        assert_type(pd.DatetimeIndex([], dtype="M8[s]"), pd.DatetimeIndex)
        assert_type(pd.DatetimeIndex([], dtype="M8[ms]"), pd.DatetimeIndex)
        assert_type(pd.DatetimeIndex([], dtype="M8[us]"), pd.DatetimeIndex)
        assert_type(pd.DatetimeIndex([], dtype="M8[ns]"), pd.DatetimeIndex)
        assert_type(pd.DatetimeIndex([], dtype="<M8[s]"), pd.DatetimeIndex)
        assert_type(pd.DatetimeIndex([], dtype="<M8[ms]"), pd.DatetimeIndex)
        assert_type(pd.DatetimeIndex([], dtype="<M8[us]"), pd.DatetimeIndex)
        assert_type(pd.DatetimeIndex([], dtype="<M8[ns]"), pd.DatetimeIndex)

    if TYPE_CHECKING_INVALID_USAGE:
        # Unsupported resolutions should be rejected by type checkers
        pd.DatetimeIndex([], dtype="datetime64[Y]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.DatetimeIndex([], dtype="datetime64[M]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.DatetimeIndex([], dtype="datetime64[W]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.DatetimeIndex([], dtype="datetime64[D]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.DatetimeIndex([], dtype="datetime64[h]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.DatetimeIndex([], dtype="datetime64[m]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.DatetimeIndex([], dtype="datetime64[μs]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.DatetimeIndex([], dtype="datetime64[ps]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.DatetimeIndex([], dtype="datetime64[fs]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.DatetimeIndex([], dtype="datetime64[as]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.DatetimeIndex([], dtype="M8[Y]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.DatetimeIndex([], dtype="M8[M]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.DatetimeIndex([], dtype="M8[W]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.DatetimeIndex([], dtype="M8[D]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.DatetimeIndex([], dtype="M8[h]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.DatetimeIndex([], dtype="M8[m]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.DatetimeIndex([], dtype="M8[μs]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.DatetimeIndex([], dtype="M8[ps]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.DatetimeIndex([], dtype="M8[fs]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.DatetimeIndex([], dtype="M8[as]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.DatetimeIndex([], dtype="<M8[Y]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.DatetimeIndex([], dtype="<M8[M]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.DatetimeIndex([], dtype="<M8[W]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.DatetimeIndex([], dtype="<M8[D]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.DatetimeIndex([], dtype="<M8[h]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.DatetimeIndex([], dtype="<M8[m]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.DatetimeIndex([], dtype="<M8[μs]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.DatetimeIndex([], dtype="<M8[ps]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.DatetimeIndex([], dtype="<M8[fs]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
        pd.DatetimeIndex([], dtype="<M8[as]")  # type: ignore[call-overload] # pyright: ignore[reportArgumentType,reportCallIssue]
