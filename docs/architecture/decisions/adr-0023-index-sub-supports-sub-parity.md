---
status: accepted
date: 2026-09-03
deciders: [Dr-Irv, twoertwein, MarcoGorelli, loicdiridollou, cmp0xff]
consulted: [typing-sig]
informed: [pandas-stubs contributors]
---

# ADR-0023: Reflected Subtraction Overload Parity (`SupportsRSub`/`SupportsSub`)

## Context and Problem Statement

The arithmetic dunder families on `Index` are not symmetric in how they expose
element-type precision for an **external** (non-`pandas`) operand.

`__add__`/`__mul__` carry a `_typeshed.Supports*` reflected-dunder overload in
addition to their internal `Supports_Proto*` overloads (ADR-0009):

- `__add__` → `SupportsRAdd` / `__radd__` → `SupportsAdd`
- `__mul__` → `SupportsRMul` / `__rmul__` → `SupportsMul`

Each is positionally `self: Index[S2_contra], other: SupportsR<op>[S2_contra, S2_NSDT] | Sequence[...]`
and returns `Index[S2_NSDT]`. This lets the `_typeshed` protocol capture the
operand's reflected-return **scalar** dtype, giving `Index[S2_NSDT]` precision for
an operand that implements the reflected dunder itself (e.g. a custom scalar, an
ExtensionArray, or a `Series` whose reflected operation lowers to a scalar).

`__sub__`/`__rsub__` had only the internal `Supports_ProtoSub`/`Supports_ProtoRSub`
overloads (`self: Supports_ProtoSub[T_contra, S2], other: T_contra | Sequence[T_contra] -> Index[S2]`).
Those protocols are `self`-bound: they describe the *left* operand (`self`) that
contains an element of the given dtype, and derive the result from `self`'s own
element type. They cannot carve out the case where the precision comes from the
*external right operand's* reflected dunder. As a result an external operand with
a reflected `__sub__`/`__rsub__` fell through to the untyped / operator-error path,
while the same shape through `+`/`*` was pinned to a concrete `Index[S2_NSDT]`.

## Decision Drivers

- **Parity**: `-` should resolve external operands with the same precision as `+`
  and `*`.
- **Mirror an already-accepted shape**: `__add__`/`__mul__` already encode the
  `Supports*` reflected-dunder idiom; a new sub overload should match it exactly so
  the overload chains stay parallel and review is mechanical.
- **Positional-or-keyword-only compatibility**: the overload is declared in the
  positional-only (PEP 570) style used across the operator family.
- **4-checker portability**: mypy, pyright, pyrefly, and ty must each resolve the
  same overload independently; any checker divergence must be recorded rather than
  papered over with per-checker ignores.

## Considered Options

1. **Add `_typeshed.SupportsRSub`/`SupportsSub` overloads mirroring `__mul__`/`__rmul__`** *(chosen)*.
   - *Pros*: exact parity with `+`/`*`; small, mechanical diff; reuses the
     already-accepted `S2_NSDT` result bound; no new protocol surface.
   - *Cons*: overload chain is ordering-sensitive, and the `_typeshed` protocols
     match structurally — a checker that greedily matches a *container* type (e.g.
     `Index[int]`, which also has a reflected dunder) against `SupportsRSub` can
     select it for a `self: Index[int]`, `other: Index[int]` call. This is the one
     behavior to verify (see Consequences).
2. **Extend the internal `Supports_ProtoSub`/`Supports_ProtoRSub` protocols** to
   encode the reflected-return precision.
   - *Pros*: no new overload.
   - *Cons*: those protocols are `self`-bound by design (ADR-0009); retrofitting an
     external-operand dimension into them would blur the distinction ADR-0009 draws
     and is not mirrored by `__add__`/`__mul__`. Rejected for symmetry.
3. **Leave as-is**; document that `-` is intentionally less precise than `+`/`*`.
   - *Cons*: an inconsistency users already hit through `+`/`*`; no reason for `-`
     to differ. Rejected.

## Decision Outcome

Add two overloads to `pandas-stubs/core/indexes/base.pyi`, each positioned
immediately after the internal `Supports_Proto*` overload and before the concrete
numpy/`Index` overloads (the same slot `__mul__`/`__rmul__` use):

