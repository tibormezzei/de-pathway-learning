"""Session 07 reference tests, roughly in the order they were written during TDD."""

import pytest
from pyspark.testing import assertDataFrameEqual

from meter_cleaning import clean_readings, flag_invalid, latest_per_meter_day, parse_reading

COLS = ["meter_id", "reading_date", "reading_kwh", "submitted_at"]


# --- R1 parse_reading ------------------------------------------------------------

@pytest.mark.parametrize("raw, expected", [
    ("12.5", 12.5),
    ("1,234.5", 1234.5),
    (" 7 ", 7.0),
    ("-3.0", -3.0),
    ("n/a", None),
    ("", None),
    (None, None),
])
def test_parse_reading(spark, raw, expected):
    df = spark.createDataFrame([("M1", raw)], "meter_id string, reading_kwh string")
    assert parse_reading(df).first()["reading_kwh"] == expected


def test_parse_reading_produces_double_column(spark):
    df = spark.createDataFrame([("M1", "1.0")], "meter_id string, reading_kwh string")
    assert dict(parse_reading(df).dtypes)["reading_kwh"] == "double"


# --- R2 flag_invalid -------------------------------------------------------------

def test_flag_invalid(spark):
    df = spark.createDataFrame(
        [("M1", 10.0), ("M2", 0.0), ("M3", -1.0), ("M4", None)],
        "meter_id string, reading_kwh double",
    )
    expected = spark.createDataFrame(
        [("M1", 10.0, True), ("M2", 0.0, True), ("M3", -1.0, False), ("M4", None, False)],
        "meter_id string, reading_kwh double, is_valid boolean",
    )
    assertDataFrameEqual(flag_invalid(df), expected)


# --- R3 latest_per_meter_day -----------------------------------------------------

def test_latest_per_meter_day_keeps_latest_submission(spark):
    df = spark.createDataFrame([
        ("M1", "2026-03-01", "10", "2026-03-02T09:00:00"),
        ("M1", "2026-03-01", "11", "2026-03-02T17:00:00"),   # resubmitted later: wins
        ("M1", "2026-03-02", "12", "2026-03-03T09:00:00"),   # different day: kept
        ("M2", "2026-03-01", "20", "2026-03-02T09:00:00"),   # different meter: kept
    ], COLS)
    expected = spark.createDataFrame([
        ("M1", "2026-03-01", "11", "2026-03-02T17:00:00"),
        ("M1", "2026-03-02", "12", "2026-03-03T09:00:00"),
        ("M2", "2026-03-01", "20", "2026-03-02T09:00:00"),
    ], COLS)
    assertDataFrameEqual(latest_per_meter_day(df), expected)   # row order is ignored


def test_latest_per_meter_day_does_not_add_columns(spark):
    df = spark.createDataFrame([("M1", "2026-03-01", "10", "2026-03-02T09:00:00")], COLS)
    assert latest_per_meter_day(df).columns == COLS


# --- R4 clean_readings (end-to-end for the module) --------------------------------

def test_clean_readings_latest_submission_wins_even_if_invalid(spark):
    df = spark.createDataFrame([
        ("M1", "2026-03-01", "1,000.0", "2026-03-02T09:00:00"),
        ("M1", "2026-03-01", "oops", "2026-03-02T17:00:00"),
        ("M2", "2026-03-01", "-5", "2026-03-02T09:00:00"),
        ("M3", "2026-03-01", "42", "2026-03-02T09:00:00"),
    ], COLS)
    expected = spark.createDataFrame([
        ("M1", "2026-03-01", None, "2026-03-02T17:00:00", False),
        ("M2", "2026-03-01", -5.0, "2026-03-02T09:00:00", False),
        ("M3", "2026-03-01", 42.0, "2026-03-02T09:00:00", True),
    ], "meter_id string, reading_date string, reading_kwh double, submitted_at string, is_valid boolean")
    assertDataFrameEqual(clean_readings(df), expected)


def test_clean_readings_empty_input(spark):
    df = spark.createDataFrame([], ", ".join(f"{c} string" for c in COLS))
    assert clean_readings(df).count() == 0
