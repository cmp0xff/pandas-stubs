# Development paradigm with pandas-stubs

For any update to the stubs, we require an associated test case that should fail without
a proposed change, and works with a proposed change.  See <https://github.com/pandas-dev/pandas-stubs/tree/main/tests/> for examples.

The stubs are developed with a certain [philosophy](philosophy.md) that should be 
understood by developers proposing changes to the stubs.

The [`Series` and `Index` backing-array architecture](architecture.md) describes how
the stubs track both element types and physical array storage.

[Intentional type ignores](type_ignores.md) catalogs the `# type: ignore` /
`# pyright: ignore` comments that are permanent by design, as opposed to checker-disagreement
debt.

Instructions for working with the code are found here:

- [How to set up the environment](setup.md)
- [How to test the project](tests.md)
- [How to make a release](release_procedure.md)
