**Target Module**: [pandas-stubs/core/frame.pyi](../../../pandas-stubs/core/frame.pyi)

# Subsystem: DataFrame Core, 2D Slicing & Accessor Indexers (.loc, .iloc, .at, .iat)

## 1. Overview & Architectural Role

`pd.DataFrame` represents 2-dimensional tabular data. Its indexing accessors (`.loc`, `.iloc`, `.at`, `.iat`) support heterogeneous key types: scalars, slices, lists, boolean masks, callables, and tuples.

## 2. Historical Debates & Design Decisions

### Disambiguating Strings from Sequences in `.loc`
Because `str` in Python is an `Iterable[str]` and `Sequence[str]`, type checkers often fail to differentiate between selecting a single column (`df.loc[:, "col"] -> Series`) and selecting a list of columns (`df.loc[:, ["col"]] -> DataFrame`).

In PR pandas-dev/pandas-stubs#1803: Allow `df.loc[Scalar, SequenceNotStr[Scalar]]` (pandas-dev/pandas-stubs@af53c5a3839a334519c96bc67d5fe4255db59fa1), `geoffrey-eisenbarth` introduced `SequenceNotStr[Scalar]` to explicitly disambiguate scalar keys from multi-element column sequences.

### Matrix Multiplication (`DataFrame.dot`)
In PR pandas-dev/pandas-stubs#1885: TYP: Allow list as other in DataFrame.dot (pandas-dev/pandas-stubs@93b776f7d6af62abccee6081e44d86479b859b4b), `Khan3K` expanded `DataFrame.dot` to accept standard Python lists alongside Series and DataFrames.

### Why DataFrame is not schema-generic
A schema generic (`DataFrame[Person]`) that pins per-column element types is proposed from
time to time (PR pandas-dev/pandas-stubs#295, PR pandas-dev/pandas-stubs#1190,
PR pandas-dev/pandas-stubs#1548). It is not expressible in pure PEP 484/695 typing: a
`TypedDict` cannot be a `TypeVar` bound, and a `TypeVar` cannot be subscripted. Only the
schema-carrying tier (`DataFrame[Person]` returning `Series[Any]`) is pure typing;
per-column resolution requires codegen or a checker plugin. See
[ADR-0021](../decisions/adr-0021-dataframe-is-not-schema-generic.md).

## 3. Key Pull Requests & Commits

- pandas-dev/pandas-stubs#39: Fix to_dict and from_dict type stubs (pandas-dev/pandas-stubs@8fbe101a4b28335cac7391d3630288553e01ed5b)
- pandas-dev/pandas-stubs#1803: Allow `df.loc[Scalar, SequenceNotStr[Scalar]]` (pandas-dev/pandas-stubs@af53c5a3839a334519c96bc67d5fe4255db59fa1)
- pandas-dev/pandas-stubs#1885: TYP: Allow list as other in DataFrame.dot (pandas-dev/pandas-stubs@93b776f7d6af62abccee6081e44d86479b859b4b)
