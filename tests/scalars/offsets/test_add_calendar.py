import datetime as dt
from typing import assert_type

import numpy as np
import pandas as pd
from pandas.api.typing import NaTType
import pytest

from pandas.errors import PerformanceWarning

from tests import (
    TYPE_CHECKING_INVALID_USAGE,
    check,
)

from pandas.tseries.offsets import (
    FY5253,
    BHalfYearBegin,
    BHalfYearEnd,
    BQuarterBegin,
    BQuarterEnd,
    BusinessDay,
    BusinessHour,
    BusinessMonthBegin,
    BusinessMonthEnd,
    BYearBegin,
    BYearEnd,
    CustomBusinessHour,
    CustomBusinessMonthBegin,
    CustomBusinessMonthEnd,
    DateOffset,
    Day,
    Easter,
    FY5253Quarter,
    HalfYearBegin,
    HalfYearEnd,
    Hour,
    LastWeekOfMonth,
    MonthBegin,
    MonthEnd,
    QuarterBegin,
    QuarterEnd,
    SemiMonthBegin,
    SemiMonthEnd,
    Week,
    WeekOfMonth,
    YearBegin,
    YearEnd,
)


def test_dateoffset_python_scalars() -> None:
    """DateOffset handles python scalars in both directions."""
    check(assert_type(DateOffset() + dt.date(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.date(2026, 1, 1) + DateOffset(), pd.Timestamp), pd.Timestamp)
    check(
        assert_type(DateOffset() + dt.datetime(2026, 1, 1), pd.Timestamp), pd.Timestamp
    )
    check(
        assert_type(dt.datetime(2026, 1, 1) + DateOffset(), pd.Timestamp), pd.Timestamp
    )
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = DateOffset() + dt.timedelta(hours=2)  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _1 = dt.timedelta(hours=2) + DateOffset()  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]


