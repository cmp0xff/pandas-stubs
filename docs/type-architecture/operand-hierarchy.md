# Operand hierarchy

The stubs model a useful direction for binary operators: a type should not claim a
higher-tier type as a normal forward operand when that higher tier owns the relevant
result shape. Concretely, a class accepts operands at its own tier or below in the
annotated `other` parameter of a forward binary dunder; a higher-tier operand needs a
counted allowance. This is a signature-design constraint, not a description of Python's
full runtime method-resolution rules. It is about operand scope, not about containment:
the tiers span scalars and array-like values that are not containers in the
`typing.Container` sense.

## Tiers

| Tier | Registered classes | Normal operand scope |
| --- | --- | --- |
| 0 | `Timedelta`, `Timestamp`, `Period`, `Interval`, `NAType` | Scalar values |
| 1 | `ExtensionArray` | Scalars and array-like values |
| 2 | `Index`, `MultiIndex`, and Index subclasses discovered through base chains | Scalars, array-like values, and `Index` |
| 3 | `Series` | Scalars, array-like values, `Index`, and `Series` |
| 4 | `DataFrame` | Scalars, lower-dimensional types, and `DataFrame` |

The tiers describe the ownership convention used in the current operator annotations;
they do not classify every pandas object or every method. `CLASS_TIERS` in
`scripts/operand_hierarchy/model.py` holds the registered classes, and Index subclasses
are discovered through their bases rather than listed. Other scalar and array-like values
can appear in annotations, but the checker scans only these registered declaring classes.

`MultiIndex` is an `Index` subclass in the stubs and declares no forward binary dunders of
its own, so it shares `Index`'s operand scope. Its multidimensional labels are data
semantics, not operator ownership; the checker scans `MultiIndex` directly as a guard
against future higher-tier forward operands.

## Cross-tier lookup examples

When reviewing a cross-tier expression, start with the operand type whose result shape is
being represented, then inspect its forward and reflected overloads and a focused test.
For example:

| Expression to review | Relevant stub surface |
| --- | --- |
| Scalar and `Index` | `Index` operator overloads, plus the scalar's own forward overloads |
| Scalar and `Series` | `Series` operator overloads, plus the scalar's own forward overloads |
| `Index` and `Series` | `Series` operator overloads, plus `IntervalIndex`'s comparison overloads |
| `Series` and `DataFrame` | `DataFrame` operator overloads |

