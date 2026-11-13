from datetime import datetime

from pyspark.sql import functions as F

from leisure_pipeline import transform

MEMBER_COLS = "member_id string, birth_year int, home_district string, home_centre_code string, " \
              "membership_type string, joined_date date, updated_at timestamp"


def member(mid, code="LC01", mtype="Standard", updated="2025-01-01 00:00:00"):
    return (mid, 1990, "NS1", code, mtype, None, datetime.fromisoformat(updated))


def test_member_codes_are_trimmed_and_upper_cased(spark):
    df = spark.createDataFrame([member("M00001", " lc03 ")], MEMBER_COLS)
    out = transform.standardise_members(df).collect()
    assert out[0]["home_centre_code"] == "LC03"


def test_latest_member_version_wins(spark):
    df = spark.createDataFrame([
        member("M00001", "LC01", updated="2025-01-01 00:00:00"),
        member("M00001", "LC05", updated="2025-06-01 00:00:00"),
    ], MEMBER_COLS)
    out = transform.standardise_members(df).collect()
    assert len(out) == 1
    assert out[0]["home_centre_code"] == "LC05"


def test_missing_membership_type_becomes_unknown(spark):
    df = spark.createDataFrame([member("M00001", mtype=None), member("M00002", mtype="  ")], MEMBER_COLS)
    out = {r["member_id"]: r["membership_type"] for r in transform.standardise_members(df).collect()}
    assert out == {"M00001": "Unknown", "M00002": "Unknown"}


def test_card_number_maps_to_member_id_keeping_leading_zeros_meaningful(spark):
    df = spark.createDataFrame([("0001240",), ("0000007",), ("9999999",), ("ABC",)], "card_number string")
    out = [r[0] for r in df.select(transform.card_to_member_id()).collect()]
    assert out == ["M01240", "M00007", None, None]


def test_centre_names_match_regardless_of_case_and_spaces(spark):
    centres = spark.createDataFrame([("LC02", "Hillcrest Pool", "Northshire", None)],
                                    "centre_code string, centre_name string, local_authority string, opened_date date")
    visits = spark.createDataFrame([
        ("V1", "0000001", "Hillcrest Pool", datetime(2026, 1, 5, 9), datetime(2026, 1, 5, 10), "Swim"),
        ("V2", "0000001", "HILLCREST POOL", datetime(2026, 1, 5, 9), datetime(2026, 1, 5, 10), "Swim"),
        ("V3", "0000001", "Hillcrest Pool  ", datetime(2026, 1, 5, 9), datetime(2026, 1, 5, 10), "Swim"),
        ("V4", "0000001", "Nowhere Baths", datetime(2026, 1, 5, 9), datetime(2026, 1, 5, 10), "Swim"),
    ], "visit_id string, card_number string, centre string, entry_ts timestamp, exit_ts timestamp, activity string")
    out = {r["visit_id"]: r["centre_code"] for r in transform.standardise_visits(visits, centres).collect()}
    assert out == {"V1": "LC02", "V2": "LC02", "V3": "LC02", "V4": None}


def test_standardise_visits_keeps_every_row_and_computes_duration(spark):
    centres = spark.createDataFrame([("LC02", "Hillcrest Pool", "Northshire", None)],
                                    "centre_code string, centre_name string, local_authority string, opened_date date")
    visits = spark.createDataFrame([
        ("V1", "0000001", "Hillcrest Pool", datetime(2026, 1, 5, 9, 0), datetime(2026, 1, 5, 10, 15), "Swim"),
        ("V2", "0000001", "Unknown Place", datetime(2026, 1, 5, 9, 0), datetime(2026, 1, 5, 9, 30), "Gym"),
    ], "visit_id string, card_number string, centre string, entry_ts timestamp, exit_ts timestamp, activity string")
    out = transform.standardise_visits(visits, centres)
    assert out.count() == 2                       # left join: no silent loss
    assert out.filter(F.col("visit_id") == "V1").first()["duration_min"] == 75
