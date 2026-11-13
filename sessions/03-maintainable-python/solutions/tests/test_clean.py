"""A taste of what small functions make possible. Session 06 covers testing properly."""

import pandas as pd

from survey_pipeline.clean import filter_valid_ages, parse_date, standardise_region


def test_standardise_region_fixes_case_whitespace_and_aliases():
    df = pd.DataFrame({"region": [" north ", "SOUTH", "Sth", "wst"]})
    assert standardise_region(df)["region"].tolist() == ["North", "South", "South", "West"]


def test_parse_date_accepts_all_formats():
    assert parse_date("2026-01-05") == parse_date("05/01/2026") == parse_date("05-Jan-2026")


def test_parse_date_returns_none_for_garbage():
    assert parse_date("not a date") is None


def test_filter_valid_ages_drops_blank_and_out_of_range():
    df = pd.DataFrame({"age": ["", "15", "16", "120", "121", "abc"]})
    assert filter_valid_ages(df)["age"].tolist() == [16, 120]
