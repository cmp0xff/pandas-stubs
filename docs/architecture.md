# `Series` and `Index` backing-array typing

This page documents the contributor-facing architecture used to track pandas array
storage. It is a guide for maintaining overloads and tests, not a promise that every
pandas operation preserves its runtime storage.

## Why storage needs its own parameter

`Series` and `Index` were already generic in their scalar type, `S1`, but `S1` alone
cannot tell you what physically backs the values: `int` scalars can come from a
`NumpyExtensionArray`, an `IntegerArray` (pandas' nullable storage), or an
`ArrowExtensionArray`, and those differ in `.dtype`, in what `.values` returns, and in
how missing values are represented. Code that needs the concrete array had no way to
get it from `S1`.

Before this branch, `IndexOpsMixin.array` was typed with a descriptor keyed on `S1`
alone (`pandas-stubs/core/base.pyi`, via `ArrayDescriptor` in
`pandas-stubs/core/indexes/accessors.pyi`). Given only `int`, that descriptor had to
guess a single storage family, and it guessed wrong for every `Series[int]` that
wasn't NumPy-backed. That descriptor has been removed; a second type parameter
replaces it.

## The model

`Series` and `Index` are generic in two parameters, `Series[ScalarType,
BackingArrayType]` / `Index[ScalarType, BackingArrayType]`. `ScalarType` (`S1`) is the
scalar produced by scalar indexing and iteration; `BackingArrayType` (`ArrayT_co`) is
the `ExtensionArray` subclass returned by `.array`. The two are related but not
interchangeable: both `Series[int, NumpyExtensionArray]` and
`Series[int, IntegerArray]` contain integer scalars, while their missing-value and
storage semantics differ.

`ArrayT_co` is declared once, in `pandas-stubs/_typing.pyi`:
`TypeVar("ArrayT_co", bound=ExtensionArray, default=ExtensionArray, covariant=True)`.
Covariance lets a value with known storage be used where unspecified storage is
accepted; the default preserves source compatibility with every one-parameter
annotation that predates this branch (`Series[int]`, `IndexOpsMixin[bool]`, …) and
with the bare `Series` / `Index` spelling:

```python
from pandas.core.arrays.integer import IntegerArray

precise: pd.Series[int, IntegerArray] = pd.Series([1, 2], dtype="Int64")
compatible: pd.Series[int] = precise

reveal_type(compatible.array)  # ExtensionArray
```

## Where the parameter lives

| File | Role |
| --- | --- |
| `pandas-stubs/_typing.pyi` | Declares `ArrayT_co`. |
| `pandas-stubs/core/base.pyi` | `IndexOpsMixin(OpsMixin, Generic[S1, ArrayT_co, GenericT_co])` — owns `.array`, inherited by both `Series` and `Index` rather than redeclared. |
| `pandas-stubs/core/series.pyi` | Constructor/`astype` overloads that select storage; `loc`/`iloc`/`__getitem__` indexer generics that carry it through. |
| `pandas-stubs/core/indexes/base.pyi` | `Index` constructor/`astype` overloads; `to_series`. |
| `pandas-stubs/_stubs_only/__init__.pyi` | `IndexSubclassBase`; the instance-dependent `.values`/`.dtype` descriptors; `_RetainedArrayT`, `_CategoricalSeries`. |
| `core/indexes/{extension,datetimelike}.pyi` | `ExtensionIndex` and the datetime-like mixins — forward all three parameters unchanged. |
| `core/indexes/{range,datetimes,timedeltas,period,interval,category}.pyi` | Leaf classes — each pins a concrete array. |

`IndexOpsMixin` orders its parameters `[S1, ArrayT_co, GenericT_co]`: `S1` and
`ArrayT_co` are what every caller writes (`IndexOpsMixin[int, IntegerArray]`), so they
come first; `GenericT_co` (the NumPy scalar `to_numpy` returns) is mixin-internal and,
having a default, trails. `Series` and `Index` each still declare a trailing
`Generic[S1, ArrayT_co]` alongside their `IndexOpsMixin[S1, ArrayT_co]` base — that
pins the *public* spelling to exactly two parameters and keeps `GenericT_co` out of it.

## Inference at storage-selection points

Constructors and `astype` are the main places where a dtype selects physical storage.
Their overloads map literal dtype arguments and sufficiently specific input types to
both type dimensions. A semantic `Index` result is represented by its dedicated
subclass where one exists.

| Storage family | Constructor or `astype` selector | Scalar type | Backing array |
| --- | --- | --- | --- |
| NumPy | Python/NumPy `bool`, integer, float, complex, bytes, or NumPy string dtype | corresponding Python scalar | `NumpyExtensionArray` |
| Nullable pandas | `"boolean"`, `"Int64"`, `"UInt64"`, or `"Float64"` | `bool`, `int`, or `float` | `BooleanArray`, `IntegerArray`, or `FloatingArray` |
| Arrow | e.g. `"int64[pyarrow]"`, `"float64[pyarrow]"`, an Arrow timestamp dtype | corresponding Python/pandas scalar | `ArrowExtensionArray` |
| String, no explicit dtype | plain string data | `str` | `BaseStringArray` (the common base — construction alone doesn't pick a backend) |
| String, explicit dtype | `"string[python]"` / `"string[pyarrow]"` | `str` | `StringArray` / `ArrowStringArray` |
| Categorical | categorical construction, or `astype("category")` | category value type | `Categorical[value type]` |
| Datetime | datetime-like construction or conversion | `Timestamp` | `DatetimeArray` |
| Timedelta | timedelta-like construction or conversion | `Timedelta` | `TimedeltaArray` |
| Period | `Period` data or `PeriodDtype` construction | `Period` | `PeriodArray` |
| Interval | `Interval` data or interval dtype construction | `Interval[endpoint type]` | `IntervalArray` |

```python
numpy_values = pd.Series([1, 2])
reveal_type(numpy_values)  # Series[int, NumpyExtensionArray]

nullable_values = pd.Series([1, 2], dtype="Int64")
reveal_type(nullable_values)  # Series[int, IntegerArray]

arrow_index = pd.Index([1, 2]).astype("int64[pyarrow]")
reveal_type(arrow_index)  # Index[int, ArrowExtensionArray]

datetimes = pd.Series([pd.Timestamp("2020-01-01")])
reveal_type(datetimes)  # Series[Timestamp, DatetimeArray]
```

These are static mappings. They deliberately depend on inputs a type checker can
distinguish; they do not attempt to execute pandas dtype resolution.

## Propagation and widening

Operations that only select, reorder, or copy existing values return `Self`, keeping
both dimensions, because they cannot change storage: `copy`, `head`, `tail`, `sample`,
`drop`, `dropna`, `drop_duplicates`, `sort_index`, `sort_values`, `take`, `rename`,
`round`. Series slicing, boolean indexing, `.loc`, and `.iloc` carry `ArrayT_co`
through their indexer generics for the same reason. `Index.to_series()` transfers
both `S1` and `ArrayT_co` — the values move into a `Series` unchanged.

Storage widens to the `ExtensionArray` default where the contract makes precise
storage unsafe to promise: generic transforms (`map`, `where`, `replace`, some
arithmetic), whose result depends on the callable or the other operand; reductions
and aggregation pipelines (`groupby`, rolling), where the scalar type may be knowable
but the storage is not; concatenation, where inputs can share a scalar type but carry
different arrays; non-literal or ambiguous dtype arguments to constructors, `astype`,
and conversions; and methods whose runtime behavior can change storage based on
values, not just types.

The scalar dimension can stay precise at these same boundaries —
`Series[int, NumpyExtensionArray].map(str)` is `Series[str]` even though the second
parameter widens. The omitted second argument means `ExtensionArray`, not an
assertion that NumPy storage survived; a fallback overload should widen this way
rather than guess a concrete array it cannot verify.

A nullable integer series keeps `IntegerArray` through a slice:

```python
values = pd.Series([1, 2], dtype="Int64")
selected = values.iloc[:1]

reveal_type(selected)           # Series[int, IntegerArray]
reveal_type(selected.array)     # IntegerArray
reveal_type(selected.values)    # IntegerArray
reveal_type(selected.dtype)     # IntegerDtype
reveal_type(selected.unique())  # IntegerArray
```

Concretely: `.array` returns `ArrayT_co` from `IndexOpsMixin.array`.
`Series.values` returns the retained array for nullable, Arrow, string, categorical,
and interval storage, and a NumPy array for NumPy, datetime, timedelta, and period
storage, matching pandas runtime behavior. `Index.values` is always a NumPy array;
`Index.array` is the storage-aware API. `.dtype` uses the stub-only descriptors below
to pick the matching dtype class. `Series.unique()` returns the retained array where
known (`Series[Any, _RetainedArrayT] -> _RetainedArrayT`); `Index.unique()` generally
returns `Self`.

## The `Index` hierarchy

Public `Index` is deliberately two-parameter — `Index[S1, ArrayT_co]` — because that
is the spelling contributors and users write. But `to_numpy()` needs a third
parameter, the NumPy scalar it returns (`GenericT_co`), not always derivable from `S1`
or `ArrayT_co` alone. Rather than push that onto public `Index`, it is re-introduced
by a private base class:

- `IndexSubclassBase` (in `pandas._stubs_only`, `Generic[S1, ArrayT_co, GenericT_co]`,
  extending `Index[S1, ArrayT_co]`) restates all four `to_numpy` overloads with
  `GenericT_co` in scope. Every concrete `Index` subclass except `MultiIndex`
  descends from it instead of from `Index` directly.
- `ExtensionIndex[S1, ArrayT_co, GenericT_co]` and the `DatetimeIndexOpsMixin` /
  `DatetimeTimedeltaMixin` mixins forward all three parameters without pinning any.
- Leaf classes pin storage:

  | Leaf class | `S1` | `ArrayT_co` | `GenericT_co` |
  | --- | --- | --- | --- |
  | `RangeIndex` | `int` | `NumpyExtensionArray` | `np.int64` |
  | `DatetimeIndex` | `Timestamp` | `DatetimeArray` | `np.datetime64` |
  | `TimedeltaIndex` | `Timedelta` | `TimedeltaArray` | `np.timedelta64` |
  | `PeriodIndex` | `Period` | `PeriodArray` | `np.object_` |
  | `IntervalIndex` | `IntervalT` | `IntervalArray` | `np.object_` |
  | `CategoricalIndex` | `S1` | `Categorical[object]` | `Any` |

This threading is what makes inherited `.array`, storage-preserving methods, and
`to_series()` precise on every leaf class without duplicating each member per class.

Some runtime properties can't be expressed with a normal property return type because
the result depends on the instance's type arguments. Private, `type_check_only`
descriptors in `pandas._stubs_only` — `_SeriesValuesDescriptor`,
`_SeriesDtypeDescriptor`, `_IndexDtypeDescriptor`, `_CatDescriptor` — provide
overloaded `__get__` signatures for `Series.values`, `Series.dtype`, and
`Index.dtype`. They are stub implementation details and must not become public
pandas API.

## Known limitations

- `MultiIndex(Index)` is unparameterized, so every `MultiIndex` resolves to
  `Index[Any, ExtensionArray]` — its levels can carry heterogeneous scalar and
  storage types a single pair of type parameters cannot represent.
- `CategoricalIndex` pins `Categorical[object]`, so `.array` loses the category value
  type: `pd.CategoricalIndex(["a", "b"]).array` is `Categorical[object]`, not
  `Categorical[str]`. `_CategoricalSeries` (the
  `Series[CategoricalValueT, Categorical[CategoricalValueT]]` alias in
  `pandas._stubs_only`) keeps that value type on the `Series` side; `Index` has no
  equivalent yet.
- Adding the storage parameter forced `@final` off four `NDFrame` methods —
  `set_flags`, `__neg__`, `__pos__`, `convert_dtypes` — in `pandas-stubs/core/generic.pyi`,
  so `Series` can re-declare each with a storage-widening return type instead of
  `NDFrame`'s `Self`. This is a real loosening of a base contract: nothing stops
  another `NDFrame` subclass's stub from overriding these for an unrelated reason.

## Adding a storage family

1. Add a constructor overload in `series.pyi` and `indexes/base.pyi` that selects it
   from a literal dtype or a sufficiently specific input type.
2. Add a matching `astype` overload in both files.
3. Add an overload to `_SeriesDtypeDescriptor` / `_IndexDtypeDescriptor` in
   `_stubs_only/__init__.pyi` so `.dtype` resolves to the right dtype class.
4. If `.values` retains the array, add an overload to `_SeriesValuesDescriptor` and an
   entry to the `_RetainedArrayT` bound.
5. Add a `Series.unique()` overload if the array is retained through `unique()`.
6. Add assertions to `tests/series/test_backing_array.py` and
   `tests/indexes/test_backing_array.py` covering construction, `.array`, `.values`,
   `.dtype`, and `unique()`.
7. Run `poetry run poe test_all`.
