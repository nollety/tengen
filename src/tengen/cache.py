"""Cache module."""
import pathlib
import shutil
import typing as t

CACHE_DIR = pathlib.Path(".tengen_cache")


def init_cache() -> None:
    """Initialise cache."""
    CACHE_DIR.mkdir(parents=True, exist_ok=True)


def list_cache_content() -> t.List[str]:
    """List cache content."""
    return [file.name for file in CACHE_DIR.glob("*.nc")]


def remove_cache() -> None:  # pragma: no cover
    """Remove the cache."""
    try:
        shutil.rmtree(CACHE_DIR)
    except OSError as e:
        raise ValueError(f"Could not remove cache at {CACHE_DIR}") from e
