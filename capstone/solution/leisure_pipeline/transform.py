"""Standardising each source so the two systems can be joined."""
from __future__ import annotations

from pyspark.sql import DataFrame, Window
from pyspark.sql import functions as F

from . import config


def standardise_members(members: DataFrame) -> DataFrame:
    """One row per member: clean codes, fill missing type, keep the latest version."""
    latest_first = Window.partitionBy("member_id").orderBy(F.col("updated_at").desc())
    mtype = F.trim("membership_type")
    return (
        members
        .withColumn("home_centre_code", F.upper(F.trim("home_centre_code")))
        .withColumn("membership_type",
                    F.when(mtype.isNull() | (mtype == ""), F.lit(config.UNKNOWN_TYPE)).otherwise(mtype))
        .withColumn("_rn", F.row_number().over(latest_first))
        .filter(F.col("_rn") == 1)
        .drop("_rn")
    )


def card_to_member_id(card_col: str = "card_number"):
    """Turnstile card '0001240' -> CRM member id 'M01240'. Test card -> null."""
    card = F.trim(F.col(card_col))
    return (
        F.when(card == config.TEST_CARD, F.lit(None).cast("string"))
        .when(card.rlike(r"^\d+$"), F.format_string("M%05d", card.cast("int")))
    )


def standardise_visits(visits: DataFrame, centres: DataFrame) -> DataFrame:
    """Map card -> member_id and centre name -> centre_code; add duration.

    Expects exact duplicates to have been removed already (see run.py), so the
    removal can be counted for reconciliation.
    """
    centre_lookup = centres.select(
        F.lower(F.trim("centre_name")).alias("_centre_key"), "centre_code"
    )
    return (
        visits
        .withColumn("member_id", card_to_member_id())
        .withColumn("_centre_key", F.lower(F.trim("centre")))
        .join(centre_lookup, "_centre_key", "left")      # left: unmatched centres are quarantined, not lost
        .drop("_centre_key")
        .withColumn("duration_min",
                    ((F.unix_timestamp("exit_ts") - F.unix_timestamp("entry_ts")) / 60).cast("int"))
    )