The scalar rows are not one-sided: a scalar such as `Timedelta` declares its own forward
overloads for the array-like operands it broadcasts over, and those overloads are part of
the surface to review. [Scalar and Index-subclass overloads](#scalar-and-index-subclass-overloads)
states why the checker permits them and where the temporary list that records them lives.

These are lookup examples for the stubs, not a claim about the exact runtime dispatch
sequence for every operand pair.

## Structural invariant

The checker enforces three restrictions in the current stubs:

1. A `ScalarArrayIndex*` alias must not directly or transitively reference `Series` or
   `DataFrame`.
2. A `ScalarArrayIndexSeries*` alias must not directly or transitively reference
   `DataFrame`.
3. Every forward binary dunder declared directly on a scanned class must declare an
   `other` operand and must not directly or transitively reference an operand of a
   strictly higher tier.

The checker scans the tier-0 scalars `Timedelta`, `Timestamp`, `Period`, `Interval`, and
`NAType`; the tier-1 array-like `ExtensionArray`; `Index`, `MultiIndex`, and every `Index`
subclass it resolves by name, which brings in `IntervalIndex`, `TimedeltaIndex`,
`DatetimeIndex`, `PeriodIndex`, `RangeIndex`, `CategoricalIndex`, and the `Index` mixins;
and `Series` and `DataFrame`. A qualified terminal name counts, so `pd.DataFrame` in an
`other` annotation is read exactly like `DataFrame`, and it counts whether it spells the
operand or a `TypeAlias` of it, so `types.Higher` resolves where
`Higher: TypeAlias = DataFrame` does. Every definition of a `TypeAlias` name is followed,
so a name reused across modules cannot hide a reference. Every definition of a scanned
class name is checked, so a duplicate class definition cannot hide a violation behind a
later clean one. An operand spelling the tier model knows is read at that class's tier, so
`TimedeltaIndex` in an `other` annotation is the tier-2 operand `Index`;
`Interval.__gt__(IntervalIndex)` is therefore a cross-tier overload, and its diagnostic
names the canonical operand `Index`. The temporary exception list is keyed by that operand
name rather than by the spelling, so one `Index` key covers `IntervalIndex`,
`TimedeltaIndex`, and `MultiIndex` alike.

This includes arithmetic, bitwise, comparison, and matrix-multiplication dunders. The
checker deliberately excludes reflected dunders such as `__radd__`; those signatures
need their own review and focused tests. See
[Operator signatures](operator-signatures.md#dunder-parameters) for which dunders the
checker scans and how it reads the `other` operand, and
[Reflected dunders](operator-signatures.md#reflected-dunders) for why the excluded ones
are still reviewed.

## Scanned methods

Scanned: arithmetic (`__add__` through `__pow__`, including `__matmul__` and `__divmod__`),
bitwise (`__lshift__`, `__rshift__`, `__and__`, `__or__`, `__xor__`) and comparisons
(`__lt__`, `__le__`, `__eq__`, `__ne__`, `__gt__`, `__ge__`). Reflected and in-place methods
are not scanned, so `__radd__` is outside the check while `__rshift__` is scanned.

`REQUIRED_STUB_FILES` lists every file that may declare a checked class, so moving a class
to a new file requires updating it.

## A rejected signature, traced

```python
class Series:
    def __sub__(self, other: DataFrame, /) -> Series: ...
```

1. `main()` calls `check_operand_hierarchy`, which calls `StubTree.load`. That parses every
   stub, collecting aliases and bases everywhere and classes from the required files only.
2. `check_operand_hierarchy` calls `check_class("Series", observed)`. `DataFrame` (tier 4)
   is above `Series` (tier 3), so it is in the higher-tier map.
3. `_other_parameter` returns `other`, and `StubTree.references` matches `DataFrame` by
   terminal name. The counter records `("Series", "__sub__", "DataFrame")` once.
4. With no allowance, expected is 0 and observed is 1. `check_operand_hierarchy` prints to
   stderr and returns False; `main()` exits 1.

```text
ERROR: Series.__sub__ higher-tier operand DataFrame: expected 0 overload(s), observed 1; review the signature or update scripts/operand_hierarchy/exceptions.py.
```

`test_guide_traced_example` runs this example, so the trace above cannot drift from the checker.

## Scalar and Index-subclass overloads

Some legitimately cross-tier forward overloads are declared on the lower tier. The
checker permits them through a temporary exception list, `FORWARD_DUNDER_EXCEPTIONS` in
[`scripts/operand_hierarchy/exceptions.py`](../../scripts/operand_hierarchy/exceptions.py).
The list is a temporary debt with an empty-set target: keys and counts are expected to
shrink, and an empty file is the end state. A key is deleted when its overloads no longer
need it — because the signatures changed or because the rule now permits the shape. Each
key is `(class, dunder, forbidden)` and maps to a positive count; there are no wildcards.
The count follows these rules:

- Each declaration contributes once per distinct canonical higher tier, regardless of
  alias spelling: a declaration naming two spellings of `Index` counts once, while
  `Index | Series` on a scalar counts once per operand.
- Both branches of a conditional count, even when a type checker selects only one.
- Reordering declarations or using an equivalent alias does not change a count.
- Observed and recorded counts must match exactly: a new combination, increase, decrease
  or unused entry fails until the registry is updated.

For example, `("Period", "__sub__", "Index"): 2` records two declarations. This page
states the policy and the target; it does not repeat the list.

These overloads do not violate the rule, because the scalar's implementation is the
dispatch entry point for `scalar op array`. Python calls the scalar's forward dunder
first, pandas broadcasts the scalar over the array-like operand, and the stub declares the
result — an `Index`, a `TimedeltaIndex`, or a `Series` — on the scalar side, because that
is where the runtime operation lives. The operand tier still owns the result shape; the
lower tier declares the entry point that produces that shape rather than claiming the
operand scope itself. `IntervalIndex` is the same shape two tiers up: its comparison
overloads against a `Series` return `Series[bool]`, so the result shape belongs to
`Series` and the `Index` side declares the overload that pandas dispatches to.

Most of the current keys are scalar dispatch-entry-point overloads. The retirement tracked
in pandas-dev/pandas-stubs#2023 encodes that dispatch rule so those overloads are
permitted by the rule rather than by counted allowances, treats the `IntervalIndex`
comparison keys the same way, and moves `Series.__matmul__(DataFrame)` to
`DataFrame.__rmatmul__(Series)`; after those steps the registry and count mechanism can be
deleted.

## Matrix multiplication

`Series.__matmul__(DataFrame)` is the only key for `Series`, which otherwise keeps its
operand scope. It is listed rather than omitted from the scan:
the stubs return a `Series` for this matrix-multiplication overload. Pandas supports the
expression at runtime, and `tests/series/test_series.py::test_types_dot` exercises the
forward operation. Removing the overload would therefore regress valid code unless pandas
changes which operand owns this runtime operation.

The measured exit is to add a `DataFrame.__rmatmul__(Series)` overload and remove this
key, moving the result shape to the tier that owns it. `pandas-stubs/core/frame.pyi` does
not declare that overload today; pandas-dev/pandas-stubs#2023 tracks the step.

## Changing the list

The intended direction is one-way: keys and counts shrink, and the target is no list at
all. The checker rejects every higher-tier operand outside the dispatch rule.
pandas-dev/pandas-stubs#2023 tracks the CI ratchet that will reject new keys and count
increases; until it lands, an addition or increase needs the review argument below. Never
raise a count merely to silence a failure.

Changing the list normally means removing an entry. An addition or count change requires
all of the following in the same review:

1. Argue it in the review and in the commit message, next to the overload that needs it.
   The list carries no per-key rationale, so the reviewer must see the key, the stub
   overload that requires it, and the evidence — a runtime expression or a focused test —
   that removing the key would regress valid code.
2. Add or update the key and count in `scripts/operand_hierarchy/exceptions.py`: a
   `(class, dunder, forbidden)` tuple with a positive count.
3. Add the focused test that covers the overload in
   `tests/test_check_operand_hierarchy.py`.
4. Use it. The checker compares observed combinations with the registry exactly, so a
   key whose recorded count no longer matches fails and must be removed or corrected. A
   key that no scanned site matches fails with `expected N overload(s), observed 0`. The
   `architecture` CI job runs that comparison, so a key cannot outlive the overloads that
   needed it — deleting a scanned class or narrowing an operand surfaces the dead keys by
   name instead of leaving them permitting nothing.

## Scope limits

The checker's reading of a signature has these limits:

- **Reflected dunders.** `__radd__` and its siblings run only after the higher-tier left
  operand declined the forward operation, so the forward rule does not apply to them; see
  [Reflected dunders](operator-signatures.md#reflected-dunders).
- **Tier-1 spellings the tier model cannot resolve.** Tier 1 is registered through the
  `ExtensionArray` ABC, so the check reaches a tier-1 operand whenever the annotation
  spells `ExtensionArray`, or a `TypeAlias` chain such as `ArrayLike` or `ListLike` that
  reaches it. A concrete array-like such as `Categorical` is not read at tier 1: the
  checker inherits through base classes for `Index` subclasses only, so an annotation that
  names `Categorical` without an alias chain to `ExtensionArray` is an unknown spelling.
- **String-literal annotations.** The checker reads syntax trees rather than resolving
  forward references, so an operand written as a string literal is not seen.
- **Operand spelling in another parameter.** It reads one parameter named `other` per
  dunder; `other` may be positional, keyword-only or variadic, but it must be annotated. A
  scanned dunder that renames its operand fails rather than being silently skipped.
- **Unions and generic arguments.** Names match by terminal name (`pd.DataFrame` is
  `DataFrame`); unions, qualified names and generic arguments are searched syntactically.
- **Alias expansion.** Only `TypeAlias`-annotated aliases (bare or qualified) are
  expanded, transitively. Aliases resolve globally by terminal name, not by scope, so
  same-named aliases contribute; duplicates are kept and cycles terminate.
- **Conditional and nested declarations.** Both branches of class-level and module-level
  `if` statements are scanned without evaluating conditions. Nested functions and classes are
  not entered, and inherited methods are not resolved.
- **Other unsupported forms.** Implicit aliases, PEP 695 `type` aliases, TypeVar bounds,
  import renaming, async methods, callable class attributes and other class families are not
  read.
- **Passing is not proof.** The check validates signature structure only; type-checker and
  runtime tests remain necessary.

## Running the checks

- `poetry run poe pytest_architecture` runs the synthetic cases, anchor validation and a
  strict check of the real stubs. CI runs it in a dedicated Ubuntu job on Python 3.11.
  `poe test` and `poe test_all` include it once; ordinary `poe pytest` excludes it.
- `python -S scripts/check_operand_hierarchy.py` is the stdlib-only check. It prints
  combination and occurrence counts. Exit 0 is success, 1 is a contract violation. A missing
  required file is a violation; syntax errors name the file and surface as exceptions.