def test_businesshour_python_scalars() -> None:
    """BusinessHour handles python scalars in both directions."""
    check(assert_type(BusinessHour() + dt.date(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.date(2026, 1, 1) + BusinessHour(), pd.Timestamp), pd.Timestamp)
    check(
        assert_type(BusinessHour() + dt.datetime(2026, 1, 1), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(dt.datetime(2026, 1, 1) + BusinessHour(), pd.Timestamp),
        pd.Timestamp,
    )
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = BusinessHour() + dt.timedelta(hours=2)  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _1 = dt.timedelta(hours=2) + BusinessHour()  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]


def test_weekofmonth_python_scalars() -> None:
    """WeekOfMonth handles python scalars in both directions."""
    check(assert_type(WeekOfMonth() + dt.date(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.date(2026, 1, 1) + WeekOfMonth(), pd.Timestamp), pd.Timestamp)
    check(
        assert_type(WeekOfMonth() + dt.datetime(2026, 1, 1), pd.Timestamp), pd.Timestamp
    )
    check(
        assert_type(dt.datetime(2026, 1, 1) + WeekOfMonth(), pd.Timestamp), pd.Timestamp
    )
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = WeekOfMonth() + dt.timedelta(hours=2)  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _1 = dt.timedelta(hours=2) + WeekOfMonth()  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]


def test_yearend_python_scalars() -> None:
    """YearEnd handles python scalars in both directions."""
    check(assert_type(YearEnd() + dt.date(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.date(2026, 1, 1) + YearEnd(), pd.Timestamp), pd.Timestamp)
    check(assert_type(YearEnd() + dt.datetime(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.datetime(2026, 1, 1) + YearEnd(), pd.Timestamp), pd.Timestamp)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = YearEnd() + dt.timedelta(hours=2)  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _1 = dt.timedelta(hours=2) + YearEnd()  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]


def test_quarterend_python_scalars() -> None:
    """QuarterEnd handles python scalars in both directions."""
    check(assert_type(QuarterEnd() + dt.date(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.date(2026, 1, 1) + QuarterEnd(), pd.Timestamp), pd.Timestamp)
    check(
        assert_type(QuarterEnd() + dt.datetime(2026, 1, 1), pd.Timestamp), pd.Timestamp
    )
    check(
        assert_type(dt.datetime(2026, 1, 1) + QuarterEnd(), pd.Timestamp), pd.Timestamp
    )
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = QuarterEnd() + dt.timedelta(hours=2)  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _1 = dt.timedelta(hours=2) + QuarterEnd()  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]


def test_halfyearend_python_scalars() -> None:
    """HalfYearEnd handles python scalars in both directions."""
    check(assert_type(HalfYearEnd() + dt.date(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.date(2026, 1, 1) + HalfYearEnd(), pd.Timestamp), pd.Timestamp)
    check(
        assert_type(HalfYearEnd() + dt.datetime(2026, 1, 1), pd.Timestamp), pd.Timestamp
    )
    check(
        assert_type(dt.datetime(2026, 1, 1) + HalfYearEnd(), pd.Timestamp), pd.Timestamp
    )
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = HalfYearEnd() + dt.timedelta(hours=2)  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _1 = dt.timedelta(hours=2) + HalfYearEnd()  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]


def test_monthend_python_scalars() -> None:
    """MonthEnd handles python scalars in both directions."""
    check(assert_type(MonthEnd() + dt.date(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.date(2026, 1, 1) + MonthEnd(), pd.Timestamp), pd.Timestamp)
    check(assert_type(MonthEnd() + dt.datetime(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.datetime(2026, 1, 1) + MonthEnd(), pd.Timestamp), pd.Timestamp)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = MonthEnd() + dt.timedelta(hours=2)  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _1 = dt.timedelta(hours=2) + MonthEnd()  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]


def test_semimonthend_python_scalars() -> None:
    """SemiMonthEnd handles python scalars in both directions."""
    check(assert_type(SemiMonthEnd() + dt.date(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.date(2026, 1, 1) + SemiMonthEnd(), pd.Timestamp), pd.Timestamp)
    check(
        assert_type(SemiMonthEnd() + dt.datetime(2026, 1, 1), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(dt.datetime(2026, 1, 1) + SemiMonthEnd(), pd.Timestamp),
        pd.Timestamp,
    )
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = SemiMonthEnd() + dt.timedelta(hours=2)  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _1 = dt.timedelta(hours=2) + SemiMonthEnd()  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]


def test_week_python_scalars() -> None:
    """Week handles python scalars in both directions."""
    check(assert_type(Week() + dt.date(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.date(2026, 1, 1) + Week(), pd.Timestamp), pd.Timestamp)
    check(assert_type(Week() + dt.datetime(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.datetime(2026, 1, 1) + Week(), pd.Timestamp), pd.Timestamp)


def test_fy5253_python_scalars() -> None:
    """FY5253 handles python scalars in both directions."""
    check(assert_type(FY5253() + dt.date(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.date(2026, 1, 1) + FY5253(), pd.Timestamp), pd.Timestamp)
    check(assert_type(FY5253() + dt.datetime(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.datetime(2026, 1, 1) + FY5253(), pd.Timestamp), pd.Timestamp)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = FY5253() + dt.timedelta(hours=2)  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _1 = dt.timedelta(hours=2) + FY5253()  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]


def test_fy5253quarter_python_scalars() -> None:
    """FY5253Quarter handles python scalars in both directions."""
    check(
        assert_type(FY5253Quarter() + dt.date(2026, 1, 1), pd.Timestamp), pd.Timestamp
    )
    check(
        assert_type(dt.date(2026, 1, 1) + FY5253Quarter(), pd.Timestamp), pd.Timestamp
    )
    check(
        assert_type(FY5253Quarter() + dt.datetime(2026, 1, 1), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(dt.datetime(2026, 1, 1) + FY5253Quarter(), pd.Timestamp),
        pd.Timestamp,
    )
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = FY5253Quarter() + dt.timedelta(hours=2)  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _1 = dt.timedelta(hours=2) + FY5253Quarter()  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]


def test_easter_python_scalars() -> None:
    """Easter handles python scalars in both directions."""
    check(assert_type(Easter() + dt.date(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.date(2026, 1, 1) + Easter(), pd.Timestamp), pd.Timestamp)
    check(assert_type(Easter() + dt.datetime(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.datetime(2026, 1, 1) + Easter(), pd.Timestamp), pd.Timestamp)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = Easter() + dt.timedelta(hours=2)  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _1 = dt.timedelta(hours=2) + Easter()  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]


def test_custombusinessmonthend_python_scalars() -> None:
    """CustomBusinessMonthEnd handles python scalars in both directions."""
    check(
        assert_type(CustomBusinessMonthEnd() + dt.date(2026, 1, 1), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(dt.date(2026, 1, 1) + CustomBusinessMonthEnd(), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(CustomBusinessMonthEnd() + dt.datetime(2026, 1, 1), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(dt.datetime(2026, 1, 1) + CustomBusinessMonthEnd(), pd.Timestamp),
        pd.Timestamp,
    )
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = CustomBusinessMonthEnd() + dt.timedelta(hours=2)  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _1 = dt.timedelta(hours=2) + CustomBusinessMonthEnd()  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]


def test_week_durations_python() -> None:
    """Python durations follow the concrete offset result family."""
    check(
        assert_type(Week(weekday=None) + dt.timedelta(hours=1), dt.timedelta),
        dt.timedelta,
    )
    check(
        assert_type(dt.timedelta(hours=1) + Week(weekday=None), dt.timedelta),
        dt.timedelta,
    )


def test_custombusinesshour_date() -> None:
    """CustomBusinessHour inherits calendar date addition."""
    check(
        assert_type(CustomBusinessHour() + dt.date(2026, 1, 1), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(dt.date(2026, 1, 1) + CustomBusinessHour(), pd.Timestamp),
        pd.Timestamp,
    )


def test_lastweekofmonth_date() -> None:
    """LastWeekOfMonth inherits calendar date addition."""
    check(
        assert_type(LastWeekOfMonth() + dt.date(2026, 1, 1), pd.Timestamp), pd.Timestamp
    )
    check(
        assert_type(dt.date(2026, 1, 1) + LastWeekOfMonth(), pd.Timestamp), pd.Timestamp
    )


def test_yearbegin_date() -> None:
    """YearBegin inherits calendar date addition."""
    check(assert_type(YearBegin() + dt.date(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.date(2026, 1, 1) + YearBegin(), pd.Timestamp), pd.Timestamp)


def test_byearbegin_date() -> None:
    """BYearBegin inherits calendar date addition."""
    check(assert_type(BYearBegin() + dt.date(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.date(2026, 1, 1) + BYearBegin(), pd.Timestamp), pd.Timestamp)


def test_byearend_date() -> None:
    """BYearEnd inherits calendar date addition."""
    check(assert_type(BYearEnd() + dt.date(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.date(2026, 1, 1) + BYearEnd(), pd.Timestamp), pd.Timestamp)


def test_quarterbegin_date() -> None:
    """QuarterBegin inherits calendar date addition."""
    check(assert_type(QuarterBegin() + dt.date(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.date(2026, 1, 1) + QuarterBegin(), pd.Timestamp), pd.Timestamp)


def test_bquarterbegin_date() -> None:
    """BQuarterBegin inherits calendar date addition."""
    check(
        assert_type(BQuarterBegin() + dt.date(2026, 1, 1), pd.Timestamp), pd.Timestamp
    )
    check(
        assert_type(dt.date(2026, 1, 1) + BQuarterBegin(), pd.Timestamp), pd.Timestamp
    )


def test_bquarterend_date() -> None:
    """BQuarterEnd inherits calendar date addition."""
    check(assert_type(BQuarterEnd() + dt.date(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.date(2026, 1, 1) + BQuarterEnd(), pd.Timestamp), pd.Timestamp)


def test_halfyearbegin_date() -> None:
    """HalfYearBegin inherits calendar date addition."""
    check(
        assert_type(HalfYearBegin() + dt.date(2026, 1, 1), pd.Timestamp), pd.Timestamp
    )
    check(
        assert_type(dt.date(2026, 1, 1) + HalfYearBegin(), pd.Timestamp), pd.Timestamp
    )


def test_bhalfyearbegin_date() -> None:
    """BHalfYearBegin inherits calendar date addition."""
    check(
        assert_type(BHalfYearBegin() + dt.date(2026, 1, 1), pd.Timestamp), pd.Timestamp
    )
    check(
        assert_type(dt.date(2026, 1, 1) + BHalfYearBegin(), pd.Timestamp), pd.Timestamp
    )


def test_bhalfyearend_date() -> None:
    """BHalfYearEnd inherits calendar date addition."""
    check(assert_type(BHalfYearEnd() + dt.date(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.date(2026, 1, 1) + BHalfYearEnd(), pd.Timestamp), pd.Timestamp)


def test_monthbegin_date() -> None:
    """MonthBegin inherits calendar date addition."""
    check(assert_type(MonthBegin() + dt.date(2026, 1, 1), pd.Timestamp), pd.Timestamp)
    check(assert_type(dt.date(2026, 1, 1) + MonthBegin(), pd.Timestamp), pd.Timestamp)


def test_businessmonthbegin_date() -> None:
    """BusinessMonthBegin inherits calendar date addition."""
    check(
        assert_type(BusinessMonthBegin() + dt.date(2026, 1, 1), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(dt.date(2026, 1, 1) + BusinessMonthBegin(), pd.Timestamp),
        pd.Timestamp,
    )


def test_businessmonthend_date() -> None:
    """BusinessMonthEnd inherits calendar date addition."""
    check(
        assert_type(BusinessMonthEnd() + dt.date(2026, 1, 1), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(dt.date(2026, 1, 1) + BusinessMonthEnd(), pd.Timestamp),
        pd.Timestamp,
    )


def test_semimonthbegin_date() -> None:
    """SemiMonthBegin inherits calendar date addition."""
    check(
        assert_type(SemiMonthBegin() + dt.date(2026, 1, 1), pd.Timestamp), pd.Timestamp
    )
    check(
        assert_type(dt.date(2026, 1, 1) + SemiMonthBegin(), pd.Timestamp), pd.Timestamp
    )


def test_custombusinessmonthbegin_date() -> None:
    """CustomBusinessMonthBegin inherits calendar date addition."""
    check(
        assert_type(CustomBusinessMonthBegin() + dt.date(2026, 1, 1), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(dt.date(2026, 1, 1) + CustomBusinessMonthBegin(), pd.Timestamp),
        pd.Timestamp,
    )


def test_dateoffset_numpy_scalars() -> None:
    """DateOffset handles numpy scalars in both directions."""
    check(
        assert_type(DateOffset() + np.datetime64("2026-01-01"), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(np.datetime64("2026-01-01") + DateOffset(), pd.Timestamp),
        pd.Timestamp,
    )
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = DateOffset().__add__(np.timedelta64(2, "h"))  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = DateOffset().__radd__(np.timedelta64(2, "h"))  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]


def test_businesshour_numpy_scalars() -> None:
    """BusinessHour handles numpy scalars in both directions."""
    check(
        assert_type(BusinessHour() + np.datetime64("2026-01-01"), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(np.datetime64("2026-01-01") + BusinessHour(), pd.Timestamp),
        pd.Timestamp,
    )
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = BusinessHour().__add__(np.timedelta64(2, "h"))  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = BusinessHour().__radd__(np.timedelta64(2, "h"))  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]


def test_weekofmonth_numpy_scalars() -> None:
    """WeekOfMonth handles numpy scalars in both directions."""
    check(
        assert_type(WeekOfMonth() + np.datetime64("2026-01-01"), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(np.datetime64("2026-01-01") + WeekOfMonth(), pd.Timestamp),
        pd.Timestamp,
    )
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = WeekOfMonth().__add__(np.timedelta64(2, "h"))  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = WeekOfMonth().__radd__(np.timedelta64(2, "h"))  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]


def test_yearend_numpy_scalars() -> None:
    """YearEnd handles numpy scalars in both directions."""
    check(
        assert_type(YearEnd() + np.datetime64("2026-01-01"), pd.Timestamp), pd.Timestamp
    )
    check(
        assert_type(np.datetime64("2026-01-01") + YearEnd(), pd.Timestamp), pd.Timestamp
    )
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = YearEnd().__add__(np.timedelta64(2, "h"))  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = YearEnd().__radd__(np.timedelta64(2, "h"))  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]


def test_quarterend_numpy_scalars() -> None:
    """QuarterEnd handles numpy scalars in both directions."""
    check(
        assert_type(QuarterEnd() + np.datetime64("2026-01-01"), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(np.datetime64("2026-01-01") + QuarterEnd(), pd.Timestamp),
        pd.Timestamp,
    )
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = QuarterEnd().__add__(np.timedelta64(2, "h"))  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = QuarterEnd().__radd__(np.timedelta64(2, "h"))  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]


def test_halfyearend_numpy_scalars() -> None:
    """HalfYearEnd handles numpy scalars in both directions."""
    check(
        assert_type(HalfYearEnd() + np.datetime64("2026-01-01"), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(np.datetime64("2026-01-01") + HalfYearEnd(), pd.Timestamp),
        pd.Timestamp,
    )
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = HalfYearEnd().__add__(np.timedelta64(2, "h"))  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = HalfYearEnd().__radd__(np.timedelta64(2, "h"))  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]


def test_monthend_numpy_scalars() -> None:
    """MonthEnd handles numpy scalars in both directions."""
    check(
        assert_type(MonthEnd() + np.datetime64("2026-01-01"), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(np.datetime64("2026-01-01") + MonthEnd(), pd.Timestamp),
        pd.Timestamp,
    )
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = MonthEnd().__add__(np.timedelta64(2, "h"))  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = MonthEnd().__radd__(np.timedelta64(2, "h"))  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]


def test_semimonthend_numpy_scalars() -> None:
    """SemiMonthEnd handles numpy scalars in both directions."""
    check(
        assert_type(SemiMonthEnd() + np.datetime64("2026-01-01"), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(np.datetime64("2026-01-01") + SemiMonthEnd(), pd.Timestamp),
        pd.Timestamp,
    )
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = SemiMonthEnd().__add__(np.timedelta64(2, "h"))  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = SemiMonthEnd().__radd__(np.timedelta64(2, "h"))  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]


def test_week_numpy_scalars() -> None:
    """Week handles numpy scalars in both directions."""
    check(assert_type(Week() + np.datetime64("2026-01-01"), pd.Timestamp), pd.Timestamp)
    check(assert_type(np.datetime64("2026-01-01") + Week(), pd.Timestamp), pd.Timestamp)


def test_fy5253_numpy_scalars() -> None:
    """FY5253 handles numpy scalars in both directions."""
    check(
        assert_type(FY5253() + np.datetime64("2026-01-01"), pd.Timestamp), pd.Timestamp
    )
    check(
        assert_type(np.datetime64("2026-01-01") + FY5253(), pd.Timestamp), pd.Timestamp
    )
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = FY5253().__add__(np.timedelta64(2, "h"))  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = FY5253().__radd__(np.timedelta64(2, "h"))  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]


def test_fy5253quarter_numpy_scalars() -> None:
    """FY5253Quarter handles numpy scalars in both directions."""
    check(
        assert_type(FY5253Quarter() + np.datetime64("2026-01-01"), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(np.datetime64("2026-01-01") + FY5253Quarter(), pd.Timestamp),
        pd.Timestamp,
    )
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = FY5253Quarter().__add__(np.timedelta64(2, "h"))  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = FY5253Quarter().__radd__(np.timedelta64(2, "h"))  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]


def test_easter_numpy_scalars() -> None:
    """Easter handles numpy scalars in both directions."""
    check(
        assert_type(Easter() + np.datetime64("2026-01-01"), pd.Timestamp), pd.Timestamp
    )
    check(
        assert_type(np.datetime64("2026-01-01") + Easter(), pd.Timestamp), pd.Timestamp
    )
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = Easter().__add__(np.timedelta64(2, "h"))  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = Easter().__radd__(np.timedelta64(2, "h"))  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]


def test_custombusinessmonthend_numpy_scalars() -> None:
    """CustomBusinessMonthEnd handles numpy scalars in both directions."""
    check(
        assert_type(
            CustomBusinessMonthEnd() + np.datetime64("2026-01-01"), pd.Timestamp
        ),
        pd.Timestamp,
    )
    check(
        assert_type(
            np.datetime64("2026-01-01") + CustomBusinessMonthEnd(), pd.Timestamp
        ),
        pd.Timestamp,
    )
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = CustomBusinessMonthEnd().__add__(np.timedelta64(2, "h"))  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = CustomBusinessMonthEnd().__radd__(np.timedelta64(2, "h"))  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]


def test_week_durations_numpy() -> None:
    """Numpy durations follow the concrete offset result family."""
    check(
        assert_type(Week(weekday=None) + np.timedelta64(1, "h"), dt.timedelta),
        dt.timedelta,
    )
    check(
        assert_type(np.timedelta64(1, "h") + Week(weekday=None), dt.timedelta),
        dt.timedelta,
    )


def test_dateoffset_pandas_scalars() -> None:
    """DateOffset handles pandas scalars in both directions."""
    check(
        assert_type(DateOffset() + pd.Timestamp("2026-01-01"), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(pd.Timestamp("2026-01-01") + DateOffset(), pd.Timestamp),
        pd.Timestamp,
    )
    check(assert_type(DateOffset() + pd.NaT, NaTType), NaTType)
    check(assert_type(pd.NaT + DateOffset(), NaTType), NaTType)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = DateOffset() + pd.Timedelta("2h")  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _1 = pd.Timedelta("2h") + DateOffset()  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]


def test_businesshour_pandas_scalars() -> None:
    """BusinessHour handles pandas scalars in both directions."""
    check(
        assert_type(BusinessHour() + pd.Timestamp("2026-01-01"), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(pd.Timestamp("2026-01-01") + BusinessHour(), pd.Timestamp),
        pd.Timestamp,
    )
    check(assert_type(BusinessHour() + pd.NaT, NaTType), NaTType)
    check(assert_type(pd.NaT + BusinessHour(), NaTType), NaTType)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = BusinessHour() + pd.Timedelta("2h")  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _1 = pd.Timedelta("2h") + BusinessHour()  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]


def test_weekofmonth_pandas_scalars() -> None:
    """WeekOfMonth handles pandas scalars in both directions."""
    check(
        assert_type(WeekOfMonth() + pd.Timestamp("2026-01-01"), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(pd.Timestamp("2026-01-01") + WeekOfMonth(), pd.Timestamp),
        pd.Timestamp,
    )
    check(assert_type(WeekOfMonth() + pd.NaT, NaTType), NaTType)
    check(assert_type(pd.NaT + WeekOfMonth(), NaTType), NaTType)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = WeekOfMonth() + pd.Timedelta("2h")  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _1 = pd.Timedelta("2h") + WeekOfMonth()  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]


def test_yearend_pandas_scalars() -> None:
    """YearEnd handles pandas scalars in both directions."""
    check(
        assert_type(YearEnd() + pd.Timestamp("2026-01-01"), pd.Timestamp), pd.Timestamp
    )
    check(
        assert_type(pd.Timestamp("2026-01-01") + YearEnd(), pd.Timestamp), pd.Timestamp
    )
    check(assert_type(YearEnd() + pd.NaT, NaTType), NaTType)
    check(assert_type(pd.NaT + YearEnd(), NaTType), NaTType)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = YearEnd() + pd.Timedelta("2h")  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _1 = pd.Timedelta("2h") + YearEnd()  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]


def test_quarterend_pandas_scalars() -> None:
    """QuarterEnd handles pandas scalars in both directions."""
    check(
        assert_type(QuarterEnd() + pd.Timestamp("2026-01-01"), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(pd.Timestamp("2026-01-01") + QuarterEnd(), pd.Timestamp),
        pd.Timestamp,
    )
    check(assert_type(QuarterEnd() + pd.NaT, NaTType), NaTType)
    check(assert_type(pd.NaT + QuarterEnd(), NaTType), NaTType)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = QuarterEnd() + pd.Timedelta("2h")  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _1 = pd.Timedelta("2h") + QuarterEnd()  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]


def test_halfyearend_pandas_scalars() -> None:
    """HalfYearEnd handles pandas scalars in both directions."""
    check(
        assert_type(HalfYearEnd() + pd.Timestamp("2026-01-01"), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(pd.Timestamp("2026-01-01") + HalfYearEnd(), pd.Timestamp),
        pd.Timestamp,
    )
    check(assert_type(HalfYearEnd() + pd.NaT, NaTType), NaTType)
    check(assert_type(pd.NaT + HalfYearEnd(), NaTType), NaTType)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = HalfYearEnd() + pd.Timedelta("2h")  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _1 = pd.Timedelta("2h") + HalfYearEnd()  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]


def test_monthend_pandas_scalars() -> None:
    """MonthEnd handles pandas scalars in both directions."""
    check(
        assert_type(MonthEnd() + pd.Timestamp("2026-01-01"), pd.Timestamp), pd.Timestamp
    )
    check(
        assert_type(pd.Timestamp("2026-01-01") + MonthEnd(), pd.Timestamp), pd.Timestamp
    )
    check(assert_type(MonthEnd() + pd.NaT, NaTType), NaTType)
    check(assert_type(pd.NaT + MonthEnd(), NaTType), NaTType)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = MonthEnd() + pd.Timedelta("2h")  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _1 = pd.Timedelta("2h") + MonthEnd()  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]


def test_semimonthend_pandas_scalars() -> None:
    """SemiMonthEnd handles pandas scalars in both directions."""
    check(
        assert_type(SemiMonthEnd() + pd.Timestamp("2026-01-01"), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(pd.Timestamp("2026-01-01") + SemiMonthEnd(), pd.Timestamp),
        pd.Timestamp,
    )
    check(assert_type(SemiMonthEnd() + pd.NaT, NaTType), NaTType)
    check(assert_type(pd.NaT + SemiMonthEnd(), NaTType), NaTType)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = SemiMonthEnd() + pd.Timedelta("2h")  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _1 = pd.Timedelta("2h") + SemiMonthEnd()  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]


def test_week_pandas_scalars() -> None:
    """Week handles pandas scalars in both directions."""
    check(assert_type(Week() + pd.Timestamp("2026-01-01"), pd.Timestamp), pd.Timestamp)
    check(assert_type(pd.Timestamp("2026-01-01") + Week(), pd.Timestamp), pd.Timestamp)
    check(assert_type(Week() + pd.NaT, NaTType), NaTType)
    check(assert_type(pd.NaT + Week(), NaTType), NaTType)


def test_fy5253_pandas_scalars() -> None:
    """FY5253 handles pandas scalars in both directions."""
    check(
        assert_type(FY5253() + pd.Timestamp("2026-01-01"), pd.Timestamp), pd.Timestamp
    )
    check(
        assert_type(pd.Timestamp("2026-01-01") + FY5253(), pd.Timestamp), pd.Timestamp
    )
    check(assert_type(FY5253() + pd.NaT, NaTType), NaTType)
    check(assert_type(pd.NaT + FY5253(), NaTType), NaTType)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = FY5253() + pd.Timedelta("2h")  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _1 = pd.Timedelta("2h") + FY5253()  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]


def test_fy5253quarter_pandas_scalars() -> None:
    """FY5253Quarter handles pandas scalars in both directions."""
    check(
        assert_type(FY5253Quarter() + pd.Timestamp("2026-01-01"), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(pd.Timestamp("2026-01-01") + FY5253Quarter(), pd.Timestamp),
        pd.Timestamp,
    )
    check(assert_type(FY5253Quarter() + pd.NaT, NaTType), NaTType)
    check(assert_type(pd.NaT + FY5253Quarter(), NaTType), NaTType)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = FY5253Quarter() + pd.Timedelta("2h")  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _1 = pd.Timedelta("2h") + FY5253Quarter()  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]


def test_easter_pandas_scalars() -> None:
    """Easter handles pandas scalars in both directions."""
    check(
        assert_type(Easter() + pd.Timestamp("2026-01-01"), pd.Timestamp), pd.Timestamp
    )
    check(
        assert_type(pd.Timestamp("2026-01-01") + Easter(), pd.Timestamp), pd.Timestamp
    )
    check(assert_type(Easter() + pd.NaT, NaTType), NaTType)
    check(assert_type(pd.NaT + Easter(), NaTType), NaTType)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = Easter() + pd.Timedelta("2h")  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _1 = pd.Timedelta("2h") + Easter()  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]


def test_custombusinessmonthend_pandas_scalars() -> None:
    """CustomBusinessMonthEnd handles pandas scalars in both directions."""
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
    check(assert_type(CustomBusinessMonthEnd() + pd.NaT, NaTType), NaTType)
    check(assert_type(pd.NaT + CustomBusinessMonthEnd(), NaTType), NaTType)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = CustomBusinessMonthEnd() + pd.Timedelta("2h")  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]
        _1 = pd.Timedelta("2h") + CustomBusinessMonthEnd()  # type: ignore[operator] # pyright: ignore[reportOperatorIssue,reportUnknownVariableType] # pyrefly: ignore[unsupported-operation] # ty: ignore[unsupported-operator]


def test_week_durations_pandas() -> None:
    """Pandas durations follow the concrete offset result family."""
    check(
        assert_type(Week(weekday=None) + pd.Timedelta("1h"), pd.Timedelta), pd.Timedelta
    )
    check(
        assert_type(pd.Timedelta("1h") + Week(weekday=None), pd.Timedelta), pd.Timedelta
    )


def test_week_of_month_regression() -> None:
    """Preserve WeekOfMonth constructor cases from GH 320."""
    check(
        assert_type(WeekOfMonth(2, True) + pd.Timestamp("9/23/2022"), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(pd.Timestamp("9/23/2022") + WeekOfMonth(2, True), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(LastWeekOfMonth(2, 3) + pd.Timestamp("9/23/2022"), pd.Timestamp),
        pd.Timestamp,
    )
    check(
        assert_type(pd.Timestamp("9/23/2022") + LastWeekOfMonth(2, 3), pd.Timestamp),
        pd.Timestamp,
    )


def test_half_year_offsets() -> None:
    """Test half-year offsets introduced in pandas 3.0 GH1654."""
    ts = pd.Timestamp(2024, 2, 1)
    check(assert_type(HalfYearBegin() + ts, pd.Timestamp), pd.Timestamp)
    check(assert_type(ts + HalfYearBegin(), pd.Timestamp), pd.Timestamp)
    check(assert_type(HalfYearEnd() + ts, pd.Timestamp), pd.Timestamp)
    check(assert_type(ts + HalfYearEnd(), pd.Timestamp), pd.Timestamp)
    check(assert_type(BHalfYearBegin() + ts, pd.Timestamp), pd.Timestamp)
    check(assert_type(ts + BHalfYearBegin(), pd.Timestamp), pd.Timestamp)
    check(assert_type(BHalfYearEnd() + ts, pd.Timestamp), pd.Timestamp)
    check(assert_type(ts + BHalfYearEnd(), pd.Timestamp), pd.Timestamp)


def test_week_offsets() -> None:
    """Week offset combinations require weekday=None."""
    check(assert_type(Week(weekday=None) + Day(), dt.timedelta), dt.timedelta)
    check(assert_type(Day() + Week(weekday=None), dt.timedelta), dt.timedelta)
    check(
        assert_type(Week(1, weekday=None) + Week(2, weekday=None), dt.timedelta),
        dt.timedelta,
    )
    check(
        assert_type(Week(2, weekday=None) + Week(1, weekday=None), dt.timedelta),
        dt.timedelta,
    )
    check(assert_type(Week(weekday=None) + Hour(), pd.Timedelta), pd.Timedelta)
    check(assert_type(Hour() + Week(weekday=None), pd.Timedelta), pd.Timedelta)
    check(assert_type(Week(weekday=None) + BusinessDay(), BusinessDay), BusinessDay)
    check(assert_type(BusinessDay() + Week(weekday=None), BusinessDay), BusinessDay)


def test_dateoffset_numpy_arrays() -> None:
    """DateOffset supports object arrays, including empty arrays."""
    values = np.array([dt.datetime(2026, 1, 1)], dtype=object)
    empty = np.array([], dtype=object)
    check(DateOffset() + values, np.ndarray)
    check(values + DateOffset(), np.ndarray)
    check(DateOffset() + empty, np.ndarray)
    check(empty + DateOffset(), np.ndarray)
    # NumPy expressions can hide the offset's declared array result.
    check(
        assert_type(
            DateOffset().__add__(values),
            np.ndarray[tuple[int, ...], np.dtype[np.generic]],
        ),
        np.ndarray,
    )
    check(
        assert_type(
            DateOffset().__radd__(values),
            np.ndarray[tuple[int, ...], np.dtype[np.generic]],
        ),
        np.ndarray,
    )


def test_businesshour_numpy_arrays() -> None:
    """BusinessHour supports object arrays, including empty arrays."""
    values = np.array([dt.datetime(2026, 1, 1)], dtype=object)
    empty = np.array([], dtype=object)
    check(BusinessHour() + values, np.ndarray)
    check(values + BusinessHour(), np.ndarray)
    check(BusinessHour() + empty, np.ndarray)
    check(empty + BusinessHour(), np.ndarray)
    # NumPy expressions can hide the offset's declared array result.
    check(
        assert_type(
            BusinessHour().__add__(values),
            np.ndarray[tuple[int, ...], np.dtype[np.generic]],
        ),
        np.ndarray,
    )
    check(
        assert_type(
            BusinessHour().__radd__(values),
            np.ndarray[tuple[int, ...], np.dtype[np.generic]],
        ),
        np.ndarray,
    )


def test_weekofmonth_numpy_arrays() -> None:
    """WeekOfMonth supports object arrays, including empty arrays."""
    values = np.array([dt.datetime(2026, 1, 1)], dtype=object)
    empty = np.array([], dtype=object)
    check(WeekOfMonth() + values, np.ndarray)
    check(values + WeekOfMonth(), np.ndarray)
    check(WeekOfMonth() + empty, np.ndarray)
    check(empty + WeekOfMonth(), np.ndarray)
    # NumPy expressions can hide the offset's declared array result.
    check(
        assert_type(
            WeekOfMonth().__add__(values),
            np.ndarray[tuple[int, ...], np.dtype[np.generic]],
        ),
        np.ndarray,
    )
    check(
        assert_type(
            WeekOfMonth().__radd__(values),
            np.ndarray[tuple[int, ...], np.dtype[np.generic]],
        ),
        np.ndarray,
    )


def test_yearend_numpy_arrays() -> None:
    """YearEnd supports object arrays, including empty arrays."""
    values = np.array([dt.datetime(2026, 1, 1)], dtype=object)
    empty = np.array([], dtype=object)
    check(YearEnd() + values, np.ndarray)
    check(values + YearEnd(), np.ndarray)
    check(YearEnd() + empty, np.ndarray)
    check(empty + YearEnd(), np.ndarray)
    # NumPy expressions can hide the offset's declared array result.
    check(
        assert_type(
            YearEnd().__add__(values), np.ndarray[tuple[int, ...], np.dtype[np.generic]]
        ),
        np.ndarray,
    )
    check(
        assert_type(
            YearEnd().__radd__(values),
            np.ndarray[tuple[int, ...], np.dtype[np.generic]],
        ),
        np.ndarray,
    )


def test_quarterend_numpy_arrays() -> None:
    """QuarterEnd supports object arrays, including empty arrays."""
    values = np.array([dt.datetime(2026, 1, 1)], dtype=object)
    empty = np.array([], dtype=object)
    check(QuarterEnd() + values, np.ndarray)
    check(values + QuarterEnd(), np.ndarray)
    check(QuarterEnd() + empty, np.ndarray)
    check(empty + QuarterEnd(), np.ndarray)
    # NumPy expressions can hide the offset's declared array result.
    check(
        assert_type(
            QuarterEnd().__add__(values),
            np.ndarray[tuple[int, ...], np.dtype[np.generic]],
        ),
        np.ndarray,
    )
    check(
        assert_type(
            QuarterEnd().__radd__(values),
            np.ndarray[tuple[int, ...], np.dtype[np.generic]],
        ),
        np.ndarray,
    )


def test_halfyearend_numpy_arrays() -> None:
    """HalfYearEnd supports object arrays, including empty arrays."""
    values = np.array([dt.datetime(2026, 1, 1)], dtype=object)
    empty = np.array([], dtype=object)
    check(HalfYearEnd() + values, np.ndarray)
    check(values + HalfYearEnd(), np.ndarray)
    check(HalfYearEnd() + empty, np.ndarray)
    check(empty + HalfYearEnd(), np.ndarray)
    # NumPy expressions can hide the offset's declared array result.
    check(
        assert_type(
            HalfYearEnd().__add__(values),
            np.ndarray[tuple[int, ...], np.dtype[np.generic]],
        ),
        np.ndarray,
    )
    check(
        assert_type(
            HalfYearEnd().__radd__(values),
            np.ndarray[tuple[int, ...], np.dtype[np.generic]],
        ),
        np.ndarray,
    )


def test_monthend_numpy_arrays() -> None:
    """MonthEnd supports object arrays, including empty arrays."""
    values = np.array([dt.datetime(2026, 1, 1)], dtype=object)
    empty = np.array([], dtype=object)
    check(MonthEnd() + values, np.ndarray)
    check(values + MonthEnd(), np.ndarray)
    check(MonthEnd() + empty, np.ndarray)
    check(empty + MonthEnd(), np.ndarray)
    # NumPy expressions can hide the offset's declared array result.
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


def test_semimonthend_numpy_arrays() -> None:
    """SemiMonthEnd supports object arrays, including empty arrays."""
    values = np.array([dt.datetime(2026, 1, 1)], dtype=object)
    empty = np.array([], dtype=object)
    check(SemiMonthEnd() + values, np.ndarray)
    check(values + SemiMonthEnd(), np.ndarray)
    check(SemiMonthEnd() + empty, np.ndarray)
    check(empty + SemiMonthEnd(), np.ndarray)
    # NumPy expressions can hide the offset's declared array result.
    check(
        assert_type(
            SemiMonthEnd().__add__(values),
            np.ndarray[tuple[int, ...], np.dtype[np.generic]],
        ),
        np.ndarray,
    )
    check(
        assert_type(
            SemiMonthEnd().__radd__(values),
            np.ndarray[tuple[int, ...], np.dtype[np.generic]],
        ),
        np.ndarray,
    )


def test_week_numpy_arrays() -> None:
    """Week supports object arrays, including empty arrays."""
    values = np.array([dt.datetime(2026, 1, 1)], dtype=object)
    empty = np.array([], dtype=object)
    check(Week() + values, np.ndarray)
    check(values + Week(), np.ndarray)
    check(Week() + empty, np.ndarray)
    check(empty + Week(), np.ndarray)
    # NumPy expressions can hide the offset's declared array result.
    check(
        assert_type(
            Week().__add__(values), np.ndarray[tuple[int, ...], np.dtype[np.generic]]
        ),
        np.ndarray,
    )
    check(
        assert_type(
            Week().__radd__(values), np.ndarray[tuple[int, ...], np.dtype[np.generic]]
        ),
        np.ndarray,
    )


def test_fy5253_numpy_arrays() -> None:
    """FY5253 supports object arrays, including empty arrays."""
    values = np.array([dt.datetime(2026, 1, 1)], dtype=object)
    empty = np.array([], dtype=object)
    check(FY5253() + values, np.ndarray)
    check(values + FY5253(), np.ndarray)
    check(FY5253() + empty, np.ndarray)
    check(empty + FY5253(), np.ndarray)
    # NumPy expressions can hide the offset's declared array result.
    check(
        assert_type(
            FY5253().__add__(values), np.ndarray[tuple[int, ...], np.dtype[np.generic]]
        ),
        np.ndarray,
    )
    check(
        assert_type(
            FY5253().__radd__(values), np.ndarray[tuple[int, ...], np.dtype[np.generic]]
        ),
        np.ndarray,
    )


def test_fy5253quarter_numpy_arrays() -> None:
    """FY5253Quarter supports object arrays, including empty arrays."""
    values = np.array([dt.datetime(2026, 1, 1)], dtype=object)
    empty = np.array([], dtype=object)
    check(FY5253Quarter() + values, np.ndarray)
    check(values + FY5253Quarter(), np.ndarray)
    check(FY5253Quarter() + empty, np.ndarray)
    check(empty + FY5253Quarter(), np.ndarray)
    # NumPy expressions can hide the offset's declared array result.
    check(
        assert_type(
            FY5253Quarter().__add__(values),
            np.ndarray[tuple[int, ...], np.dtype[np.generic]],
        ),
        np.ndarray,
    )
    check(
        assert_type(
            FY5253Quarter().__radd__(values),
            np.ndarray[tuple[int, ...], np.dtype[np.generic]],
        ),
        np.ndarray,
    )


def test_easter_numpy_arrays() -> None:
    """Easter supports object arrays, including empty arrays."""
    values = np.array([dt.datetime(2026, 1, 1)], dtype=object)
    empty = np.array([], dtype=object)
    check(Easter() + values, np.ndarray)
    check(values + Easter(), np.ndarray)
    check(Easter() + empty, np.ndarray)
    check(empty + Easter(), np.ndarray)
    # NumPy expressions can hide the offset's declared array result.
    check(
        assert_type(
            Easter().__add__(values), np.ndarray[tuple[int, ...], np.dtype[np.generic]]
        ),
        np.ndarray,
    )
    check(
        assert_type(
            Easter().__radd__(values), np.ndarray[tuple[int, ...], np.dtype[np.generic]]
        ),
        np.ndarray,
    )


def test_custombusinessmonthend_numpy_arrays() -> None:
    """CustomBusinessMonthEnd supports object arrays, including empty arrays."""
    values = np.array([dt.datetime(2026, 1, 1)], dtype=object)
    empty = np.array([], dtype=object)
    check(CustomBusinessMonthEnd() + values, np.ndarray)
    check(values + CustomBusinessMonthEnd(), np.ndarray)
    check(CustomBusinessMonthEnd() + empty, np.ndarray)
    check(empty + CustomBusinessMonthEnd(), np.ndarray)
    # NumPy expressions can hide the offset's declared array result.
    check(
        assert_type(
            CustomBusinessMonthEnd().__add__(values),
            np.ndarray[tuple[int, ...], np.dtype[np.generic]],
        ),
        np.ndarray,
    )
    check(
        assert_type(
            CustomBusinessMonthEnd().__radd__(values),
            np.ndarray[tuple[int, ...], np.dtype[np.generic]],
        ),
        np.ndarray,
    )


def test_dateoffset_index() -> None:
    """DateOffset uses container dispatch for index addition."""
    values = pd.date_range("2026-01-01", periods=2)
    check(assert_type(DateOffset() + values, pd.DatetimeIndex), pd.DatetimeIndex)
    check(assert_type(values + DateOffset(), pd.DatetimeIndex), pd.DatetimeIndex)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = DateOffset().__add__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = DateOffset().__radd__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]


def test_businesshour_index() -> None:
    """BusinessHour uses container dispatch for index addition."""
    values = pd.date_range("2026-01-01", periods=2)
    with pytest.warns(PerformanceWarning, match="Non-vectorized DateOffset"):
        check(assert_type(BusinessHour() + values, pd.DatetimeIndex), pd.DatetimeIndex)
        check(assert_type(values + BusinessHour(), pd.DatetimeIndex), pd.DatetimeIndex)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = BusinessHour().__add__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = BusinessHour().__radd__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]


def test_weekofmonth_index() -> None:
    """WeekOfMonth uses container dispatch for index addition."""
    values = pd.date_range("2026-01-01", periods=2)
    with pytest.warns(PerformanceWarning, match="Non-vectorized DateOffset"):
        check(assert_type(WeekOfMonth() + values, pd.DatetimeIndex), pd.DatetimeIndex)
        check(assert_type(values + WeekOfMonth(), pd.DatetimeIndex), pd.DatetimeIndex)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = WeekOfMonth().__add__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = WeekOfMonth().__radd__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]


def test_yearend_index() -> None:
    """YearEnd uses container dispatch for index addition."""
    values = pd.date_range("2026-01-01", periods=2)
    check(assert_type(YearEnd() + values, pd.DatetimeIndex), pd.DatetimeIndex)
    check(assert_type(values + YearEnd(), pd.DatetimeIndex), pd.DatetimeIndex)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = YearEnd().__add__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = YearEnd().__radd__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]


def test_quarterend_index() -> None:
    """QuarterEnd uses container dispatch for index addition."""
    values = pd.date_range("2026-01-01", periods=2)
    check(assert_type(QuarterEnd() + values, pd.DatetimeIndex), pd.DatetimeIndex)
    check(assert_type(values + QuarterEnd(), pd.DatetimeIndex), pd.DatetimeIndex)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = QuarterEnd().__add__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = QuarterEnd().__radd__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]


def test_halfyearend_index() -> None:
    """HalfYearEnd uses container dispatch for index addition."""
    values = pd.date_range("2026-01-01", periods=2)
    check(assert_type(HalfYearEnd() + values, pd.DatetimeIndex), pd.DatetimeIndex)
    check(assert_type(values + HalfYearEnd(), pd.DatetimeIndex), pd.DatetimeIndex)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = HalfYearEnd().__add__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = HalfYearEnd().__radd__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]


def test_monthend_index() -> None:
    """MonthEnd uses container dispatch for index addition."""
    values = pd.date_range("2026-01-01", periods=2)
    check(assert_type(MonthEnd() + values, pd.DatetimeIndex), pd.DatetimeIndex)
    check(assert_type(values + MonthEnd(), pd.DatetimeIndex), pd.DatetimeIndex)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = MonthEnd().__add__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = MonthEnd().__radd__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]


def test_semimonthend_index() -> None:
    """SemiMonthEnd uses container dispatch for index addition."""
    values = pd.date_range("2026-01-01", periods=2)
    check(assert_type(SemiMonthEnd() + values, pd.DatetimeIndex), pd.DatetimeIndex)
    check(assert_type(values + SemiMonthEnd(), pd.DatetimeIndex), pd.DatetimeIndex)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = SemiMonthEnd().__add__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = SemiMonthEnd().__radd__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]


def test_week_index() -> None:
    """Week uses container dispatch for index addition."""
    values = pd.date_range("2026-01-01", periods=2)
    check(assert_type(Week() + values, pd.DatetimeIndex), pd.DatetimeIndex)
    check(assert_type(values + Week(), pd.DatetimeIndex), pd.DatetimeIndex)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = Week().__add__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = Week().__radd__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]


def test_fy5253_index() -> None:
    """FY5253 uses container dispatch for index addition."""
    values = pd.date_range("2026-01-01", periods=2)
    with pytest.warns(PerformanceWarning, match="Non-vectorized DateOffset"):
        check(assert_type(FY5253() + values, pd.DatetimeIndex), pd.DatetimeIndex)
        check(assert_type(values + FY5253(), pd.DatetimeIndex), pd.DatetimeIndex)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = FY5253().__add__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = FY5253().__radd__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]


def test_fy5253quarter_index() -> None:
    """FY5253Quarter uses container dispatch for index addition."""
    values = pd.date_range("2026-01-01", periods=2)
    with pytest.warns(PerformanceWarning, match="Non-vectorized DateOffset"):
        check(assert_type(FY5253Quarter() + values, pd.DatetimeIndex), pd.DatetimeIndex)
        check(assert_type(values + FY5253Quarter(), pd.DatetimeIndex), pd.DatetimeIndex)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = FY5253Quarter().__add__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = FY5253Quarter().__radd__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]


def test_easter_index() -> None:
    """Easter uses container dispatch for index addition."""
    values = pd.date_range("2026-01-01", periods=2)
    with pytest.warns(PerformanceWarning, match="Non-vectorized DateOffset"):
        check(assert_type(Easter() + values, pd.DatetimeIndex), pd.DatetimeIndex)
        check(assert_type(values + Easter(), pd.DatetimeIndex), pd.DatetimeIndex)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = Easter().__add__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = Easter().__radd__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]


def test_custombusinessmonthend_index() -> None:
    """CustomBusinessMonthEnd uses container dispatch for index addition."""
    values = pd.date_range("2026-01-01", periods=2)
    with pytest.warns(PerformanceWarning, match="Non-vectorized DateOffset"):
        check(
            assert_type(CustomBusinessMonthEnd() + values, pd.DatetimeIndex),
            pd.DatetimeIndex,
        )
        check(
            assert_type(values + CustomBusinessMonthEnd(), pd.DatetimeIndex),
            pd.DatetimeIndex,
        )
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = CustomBusinessMonthEnd().__add__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = CustomBusinessMonthEnd().__radd__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]


