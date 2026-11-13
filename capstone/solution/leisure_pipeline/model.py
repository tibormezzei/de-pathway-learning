"""Dimensional output: fact_visit + dim_member, dim_centre, dim_date."""
from __future__ import annotations

from datetime import date

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F

from . import config


def age_band(age_col):
    expr = None
    for label, lo, hi in config.AGE_BANDS:
        cond = age_col.between(lo, hi)
        expr = F.when(cond, label) if expr is None else expr.when(cond, label)
    return expr.otherwise("Unknown")


def build_dim_member(members: DataFrame, as_of: date = config.AGE_AS_OF) -> DataFrame:
    """Type 1 dimension: current attributes only (see README for the SCD2 trade-off)."""
    age = F.lit(as_of.year) - F.col("birth_year")
    return members.select(
        "member_id",
        "membership_type",
        age_band(age).alias("age_band"),
        "home_district",
        "home_centre_code",
        "joined_date",
    )


def build_dim_centre(centres: DataFrame) -> DataFrame:
    return centres.select("centre_code", "centre_name", "local_authority", "opened_date")


def build_dim_date(spark: SparkSession, start: date = config.PERIOD_START,
                   end: date = config.PERIOD_END) -> DataFrame:
    n_days = (end - start).days + 1
    d = F.date_add(F.lit(start), F.col("id").cast("int"))
    return (
        spark.range(n_days)
        .select(d.alias("date"))
        .select(
            F.date_format("date", "yyyyMMdd").cast("int").alias("date_key"),
            "date",
            F.date_format("date", "yyyy-MM").alias("year_month"),
            F.date_format("date", "EEEE").alias("day_name"),
            F.dayofweek("date").isin(1, 7).alias("is_weekend"),
        )
    )


def build_fact_visit(valid_visits: DataFrame) -> DataFrame:
    """Grain: one row per valid turnstile visit."""
    return valid_visits.select(
        "visit_id",
        F.date_format("entry_ts", "yyyyMMdd").cast("int").alias("date_key"),
        "member_id",
        "centre_code",
        "activity",
        "entry_ts",
        F.hour("entry_ts").alias("entry_hour"),
        "duration_min",
    )
