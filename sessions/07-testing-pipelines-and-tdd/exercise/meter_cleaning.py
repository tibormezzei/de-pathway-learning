"""Cleaning smart-meter readings. Build this test-first!

Input columns (all strings, as they arrive from the supplier):
    meter_id, reading_date (yyyy-MM-dd), reading_kwh (e.g. "1,234.5"), submitted_at (ISO timestamp)

Requirements (see exercise/README.md):
    R1 parse_reading         reading_kwh text -> double; thousands separators allowed; junk -> null
    R2 flag_invalid          add is_valid: True only if reading_kwh is not null and >= 0
    R3 latest_per_meter_day  keep only the latest submitted_at per (meter_id, reading_date)
    R4 clean_readings        parse -> latest -> flag
"""

from pyspark.sql import DataFrame, Window          # noqa: F401  (you'll need these)
from pyspark.sql import functions as F             # noqa: F401


def parse_reading(df: DataFrame) -> DataFrame:
    raise NotImplementedError


def flag_invalid(df: DataFrame) -> DataFrame:
    raise NotImplementedError


def latest_per_meter_day(df: DataFrame) -> DataFrame:
    raise NotImplementedError


def clean_readings(df: DataFrame) -> DataFrame:
    raise NotImplementedError