def test_yearend_zero_index() -> None:
    """Preserve zero-offset YearEnd addition to a business-date index."""
    values = pd.bdate_range("2024-09-01", "2024-09-10")
    check(assert_type(YearEnd(0) + values, pd.DatetimeIndex), pd.DatetimeIndex)
    check(assert_type(values + YearEnd(0), pd.DatetimeIndex), pd.DatetimeIndex)


def test_dateoffset_series() -> None:
    """DateOffset uses container dispatch for series addition."""
    values = pd.Series(pd.date_range("2026-01-01", periods=2))
    check(assert_type(DateOffset() + values, "pd.Series[pd.Timestamp]"), pd.Series)
    check(assert_type(values + DateOffset(), "pd.Series[pd.Timestamp]"), pd.Series)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = DateOffset().__add__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = DateOffset().__radd__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]


def test_businesshour_series() -> None:
    """BusinessHour uses container dispatch for series addition."""
    values = pd.Series(pd.date_range("2026-01-01", periods=2))
    with pytest.warns(PerformanceWarning, match="Non-vectorized DateOffset"):
        check(
            assert_type(BusinessHour() + values, "pd.Series[pd.Timestamp]"), pd.Series
        )
        check(
            assert_type(values + BusinessHour(), "pd.Series[pd.Timestamp]"), pd.Series
        )
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = BusinessHour().__add__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = BusinessHour().__radd__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]


