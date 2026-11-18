from __future__ import annotations

from pathlib import Path

import pytest

from scripts.ndarray_params.check import (
    check_ndarray_params,
    find_ndarray_params,
    main,
    write_burndown,
)


def _write_stub(
    tmp_path: Path, source: str, relative: str = "core/example.pyi"
) -> Path:
    root = tmp_path / "pandas-stubs"
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(source, encoding="utf-8")
    return root


@pytest.mark.parametrize(
    "annotation",
    [
        "np_ndarray",
        "np_ndarray_float",
        "np_ndarray_object[ShapeT]",
        "list[np_ndarray_bool | None]",
        "Callable[[int], np_ndarray]",
        "np.ndarray[Any, Any]",
        "numpy.ndarray[Any, Any]",
        "npt.NDArray[Any]",
        "numpy.typing.NDArray[Any]",
        "ndarray[Any, Any]",
        "NDArray[Any]",
        "Renamed[Any]",
        "xp.ndarray[Any, Any]",
        "nt.NDArray[Any]",
        '"np_ndarray_float | None"',
    ],
)
def test_detect_spellings(tmp_path: Path, annotation: str) -> None:
    root = _write_stub(
        tmp_path,
        f"import numpy as xp\nimport numpy.typing as nt\nfrom numpy import ndarray\nfrom numpy.typing import NDArray, NDArray as Renamed\ndef f(x: {annotation}) -> None: ...",
    )
    assert find_ndarray_params(root) == {"pandas.core.example:f:x"}


@pytest.mark.parametrize(
    "annotation",
    ["np_1darray", "np_1darray_float", "np_2darray", "Alias", "ndarray", "NDArray"],
)
def test_ignored_annotations(tmp_path: Path, annotation: str) -> None:
    root = _write_stub(
        tmp_path,
        f"Alias: TypeAlias = np_ndarray\ndef f(x: {annotation}) -> np_ndarray: ...",
    )
    assert find_ndarray_params(root) == set()


def test_scopes_parameter_kinds_and_overloads(tmp_path: Path) -> None:
    root = _write_stub(
        tmp_path,
        """
class Outer:
    class Inner:
        @overload
        def f(self, x: np_ndarray, /, y: np_ndarray, *args: np_ndarray,
              z: np_ndarray, **kwargs: np_ndarray) -> None: ...
        @overload
        def f(self, x: np_ndarray) -> None: ...
    @classmethod
    def g(cls, x: np_ndarray) -> None: ...
if VERSION:
    async def f(x: np_ndarray) -> None: ...
""",
        "core/__init__.pyi",
    )
    assert find_ndarray_params(root) == {
        *(f"pandas.core:Outer.Inner.f:{p}" for p in ["x", "y", "args", "z", "kwargs"]),
        "pandas.core:Outer.g:x",
        "pandas.core:f:x",
    }
    _write_stub(tmp_path, "def f(self: np_ndarray) -> None: ...", "__init__.pyi")
    assert "pandas:f:self" in find_ndarray_params(root)


@pytest.mark.parametrize(
    "source, permanent_text, burndown_text, diagnostic",
    [
        ("def f(x: np_ndarray) -> None: ...", "", "", "unlisted n-D parameter"),
        ("", "", "pandas.core.example:f:x\n", "stale burndown entry"),
        ("", "pandas.core.example:f:x\n", "", "stale permanent entry"),
        (
            "def f(x: np_ndarray) -> None: ...",
            "pandas.core.example:f:x\n",
            "pandas.core.example:f:x\n",
            "in both lists",
        ),
        ("", "pandas:f:x\npandas:f:x\n", "", "duplicate pandas:f:x"),
        ("", "", "pandas:f:x\npandas:f:x\n", "duplicate pandas:f:x"),
        ("", "", "pandas:z:x\npandas:a:x\n", "entries are not sorted"),
    ],
)
def test_allowlist_failures(
    tmp_path: Path,
    source: str,
    permanent_text: str,
    burndown_text: str,
    diagnostic: str,
    capsys: pytest.CaptureFixture[str],
) -> None:
    root = _write_stub(tmp_path, source)
    permanent, burndown = tmp_path / "permanent.txt", tmp_path / "burndown.txt"
    permanent.write_text(permanent_text, encoding="utf-8")
    burndown.write_text(burndown_text, encoding="utf-8")
    assert not check_ndarray_params(root, permanent, burndown)
    assert diagnostic in capsys.readouterr().err


def test_regenerate_and_comments(tmp_path: Path) -> None:
    root = _write_stub(
        tmp_path,
        "\n".join(f"def {name}(x: np_ndarray) -> None: ..." for name in "zma"),
    )
    permanent, burndown = tmp_path / "permanent.txt", tmp_path / "burndown.txt"
    permanent.write_text(
        "# Permanent\n\npandas.core.example:z:x # reason\n", encoding="utf-8"
    )
    expected = "# Keep header\n\npandas.core.example:a:x\npandas.core.example:m:x\n"
    burndown.write_text(expected + "pandas:stale:x\n", encoding="utf-8")
    write_burndown(root, permanent, burndown)
    assert burndown.read_text(encoding="utf-8") == expected
    write_burndown(root, permanent, burndown)
    assert burndown.read_text(encoding="utf-8") == expected
    assert check_ndarray_params(root, permanent, burndown)


def test_regenerate_refuses_new_keys(tmp_path: Path) -> None:
    root = _write_stub(tmp_path, "def f(x: np_ndarray) -> None: ...")
    permanent, burndown = tmp_path / "permanent.txt", tmp_path / "burndown.txt"
    permanent.write_text("", encoding="utf-8")
    burndown.write_text("# Header\n", encoding="utf-8")
    with pytest.raises(ValueError, match=r"pandas\.core\.example:f:x: unlisted"):
        write_burndown(root, permanent, burndown)
    assert burndown.read_text(encoding="utf-8") == "# Header\n"


def test_repository_matches_allowlists() -> None:
    assert main([]) == 0


def test_main_failure_status(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("scripts.ndarray_params.check._REPO_ROOT", tmp_path)
    assert main([]) == 1
