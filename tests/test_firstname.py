"""Check name helpers in both the BibTeX and RIS implementations."""

from pathlib import Path
import runpy

import pytest


@pytest.fixture(params=["lines", "linesRis"])
def helpers(request):
    root = Path(__file__).resolve().parents[1]
    return runpy.run_path(str(root / request.param / "firstname.py"))


@pytest.mark.parametrize("names, expected", [
    ("Doe, Jane", [5]),
    ("Doe, Jane and Smith, John", [5, 21]),
    ("Kniesel, Günter", [9]),
    ("Jane Doe", []),
    ("", []),
    ("J", []),
    ("Doe, ", []),
])
def test_first_initial_positions(helpers, names, expected):
    assert helpers["firstinitial"](names) == expected


@pytest.mark.parametrize("names, indices, expected", [
    ("Doe, Jane and Smith, John", [3, 19], [",", ","]),
    ("Jane Doe", [], []),
    ("", [], []),
])
def test_characters_at_comma_positions(helpers, names, indices, expected):
    assert helpers["printFromCommaIndex"](names, indices) == expected
