# Suppression debt inventory (scratch — delete before PR)

Permanent, intentional ignores live in `docs/type_ignores.md` — this file is only
checker-disagreement debt.

Not linked from `docs/README.md`. Tracks every `# (type|pyright|pyrefly|ty): ignore`
comment *added* by `e2d7933` (`TYP add backing-array generic to Series and Index`) plus
the follow-up `IndexOpsMixin` refactor, so it can be re-run and shrunk as suppressions
are removed. Counts are added lines only (`git diff cebd954 -- <path> | grep '^\+' | grep
-cE '# (type|pyright|pyrefly|ty): ?ignore'`), not total ignores in the file — pre-existing
ignores are out of scope.

Baseline after `e2d7933`: 46 stub ignores, 98 test ignores. Re-checked after the
`IndexOpsMixin[S1, ArrayT_co, GenericT_co]` reorder: the reorder itself didn't touch any
of these lines, but the accompanying `Series.array`/`Index.array` deduplication (moving
`.array` onto `IndexOpsMixin` and deleting the two redeclarations) removed one
override-variance ignore that no longer applied, so the stub count is **45**, not 46.
`poe test_all` reports no unused ignores against the current total, so nothing here is
stale.

Of the current 45 stub ignores, 17 turned out to be permanent by design rather than
debt and were moved to `docs/type_ignores.md`: 5 private-symbol-import ignores
(`reportPrivateUsage` on the `pandas._stubs_only` descriptor imports) and 12
overload-overlap ignores that reflect a genuine subtype relationship between overload
branches (the numeric tower on `diff`, `StringArray <: BaseStringArray` on `astype`, and
the universal-subtype `Sequence[Never]` branch on `Series.__new__`). The stub total
below is the remainder: 45 − 5 − 12 = **28**.

Distinction kept from the current `architecture.md` draft: ignores inside
`TYPE_CHECKING_INVALID_USAGE` blocks are intentional (they prove a type checker rejects
invalid code) and are **not** tracked here. Every row below is either an ignore on a
positive `assert_type` call (accepted code, debt) or a stub-side ignore with no
`TYPE_CHECKING_INVALID_USAGE` guard.

## Stubs — 28

| Category | File | Count | Locating grep | Removal condition |
| --- | --- | --- | --- | --- |
| Generic specialization disagreements | `core/arrays/categorical.pyi` | 8 | `grep -n 'type-var\|bad-specialization\|invalid-type-arguments' pandas-stubs/core/arrays/categorical.pyi` | `CategoricalValueT = TypeVar("CategoricalValueT", str, int, float, object, default=object)` is a constrained TypeVar whose `object` member violates `S1`'s `bound=SeriesDType` — checkers are correctly rejecting `Series[CategoricalValueT, Categorical[CategoricalValueT]]`. Concrete fix path: the sibling overload at `_stubs_only/__init__.pyi:161-165` uses `CategoricalValueT1` (`str, int, float` only, no `object`) for the identical `Series[CategoricalValueT1, Categorical[CategoricalValueT1]]` shape and needs zero ignores. Removable once `CategoricalValueT`'s `object` member is dropped or narrowed the same way, without losing the ability to type an untyped `Categorical`. |
| Generic specialization disagreements | `_stubs_only/__init__.pyi` | 4 | `grep -n 'type-var\|bad-specialization\|invalid-type-arguments' pandas-stubs/_stubs_only/__init__.pyi` | Same condition as above — these ignores sit on the `_CategoricalSeries` alias and its two descriptor `__get__` overloads, which are built from the same `CategoricalValueT`. |
| Constructor overload overlap (non-subtype) | `core/indexes/base.pyi` | 2 | `grep -n 'overload-overlap\]' pandas-stubs/core/indexes/base.pyi` (the `__new__` overload pair for PyArrow timestamp/timedelta dtypes) | Both overloads share `data: AxesData`; the overlap comes from `PyArrowTimestampDtypeArg`/`PyArrowTimedeltaDtypeArg` not being provably disjoint unions — unlike the numeric-tower/subclass overlaps in `docs/type_ignores.md`, this one is not backed by an actual subtype relationship. Removable if the literal/`pa.DataType` partitions can be narrowed so the two domains are disjoint, or checkers learn to prove that on their own. |
| Inherited-method override variance | `core/series.pyi` | 11 | `grep -n 'bad-override\|invalid-method-override\|reportIncompatibleMethodOverride\]' pandas-stubs/core/series.pyi` | `set_flags`, `__neg__`, `__pos__`, `__abs__`, `convert_dtypes` (2 lines), `T`, and the arithmetic dunders (`__mod__`/`__pow__`/`__rmod__`/`__rpow__`) return `Series[S1]` where the base (`NDFrame`) declares `Self`. Root cause found: since `Series` is `Generic[S1, ArrayT_co]` with `ArrayT_co` defaulting to `ExtensionArray`, a bare `Series[S1]` resolves to `Series[S1, ExtensionArray]`, silently dropping the backing-array parameter these methods could in fact preserve. Removable by returning `Series[S1, ArrayT_co]` instead of `Series[S1]` from these overrides — plausibly a fixable incompleteness in this branch's overrides, flagged to the user as a follow-up, not resolved here. |
| Inherited-method override variance | `core/indexes/range.pyi` | 2 | `grep -n 'bad-override\|invalid-method-override\|reportIncompatibleMethodOverride\]' pandas-stubs/core/indexes/range.pyi` | `union`, `where` overrides on `RangeIndex`. Same mechanism and removal condition as above. |
| Inherited-method override variance | `core/indexes/category.pyi` | 1 | `grep -n 'bad-override\|invalid-method-override\|reportIncompatibleMethodOverride\]' pandas-stubs/core/indexes/category.pyi` | `insert` override on `CategoricalIndex`. Same mechanism and removal condition as above. |

