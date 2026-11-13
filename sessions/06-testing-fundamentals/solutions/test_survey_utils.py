"""Session 06 reference tests. They're written against the docstrings, so 3 of them fail on the
buggy exercise/survey_utils.py and all pass on solutions/survey_utils.py.

Run:  python -m pytest -v solutions          (fixed code: all pass)
      python -m pytest -v solutions --buggy  (exercise code: see the failures)
"""

import pytest


@pytest.fixture
def utils(request):
    """Import either the buggy (exercise) or fixed (solutions) module."""
    import importlib.util
    from pathlib import Path

    folder = "exercise" if request.config.getoption("--buggy") else "solutions"
    path = Path(__file__).resolve().parents[1] / folder / "survey_utils.py"
    spec = importlib.util.spec_from_file_location(f"survey_utils_{folder}", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# --- normalise_postcode --------------------------------------------------------------

@pytest.mark.parametrize("raw", ["np108xg", "NP10 8XG", "  np10 8xg ", "np10   8xg", "\tnp108xg\n"])
def test_normalise_postcode_variants(utils, raw):
    assert utils.normalise_postcode(raw) == "NP10 8XG"


def test_normalise_postcode_short_outward_code(utils):
    assert utils.normalise_postcode("m11ae") == "M1 1AE"


# --- age_band --------------------------------------------------------------------

@pytest.mark.parametrize("age, expected", [
    (0, "0-15"), (15, "0-15"),
    (16, "16-24"), (24, "16-24"),
    (25, "25-44"), (44, "25-44"),
    (45, "45-64"), (64, "45-64"),          # BUG: 64 returns "65+"
    (65, "65+"), (110, "65+"),
])
def test_age_band_boundaries(utils, age, expected):
    assert utils.age_band(age) == expected


def test_age_band_rejects_negative_age(utils):
    with pytest.raises(ValueError, match="negative"):
        utils.age_band(-1)


# --- response_rate ---------------------------------------------------------------

@pytest.mark.parametrize("complete, issued, expected", [
    (50, 100, 50.0),
    (1, 3, 33.3),
    (2, 3, 66.7),
    (0, 10, 0.0),
    (10, 10, 100.0),
])
def test_response_rate(utils, complete, issued, expected):
    assert utils.response_rate(complete, issued) == expected


def test_response_rate_none_when_nothing_issued(utils):
    assert utils.response_rate(0, 0) is None            # BUG: ZeroDivisionError


@pytest.mark.parametrize("complete, issued", [(11, 10), (-1, 10), (1, -10)])
def test_response_rate_rejects_invalid_counts(utils, complete, issued):
    with pytest.raises(ValueError):
        utils.response_rate(complete, issued)


# --- parse_bool ------------------------------------------------------------------

@pytest.mark.parametrize("value", ["y", "yes", "true", "1", "Y", "YES", "True", " yes "])
def test_parse_bool_true(utils, value):
    assert utils.parse_bool(value) is True              # BUG: upper case fails


@pytest.mark.parametrize("value", ["n", "no", "false", "0", "N", "No", "FALSE", "  n"])
def test_parse_bool_false(utils, value):
    assert utils.parse_bool(value) is False


@pytest.mark.parametrize("value", ["", "maybe", "2", "yess"])
def test_parse_bool_rejects_other_values(utils, value):
    with pytest.raises(ValueError):
        utils.parse_bool(value)
