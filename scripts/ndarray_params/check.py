# ruff: noqa: T201
"""Ratchet direct n-D ndarray parameter annotations; type aliases are not resolved."""

from __future__ import annotations

import argparse
import ast
from collections import Counter
from pathlib import Path
import sys

_REPO_ROOT = Path(__file__).resolve().parents[2]
_PERMANENT = Path("scripts/test/ndarray-params-permanent.txt")
_BURNDOWN = Path("scripts/test/ndarray-params-burndown.txt")
_ARRAY_NAMES = {"np.ndarray", "numpy.ndarray", "npt.NDArray", "numpy.typing.NDArray"}


def _dotted_name(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return f"{_dotted_name(node.value)}.{node.attr}"
    return ""


def _contains_ndarray(annotation: ast.AST, imported: set[str]) -> bool:
    for node in ast.walk(annotation):
        name = _dotted_name(node)
        if name.startswith("np_ndarray") or name in _ARRAY_NAMES | imported:
            return True
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            # Quoted forward annotations have their own expression AST.
            try:
                expression = ast.parse(node.value, mode="eval")
            except SyntaxError:
                continue
            if _contains_ndarray(expression, imported):
                return True
    return False


def _find_parameters(
    node: ast.AST,
    module: str,
    imported: set[str],
    scope: tuple[str, ...] = (),
) -> set[str]:
    keys: set[str] = set()
    if isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
        scope = (*scope, node.name)
    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
        args = node.args
        parameters = [*args.posonlyargs, *args.args, *args.kwonlyargs]
        if args.vararg:
            parameters.append(args.vararg)
        if args.kwarg:
            parameters.append(args.kwarg)
        for parameter in parameters:
            if parameter.annotation and _contains_ndarray(
                parameter.annotation, imported
            ):
                keys.add(f"{module}:{'.'.join(scope)}:{parameter.arg}")
    for child in ast.iter_child_nodes(node):
        keys.update(_find_parameters(child, module, imported, scope))
    return keys


def find_ndarray_params(stub_root: Path) -> set[str]:
    """Return the keys of n-D parameters; raise ValueError if no stubs are found."""
    keys: set[str] = set()
    paths = sorted(stub_root.rglob("*.pyi"))
    if not paths:
        raise ValueError(f"No stub files found in {stub_root}")
    for path in paths:
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        imported = {
            alias.asname or alias.name
            for node in ast.walk(tree)
            if isinstance(node, ast.ImportFrom)
            and node.module in {"numpy", "numpy.typing"}
            and not node.level
            for alias in node.names
            if (node.module, alias.name)
            in {("numpy", "ndarray"), ("numpy.typing", "NDArray")}
        }
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    if alias.asname and alias.name == "numpy":
                        imported |= {
                            f"{alias.asname}.ndarray",
                            f"{alias.asname}.typing.NDArray",
                        }
                    elif alias.asname and alias.name == "numpy.typing":
                        imported.add(f"{alias.asname}.NDArray")
        parts = list(path.relative_to(stub_root).with_suffix("").parts)
        if parts[-1] == "__init__":
            parts.pop()
        keys.update(_find_parameters(tree, ".".join(["pandas", *parts]), imported))
    return keys


def _read_allowlist(path: Path) -> tuple[set[str], list[str]]:
    entries = [
        entry
        for line in path.read_text(encoding="utf-8").splitlines()
        if (entry := line.partition("#")[0].strip())
    ]
    problems = [
        f"{path}: duplicate {key}; delete the repeated line."
        for key, count in sorted(Counter(entries).items())
        if count > 1
    ]
    if entries != sorted(entries):
        problems.append(f"{path}: entries are not sorted; sort the keys.")
    return set(entries), problems


def check_ndarray_params(stub_root: Path, permanent: Path, burndown: Path) -> bool:
    found = find_ndarray_params(stub_root)
    allowed, problems = _read_allowlist(permanent)
    remaining, more_problems = _read_allowlist(burndown)
    problems.extend(more_problems)
    for key in sorted(found - allowed - remaining):
        problems.append(
            f"{key}: unlisted n-D parameter; use np_1darray* for 1-D input, "
            "or document genuine n-D support in the permanent list."
        )
    for key in sorted(remaining - found):
        problems.append(
            f"{key}: stale burndown entry; delete its line from {burndown}."
        )
    for key in sorted(allowed - found):
        problems.append(
            f"{key}: stale permanent entry; delete its line from {permanent}."
        )
    for key in sorted(allowed & remaining):
        problems.append(f"{key}: in both lists; keep it in only one list.")
    for problem in problems:
        print(problem, file=sys.stderr)
    return not problems


def write_burndown(stub_root: Path, permanent: Path, burndown: Path) -> None:
    """Rewrite the burndown entries from the stubs, keeping its leading comment header."""
    allowed, problems = _read_allowlist(permanent)
    if problems:
        raise ValueError("\n".join(problems))
    header: list[str] = []
    for line in burndown.read_text(encoding="utf-8").splitlines(keepends=True):
        if line.strip() and not line.startswith("#"):
            break
        header.append(line)
    entries = sorted(find_ndarray_params(stub_root) - allowed)
    burndown.write_text(
        "".join(header) + "".join(f"{key}\n" for key in entries), encoding="utf-8"
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-burndown", action="store_true")
    args = parser.parse_args(argv)
    stub_root = _REPO_ROOT / "pandas-stubs"
    permanent, burndown = _REPO_ROOT / _PERMANENT, _REPO_ROOT / _BURNDOWN
    try:
        if args.write_burndown:
            write_burndown(stub_root, permanent, burndown)
        valid = check_ndarray_params(stub_root, permanent, burndown)
    except (OSError, SyntaxError, ValueError) as error:
        print(str(error), file=sys.stderr)
        return 1
    if valid:
        print("ndarray parameter allowlists match the stubs.")
    return 0 if valid else 1
