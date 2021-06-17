"""Test cases for the __main__ module."""
from typing import Any

import pytest
from click.testing import CliRunner

from tengen import __main__


@pytest.fixture
def runner() -> CliRunner:
    """Fixture for invoking command-line interfaces."""
    return CliRunner()


def test_main_succeeds(runner: CliRunner, tmpdir: Any) -> None:
    """It exits with a status code of zero."""
    result = runner.invoke(
        __main__.main,
        ["--identifier=thuillier_2003", f"--file-name={tmpdir / 'ds.nc'}"],
    )
    assert result.exit_code == 0
