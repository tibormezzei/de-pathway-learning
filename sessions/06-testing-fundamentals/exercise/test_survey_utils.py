"""Session 06 exercise: write tests from the docstrings in survey_utils.py.

Run:  python -m pytest -v exercise
"""

import pytest

from survey_utils import age_band, normalise_postcode, parse_bool, response_rate


# --- Example tests to get you started ---------------------------------------------

def test_normalise_postcode_adds_space_and_uppercases():
    # Arrange
    raw = "np108xg"
    # Act
    result = normalise_postcode(raw)
    # Assert
    assert result == "NP10 8XG"


@pytest.mark.parametrize("age, expected", [
    (0, "0-15"),
    (30, "25-44"),
])
def test_age_band(age, expected):
    assert age_band(age) == expected


def test_age_band_rejects_negative_age():
    with pytest.raises(ValueError):
        age_band(-1)


# --- Your tests ------------------------------------------------------------------
# TODO normalise_postcode: whitespace (leading, trailing, internal; remember whitespace isn't
#      only spaces), already-correct input, a short postcode like "M1 1AE"
# TODO age_band: add the BOUNDARIES to the parametrize list (15/16, 24/25, 44/45, 64/65)
# TODO response_rate: a normal case, rounding, issued == 0, complete > issued, negatives
# TODO parse_bool: every True value, every False value, case, whitespace, an invalid value
