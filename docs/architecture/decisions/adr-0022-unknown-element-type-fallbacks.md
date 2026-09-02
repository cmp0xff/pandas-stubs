---
status: proposed
date: 2026-09-02
deciders: [Dr-Irv, twoertwein, MarcoGorelli, loicdiridollou, cmp0xff]
consulted: [typing-sig]
informed: [pandas-stubs contributors]
---

# ADR-0022: Unknown / Uninferrable Element-Type Fallbacks

## Context and Problem Statement

`docs/philosophy.md` states the project's rule for values whose type cannot be
statically inferred:

> Note that in the above example, `s` is just typed as `Series` (which defaults to
> `Series[Any]`) because its type cannot be statically inferred.

The same "we cannot know the element type here" situation is currently answered with
three different fallbacks, depending on which API surface is used:

| expression | current static type |
| :--- | :--- |
| `df["gateway"]` | `Series[Any]` |
| `df.iterrows()` → `r["gateway"]` | `Series[Any]` → `Any` |
| `df.itertuples(name=None)` | `Iterator[tuple[Any, ...]]` |
| `df.itertuples()` → `row.gateway` | `Scalar` (16-member union) |
| `df.loc[0, "gateway"]` | `Scalar` (16-member union) |
| bare `pd.Series` | `Series[Any]` |
| bare `pd.Categorical` | `Categorical[object]` |

Observed with pyright 1.1.411 and ty 0.0.76 against pandas-stubs 3.0.5.260730.

The inconsistencies are user-visible:

- pandas-dev/pandas-stubs#1892: `PandasNamedTuple.__getattr__` returns `Scalar`, so a
  string column read through `df.itertuples()` rejects `len(row.gateway)` and
  `row.gateway.upper()`, while the same column read through `df["gateway"]` or
  `df.iterrows()` is `Any` and is accepted.
- pandas-dev/pandas-stubs#1361: `.loc` assignment rejects `Enum` members because the
  `Scalar` union is a closed world that does not contain `Enum` (related:
  pandas-dev/pandas-stubs#1288, where `Series.eq(Thing.ONE)` is rejected on the same
  grounds).
- `Categorical` alone resolves to `Categorical[object]`, while `Series` alone resolves
  to `Series[Any]`, even though both fallbacks answer the same question: "what is the
  element type of this uninferrable container?".

## Decision Drivers

- **Consistency**: use one fallback style for "the element type cannot be inferred".
- **Backward compatibility**: bare `Series`, `Categorical`, and `PandasNamedTuple`
  must remain valid annotations.
- **Opt-in precision**: users who know the element type should be able to get it
  checked without `cast`.
- **4-checker portability**: mypy, pyright, pyrefly, and ty must all accept the
  mechanism, including PEP 696 legality.
- **Soundness vs permissiveness**: `Any` is maximally permissive; `Scalar`/`object`
  are closed-world restrictions that can reject legitimate values.

## Status Quo: Four Fallback Styles

### 1. `Series`: bound TypeVar with `default=Any`

```python
# _typing.pyi
S0 = TypeVar("S0", bound=SeriesDType, default=Any)
S1 = TypeVar("S1", bound=SeriesDType, default=Any)
```

Bare `Series` therefore means `Series[Any]`. This is the documented rule in
`docs/philosophy.md` and the model the other sites are compared against.

### 2. `Categorical`: constrained TypeVar with `default=object`

```python
# core/dtypes/dtypes.pyi
CategoricalValueT = TypeVar(
    "CategoricalValueT", str, int, float, object, default=object
)
CategoricalValueT1 = TypeVar("CategoricalValueT1", str, int, float)
```

Bare `Categorical` means `Categorical[object]`, not `Categorical[Any]`.

PEP 696 requires a constrained TypeVar's default to be one of the constraints (a
subtype is not enough, and `Any` is rejected; mypy reports
"TypeVar default must be one of the constraint types"). Therefore `default=Any`
cannot be added to `CategoricalValueT` as currently declared. Any change that wants an
`Any`-like fallback must either remove the default or convert the TypeVar to a bound.

### 3. `PandasNamedTuple`: no TypeVar, hard-coded `Scalar`

```python
# core/frame.pyi
@type_check_only
class PandasNamedTuple(tuple[Any, ...]):
    def __getattr__(self, field: str, /) -> Scalar: ...
```

