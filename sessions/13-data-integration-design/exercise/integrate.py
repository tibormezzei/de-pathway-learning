"""Session 13 exercise: integrate appointments (source B) with the practice registry (source A).

Output: appointments per health board per month, plus a reconciliation and a quarantine of unmatched rows.
Run from the session folder:  python exercise/integrate.py

Complete the three TODO functions. See exercise/README.md.
"""

import os
import sys
from functools import reduce
from pathlib import Path

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F

os.environ.setdefault("PYSPARK_PYTHON", sys.executable)
DATA = Path(__file__).resolve().parents[1] / "data"

# Versioned lookup: each version and the months it applies to (inclusive, yyyy-mm)
BOARD_LOOKUP_VERSIONS = [
    ("practice_board_v1.csv", "2026-01", "2026-03"),
    ("practice_board_v2.csv", "2026-04", "9999-12"),
]


def read(spark: SparkSession, name: str) -> DataFrame:
    return spark.read.csv((DATA / name).as_posix(), header=True, inferSchema=False)


# --- Step 1: standardise the join key -------------------------------------------
def standardise_code(df: DataFrame, col: str) -> DataFrame:
    """'  w-00012 ' -> 'W00012': trim, upper-case, remove separators."""
    # TODO: trim, upper-case, and remove spaces and hyphens
    #       (F.trim, F.upper, F.regexp_replace)
    return df


# --- Step 2: map merged practices to their successor (from the effective month) --
def apply_mergers(df: DataFrame, mergers: DataFrame) -> DataFrame:
    # TODO: left-join to mergers where practice_code == old_code AND month >= effective_month,
    #       then replace practice_code with new_code where there is one (F.coalesce),
    #       and drop the merger columns.
    return df


# --- Step 3: attach the board using the lookup version valid for each month ---------
def versioned_board_lookup(spark: SparkSession) -> DataFrame:
    versions = [
        read(spark, file).withColumn("valid_from", F.lit(start)).withColumn("valid_to", F.lit(end))
        for file, start, end in BOARD_LOOKUP_VERSIONS
    ]
    return reduce(DataFrame.unionByName, versions)


def attach_board(df: DataFrame, lookup: DataFrame) -> DataFrame:
    # TODO: left-join to the lookup on practice_code AND month BETWEEN valid_from AND valid_to,
    #       then drop the duplicate practice_code and the valid_from/valid_to columns.
    #       (Until this is done, board_code doesn't exist and integrate() will fail.)
    return df


# --- Pipeline ---------------------------------------------------------------------
def integrate(spark: SparkSession) -> tuple[DataFrame, DataFrame, dict]:
    raw = read(spark, "appointments.csv").withColumn("appointments", F.col("appointments").cast("long"))
    practices = read(spark, "practices.csv")

    df = standardise_code(raw, "org_code").withColumnRenamed("org_code", "practice_code")
    df = apply_mergers(df, read(spark, "practice_mergers.csv"))
    df = attach_board(df, versioned_board_lookup(spark))

    known = df.join(practices.select("practice_code"), "practice_code", "left_semi")
    matched = known.filter(F.col("board_code").isNotNull())
    unmatched = df.join(matched.select("practice_code", "month").distinct(),
                        ["practice_code", "month"], "left_anti")

    result = (matched.join(read(spark, "boards.csv"), "board_code", "left")
              .groupBy("month", "board_code", "board_name")
              .agg(F.sum("appointments").alias("appointments"),
                   F.countDistinct("practice_code").alias("practices"))
              .orderBy("month", "board_code"))

    totals = {
        "rows_in": raw.count(),
        "appointments_in": raw.agg(F.sum("appointments")).first()[0],
        "appointments_out": result.agg(F.sum("appointments")).first()[0],
        "appointments_quarantined": unmatched.agg(F.sum("appointments")).first()[0] or 0,
        "rows_quarantined": unmatched.count(),
    }
    return result, unmatched, totals


def main() -> None:
    spark = (SparkSession.builder.master("local[2]").appName("integrate")
             .config("spark.sql.shuffle.partitions", "4").getOrCreate())
    spark.sparkContext.setLogLevel("ERROR")

    result, unmatched, t = integrate(spark)
    result.show(40, truncate=False)
    print("Quarantined (unmatched) rows:")
    unmatched.show(truncate=False)

    print("Reconciliation:")
    for k, v in t.items():
        print(f"  {k:<26}{v:>10}")
    balanced = t["appointments_in"] == t["appointments_out"] + t["appointments_quarantined"]
    print(f"  in == out + quarantined:  {balanced}")

    again, _, _ = integrate(spark)
    print(f"  idempotent (re-run gives identical output): {again.exceptAll(result).count() == 0 and result.exceptAll(again).count() == 0}")
    spark.stop()


if __name__ == "__main__":
    main()
