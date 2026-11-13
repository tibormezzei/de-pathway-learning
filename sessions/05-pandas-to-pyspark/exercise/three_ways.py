"""Session 05 exercise: one transformation, three ways.

Question: for valid trips (0 < duration <= 180 min), what are the trip count and
average duration per start station and member type? Return the 10 busiest
station/member-type combinations.

The pandas version is done. Write the PySpark and SQL versions, then run:
    python exercise/three_ways.py
"""

import os
import sys
from pathlib import Path

import duckdb
import pandas as pd
from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F

DATA = Path(__file__).resolve().parents[1] / "data"
TRIPS, STATIONS = (DATA / "trips.csv").as_posix(), (DATA / "stations.csv").as_posix()
MAX_DURATION = 180

# Spark Python workers must use this interpreter (the venv), not whatever `python` is on PATH.
os.environ.setdefault("PYSPARK_PYTHON", sys.executable)


# --- 1. pandas (done) ---------------------------------------------------------
def with_pandas() -> pd.DataFrame:
    trips = pd.read_csv(TRIPS)
    stations = pd.read_csv(STATIONS)
    valid = trips[(trips["duration_min"] > 0) & (trips["duration_min"] <= MAX_DURATION)]
    return (
        valid.merge(stations, left_on="start_station_id", right_on="station_id", how="left")
        .groupby(["station_name", "member_type"], as_index=False)
        .agg(trips=("trip_id", "count"), avg_duration=("duration_min", "mean"))
        .assign(avg_duration=lambda d: d["avg_duration"].round(1))
        .sort_values(["trips", "station_name", "member_type"], ascending=[False, True, True])
        .head(10)
        .reset_index(drop=True)
    )


# --- 2. PySpark DataFrame API (TODO) ------------------------------------------
def with_pyspark(spark: SparkSession) -> DataFrame:
    trips = spark.read.csv(TRIPS, header=True, inferSchema=True)
    stations = spark.read.csv(STATIONS, header=True, inferSchema=True)
    # TODO: filter -> join -> groupBy/agg -> orderBy -> limit
    # Useful: F.col, F.count, F.avg, F.round, F.desc, .alias(...)
    raise NotImplementedError


# --- 3. SQL (TODO) --------------------------------------------------------------
# Write ONE query. It will run unchanged in both DuckDB and Spark SQL.
# Tables available: trips, stations
SQL = """
-- TODO
"""


def with_duckdb() -> pd.DataFrame:
    con = duckdb.connect()
    con.execute(f"CREATE VIEW trips AS SELECT * FROM read_csv_auto('{TRIPS}')")
    con.execute(f"CREATE VIEW stations AS SELECT * FROM read_csv_auto('{STATIONS}')")
    return con.sql(SQL).df()


def with_spark_sql(spark: SparkSession) -> DataFrame:
    spark.read.csv(TRIPS, header=True, inferSchema=True).createOrReplaceTempView("trips")
    spark.read.csv(STATIONS, header=True, inferSchema=True).createOrReplaceTempView("stations")
    return spark.sql(SQL)


# --- compare (no changes needed) -------------------------------------------------
def same(a: pd.DataFrame, b: pd.DataFrame) -> bool:
    try:
        pd.testing.assert_frame_equal(a.reset_index(drop=True), b.reset_index(drop=True),
                                      check_dtype=False)
        return True
    except AssertionError as err:
        print(err)
        return False


def main() -> None:
    spark = (SparkSession.builder.master("local[2]").appName("three-ways")
             .config("spark.sql.shuffle.partitions", "4").getOrCreate())
    spark.sparkContext.setLogLevel("ERROR")

    pdf = with_pandas()
    print("pandas:\n", pdf, "\n")

    spark_df = with_pyspark(spark)
    print("Physical plan (look for 'Exchange' = shuffle):")
    spark_df.explain()

    results = {
        "PySpark": spark_df.toPandas(),       # fine here: the result is only 10 rows
        "Spark SQL": with_spark_sql(spark).toPandas(),
        "DuckDB": with_duckdb(),
    }
    for name, df in results.items():
        print(f"pandas == {name}: {same(pdf, df)}")

    spark.stop()


if __name__ == "__main__":
    main()
