# Intentional type-ignore comments

Most `# type: ignore` / `# pyright: ignore` / `# pyrefly: ignore` / `# ty: ignore` comments
in this project's stubs are debt: they exist because a checker currently disagrees with a
stub that could, in principle, be written more precisely, and they are tracked with a
removal condition in `docs/_debt.md`.

This file catalogs the other kind: ignores that are permanent by design. Nothing a checker
release does will let these be removed, because the "correct" signature is inexpressible —
the pandas runtime API itself is private at the point being referenced, or the overload
overlap reflects a genuine subtype relationship rather than an accident. Adding one of
these ignores defensively is not possible either way:
`reportUnnecessaryTypeIgnoreComment` (pyright) and `warn_unused_ignores` (mypy) reject an
ignore that the checker does not need.

## Private-symbol imports (`reportPrivateUsage`)

`reportPrivateUsage` is a pyright-only diagnostic — mypy has no equivalent rule. The stubs
must reference classes that pandas (or the standard library) deliberately does not export:
`@type_check_only` descriptor classes in `pandas._stubs_only`, and real private
implementation classes such as `pandas.core.indexing._LocIndexer`. No checker change makes
an underscore-prefixed name public; the ignore is permanent.

Convention: put the ignore on the `import` line, with a comment immediately above the
`from ... import (...)` block. Use the plural wording when the block imports more than one
private symbol, singular when it imports one:

```python
# The classes are private in pandas implementation. We have to ignore the private usage in the stubs.
from pandas.core.indexing import _AtIndexer  # pyright: ignore[reportPrivateUsage]
...
```

```python
# The class is private in pandas implementation. We have to ignore the private usage in the stubs.
from pandas.core.indexing import _IndexSlice  # pyright: ignore[reportPrivateUsage]
```

Sites (repo-wide):

| File:line | Symbols |
| --- | --- |
| `core/series.pyi:131` (comment), `:132-136` | `_AtIndexer`, `_IndexSliceTuple`, `_LocIndexer`, `_iAtIndexer`, `_iLocIndexer` |
| `core/frame.pyi:64` (comment), `:65-69` | same five |
| `io/formats/style_render.pyi:21` (comment), `:22` | `_IndexSlice` |
| `_libs/tslibs/timestamps.pyi:9` (comment), `:10` | `datetime._IsoCalendarDate` (private in the standard library, not pandas — same reasoning) |
| `core/series.pyi:71-72` (comment), `:65,68,73,74` | `_SeriesDtypeDescriptor`, `_SeriesValuesDescriptor`, `_CatDescriptor`, `_RetainedArrayT` |
| `core/indexes/base.pyi:38` (comment), `:40` | `_IndexDtypeDescriptor` |

The last two rows were added by the `Series`/`Index` backing-array generic (storage-tracking
second type parameter): the stubs describe `.dtype`/`.values`/`.unique()`/`.cat` in terms of
descriptor classes that live in `pandas._stubs_only` specifically so they are not part of
the public pandas API. The `series.pyi` comment names all four symbols explicitly rather than
sitting immediately above the first one: `isort` (`combine_as_imports` + `force_grid_wrap`)
deterministically relocates any comment placed earlier in that run of four single-symbol
imports down to just above the last two, so the comment says "above and below" instead of
relying on position.

## Unhashable containers (`__hash__: ClassVar[None]`)

`Series`, `Index`, `Categorical`, `DataFrame` and related containers are unhashable.
Expressing that in a stub means overriding the inherited `__hash__` — a `Callable` — with
`ClassVar[None]`, which every checker correctly reports as an incompatible override of
`object.__hash__`. There is no other way to say "this subclass is unhashable" in the type
system, so the ignore is permanent.

Sites: `_typing.pyi:1242`, `core/col.pyi:15`, `core/generic.pyi:70`,
`core/frame.pyi:382`, `core/arrays/categorical.pyi:53`, `core/indexes/base.pyi:183`,
`core/series.pyi:406`.

## Elementwise comparison dunders

`Index.__eq__`/`__ne__`/`__le__`/`__ge__`/`__lt__`/`__gt__` return `np_1darray_bool`, and the
same methods on `Series` return `Series[bool]`. Both diverge from `object`'s comparison
dunders (`__eq__(self, other: object) -> bool`), which every checker treats as a signature
each dunder must remain compatible with. That divergence is not a bug to fix — pandas'
`==`/`!=`/`<`/`<=`/`>`/`>=` on a container are elementwise, not identity, comparisons, so a
`bool`-returning signature would be actively wrong. The ignore is permanent.

Sites: `core/indexes/base.pyi:892-902`; `core/series.pyi:2691,3004-3019,3474`.

## Overload overlap from a real subtype relationship

`overload-overlap` diagnostics flag two overloads whose input domains intersect. Usually
that is a mistake. In the sites below it is not: a narrower overload is given first,
deliberately, because its input is a genuine subtype of the following overload's input, and
it returns a strictly more precise result. This is the standard "precise overload before
general overload" pattern — checkers cannot distinguish it from an accidental overlap, so
the ignore is permanent, not something a future checker release resolves.

Three sub-patterns recur:

- **Numeric tower** (`bool <: int <: float`, per the typing spec) — `Series.diff` and
  `Index.diff` each give `bool`, `int`, and `float` overloads a progressively wider return,
  and each pair of adjacent levels overlaps by construction:

  ```python
  @overload
  def diff(self: Series[bool], periods: int = ...) -> Series[int]: ...
  @overload
  def diff(self: Series[int], periods: int = ...) -> Series[int]: ...  # overlaps the bool case
  @overload
  def diff(self: Series[float], periods: int = ...) -> Series[float]: ...
  ```

- **Array-class inheritance** — the `astype("string")` overload on `Series` and `Index`
  gives `StringArray` a more precise overload than the general `BaseStringArray` case, and
  `StringArray <: BaseStringArray`.

- **Universal-subtype literal** — the empty-sequence branch of `Series.__new__` types the
  input as `Sequence[Never]`, which is a subtype of every `Sequence[X]` and therefore
  overlaps every other constructor overload by construction.

Sites: `core/series.pyi` `diff` (4 lines), `astype` string branch (1 line), `__new__`
empty-sequence branch (1 line); `core/indexes/base.pyi` `diff` (4 lines), `astype` string
branch (2 lines). 12 lines total.

## How to tell if your new ignore belongs here

Ask: to remove this ignore, does the **checker** have to change, or does the **stub author**
have to change something?

- If a checker improvement (recognizing a literal partition, understanding a subtype chain,
  materializing a generic default) would make the ignore unnecessary — or the stub could be
  restated to avoid the overlap without weakening the API — it's debt: put it in
  `docs/_debt.md` with a removal condition.
- If the ignore exists because of something structurally true (a class really is private, a
  container really is unhashable, comparison really is elementwise, one overload's input
  really is a subtype of another's) that no stub rewrite or checker fix changes, it belongs
  here instead.
