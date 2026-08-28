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
| Constructor overload overlap (non-subtype) | `core/indexes/base.pyi` | 2 | `grep -n 'overload-overlap\]' pandas-stubs/core/indexes/base.pyi` (the `__new__` overload pair for PyArrow timestamp/timedelta dtypes) | Both overloads share `data: AxesData`; the overlap comes from `PyArrowTimestampDtypeArg`/`PyArrowTimedeltaDtypeArg` not being provably disjoint unions — unlike the numeric-tower/subclass overlaps in `docs/type_ignores.md`, this one is not backed by an actual subtype relationship. Removable if the literal/`pa.DataType` partitions can be narrowed so the two domains are disjoint, or checkers learn to prove the disjointness themselves. |
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
