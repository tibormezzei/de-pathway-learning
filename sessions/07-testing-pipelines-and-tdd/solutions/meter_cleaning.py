"""Cleaning smart-meter readings (session 07 reference solution, built test-first).

Input columns (all strings, as they arrive from the supplier):
    meter_id, reading_date (yyyy-MM-dd), reading_kwh (e.g. "1,234.5"), submitted_at (ISO timestamp)
"""

from pyspark.sql import DataFrame, Window
from pyspark.sql import functions as F


def parse_reading(df: DataFrame) -> DataFrame:
    """R1: convert reading_kwh text to a double. Thousands separators allowed; junk becomes null."""
    cleaned = F.regexp_replace(F.trim(F.col("reading_kwh")), ",", "")
    return df.withColumn(
        "reading_kwh",
        F.when(cleaned.rlike(r"^-?\d+(\.\d+)?$"), cleaned.cast("double")),
    )


def flag_invalid(df: DataFrame) -> DataFrame:
    """R2: add is_valid: True only if reading_kwh is not null and not negative."""
    return df.withColumn(
        "is_valid", F.coalesce(F.col("reading_kwh") >= 0, F.lit(False))
    )


def latest_per_meter_day(df: DataFrame) -> DataFrame:
    """R3: keep only the most recently submitted reading for each meter and day."""
    latest_first = Window.partitionBy("meter_id", "reading_date").orderBy(
        F.col("submitted_at").desc()
    )
    return (
        df.withColumn("_rn", F.row_number().over(latest_first))
        .filter(F.col("_rn") == 1)
        .drop("_rn")
    )


def clean_readings(df: DataFrame) -> DataFrame:
    """R4: parse, keep the latest submission, then flag validity.

    Deduplicate BEFORE flagging: a later resubmission replaces an earlier one even if
    the later one turns out to be invalid (the supplier's latest word wins).
    """
    return df.transform(parse_reading).transform(latest_per_meter_day).transform(flag_invalid)