def test_weekofmonth_series() -> None:
    """WeekOfMonth uses container dispatch for series addition."""
    values = pd.Series(pd.date_range("2026-01-01", periods=2))
    with pytest.warns(PerformanceWarning, match="Non-vectorized DateOffset"):
        check(assert_type(WeekOfMonth() + values, "pd.Series[pd.Timestamp]"), pd.Series)
        check(assert_type(values + WeekOfMonth(), "pd.Series[pd.Timestamp]"), pd.Series)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = WeekOfMonth().__add__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = WeekOfMonth().__radd__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]


def test_yearend_series() -> None:
    """YearEnd uses container dispatch for series addition."""
    values = pd.Series(pd.date_range("2026-01-01", periods=2))
    check(assert_type(YearEnd() + values, "pd.Series[pd.Timestamp]"), pd.Series)
    check(assert_type(values + YearEnd(), "pd.Series[pd.Timestamp]"), pd.Series)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = YearEnd().__add__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = YearEnd().__radd__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]


def test_quarterend_series() -> None:
    """QuarterEnd uses container dispatch for series addition."""
    values = pd.Series(pd.date_range("2026-01-01", periods=2))
    check(assert_type(QuarterEnd() + values, "pd.Series[pd.Timestamp]"), pd.Series)
    check(assert_type(values + QuarterEnd(), "pd.Series[pd.Timestamp]"), pd.Series)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = QuarterEnd().__add__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = QuarterEnd().__radd__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]


