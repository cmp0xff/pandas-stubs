---
status: accepted
date: 2026-09-03
deciders: [Dr-Irv, twoertwein, MarcoGorelli, loicdiridollou, cmp0xff]
consulted: [typing-sig]
informed: [pandas-stubs contributors]
---

# ADR-0023: Index Subtraction follows `/` — internal `Supports_ProtoSub`, no external `Supports*` parity

## Context and Problem Statement

The arithmetic dunder families on `Index` are not symmetric in how they expose
element-type precision for an **external** (non-`pandas`) operand.

`__add__`/`__mul__` carry an external `_typeshed.Supports*` reflected-dunder
overload in addition to their internal `Supports_Proto*` overloads (ADR-0009):

- `__add__` → `SupportsRAdd` / `__radd__` → `SupportsAdd`
- `__mul__` → `SupportsRMul` / `__rmul__` → `SupportsMul`

Each is `self: Index[S2_contra], other: SupportsR<op>[S2_contra, S2_NSDT] | Sequence[...]`
and returns `Index[S2_NSDT]`. This lets the `_typeshed` protocol capture the
operand's reflected-return **scalar** dtype for an operand that implements the
reflected dunder itself (e.g. a custom scalar, an ExtensionArray, or a `Series`
whose reflected operation lowers to a scalar).

`__sub__`/`__rsub__` had only the internal `Supports_ProtoSub`/`Supports_ProtoRSub`
overloads (`self: Supports_ProtoSub[T_contra, S2], other: T_contra | Sequence[T_contra] -> Index[S2]`).
Those protocols are `self`-bound: they describe the *left* operand (`self`) and
derive the result from `self`'s own element type. They cannot carve out the case
where the precision comes from the *external right operand's* reflected dunder, so
an external operand with a reflected `__sub__`/`__rsub__` fell through to the
untyped / operator-error path while the same shape through `+`/`*` was pinned to
`Index[S2_NSDT]`.

This raises a question: should `-` gain the external `_typeshed.Supports*` parity
that `+`/`*` have, so an external reflected operand resolves to a concrete
`Index[S2_NSDT]`?

## Decision Drivers

- **Reflected-operand precision**: an external operand whose reflected
  `__sub__`/`__rsub__` returns a scalar dtype would ideally resolve to a concrete
  element type.
- **Not at the cost of a wrong answer for `Index[bool]`**: the invalid
  `Index[bool] - Index[bool]` must remain a type-checker **operator error**.
  `Index[bool]`'s `Never`-guarded dunders are structured precisely so these are
  rejected; an approach that silently turns them into `Index[Never]` hides a real
  error rather than improving precision.
- **Match the sibling `/` family**: `/` already resolved the same external-operand
  question with the internal `Supports_ProtoTrueDiv` + explicit `Never` guards and
  *no* external `_typeshed.Supports*` overload. `-` should follow its closer
  sibling when the two approaches conflict.
- **4-checker portability**: mypy, pyright, pyrefly, and ty must each resolve the
  same overloads independently without per-checker ignores.

## Considered Options

