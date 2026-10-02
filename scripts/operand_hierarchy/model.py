"""The operand-hierarchy model: what the checker knows before it reads a stub tree.

The definition tables live here rather than in the checker so the model reads as data,
and so a change to the tier system is a change to one file.

The tier model itself is documented in ``docs/type-architecture/operand-hierarchy.md``.
"""

from __future__ import annotations

from pathlib import Path
from typing import Final

# The scanned set is enumerated explicitly. Name heuristics cannot separate forward
# from reflected operations (a forward dunder can itself start with ``__r``, as
# ``__rshift__`` does), and a dunder outside this set — every reflected dunder, like
# ``__radd__``, plus non-operator methods such as ``__init__`` — is not scanned.
FORWARD_BINARY_DUNDERS: Final[frozenset[str]] = frozenset(
    {
        "__add__",
        "__sub__",
        "__mul__",
        "__matmul__",
        "__truediv__",
        "__floordiv__",
        "__mod__",
        "__divmod__",
        "__pow__",
        "__lshift__",
        "__rshift__",
        "__and__",
        "__or__",
        "__xor__",
        "__lt__",
        "__le__",
        "__eq__",
        "__ne__",
        "__gt__",
        "__ge__",
    }
)

# Operand names that can appear in ``other``, mapped to their tier.
TIER_OPERANDS: Final[dict[str, int]] = {
    "ExtensionArray": 1,
    "Index": 2,
    "MultiIndex": 2,
    "Series": 3,
    "DataFrame": 4,
    # The offsets are scalars, so they take sub-tiers of the scalar tier instead of a rung
    # above the containers: a container or scalar naming an offset is then an ordinary
    # lower-or-equal-tier operand, not a violation. ``BaseOffset`` is the contract every
    # offset keeps — a datetime-like operand maps to ``Timestamp`` — and is the offsets'
    # lower sub-tier. The delta families additionally accept durations and one another, and
    # are scalar operands themselves, so they take the scalar tier: a non-delta offset
    # naming a ``Tick``/``Day``/``Week``/``BusinessDay`` is the violation these two
    # sub-tiers exist to catch. ``Tick`` names the delta sub-tier in diagnostics and
    # exception keys; the family has no common base to name it by, since ``Day``, ``Week``
    # and ``BusinessDay`` are peers of ``Tick``, not its subclasses.
    "BaseOffset": -1,
    "Tick": 0,
    "Day": 0,
    "Week": 0,
    "BusinessDay": 0,
}

# Subtrees whose classes take a tier by walking real base classes rather than by a literal
# ``TIER_OPERANDS`` entry. Order matters: a subtree walked earlier claims its own classes,
# so the delta roots — whose classes also descend from ``BaseOffset`` — are walked before
# ``BaseOffset`` itself. ``Day`` is a root in its own right because pandas moved it off
# ``Tick`` to ``SingleConstructorOffset``; it must stay a delta either way.
TIER_ROOTS: Final[tuple[tuple[str, int], ...]] = (
    ("Index", TIER_OPERANDS["Index"]),
    ("Tick", TIER_OPERANDS["Tick"]),
    ("Day", TIER_OPERANDS["Day"]),
    ("Week", TIER_OPERANDS["Week"]),
    ("BusinessDay", TIER_OPERANDS["BusinessDay"]),
    ("BaseOffset", TIER_OPERANDS["BaseOffset"]),
)

# Tier 1 is the array-likes, registered under the ``ExtensionArray`` ABC: the operand name
# above, its canonical name below, and its stub file in ``CLASS_STUB_FILES``. It took no
# exception key when it landed, because the only classes that can violate against tier 1
# are the tier-0 scalars and none of them names an array-like in a forward dunder's
# ``other``. The first one that does needs a key, and it is also the first site to read
# ``CANONICAL_OPERAND_BY_TIER[1]``.

# The operand name a tier is registered under, so a site that spells its operand
# ``TimedeltaIndex`` or ``MultiIndex`` is looked up as ``Index``. Keyed by tier, not by
# spelling, so a spelling cannot drift out of the exception list. Spelled out rather than
# derived from ``TIER_OPERANDS`` because a tier's canonical name is a choice, not a
# derivation: ``Index`` and ``MultiIndex`` share tier 2. Tier 0 is shared by the plain
# scalars and the delta offsets, so its entry names the delta family; the only references
# into it come from ``BaseOffset`` below, which names none of them today.
CANONICAL_OPERAND_BY_TIER: Final[dict[int, str]] = {
    TIER_OPERANDS["ExtensionArray"]: "ExtensionArray",
    TIER_OPERANDS["Index"]: "Index",
    TIER_OPERANDS["Series"]: "Series",
    TIER_OPERANDS["DataFrame"]: "DataFrame",
    TIER_OPERANDS["BaseOffset"]: "BaseOffset",
    TIER_OPERANDS["Tick"]: "Tick",
}

# Every tier-0 scalar and the array-like, mapped to the stub file that declares it, so the
# class scan resolves a class through the registry and can require that file rather than
# silently skipping the class. A name in this table that is absent from ``TIER_OPERANDS``
# is a tier-0 scalar. ``Index``, ``MultiIndex``, ``Series`` and ``DataFrame`` are tiered by
# ``TIER_OPERANDS`` directly; the files declaring them are the literal entries of
# ``REQUIRED_STUB_FILES`` below rather than keys here.
CLASS_STUB_FILES: Final[dict[str, Path]] = {
    "Timedelta": Path("_libs/tslibs/timedeltas.pyi"),
    "Timestamp": Path("_libs/tslibs/timestamps.pyi"),
    "Period": Path("_libs/tslibs/period.pyi"),
    "Interval": Path("_libs/interval.pyi"),
    "NAType": Path("_libs/missing.pyi"),
    "ExtensionArray": Path("core/arrays/base.pyi"),
    "BaseOffset": Path("_libs/tslibs/offsets.pyi"),
}

# Every file that declares a scanned class. The list is explicit so that moving a class
# to a new file fails the scan loudly instead of silently dropping it.
REQUIRED_STUB_FILES: Final[tuple[Path, ...]] = tuple(
    sorted(
        {
            Path("core/base.pyi"),
            Path("core/frame.pyi"),
            Path("core/indexes/base.pyi"),
            Path("core/indexes/category.pyi"),
            Path("core/indexes/datetimelike.pyi"),
            Path("core/indexes/datetimes.pyi"),
            Path("core/indexes/extension.pyi"),
            Path("core/indexes/interval.pyi"),
            Path("core/indexes/multi.pyi"),
            Path("core/indexes/period.pyi"),
            Path("core/indexes/range.pyi"),
            Path("core/indexes/timedeltas.pyi"),
            Path("core/series.pyi"),
            Path("_stubs_only/__init__.pyi"),
            *CLASS_STUB_FILES.values(),
        }
    )
)