The class is not generic, so there is no way to parametrize a homogeneous row
(`PandasNamedTuple[str]`); every attribute access returns the full 16-member `Scalar`
union.

### 4. `ScalarT0`: bound TypeVar with `default=` the bound itself

```python
# _typing.pyi
ScalarT0 = TypeVar("ScalarT0", bound=Scalar, default=Scalar)
```

Used by `pd.notna(obj: ScalarT0 | NaTType | NAType | None) -> TypeIs[ScalarT0]`. This
is a fourth default style — the default is the closed-world union itself — but it is
internally consistent (a `TypeIs` guard over `Scalar` inputs) and is listed here only
to complete the taxonomy.

The `Scalar` union itself is:

```python
# _typing.pyi
_IndexIterScalar: TypeAlias = (
    str
    | bytes
    | datetime.date
    | datetime.datetime
    | datetime.timedelta
    | np.datetime64
    | np.timedelta64
    | bool
    | int
    | float
    | Timestamp
    | Timedelta
)
# This is wider than what is in pandas
Scalar: TypeAlias = (
    _IndexIterScalar | complex | np.integer | np.floating | np.complexfloating
)
```

## Problem Details

### pandas-dev/pandas-stubs#1892 — `itertuples()` row attributes

```python
df = pd.DataFrame({"gateway": ["NASDAQ"], "action_id": [7]})

for row in df.itertuples(index=False):
    len(row.gateway)    # rejected
    row.gateway.upper() # rejected
```

The runtime type of `row.gateway` is `str`, but the stub resolves the attribute to the
`Scalar` union. pyright rejects `.upper()` once per non-string union member
(`reportAttributeAccessIssue`) and rejects `len(...)` because `date` is not `Sized`.
The same column through the sibling APIs is `Any`:

```python
df["gateway"]          # Series[Any]
df.iterrows()          # Series (bare → Series[Any]); r["gateway"] → Any
df.itertuples(name=None)  # tuple[Any, ...]
```

The `Scalar` choice originated in PR pandas-dev/pandas-stubs#842, where the rationale
was that single-element access should mirror `.loc`:

> I'm thinking we should return `Scalar` here, because we also return `Scalar` when
> someone does `df.loc[3, "a"]`. ... I've taken the philosophy of limiting the types
> to what is "normal" usage, and if you put a funky type in a `DataFrame` or `Series`,
> then you can do a `cast` to fix it.

### pandas-dev/pandas-stubs#1361 — `.loc` assignment rejects `Enum`

```python
from enum import Enum, auto

class Thing(Enum):
    A = auto()

data = pd.DataFrame(index=[0, 1])
data.loc[:, "a"] = Thing.A
```