def test_halfyearend_series() -> None:
    """HalfYearEnd uses container dispatch for series addition."""
    values = pd.Series(pd.date_range("2026-01-01", periods=2))
    check(assert_type(HalfYearEnd() + values, "pd.Series[pd.Timestamp]"), pd.Series)
    check(assert_type(values + HalfYearEnd(), "pd.Series[pd.Timestamp]"), pd.Series)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = HalfYearEnd().__add__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = HalfYearEnd().__radd__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]


def test_monthend_series() -> None:
    """MonthEnd uses container dispatch for series addition."""
    values = pd.Series(pd.date_range("2026-01-01", periods=2))
    check(assert_type(MonthEnd() + values, "pd.Series[pd.Timestamp]"), pd.Series)
    check(assert_type(values + MonthEnd(), "pd.Series[pd.Timestamp]"), pd.Series)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = MonthEnd().__add__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = MonthEnd().__radd__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]


def test_semimonthend_series() -> None:
    """SemiMonthEnd uses container dispatch for series addition."""
    values = pd.Series(pd.date_range("2026-01-01", periods=2))
    check(assert_type(SemiMonthEnd() + values, "pd.Series[pd.Timestamp]"), pd.Series)
    check(assert_type(values + SemiMonthEnd(), "pd.Series[pd.Timestamp]"), pd.Series)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = SemiMonthEnd().__add__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = SemiMonthEnd().__radd__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]


