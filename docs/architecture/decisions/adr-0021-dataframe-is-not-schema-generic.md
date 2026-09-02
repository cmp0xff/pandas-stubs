---
status: accepted
date: 2026-09-02
deciders: [Dr-Irv, twoertwein, MarcoGorelli, loicdiridollou, cmp0xff]
consulted: [typing-sig]
informed: [pandas-stubs contributors]
---

# ADR-0021: DataFrame Is Not Schema-Generic (TypedDict-Style Schema)

## Context and Problem Statement

Several iterations of the same request ask to make `pd.DataFrame` generic over a
*record schema* so a type checker can do two things:

1. **Carry the schema in signatures** — `df: DataFrame[Person]` names the shape of a
   frame wherever it appears in a function or return annotation.
2. **Recover per-column element types on indexing** — `df["age"]` resolves to
   `Series[int]` rather than `Series[Any]`.

The desired API shape is:

```python
class Person(TypedDict):
    age: int
    name: str

df: DataFrame[Person]
age = df["age"]   # hoped: Series[int]
```

This ADR records the conclusion drawn from attempting to express that construct in
pure PEP 484/695 typing: **tier 1 (schema carrying) is expressible; tier 2 (per-column
pinpointing) is not, and requires codegen or a checker plugin.** It is the standing
architecture answer to PR pandas-dev/pandas-stubs#295, PR pandas-dev/pandas-stubs#1190,
PR pandas-dev/pandas-stubs#1548, and PR pandas-dev/pandas-stubs#1566.

## Decision Drivers