pyright still rejects this with the current stubs ("Argument of type `Literal[Thing.A]`
cannot be assigned to parameter of type ... `Scalar | ...`"). ty currently accepts the
same repro — a checker-variance worth recording. The maintainer's position in the issue
thread is that forcing `cast(Scalar, Thing.A)` is the intended workaround, and that
supporting `Enum` inside `Series` properly would require handling `Enum` arithmetic
plus a large test surface.

### `S1` bound vs `Series.__new__` overload coverage (adjacent question)

`S1` is bound to `SeriesDType`:

```python
SeriesDTypeNoStrDateTime: TypeAlias = (
    bytes
    | bool
    | int
    | float
    | complex
    | NpDtypeNoStr
    | ExtensionDtype
    | Period
    | Interval
    | CategoricalDtype
    | BaseOffset
)
SeriesDTypeNoDateTime: TypeAlias = (
    str | SeriesDTypeNoStrDateTime | type[str] | list[str]
)
SeriesDType: TypeAlias = (
    SeriesDTypeNoDateTime
    | datetime.date
    | datetime.time
    | datetime.datetime  # includes pd.Timestamp
    | datetime.timedelta  # includes pd.Timedelta
)
```

Several bound members are never produced by `Series.__new__` overloads:

- `bytes` and `complex` are only produced by `astype` and complex arithmetic.
- `datetime.time`, `NpDtypeNoStr`, `ExtensionDtype`, and `CategoricalDtype` as an
  *element* type are never returned by any constructor, `astype`, or operator overload;
  `type[str]` is only reached through `dtype: type[S1] -> Self`.

The bound is therefore best understood as the annotation space ("types a Series may be
annotated with across the API"), not the set of constructor return types. It also mixes
element types (`str`, `bytes`, `bool`, ...) with dtype-specifier types (`NpDtypeNoStr`,
`ExtensionDtype`, `CategoricalDtype`). This is an adjacent design smell worth a
separate audit; it is not required by pandas-dev/pandas-stubs#1892.

## Considered Options

### PandasNamedTuple / `itertuples()`

**Option A — generic `RowT` with `default=Any` (the proposal in pandas-dev/pandas-stubs#1892).**

```python
# _typing.pyi
RowT = TypeVar("RowT", default=Any)

# core/frame.pyi
@type_check_only
class PandasNamedTuple(tuple[Any, ...], Generic[RowT]):
    def __getattr__(self, field: str, /) -> RowT: ...
```

Unannotated code then behaves like `Series[Any]` (`df.itertuples()` →
`Iterator[PandasNamedTuple[Any]]`, `row.gateway` → `Any`), and the homogeneous case is
checkable by annotation:

```python
typed: Iterator[PandasNamedTuple[str]] = df.itertuples(index=False)
for r in typed:
    r.gateway.bit_length()  # error: "str" has no attribute "bit_length"
```

- *Pros*: consistent default with `Series`; no `cast`; opt-in checked rows; pure
  typing; bare `PandasNamedTuple` stays valid.
- *Cons*: the default is still `Any`, so nothing is checked unless the user annotates;
  the annotation is an assertion, not an inference (the iterator is `PandasNamedTuple[Any]`).

**Option B — plain `__getattr__ -> Any`.**

- *Pros*: one-line change; consistent default for unannotated code.
- *Cons*: `PandasNamedTuple` stays non-generic, so the opt-in `PandasNamedTuple[str]`
  path from Option A is lost.

**Option C — keep `Scalar` (status quo).**

- *Pros*: forces precision; consistent with `.loc`/`.at`/`.iat` single-cell extraction;
  the `cast(Iterator[OneRow], df.itertuples())` pattern already exists.
- *Cons*: the pandas-dev/pandas-stubs#1892 false errors remain; inconsistent with
  `iterrows()` and column projection.

**Option D — generic `RowT` with `bound=Scalar, default=Scalar`.**

- *Pros*: opt-in checked rows while keeping the closed world.
- *Cons*: does not fix the default behavior in pandas-dev/pandas-stubs#1892; still
  rejects `Enum`-valued columns (pandas-dev/pandas-stubs#1361).

### `CategoricalValueT` default

**Option A — drop `default=object`, keep the constraints.**

```python
CategoricalValueT = TypeVar("CategoricalValueT", str, int, float, object)
```

Unparameterized `Categorical` then falls back to the implicit `Any` for unspecified
type parameters, exactly like `Series`. This is PEP 696-compliant.

- *Pros*: minimal; matches `Series`; keeps the existing constraint list.
- *Cons*: needs 4-checker verification (bare constrained generic without an explicit
  default); the author of PR pandas-dev/pandas-stubs#1748 reported being
  "forced to set a default to the TypeVar to object", so the original constraint that
  forced `object` must be re-verified against current mypy/pyright/pyrefly/ty.

**Option B — convert to a bound TypeVar with `default=Any` (the `S1` pattern).**

```python
CategoricalValueT = TypeVar("CategoricalValueT", bound=Hashable, default=Any)
# or: bound=object
```

- *Pros*: identical shape to `S1`; `default=Any` is legal for bound TypeVars; widens
  `Categorical[X]` to all hashable category types (which would also cover `Enum`
  categories).
- *Cons*: changes constraint semantics (subtypes become legal — e.g. `Categorical[bool]`
  is rejected by the current constraint list but accepted under `bound=Hashable`); the
  `CategoricalValueT1`-based overloads may need rework; wider than the current "normal
  usage" doctrine.

**Option C — keep `default=object` (status quo).**

- *Pros*: no change; `object` is a defensible "unknown category value" that blocks
  attribute access on the values (strictness).
- *Cons*: the inconsistency with bare `Series` remains.

**Option D — reverse direction: change `S1`'s default to `object`.**

- *Pros*: uniform strictness across all containers.
- *Cons*: contradicts `docs/philosophy.md` and ADR-0002; breaking for essentially all
  unannotated user code; rejected.

### Cross-cutting policies

**Policy 1 — "unknown container element" always falls back to `Any`.**
`Series` stays as-is; `PandasNamedTuple` adopts Option A; `Categorical` adopts Option A
or B. Single-value extraction (`.loc`/`.at`/`.iat`) may remain a separate, deliberate
closed-world axis (`Scalar`), or be reopened under pandas-dev/pandas-stubs#1361. This
is the only policy that extends the existing `docs/philosophy.md` rule without a
breaking change.

**Policy 2 — closed world everywhere.**
All unknown element types resolve to `Scalar`/`object`; `Series` would need to default
to a bound-restricted type instead of `Any`. Rejected on backward-compatibility grounds
(see ADR-0002), recorded here for completeness.

**Policy 3 — hybrid, documented.**
Adopt the status quo as intentional: container projections default to `Any`
(`Series`, `iterrows`, `itertuples(name=None)`); single-value extraction defaults to
`Scalar` (`.loc`/`.at`/`.iat`, and today `itertuples()` attributes); `Categorical`
defaults to `object`. Fix only the most harmful case by moving `itertuples()`
attributes to the container-projection side via Option A, and defer the rest.

### The `Scalar` closed world (pandas-dev/pandas-stubs#1361)

Independent of the default-style question, the `Scalar` union itself is closed:

- **Widen `Scalar` to include `Enum` (and possibly `Decimal`)** — Dr-Irv's caveat:
  requires handling arithmetic for the new members and a large test surface; open to a
  contributor who wants to take it on.
- **Widen `.loc`/`__setitem__` assignment value types** — assignment is more
  permissive than extraction at runtime; `_SetItemValueNotDataFrame` could accept
  `Any`/`object` values without changing extraction types.
- **Keep `cast` as the documented workaround** — `data.loc[:, "a"] = cast(Scalar,
  Thing.A)`; the maintainer's current recommendation.

## Consequences and Open Questions

- If `PandasNamedTuple` Option A is adopted: update
  `tests/frame/test_frame.py` (currently asserts `item.a` is `Scalar`) to assert `Any`,
  and add typed-row tests for `Iterator[PandasNamedTuple[str]]`.
- If `Categorical` Option A is adopted: audit the bare `pd.Categorical` assertions in
  `tests/test_pandas.py` and related files, then run the full 4-checker pipeline to
  confirm the unparameterized constrained generic behaves identically in mypy, pyright,
  pyrefly, and ty.
- `docs/architecture/matrices/02-indexing-and-selection-matrix.md` currently describes
  `DataFrame.loc[row, col]` as returning `Any`, while the stubs return `Scalar`; that
  matrix row should be corrected in a follow-up regardless of the decision here.
- pandas-dev/pandas-stubs#1361 remains an open decision (see the three sub-options
  above); this ADR documents it but does not resolve it.

## Historical References & Provenance

- pandas-dev/pandas-stubs#1892 — `itertuples()` row attributes typed `Scalar`,
  inconsistent with `Series[Any]` elsewhere.
- pandas-dev/pandas-stubs#1361 — `DataFrame.loc` does not like assigning `Enum`s.
- pandas-dev/pandas-stubs#1288 — `Series.eq` rejects non-`SeriesDType` objects
  (`Enum`).
- PR pandas-dev/pandas-stubs#842 — introduced `PandasNamedTuple`; review comment
  (https://github.com/pandas-dev/pandas-stubs/pull/842#discussion_r1436576394) chose
  `Scalar` for consistency with `.loc`.
- PR pandas-dev/pandas-stubs#1748 — introduced `CategoricalValueT` with
  `default=object`; the author noted being "forced to set a default to the TypeVar to
  object", and Dr-Irv had suggested the unknown fallback should be `Any`.
- PR pandas-dev/pandas-stubs#1232 — adopted `default=Any` for `Series`/`Index`
  TypeVars.
- `docs/philosophy.md` — the `Series[Any]` fallback rationale.
- ADR-0002 — generic `Series` and the TypeVar bound hierarchy (including the
  "Defaulting Strategy" controversy: `Any` vs `object`).
- ADR-0011 — indexing and selection semantics for `.loc`, `.iloc`, `.at`, `.iat`.
- PEP 696 — type defaults for type parameters; constrained-TypeVar default rule.
