from datetime import date, datetime

import pytest
from pyspark.sql import functions as F

from leisure_pipeline import model


@pytest.mark.parametrize("birth_year, band", [
    (2011, "Under 16"),   # 15 at 2026-01-01
    (2010, "16-24"),      # 16
    (2001, "25-44"),      # 25
    (1981, "45-64"),      # 45
    (1962, "45-64"),      # 64
    (1961, "65+"),        # 65
])
def test_age_bands_at_boundaries(spark, birth_year, band):
    df = spark.createDataFrame([("M1", birth_year, "NS1", "LC01", "Standard", None)],
                               "member_id string, birth_year int, home_district string, "
                               "home_centre_code string, membership_type string, joined_date date")
    out = model.build_dim_member(df, as_of=date(2026, 1, 1)).first()
    assert out["age_band"] == band


def test_dim_date_covers_period_once_per_day(spark):
    d = model.build_dim_date(spark, date(2026, 1, 1), date(2026, 3, 31))
    assert d.count() == 90
    assert d.select("date_key").distinct().count() == 90
    first = d.orderBy("date").first()
    assert (first["date_key"], first["year_month"], first["day_name"], first["is_weekend"]) == \
           (20260101, "2026-01", "Thursday", False)
    assert d.filter(F.col("date_key") == 20260103).first()["is_weekend"] is True   # Saturday


def test_fact_has_one_row_per_visit_with_date_key(spark):
    valid = spark.createDataFrame([
        ("V1", "M00001", "LC01", "Gym", datetime(2026, 2, 14, 18, 30), 45),
        ("V2", "M00002", "LC02", "Swim", datetime(2026, 2, 15, 7, 5), 60),
    ], "visit_id string, member_id string, centre_code string, activity string, entry_ts timestamp, duration_min int")
    fact = model.build_fact_visit(valid)
    rows = {r["visit_id"]: r for r in fact.collect()}
    assert fact.count() == 2
    assert rows["V1"]["date_key"] == 20260214 and rows["V1"]["entry_hour"] == 18
    assert set(fact.columns) == {"visit_id", "date_key", "member_id", "centre_code",
                                 "activity", "entry_ts", "entry_hour", "duration_min"}
