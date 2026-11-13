"""Session 07 exercise: ping-pong TDD.

Person A writes ONE failing test → Person B makes it pass (simplest code possible) →
refactor together → swap roles. Repeat.

Run:  python -m pytest -v exercise
"""

from pyspark.testing import assertDataFrameEqual   # noqa: F401  (compares DataFrames, ignores row order)

from meter_cleaning import parse_reading

COLS = ["meter_id", "reading_date", "reading_kwh", "submitted_at"]


# The first test is written for you. It fails (RED). Make it pass (GREEN).
def test_parse_reading_simple_number(spark):
    df = spark.createDataFrame([("M1", "12.5")], "meter_id string, reading_kwh string")
    assert parse_reading(df).first()["reading_kwh"] == 12.5


# Next tests to write, one at a time (suggested order):
# R1  thousands separator "1,234.5" · whitespace " 7 " · junk "n/a" -> None · None -> None
#     the output column type is double
# R2  flag_invalid: positive, zero, negative, null
# R3  latest_per_meter_day: a resubmission wins · other days and meters are kept
#     no extra columns are left behind
# R4  clean_readings: if the LATEST submission is junk, the row is kept but flagged invalid
#     empty input -> empty output