```python
# __sub__: the external operand's reflected __rsub__ gives the result dtype
@overload
def __sub__(
    self: Index[S2_contra],
    other: (
        SupportsRSub[S2_contra, S2_NSDT]
        | Sequence[SupportsRSub[S2_contra, S2_NSDT]]
    ),
    /,
) -> Index[S2_NSDT]: ...

# __rsub__: the external operand's own __sub__ gives the result dtype
@overload
def __rsub__(
    self: Index[S2_contra],
    other: (
        SupportsSub[S2_contra, S2_NSDT] | Sequence[SupportsSub[S2_contra, S2_NSDT]]
    ),
    /,
) -> Index[S2_NSDT]: ...
```

`SupportsSub` and `SupportsRSub` are added to the existing `from _typeshed import (...)`
block.

### Result bound

The result is bound to `S2_NSDT` (`_typing.pyi`:

```python
SeriesDTypeNoStrDateTime: TypeAlias = (
    bytes | bool | int | float | complex | NpDtypeNoStr | ExtensionDtype
    | Period | Interval | CategoricalDtype | BaseOffset
)
S2_NSDT = TypeVar("S2_NSDT", bound=SeriesDTypeNoStrDateTime)
```

This excludes `str`/`datetime` element types, matching the constraint that
`Index` arithmetic never returns a string or date/time-indexed result). The value
is the operand's reflected-return **scalar** dtype, so it resolves only when the
operand's `__rsub__`/`__sub__` returns a scalar element type rather than another
container — which is precisely the case the `Supports_Proto*` overloads cannot
express.

## Consequences

- **Positive**: an external operand with a reflected `__sub__`/`__rsub__` that
  returns a scalar element type now resolves to `Index[S2_NSDT]` instead of the
  operator-error / untyped path. Verified with a focused test
  (`tests/indexes/int/test_sub.py::test_sub_external_reflected`): before the
  change pyright reported `Operator "-" not supported`, after it resolves the
  operand to `Index[int]`.
- **Neutral**: the new overloads do not change the resolution of any existing
  `tests/indexes/{bool,int,float,complex}/test_sub.py` result under mypy (the
  full `tests/indexes` mypy corpus is byte-identical before/after the change).
  The concrete numpy/`Index` overloads still win for the operand types they
  enumerate, because a *container* (`Index[int]`, an ndarray) whose reflected
  dunder returns a container rather than a scalar does not satisfy the
  scalar-bound `S2_NSDT` contract.
- **Open / checker divergence**: pyright and pyrefly infer `S2_NSDT` differently
  for an operand whose reflected `__rsub__` returns a scalar type different from
  the operand's own type. For `left: Index[int]` and an operand with
  `__rsub__(x: int) -> float`, pyright resolves to `Index[float]` (uses the
  reflected return type) while pyrefly resolves to `Index[int]` (ties it to the
  operand's own dtype). This is a pre-existing inference difference latent in
  `__add__`/`__mul__`, surfaced here because subtraction finally exercises the
  same shape. It is recorded, not hidden: the focused test pins the
  cross-checker-consistent case (operand reflected dunder returns the operand's
  own scalar type), and the divergent case is left asserted per-checker.
- **Scope**: this ADR covers only the `Index.__sub__`/`__rsub__` family. The
  `/`/`//` `Never` guards, a guard-checker, and `Series` parity are explicitly out
  of scope and deferred.

## Historical References & Provenance

- `pandas-stubs/core/indexes/base.pyi` — the `Index` dunder overloads. The
  `SupportsAdd`/`SupportsRAdd` and `SupportsMul`/`SupportsRMul` overloads that
  this change mirrors.
- `pandas-stubs/_typing.pyi` — `S2_contra` (contravariant `SeriesDType` bound) and
  `S2_NSDT` (`SeriesDTypeNoStrDateTime` bound).
- ADR-0009 — structural and nominal protocols for type discrimination; the origin
  of the `Supports_Proto*`/`_typeshed.Supports*` split.
- ADR-0017 — boolean arithmetic restrictions; the model for the out-of-scope
  `/`/`//` `Never` guards.
- PR pandas-dev/pandas-stubs#1938 (branch `typ-index-subtraction`,
  `ec114bec`) — landed the first `Index[bool] - bool -> Never` guard and aligned
  the `__sub__` family onto the `ElementOpsMixin` + `Supports_Proto*` idiom that
  this ADR extends.
- This change (branch `typ-index-sub-parity`) — the focused parity diff that
  implements the ADR.