## Tests — 98

All rows below are ignores attached to *positive* `assert_type`/`check(assert_type(...))`
calls — accepted code whose expected type the four checkers currently disagree on
(mostly: which side of `Series[Any] | Series[S1]` arithmetic collapses to `pd.Series`
vs. a defaulted-generic `pd.Series[Any, ExtensionArray]`). None are inside
`TYPE_CHECKING_INVALID_USAGE`.

| File | Count | Locating grep |
| --- | --- | --- |
| `series/test_truediv.py` | 17 | `grep -n 'assert-type\]\|type-assertion-failure\]' tests/series/test_truediv.py` |
| `series/test_add.py` | 16 | `grep -n 'assert-type\]\|type-assertion-failure\]' tests/series/test_add.py` |
| `series/test_sub.py` | 14 | `grep -n 'assert-type\]\|type-assertion-failure\]' tests/series/test_sub.py` |
| `series/test_mul.py` | 12 | `grep -n 'assert-type\]\|type-assertion-failure\]' tests/series/test_mul.py` |
| `indexes/test_add.py` | 6 | `grep -n 'assert-type\]\|type-assertion-failure\]' tests/indexes/test_add.py` |
| `indexes/test_mul.py` | 6 | `grep -n 'assert-type\]\|type-assertion-failure\]' tests/indexes/test_mul.py` |
| `indexes/test_sub.py` | 6 | `grep -n 'assert-type\]\|type-assertion-failure\]' tests/indexes/test_sub.py` |
| `indexes/test_truediv.py` | 6 | `grep -n 'assert-type\]\|type-assertion-failure\]' tests/indexes/test_truediv.py` |
| `frame/test_frame.py` | 5 | `grep -n 'assert-type\]\|type-assertion-failure\]' tests/frame/test_frame.py` |
| `series/test_floordiv.py` | 4 | `grep -n 'assert-type\]\|type-assertion-failure\]' tests/series/test_floordiv.py` |
| `indexes/test_floordiv.py` | 3 | `grep -n 'assert-type\]\|type-assertion-failure\]' tests/indexes/test_floordiv.py` |
| `indexes/test_indexes.py` | 2 | `grep -n 'assert-type\]\|type-assertion-failure\]' tests/indexes/test_indexes.py` (both on `.append(...)`) |
| `test_natype.py` | 1 | `grep -n 'assert-type\]\|type-assertion-failure\]' tests/test_natype.py` (on `divmod(na, idx_int)`) |

