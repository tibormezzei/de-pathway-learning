"""Split visits into valid rows and a quarantine with one reason per row."""
from __future__ import annotations

from pyspark.sql import DataFrame
from pyspark.sql import functions as F

from . import config


def reject_reason(known_member: str = "_known_member"):
    """First failing rule wins (order = config.REJECT_REASONS). Null-safe."""
    return (
        F.when(F.trim("card_number") == config.TEST_CARD, "test_card")
        .when(F.col(known_member).isNull(), "unknown_member")
        .when(F.col("centre_code").isNull(), "unknown_centre")
        .when(F.col("entry_ts").isNull() | F.col("exit_ts").isNull(), "missing_timestamp")
        .when(F.col("exit_ts") <= F.col("entry_ts"), "exit_not_after_entry")
        .when(F.col("activity").isNull() | ~F.col("activity").isin(config.VALID_ACTIVITIES),
              "unknown_activity")
    )


def split_valid(visits: DataFrame, members: DataFrame) -> tuple[DataFrame, DataFrame]:
    known = members.select("member_id", F.lit(True).alias("_known_member"))
    checked = (
        visits.join(known, "member_id", "left")
        .withColumn("reject_reason", reject_reason())
        .drop("_known_member")
    )
    valid = checked.filter(F.col("reject_reason").isNull()).drop("reject_reason")
    quarantine = checked.filter(F.col("reject_reason").isNotNull())
    return valid, quarantine
