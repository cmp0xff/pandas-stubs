# Type Architecture

The normative description of the container hierarchy now lives in
[`docs/type-architecture/`](../../type-architecture/README.md) and is enforced by
[`scripts/check_operand_hierarchy.py`](../../../scripts/check_operand_hierarchy.py)
(implementation in `scripts/operand_hierarchy/`).

The earlier 4-level model kept here is superseded:

- `CLASS_TIERS` in `scripts/operand_hierarchy/model.py` defines five tiers — scalars,
  `ExtensionArray`, `Index`/`MultiIndex` (plus subclasses), `Series`, `DataFrame` — see
  [Operand hierarchy](../../type-architecture/operand-hierarchy.md).
- `__matmul__` is scanned like the other forward arithmetic dunders;
  `Series.__matmul__(DataFrame)` is a counted allowance, not an unchecked exception.

The ADRs in [`../decisions/`](../decisions/), the [subsystem guides](../subsystems/) and
the [type matrices](../matrices/) remain the history behind those rules.