def test_week_series() -> None:
    """Week uses container dispatch for series addition."""
    values = pd.Series(pd.date_range("2026-01-01", periods=2))
    check(assert_type(Week() + values, "pd.Series[pd.Timestamp]"), pd.Series)
    check(assert_type(values + Week(), "pd.Series[pd.Timestamp]"), pd.Series)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = Week().__add__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = Week().__radd__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]


def test_fy5253_series() -> None:
    """FY5253 uses container dispatch for series addition."""
    values = pd.Series(pd.date_range("2026-01-01", periods=2))
    with pytest.warns(PerformanceWarning, match="Non-vectorized DateOffset"):
        check(assert_type(FY5253() + values, "pd.Series[pd.Timestamp]"), pd.Series)
        check(assert_type(values + FY5253(), "pd.Series[pd.Timestamp]"), pd.Series)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = FY5253().__add__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = FY5253().__radd__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]


def test_fy5253quarter_series() -> None:
    """FY5253Quarter uses container dispatch for series addition."""
    values = pd.Series(pd.date_range("2026-01-01", periods=2))
    with pytest.warns(PerformanceWarning, match="Non-vectorized DateOffset"):
        check(
            assert_type(FY5253Quarter() + values, "pd.Series[pd.Timestamp]"), pd.Series
        )
        check(
            assert_type(values + FY5253Quarter(), "pd.Series[pd.Timestamp]"), pd.Series
        )
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = FY5253Quarter().__add__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = FY5253Quarter().__radd__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]


