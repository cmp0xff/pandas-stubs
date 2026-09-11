import datetime as dt
from typing import assert_type

import numpy as np
import pandas as pd
from pandas.api.typing import NaTType

from tests import (
    TYPE_CHECKING_INVALID_USAGE,
    check,
)

from pandas.tseries.offsets import (
    FY5253,
    BusinessDay,
    BusinessHour,
    CustomBusinessMonthEnd,
    DateOffset,
    Day,
    Easter,
    FY5253Quarter,
    HalfYearEnd,
    Hour,
    MonthEnd,
    QuarterEnd,
    SemiMonthEnd,
    Week,
    WeekOfMonth,
    YearEnd,
)


def test_calendar_python_scalars() -> None:
    """Python dates become Timestamp; durations follow the offset family."""
    check(assert_type(MonthEnd() + dt.date(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.date(2026, 1, 1) + MonthEnd(), pd.Timestamp), pd.Timestamp)
    check(
        assert_type(MonthEnd().__add__(dt.date(2026, 1, 1)), pd.Timestamp), pd.Timestamp
    )
    check(
        assert_type(MonthEnd().__radd__(dt.date(2026, 1, 1)), pd.Timestamp),
        pd.Timestamp,
    )
    check(assert_type(MonthEnd() + dt.datetime(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.datetime(2026, 1, 1) + MonthEnd(), pd.Timestamp), pd.Timestamp)
    check(
        assert_type(MonthEnd().__add__(dt.datetime(2026, 1, 1)), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(MonthEnd().__radd__(dt.datetime(2026, 1, 1)), pd.Timestamp),
        pd.Timestamp,
    )
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = MonthEnd() + dt.timedelta(hours=2)  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _1 = dt.timedelta(hours=2) + MonthEnd()  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _2 = MonthEnd().__add__(dt.timedelta(hours=2))  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _3 = MonthEnd().__radd__(dt.timedelta(hours=2))  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]


def test_week_durations_python() -> None:
    """Python durations follow the concrete offset result family."""
    check(assert_type(Week() + dt.timedelta(hours=1), dt.timedelta), dt.timedelta)
    check(assert_type(dt.timedelta(hours=1) + Week(), dt.timedelta), dt.timedelta)
    check(
        assert_type(Week().__add__(dt.timedelta(hours=1)), dt.timedelta), dt.timedelta
    )
    check(
        assert_type(Week().__radd__(dt.timedelta(hours=1)), dt.timedelta), dt.timedelta
    )


def test_calendar_numpy_scalars() -> None:
    """NumPy temporal scalars use the supported scalar results."""
    check(
        assert_type(MonthEnd() + np.datetime64("2026-01-01"), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(np.datetime64("2026-01-01") + MonthEnd(), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(MonthEnd().__add__(np.datetime64("2026-01-01")), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(MonthEnd().__radd__(np.datetime64("2026-01-01")), pd.Timestamp),
        pd.Timestamp,
    )
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = MonthEnd().__add__(np.timedelta64(2, "h"))  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = MonthEnd().__radd__(np.timedelta64(2, "h"))  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]


def test_week_durations_numpy() -> None:
    """Numpy durations follow the concrete offset result family."""
    check(assert_type(Week() + np.timedelta64(1, "h"), dt.timedelta), dt.timedelta)
    check(assert_type(np.timedelta64(1, "h") + Week(), dt.timedelta), dt.timedelta)
    check(
        assert_type(Week().__add__(np.timedelta64(1, "h")), dt.timedelta), dt.timedelta
    )
    check(
        assert_type(Week().__radd__(np.timedelta64(1, "h")), dt.timedelta), dt.timedelta
    )


def test_calendar_pandas_scalars() -> None:
    """Timestamp and NaT retain pandas scalar results."""
    check(
        assert_type(MonthEnd() + pd.Timestamp("2026-01-01"), pd.Timestamp), pd.Timestamp
    )
    check(
        assert_type(pd.Timestamp("2026-01-01") + MonthEnd(), pd.Timestamp), pd.Timestamp
    )
    check(
        assert_type(MonthEnd().__add__(pd.Timestamp("2026-01-01")), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(MonthEnd().__radd__(pd.Timestamp("2026-01-01")), pd.Timestamp),
        pd.Timestamp,
    )
    check(assert_type(MonthEnd() + pd.NaT, NaTType), NaTType)
    check(assert_type(pd.NaT + MonthEnd(), NaTType), NaTType)
    check(assert_type(MonthEnd().__add__(pd.NaT), NaTType), NaTType)
    check(assert_type(MonthEnd().__radd__(pd.NaT), NaTType), NaTType)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = MonthEnd() + pd.Timedelta("2h")  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _1 = pd.Timedelta("2h") + MonthEnd()  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _2 = MonthEnd().__add__(pd.Timedelta("2h"))  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _3 = MonthEnd().__radd__(pd.Timedelta("2h"))  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]


def test_dateoffset_scalar() -> None:
    """Calendar implementation families return Timestamp and propagate NaT."""
    check(
        assert_type(DateOffset() + pd.Timestamp("2026-01-01"), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(pd.Timestamp("2026-01-01") + DateOffset(), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(DateOffset().__add__(pd.Timestamp("2026-01-01")), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(DateOffset().__radd__(pd.Timestamp("2026-01-01")), pd.Timestamp),
        pd.Timestamp,
    )
    check(assert_type(DateOffset() + pd.NaT, NaTType), NaTType)
    check(assert_type(pd.NaT + DateOffset(), NaTType), NaTType)
    check(assert_type(DateOffset().__add__(pd.NaT), NaTType), NaTType)
    check(assert_type(DateOffset().__radd__(pd.NaT), NaTType), NaTType)


def test_businesshour_scalar() -> None:
    """Calendar implementation families return Timestamp and propagate NaT."""
    check(
        assert_type(BusinessHour() + pd.Timestamp("2026-01-01"), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(pd.Timestamp("2026-01-01") + BusinessHour(), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(BusinessHour().__add__(pd.Timestamp("2026-01-01")), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(BusinessHour().__radd__(pd.Timestamp("2026-01-01")), pd.Timestamp),
        pd.Timestamp,
    )
    check(assert_type(BusinessHour() + pd.NaT, NaTType), NaTType)
    check(assert_type(pd.NaT + BusinessHour(), NaTType), NaTType)
    check(assert_type(BusinessHour().__add__(pd.NaT), NaTType), NaTType)
    check(assert_type(BusinessHour().__radd__(pd.NaT), NaTType), NaTType)


def test_weekofmonth_scalar() -> None:
    """Calendar implementation families return Timestamp and propagate NaT."""
    check(
        assert_type(WeekOfMonth() + pd.Timestamp("2026-01-01"), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(pd.Timestamp("2026-01-01") + WeekOfMonth(), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(WeekOfMonth().__add__(pd.Timestamp("2026-01-01")), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(WeekOfMonth().__radd__(pd.Timestamp("2026-01-01")), pd.Timestamp),
        pd.Timestamp,
    )
    check(assert_type(WeekOfMonth() + pd.NaT, NaTType), NaTType)
    check(assert_type(pd.NaT + WeekOfMonth(), NaTType), NaTType)
    check(assert_type(WeekOfMonth().__add__(pd.NaT), NaTType), NaTType)
    check(assert_type(WeekOfMonth().__radd__(pd.NaT), NaTType), NaTType)


def test_yearend_scalar() -> None:
    """Calendar implementation families return Timestamp and propagate NaT."""
    check(
        assert_type(YearEnd() + pd.Timestamp("2026-01-01"), pd.Timestamp), pd.Timestamp
    )
    check(
        assert_type(pd.Timestamp("2026-01-01") + YearEnd(), pd.Timestamp), pd.Timestamp
    )
    check(
        assert_type(YearEnd().__add__(pd.Timestamp("2026-01-01")), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(YearEnd().__radd__(pd.Timestamp("2026-01-01")), pd.Timestamp),
        pd.Timestamp,
    )
    check(assert_type(YearEnd() + pd.NaT, NaTType), NaTType)
    check(assert_type(pd.NaT + YearEnd(), NaTType), NaTType)
    check(assert_type(YearEnd().__add__(pd.NaT), NaTType), NaTType)
    check(assert_type(YearEnd().__radd__(pd.NaT), NaTType), NaTType)


def test_quarterend_scalar() -> None:
    """Calendar implementation families return Timestamp and propagate NaT."""
    check(
        assert_type(QuarterEnd() + pd.Timestamp("2026-01-01"), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(pd.Timestamp("2026-01-01") + QuarterEnd(), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(QuarterEnd().__add__(pd.Timestamp("2026-01-01")), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(QuarterEnd().__radd__(pd.Timestamp("2026-01-01")), pd.Timestamp),
        pd.Timestamp,
    )
    check(assert_type(QuarterEnd() + pd.NaT, NaTType), NaTType)
    check(assert_type(pd.NaT + QuarterEnd(), NaTType), NaTType)
    check(assert_type(QuarterEnd().__add__(pd.NaT), NaTType), NaTType)
    check(assert_type(QuarterEnd().__radd__(pd.NaT), NaTType), NaTType)


def test_halfyearend_scalar() -> None:
    """Calendar implementation families return Timestamp and propagate NaT."""
    check(
        assert_type(HalfYearEnd() + pd.Timestamp("2026-01-01"), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(pd.Timestamp("2026-01-01") + HalfYearEnd(), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(HalfYearEnd().__add__(pd.Timestamp("2026-01-01")), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(HalfYearEnd().__radd__(pd.Timestamp("2026-01-01")), pd.Timestamp),
        pd.Timestamp,
    )
    check(assert_type(HalfYearEnd() + pd.NaT, NaTType), NaTType)
    check(assert_type(pd.NaT + HalfYearEnd(), NaTType), NaTType)
    check(assert_type(HalfYearEnd().__add__(pd.NaT), NaTType), NaTType)
    check(assert_type(HalfYearEnd().__radd__(pd.NaT), NaTType), NaTType)


def test_monthend_scalar() -> None:
    """Calendar implementation families return Timestamp and propagate NaT."""
    check(
        assert_type(MonthEnd() + pd.Timestamp("2026-01-01"), pd.Timestamp), pd.Timestamp
    )
    check(
        assert_type(pd.Timestamp("2026-01-01") + MonthEnd(), pd.Timestamp), pd.Timestamp
    )
    check(
        assert_type(MonthEnd().__add__(pd.Timestamp("2026-01-01")), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(MonthEnd().__radd__(pd.Timestamp("2026-01-01")), pd.Timestamp),
        pd.Timestamp,
    )
    check(assert_type(MonthEnd() + pd.NaT, NaTType), NaTType)
    check(assert_type(pd.NaT + MonthEnd(), NaTType), NaTType)
    check(assert_type(MonthEnd().__add__(pd.NaT), NaTType), NaTType)
    check(assert_type(MonthEnd().__radd__(pd.NaT), NaTType), NaTType)


def test_semimonthend_scalar() -> None:
    """Calendar implementation families return Timestamp and propagate NaT."""
    check(
        assert_type(SemiMonthEnd() + pd.Timestamp("2026-01-01"), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(pd.Timestamp("2026-01-01") + SemiMonthEnd(), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(SemiMonthEnd().__add__(pd.Timestamp("2026-01-01")), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(SemiMonthEnd().__radd__(pd.Timestamp("2026-01-01")), pd.Timestamp),
        pd.Timestamp,
    )
    check(assert_type(SemiMonthEnd() + pd.NaT, NaTType), NaTType)
    check(assert_type(pd.NaT + SemiMonthEnd(), NaTType), NaTType)
    check(assert_type(SemiMonthEnd().__add__(pd.NaT), NaTType), NaTType)
    check(assert_type(SemiMonthEnd().__radd__(pd.NaT), NaTType), NaTType)


def test_week_scalar() -> None:
    """Calendar implementation families return Timestamp and propagate NaT."""
    check(assert_type(Week() + pd.Timestamp("2026-01-01"), pd.Timestamp), pd.Timestamp)
    check(assert_type(pd.Timestamp("2026-01-01") + Week(), pd.Timestamp), pd.Timestamp)
    check(
        assert_type(Week().__add__(pd.Timestamp("2026-01-01")), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(Week().__radd__(pd.Timestamp("2026-01-01")), pd.Timestamp),
        pd.Timestamp,
    )
    check(assert_type(Week() + pd.NaT, NaTType), NaTType)
    check(assert_type(pd.NaT + Week(), NaTType), NaTType)
    check(assert_type(Week().__add__(pd.NaT), NaTType), NaTType)
    check(assert_type(Week().__radd__(pd.NaT), NaTType), NaTType)


def test_fy5253_scalar() -> None:
    """Calendar implementation families return Timestamp and propagate NaT."""
    check(
        assert_type(FY5253() + pd.Timestamp("2026-01-01"), pd.Timestamp), pd.Timestamp
    )
    check(
        assert_type(pd.Timestamp("2026-01-01") + FY5253(), pd.Timestamp), pd.Timestamp
    )
    check(
        assert_type(FY5253().__add__(pd.Timestamp("2026-01-01")), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(FY5253().__radd__(pd.Timestamp("2026-01-01")), pd.Timestamp),
        pd.Timestamp,
    )
    check(assert_type(FY5253() + pd.NaT, NaTType), NaTType)
    check(assert_type(pd.NaT + FY5253(), NaTType), NaTType)
    check(assert_type(FY5253().__add__(pd.NaT), NaTType), NaTType)
    check(assert_type(FY5253().__radd__(pd.NaT), NaTType), NaTType)


def test_fy5253quarter_scalar() -> None:
    """Calendar implementation families return Timestamp and propagate NaT."""
    check(
        assert_type(FY5253Quarter() + pd.Timestamp("2026-01-01"), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(pd.Timestamp("2026-01-01") + FY5253Quarter(), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(FY5253Quarter().__add__(pd.Timestamp("2026-01-01")), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(FY5253Quarter().__radd__(pd.Timestamp("2026-01-01")), pd.Timestamp),
        pd.Timestamp,
    )
    check(assert_type(FY5253Quarter() + pd.NaT, NaTType), NaTType)
    check(assert_type(pd.NaT + FY5253Quarter(), NaTType), NaTType)
    check(assert_type(FY5253Quarter().__add__(pd.NaT), NaTType), NaTType)
    check(assert_type(FY5253Quarter().__radd__(pd.NaT), NaTType), NaTType)


def test_easter_scalar() -> None:
    """Calendar implementation families return Timestamp and propagate NaT."""
    check(
        assert_type(Easter() + pd.Timestamp("2026-01-01"), pd.Timestamp), pd.Timestamp
    )
    check(
        assert_type(pd.Timestamp("2026-01-01") + Easter(), pd.Timestamp), pd.Timestamp
    )
    check(
        assert_type(Easter().__add__(pd.Timestamp("2026-01-01")), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(Easter().__radd__(pd.Timestamp("2026-01-01")), pd.Timestamp),
        pd.Timestamp,
    )
    check(assert_type(Easter() + pd.NaT, NaTType), NaTType)
    check(assert_type(pd.NaT + Easter(), NaTType), NaTType)
    check(assert_type(Easter().__add__(pd.NaT), NaTType), NaTType)
    check(assert_type(Easter().__radd__(pd.NaT), NaTType), NaTType)


def test_custombusinessmonthend_scalar() -> None:
    """Calendar implementation families return Timestamp and propagate NaT."""
    check(
        assert_type(
            CustomBusinessMonthEnd() + pd.Timestamp("2026-01-01"), pd.Timestamp
        ),
        pd.Timestamp,
    )
    check(
        assert_type(
            pd.Timestamp("2026-01-01") + CustomBusinessMonthEnd(), pd.Timestamp
        ),
        pd.Timestamp,
    )
    check(
        assert_type(
            CustomBusinessMonthEnd().__add__(pd.Timestamp("2026-01-01")), pd.Timestamp
        ),
        pd.Timestamp,
    )
    check(
        assert_type(
            CustomBusinessMonthEnd().__radd__(pd.Timestamp("2026-01-01")), pd.Timestamp
        ),
        pd.Timestamp,
    )
    check(assert_type(CustomBusinessMonthEnd() + pd.NaT, NaTType), NaTType)
    check(assert_type(pd.NaT + CustomBusinessMonthEnd(), NaTType), NaTType)
    check(assert_type(CustomBusinessMonthEnd().__add__(pd.NaT), NaTType), NaTType)
    check(assert_type(CustomBusinessMonthEnd().__radd__(pd.NaT), NaTType), NaTType)


def test_week_durations_pandas() -> None:
    """Pandas durations follow the concrete offset result family."""
    check(assert_type(Week() + pd.Timedelta("1h"), pd.Timedelta), pd.Timedelta)
    check(assert_type(pd.Timedelta("1h") + Week(), pd.Timedelta), pd.Timedelta)
    check(assert_type(Week().__add__(pd.Timedelta("1h")), pd.Timedelta), pd.Timedelta)
    check(assert_type(Week().__radd__(pd.Timedelta("1h")), pd.Timedelta), pd.Timedelta)


def test_week_offsets() -> None:
    """Week offset combinations require weekday=None."""
    check(assert_type(Week() + Day(), dt.timedelta), dt.timedelta)
    check(assert_type(Day() + Week(), dt.timedelta), dt.timedelta)
    check(assert_type(Week().__add__(Day()), dt.timedelta), dt.timedelta)
    check(assert_type(Week().__radd__(Day()), dt.timedelta), dt.timedelta)
    check(assert_type(Week(1) + Week(2), dt.timedelta), dt.timedelta)
    check(assert_type(Week(2) + Week(1), dt.timedelta), dt.timedelta)
    check(assert_type(Week(1).__add__(Week(2)), dt.timedelta), dt.timedelta)
    check(assert_type(Week(1).__radd__(Week(2)), dt.timedelta), dt.timedelta)
    check(assert_type(Week() + Hour(), pd.Timedelta), pd.Timedelta)
    check(assert_type(Hour() + Week(), pd.Timedelta), pd.Timedelta)
    check(assert_type(Week().__add__(Hour()), pd.Timedelta), pd.Timedelta)
    check(assert_type(Week().__radd__(Hour()), pd.Timedelta), pd.Timedelta)
    check(assert_type(Week() + BusinessDay(), BusinessDay), BusinessDay)
    check(assert_type(BusinessDay() + Week(), BusinessDay), BusinessDay)
    check(assert_type(Week().__add__(BusinessDay()), BusinessDay), BusinessDay)
    check(assert_type(Week().__radd__(BusinessDay()), BusinessDay), BusinessDay)


def test_calendar_numpy_arrays() -> None:
    """Object-array results do not promise shape or dtype preservation."""
    values = np.array([dt.datetime(2026, 1, 1)], dtype=object)
    check(
        assert_type(
            MonthEnd().__add__(values),
            np.ndarray[tuple[int, ...], np.dtype[np.generic]],
        ),
        np.ndarray,
    )
    check(
        assert_type(
            MonthEnd().__radd__(values),
            np.ndarray[tuple[int, ...], np.dtype[np.generic]],
        ),
        np.ndarray,
    )
    empty = np.array([], dtype=object)
    check(
        assert_type(
            MonthEnd().__add__(empty), np.ndarray[tuple[int, ...], np.dtype[np.generic]]
        ),
        np.ndarray,
    )
    check(
        assert_type(
            MonthEnd().__radd__(empty),
            np.ndarray[tuple[int, ...], np.dtype[np.generic]],
        ),
        np.ndarray,
    )


def test_calendar_index() -> None:
    """Containers support expressions through their own dispatch."""
    values = pd.date_range("2026-01-01", periods=2)
    check(assert_type(MonthEnd() + values, pd.DatetimeIndex), pd.DatetimeIndex)
    check(assert_type(values + MonthEnd(), pd.DatetimeIndex), pd.DatetimeIndex)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = MonthEnd().__add__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = MonthEnd().__radd__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]


def test_calendar_series() -> None:
    """Containers support expressions through their own dispatch."""
    values = pd.Series(pd.date_range("2026-01-01", periods=2))
    check(assert_type(MonthEnd() + values, "pd.Series[pd.Timestamp]"), pd.Series)
    check(assert_type(values + MonthEnd(), "pd.Series[pd.Timestamp]"), pd.Series)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = MonthEnd().__add__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = MonthEnd().__radd__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
