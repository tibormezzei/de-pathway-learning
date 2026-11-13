"""Reading and writing. The only module that knows about file paths and formats."""
from __future__ import annotations

import os
import shutil
from pathlib import Path

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import types as T

CENTRES_SCHEMA = T.StructType([
    T.StructField("centre_code", T.StringType()),
    T.StructField("centre_name", T.StringType()),
    T.StructField("local_authority", T.StringType()),
    T.StructField("opened_date", T.DateType()),
])

MEMBERS_SCHEMA = T.StructType([
    T.StructField("member_id", T.StringType()),
    T.StructField("birth_year", T.IntegerType()),
    T.StructField("home_district", T.StringType()),
    T.StructField("home_centre_code", T.StringType()),
    T.StructField("membership_type", T.StringType()),
    T.StructField("joined_date", T.DateType()),
    T.StructField("updated_at", T.TimestampType()),
])

# card_number stays a STRING: leading zeros are part of the identifier
VISITS_SCHEMA = T.StructType([
    T.StructField("visit_id", T.StringType()),
    T.StructField("card_number", T.StringType()),
    T.StructField("centre", T.StringType()),
    T.StructField("entry_ts", T.TimestampType()),
    T.StructField("exit_ts", T.TimestampType()),
    T.StructField("activity", T.StringType()),
])


def _read_csv(spark: SparkSession, path: Path, schema: T.StructType) -> DataFrame:
    # ignoreTrailingWhiteSpace=False: we want to SEE messy values and clean them explicitly
    return spark.read.csv(str(path), header=True, schema=schema, mode="FAILFAST",
                          ignoreLeadingWhiteSpace=False, ignoreTrailingWhiteSpace=False)


def read_sources(spark: SparkSession, data_dir: Path) -> dict[str, DataFrame]:
    return {
        "centres": _read_csv(spark, data_dir / "centres.csv", CENTRES_SCHEMA),
        "members": _read_csv(spark, data_dir / "members.csv", MEMBERS_SCHEMA),
        "visits": _read_csv(spark, data_dir / "visits.csv", VISITS_SCHEMA),
    }


def write_tables(tables: dict[str, DataFrame], out_dir: Path, engine: str = "auto") -> None:
    """Overwrite each table: re-running produces the same output (idempotent).

    engine="spark"  : normal Spark writer, used on CDP / Dataproc / Linux / Mac.
    engine="pandas" : local Windows fallback. Spark's writer needs hadoop.dll on
                      Windows; data this small can go via pandas + pyarrow instead.
    engine="auto"   : pandas on Windows, spark elsewhere.
    """
    if engine == "auto":
        engine = "pandas" if os.name == "nt" else "spark"
    for name, df in tables.items():
        target = out_dir / name
        if engine == "spark":
            df.write.mode("overwrite").parquet(str(target))
        else:
            if target.exists():
                shutil.rmtree(target)
            target.mkdir(parents=True)
            # microsecond timestamps: Spark cannot read pandas' default nanoseconds
            df.toPandas().to_parquet(target / "part-00000.parquet", index=False,
                                     coerce_timestamps="us", allow_truncated_timestamps=True)