def test_easter_series() -> None:
    """Easter uses container dispatch for series addition."""
    values = pd.Series(pd.date_range("2026-01-01", periods=2))
    with pytest.warns(PerformanceWarning, match="Non-vectorized DateOffset"):
        check(assert_type(Easter() + values, "pd.Series[pd.Timestamp]"), pd.Series)
        check(assert_type(values + Easter(), "pd.Series[pd.Timestamp]"), pd.Series)
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = Easter().__add__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = Easter().__radd__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]


def test_custombusinessmonthend_series() -> None:
    """CustomBusinessMonthEnd uses container dispatch for series addition."""
    values = pd.Series(pd.date_range("2026-01-01", periods=2))
    with pytest.warns(PerformanceWarning, match="Non-vectorized DateOffset"):
        check(
            assert_type(CustomBusinessMonthEnd() + values, "pd.Series[pd.Timestamp]"),
            pd.Series,
        )
        check(
            assert_type(values + CustomBusinessMonthEnd(), "pd.Series[pd.Timestamp]"),
            pd.Series,
        )
    if TYPE_CHECKING_INVALID_USAGE:
        _0 = CustomBusinessMonthEnd().__add__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
        _1 = CustomBusinessMonthEnd().__radd__(values)  # type: ignore[operator] # pyright: ignore[reportCallIssue,reportArgumentType,reportUnknownVariableType] # pyrefly: ignore[no-matching-overload] # ty: ignore[no-matching-overload]