1. **Add `_typeshed.SupportsRSub`/`SupportsSub` overloads mirroring `__mul__`/`__rmul__`** *(tried, rejected)*.
   - Implemented as commit `bc985f07` on `typ-index-subtraction` (#1938).
   - *Pros*: exact parity with `+`/`*`; reuses the accepted `S2_NSDT` result bound.
   - *Cons*: the greedy capture of `Index[bool]` (below) turns a genuine operator
     error into `Index[Never]`. This is the direct reason the option is rejected.
     The `bool <: int` subtype chain cannot be excluded by any bound or constraint
     on the protocol, so the capture is inherent to the external-overload shape
     and is not patchable without abandoning the parity it was chosen for.

2. **Per-dtype concrete-self overloads** (`Index[int]`, `Index[float]`,
   `Index[complex]`) for the external operand.
   - *Pros*: avoids the `Index[bool]` capture, because `Index` is invariant — a
     `self: Index[int]` overload is not satisfiable by `Index[bool]`, so `bool <: int`
     cannot leak through.
   - *Cons*: three extra overloads per direction, and it breaks the `+`/`*` symmetry
     the parity goal originally sought. Parity is dropped rather than replaced with
     a shape `+`/`*` does not share.

3. **Follow `/`: internal `Supports_Proto*` + `Never` guards, no external
   overload** *(chosen)*.
   - The `__truediv__`/`__rtruediv__` family uses exactly this shape: a self-bound
     `Supports_ProtoTrueDiv`/`Supports_ProtoRTrueDiv` plus explicit `Never` guards,
     and no `_typeshed.Supports*`.
   - *Pros*: consistent with `/`; no external protocol surface; `Index[bool] -
     Index[bool]` stays an operator error.
   - *Cons*: an external operand with a reflected `__sub__`/`__rsub__` that returns a
     scalar dtype is an operator error rather than resolving to `Index[S2_NSDT]` —
     a narrow, known precision gap that `+`/`*` have and `-` does not.

## Decision Outcome

`Index.__sub__`/`__rsub__` follow the `/` family. They use only the internal,
self-bound `Supports_ProtoSub`/`Supports_ProtoRSub` overloads plus the explicit
`Never` guards, and carry **no** external `_typeshed.SupportsRSub`/`SupportsSub`
overload. `SupportsSub`/`SupportsRSub` were added to the
`from _typeshed import (…)` block by the parity attempt (`bc985f07`) and are
now removed.

The rationale for rejecting the external `Supports*` form is the bool capture:
because `bool <: int` and `Index[bool]`'s `Never`-guarded dunders make
`Index[bool]` structurally satisfy `SupportsRSub[bool, Never]`/`SupportsSub[bool, Never]`,
an external `_typeshed.Supports*` overload with `self: Index[S2_contra]` greedily
captures `Index[bool]`. It resolves the invalid `Index[bool] - Index[bool]` in both
directions to `Index[Never]` instead of the operator error the `Never` guards are
meant to produce. Keeping parity therefore required extending the bool guard with
`np_ndarray_bool` to paper over one downstream divergence; following `/` removes
the need for that workaround entirely.

## Consequences

- **`Index[bool] - Index[bool]` is again an operator error** in both directions,
  suppressed in `tests/indexes/bool/test_sub.py` under `TYPE_CHECKING_INVALID_USAGE`
  with `# type: ignore[operator]`, `# pyright: ignore[reportOperatorIssue,reportUnknownVariableType]`,
  and `# pyrefly: ignore[unsupported-operation]`.
- **No external `_ReflectedSub` test**: `tests/indexes/int/test_sub.py` no longer
  carries `test_sub_external_reflected`; `Index[int] - <external scalar>` is an
  operator error, pinned by that test's absence.
- **External-operand precision gap**: an external operand with a reflected
  `__sub__`/`__rsub__` returning a scalar dtype does not resolve to `Index[S2_NSDT]`
  under `-` (unlike `+`/`*`). This is the accepted trade-off.
- **datetimeindex numpy over-approximation**: in `tests/indexes/datetimeindex/test_sub.py`,
  `s - left` (where `s` is `ndarray[datetime64]`) statically resolves to
  `ndarray[datetime64]` while returning a `TimedeltaIndex` at runtime, and
  `d - left` (where `d` is `ndarray[timedelta64]`) statically resolves to
  `ndarray[timedelta64]` while raising `TypeError` at runtime. This is because
  numpy's typeshed over-approximates `ndarray.__sub__`, and our `__rsub__` cannot
  override it. The assertions are static-only and correct; the numpy resolution is
  independent of this decision.
- **Cross-checker consistency**: under the real poetry harness (no ad-hoc
  `--pythonpath`), mypy, pyright, pyrefly, and ty are all clean; the reverted bool
  `# type: ignore[operator]` comments are actually used, i.e. no unused-ignore, and
  the `tests/indexes/test_sub.py` (`Index[Any]`) corpus is unchanged.
- **Scope**: this ADR covers only the `Index.__sub__`/`__rsub__` family. `/`/`//`
  `Never` guards, a guard-checker, and `Series` parity are out of scope.

## Historical References & Provenance

- `pandas-stubs/core/indexes/base.pyi` — the `Index` dunder overloads: the `+`/`*`
  `Supports*` overloads and the sibling `/` `Supports_ProtoTrueDiv` + `Never` shape
  this ADR follows.
- `pandas-stubs/_typing.pyi` — `S2_contra` (contravariant `SeriesDType` bound) and
  `S2_NSDT` (`SeriesDTypeNoStrDateTime` bound), kept only where relevant to the
  rejected `+`/`*`-shaped option.
- ADR-0009 — structural and nominal protocols for type discrimination; the origin
  of the `Supports_Proto*`/`_typeshed.Supports*` split.
- ADR-0017 — boolean arithmetic restrictions; the model for the `Never` guards.
- PR pandas-dev/pandas-stubs#1938 (branch `typ-index-subtraction`):
  - `ec114bec` — aligned the `__sub__` family onto the `ElementOpsMixin` +
    `Supports_Proto*` idiom and added the first `Index[bool] - bool -> Never` guard.
  - `bc985f07` — added external `_typeshed.SupportsRSub`/`SupportsSub` parity
    overloads; recorded here as tried-and-rejected. It introduced the `Index[bool]`
    capture (`Index[bool] - Index[bool] -> Index[Never]`) and the `np_ndarray_bool`
    guard extension.
  - follow-up commit — reverted the parity/external overload and the guard
    extension so `-` follows `/`; the shape this ADR adopts.
