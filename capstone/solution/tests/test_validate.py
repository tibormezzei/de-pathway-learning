from datetime import datetime

import pytest

from leisure_pipeline import validate

COLS = ("visit_id string, card_number string, member_id string, centre_code string, "
        "entry_ts timestamp, exit_ts timestamp, activity string")
T0 = datetime(2026, 2, 1, 10, 0)
T1 = datetime(2026, 2, 1, 11, 0)


def good(**overrides):
    row = dict(visit_id="V1", card_number="0000001", member_id="M00001", centre_code="LC01",
               entry_ts=T0, exit_ts=T1, activity="Gym")
    row.update(overrides)
    return row


@pytest.fixture
def members(spark):
    return spark.createDataFrame([("M00001",)], "member_id string")


def reason_for(spark, members, row):
    df = spark.createDataFrame([tuple(row.values())], COLS)
    valid, quarantine = validate.split_valid(df, members)
    q = quarantine.collect()
    return q[0]["reject_reason"] if q else None


def test_good_row_is_valid(spark, members):
    assert reason_for(spark, members, good()) is None


@pytest.mark.parametrize("overrides, expected", [
    (dict(card_number="9999999", member_id=None), "test_card"),
    (dict(member_id="M09999"), "unknown_member"),
    (dict(centre_code=None), "unknown_centre"),
    (dict(exit_ts=None), "missing_timestamp"),
    (dict(exit_ts=T0), "exit_not_after_entry"),
    (dict(exit_ts=datetime(2026, 2, 1, 9, 0)), "exit_not_after_entry"),
    (dict(activity="UNK"), "unknown_activity"),
    (dict(activity=None), "unknown_activity"),        # null must not slip through isin()
])
def test_each_rule_quarantines_with_its_reason(spark, members, overrides, expected):
    assert reason_for(spark, members, good(**overrides)) == expected


def test_first_failing_rule_wins(spark, members):
    # unknown member AND bad activity -> reported as unknown_member
    assert reason_for(spark, members, good(member_id="M09999", activity="UNK")) == "unknown_member"


def test_split_is_lossless(spark, members):
    rows = [tuple(good(visit_id=f"V{i}", activity=a).values())
            for i, a in enumerate(["Gym", "UNK", "Swim", None, "Class"])]
    df = spark.createDataFrame(rows, COLS)
    valid, quarantine = validate.split_valid(df, members)
    assert valid.count() + quarantine.count() == df.count()
    assert valid.count() == 3