- **Expressiveness**: `DataFrame[Person]` should name the schema in a signature
  (satisfies #295).
- **Per-column type recovery**: `df["age"]` should yield `Series[int]` where the key is a
  known column (#1190, #1566).
- **Soundness**: the mechanism must be real PEP 484/695 typing and be accepted uniformly
  by mypy, pyright, pyrefly, and ty — not a checker-specific extension that the others
  reject.
- **Backward compatibility**: a bare `DataFrame` must stay valid, exactly as bare
  `Series` stays valid (see ADR-0002).

## Considered Options

1. **Generic over a `TypedDict` bound** — `TypeVar("S", bound=TypedDict)`.
   - *Pros*: reads naturally as "a DataFrame over a schema".
   - *Cons*: not expressible (see the three spec-level facts below).
2. **Generic over a phantom schema parameter** — `class DataFrame(Generic[Schema])` that
   carries `DataFrame[Person]` but returns `Series[Any]` from indexing. *(Chosen for the
   pure-typing tier.)*
   - *Pros*: pure typing, uniformly accepted, satisfies #295.
   - *Cons*: `df["age"]` collapses to `Series[Any]`.
3. **Concrete `Literal` overloads (codegen)** — one `@overload` per known column key.
   - *Pros*: exact `Series[int]` / `Series[str]` resolution; real static checking (#1190).
   - *Cons*: requires generating the overload set; loses precision on unknown keys.
4. **Checker plugin reading the schema's `__annotations__`** — a checker-specific
   solution.
   - *Pros*: precise without codegen; no stub bloat.
   - *Cons*: not pure typing; not portable across the 4-checker pipeline.
5. **Do nothing** — leave `DataFrame` non-generic.
   - *Cons*: ignores the recurring request and the schema-carrying tier that *is* free.

## Decision Outcome

Adopt **tier 1** — a phantom generic parameter — as the only pure-typing option, and
accept that **per-column enforcement is out of reach for pure PEP 484/695 typing**. The
following two spec-level facts make the naive "generic over a TypedDict" impossible, and
they are independent of any single checker:

### Spec-level fact 1: a `TypedDict` cannot be a `TypeVar` bound

A `TypedDict` is a special typing form, not a real class and not a `dict` subtype, so it
cannot appear as a `TypeVar` bound.

```python
S = TypeVar("S", bound=TypedDict)
# mypy: Variable "typing.TypedDict" is not valid as a type  [valid-type]
```

### Spec-level fact 2: a `TypeVar` cannot be subscripted

`S[key]` has no meaning under PEP 484/695. There is no operation that recovers "the type
of field `key` of schema `S`"; type-level indexing requires `Literal` keys against a
*concrete* class, not a type variable.

```python
class DataFrame(Generic[S]):
    def __getitem__(self, key: str) -> Series[S[key]]: ...
# mypy: Type variable "S" used with arguments  [valid-type]
```

### Spec-level fact 3: schema-aware per-column returns are not pure typing

Because facts 1 and 2 close the "generic over a schema" path, per-column returns
(`__getitem__` / `__getattr__` / `itertuples`) can only become schema-aware via **concrete
`Literal` overloads (codegen)** or a **checker plugin** reading the schema's
`__annotations__`. Neither is "pure typing".

### Two full-tiers

| Tier | Pure typing? | `df["age"]` | Buys |
| :--- | :--- | :--- | :--- |
| Carry the schema — `DataFrame[Person]` | ✅ trivial | `Series[Any]` | names schema in signatures (#295) |
| Enforce per-column types — `df["age"] -> Series[int]` | ❌ codegen/plugin | `Series[int]` | real static checking |

## Minimal Example

Self-contained (no pandas / pandas-stubs / numpy); verified with `mypy 2.3.1 -c`:

```python
from typing import Any, Generic, Literal, TypeVar, TypedDict, overload

T = TypeVar("T")

class Series(Generic[T]):                    # stand-in for pandas.Series
    def sum(self) -> T: ...

class Person(TypedDict):
    age: int
    name: str

# S = TypeVar("S", bound=TypedDict)                       # ❌ not a valid bound
# class DataFrame(Generic[S]):
#     def __getitem__(self, key: str) -> Series[S[key]]:  # ❌ cannot subscript a TypeVar

Schema = TypeVar("Schema")
class DataFrame(Generic[Schema]):            # ✅ Tier 1: phantom schema param
    def __getitem__(self, key: str) -> Series[Any]: ...
# df: DataFrame[Person] ; df["age"] -> Series[Any]

class PersonFrame:                            # ✅ Tier 2: codegen Literal overloads
    @overload
    def __getitem__(self, key: Literal["age"]) -> Series[int]: ...
    @overload
    def __getitem__(self, key: Literal["name"]) -> Series[str]: ...
    @overload
    def __getitem__(self, key: str) -> Series[Any]: ...
    def __getitem__(self, key: str) -> Series[Any]: ...
```

The ❌ lines error exactly as quoted; the ✅ tiers reveal `DataFrame[Person]` /
`Series[int]` / `Series[str]` / `Series[Any]`. Because the failure is at the spec level,
pyright, pyrefly, and ty agree with mypy.

## Consequences

- **Positive**: `DataFrame[Person]` names the schema anywhere a `DataFrame` appears in a
  signature, satisfying the core of #295.
- **Negative / Neutral**: for the pure-typing tier, `df["col"]` stays `Series[Any]`, so a
  frame's indexer gives no more element-type information today than in ADR-0002's original
  "Dynamic DataFrame column indexing" consequence.
- **Negative / Neutral**: per-column precision (`df["age"] -> Series[int]`) costs codegen
  or a checker plugin, both of which are out of scope for the stubs themselves and would
  not follow the 4-checker pipeline.
- **Guidance**: do not add a `bound=TypedDict` schema generic to `DataFrame`; prefer
  explicit `Literal` overloads where a caller genuinely needs column precision.

## Historical References & Provenance

- **Primary / related pull requests & issues**:
  - pandas-dev/pandas-stubs#295: DataFrame with generic type.
  - pandas-dev/pandas-stubs#1190: `pd.DataFrame[OrderSchema]`.
  - pandas-dev/pandas-stubs#1548: schema-generic DataFrame request.
  - pandas-dev/pandas-stubs#1566: closed PR proposing schema-generic DataFrame.
  - pandas-dev/pandas-stubs#1892: DataFrame typing discussion context.
- **Cross references**:
  - ADR-0002 — Generic Series and TypeVar Bound Hierarchy (the `Series[Any]` fallback for
    dynamic indexing).
  - ADR-0011 — Indexing and Selection Semantics for Accessors (the accessor-return model
    that tier 2 would need to extend).

## Controversies and Open Questions

1. **Worth the codegen?** Whether a future schema-aware `DataFrame` should generate
   `Literal` overloads from a schema (mirroring the `Literal`-key pattern in the minimal
   example) remains open; no one has taken on the generator.
2. **Checker plugin route**: if a plugin approach is ever pursued, it must be gated behind
   the 4-checker pipeline's `pyright`/`pyrefly`/`ty` support rather than relying on mypy
   alone.
3. **PEP 695 `TypeVar` parameters**: a future PEP that adds a "field-of-type-variable"
   operator could reopen tier 2; until such a PEP lands, the verdict above stands.