Removal condition (all rows): all supported checkers materialize generic defaults for
arithmetic results consistently, or the expected type in the `assert_type` call can be
made explicit without weakening the tested API.

### Confirmed mechanism (95 of 98 rows: every row above except the single
### `frame/test_frame.py` `test_types_unique` case and the `test_natype.py` row)

Root cause, confirmed by live bisection against this branch and by a standalone
pandas/numpy-free repro (`mypy 2.3.1`; not reproduced on pyright, pyrefly, or ty — see
the four-checker matrix below):

Whenever an `Any`-typed operand makes two or more `__add__`/`__sub__`/`__mul__`/
`__truediv__`/`__floordiv__`/`.add`/`.radd`/... overloads on `Series`/`Index` match
simultaneously (`Any` is compatible with every candidate's parameter type), and the
matched overloads' return types are not "equivalent modulo `Any`" in mypy's sense, mypy
intentionally infers `Any` for the *entire* return type's type arguments — not just the
one argument that actually varies between the matched candidates. `Series`/`Index` had
only one type parameter before this branch, so "the whole return became `Any`" and "the
one parameter that differs became `Any`" were indistinguishable; the second
(`ArrayT_co`) parameter this branch adds is what makes the over-widening visible as an
`assert-type` mismatch (`Series[Any, Any]` instead of the expected
`Series[Any, ExtensionArray]`).

This is not a novel mypy bug: it is the intentional gradual-typing soundness rule
explained by mypy core maintainer @ilevkivskyi on
[python/mypy#19952](https://github.com/python/mypy/issues/19952) — filed from this
project against a single-type-parameter reproduction of the identical mechanism,
already closed as working-as-intended ("replacing a precise type with `Any` should not
cause new errors"). The general disagreement between mypy/pyright/pyrefly/ty on overload
resolution with `Any` arguments is tracked on this repo's own
[pandas-dev/pandas-stubs#1781](https://github.com/pandas-dev/pandas-stubs/issues/1781),
which cross-references #19952. Given a maintainer already confirmed the single-parameter
case is intentional, the multi-parameter case was filed as
[python/mypy#21903](https://github.com/python/mypy/issues/21903) (open, filed 2026-08-28),
asking whether widening *every* type argument — rather than only the ones the matched
overloads actually disagree on — is intended, or whether the single-parameter rule was
meant to stop at the parameter that actually varies.

Minimal, pandas/numpy-free repro (the one filed as `python/mypy#21903`), re-verified at
the repo's own floor (`python-version = "3.11"`) against all four checkers this project
supports. Two prior
attempts at this repro were wrong and are recorded for posterity, not repeated: an
earlier version used `typing.TypeVar(..., default=EA)`, which requires Python ≥ 3.13
(PEP 696) and made pyright/ty fail on portability grounds alone, independent of the
actual mechanism — the fix is `typing_extensions.TypeVar`, mirroring
`pandas-stubs/_typing.pyi:44-46`. A second version additionally put the `Any` operand on
the wrong side (`other`, not `self`) relative to the real failing call
(`tests/series/test_add.py:53`, where the **receiver** `left_i` carries the `Any`), and
that version also happened to trip `ty` — an independent disagreement, not a cascade
from the portability bug. The version below fixes both: it matches the real call shape
(`Ser2[Any, EA] + Sequence[Any]`, with a `Supports_ProtoAdd`-style protocol overload
alongside a concrete-`self` overload, mirroring `pandas-stubs/core/series.pyi:2232`) and
is mypy-only.

```python
from collections.abc import Sequence
from typing import Any, Generic, Protocol, assert_type, overload

from typing_extensions import TypeVar

S1 = TypeVar("S1")


class EA: ...


A = TypeVar("A", bound=EA, default=EA, covariant=True)
S2 = TypeVar("S2", bound=EA)
S2_contra = TypeVar("S2_contra", bound=EA, contravariant=True)


class Supports_ProtoAdd(Protocol[S2_contra, S2]):
    def _proto_add(self, other: S2_contra, /) -> "Ser2[S2, EA]": ...


class Ser2(Generic[S1, A]):
    def _proto_add(self, other: Any, /) -> "Ser2[Any, EA]":
        raise NotImplementedError

    @overload
    def __add__(
        self: Supports_ProtoAdd[S2_contra, S2],
        other: "S2_contra | Sequence[S2_contra]",
    ) -> "Ser2[S2]": ...
    @overload
    def __add__(self: "Ser2[bool, EA]", other: Sequence[Any]) -> "Ser2[int]": ...
    def __add__(self, other: Any) -> Any:
        raise NotImplementedError


def f(a2: "Ser2[Any, EA]", seq: "Sequence[Any]") -> None:
    assert_type(a2 + seq, "Ser2[Any, EA]")
    # mypy 2.3.1 @3.11: error: Expression is of type "Ser2[Any, Any]", not "Ser2[Any, EA]"  [assert-type]
```

Measured matrix, all runs at `--python-version 3.11` / `--pythonversion 3.11` (the repo's
own floor), from this session:

| Checker | Result at repo floor (3.11) |
| --- | --- |
| mypy 2.3.1 | **fails** (the intended demo): `Ser2[Any, Any]`, not `Ser2[Any, EA]` |
| pyright | 0 errors |
| pyrefly | 0 errors — **caveat**: run outside the repo falls back to the `basic` preset ("No `pyrefly.toml` found"), so this is weaker evidence than a real project-config run, not a strict pass |
| ty | 0 errors — `All checks passed!` |

So the repro is mypy-only, matching the real category-A/B/C ignores at
`tests/series/test_add.py:53,59,65,71` etc., which carry a bare
`# type: ignore[assert-type]` with no ty/pyrefly companion.

Two bounded stub-side workarounds were tried and abandoned (do not retry without a new
angle):

- **Change `ArrayT_co`'s default from `ExtensionArray` to `Any`**
  (`pandas-stubs/_typing.pyi:938`). Since the degraded type is always `Any` in that slot,
  this would make the 95 assertions correct without an ignore — but it also changes every
  *other* bare `Series`/`Index` return elsewhere in the stubs to default to
  `[…, Any]` instead of `[…, ExtensionArray]`. Tried directly: **270 new mypy errors**
  across 48 files (`poetry run mypy pandas-stubs tests --no-incremental`), including
  colliding with the `test_types_unique` one-off above by changing which overload it
  dispatches to. Reverted.
- **Hoist a `self: Series[Any, Any], other: Any -> Series` catch-all `__add__` overload
  to the front of the overload list** (mirrors mypy's own suggested workaround of
  reordering overloads). Tried on `Series.__add__` only: no effect — mypy's
  ambiguous-overload-with-`Any` check evaluates all candidates regardless of declaration
  order, so a hoisted catch-all doesn't prevent the widening once a later, narrower
  overload could also match. Reverted.

No further stub-side fix attempt is planned. The tracker for these 95 ignores now exists:
`python/mypy#21903`. A single anchor comment pointing at it has been added at the
canonical site, `tests/series/test_add.py:51-52`, the same way the `test_natype.py` row
already points at `facebook/pyrefly#3822` and the `test_types_unique` row points at
`astral-sh/ty#2182`. The other 94 sites are left bare, since they share the identical
root cause and are trivially found by the shared repro; annotate them individually only
if that stops being true. Because this file is deleted before the PR, any per-site
comments added later must cite `python/mypy#21903` / `pandas-dev/pandas-stubs#1781`
directly rather than pointing back at this document.

## Re-running this after further changes

```bash
git diff cebd954 -- 'pandas-stubs/**/*.pyi' 'pandas-stubs/*.pyi' \
  | grep -E '^\+' | grep -cE '# (type|pyright|pyrefly|ty): ?ignore'
git diff cebd954 -- 'tests/**/*.py' 'tests/*.py' \
  | grep -E '^\+' | grep -cE '# (type|pyright|pyrefly|ty): ?ignore'
```

If `poe test_all` starts failing on an unused-ignore diagnostic, that ignore's row above
is stale — delete the row (and the ignore comment) rather than suppressing the new
diagnostic.

**Delete this file before opening the PR.**
