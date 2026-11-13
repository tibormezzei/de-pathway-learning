"""End-to-end test on a tiny hand-made dataset: reconciliation + idempotency."""
from pathlib import Path

import pandas as pd

from leisure_pipeline.__main__ import run

CENTRES = """centre_code,centre_name,local_authority,opened_date
LC01,Riverside Leisure Centre,Northshire,2009-05-01
LC02,Hillcrest Pool,Northshire,1998-09-14
"""
MEMBERS = """member_id,birth_year,home_district,home_centre_code,membership_type,joined_date,updated_at
M00001,1990,NS1,lc01,Standard,2020-01-01,2020-01-02 00:00:00
M00002,2012,NS2,LC02,Junior,2021-01-01,2021-01-02 00:00:00
M00002,2012,NS2,LC01,Junior,2021-01-01,2023-05-01 00:00:00
"""
VISITS = """visit_id,card_number,centre,entry_ts,exit_ts,activity
V1,0000001,Riverside Leisure Centre,2026-01-05 09:00:00,2026-01-05 10:00:00,Gym
V2,0000002,HILLCREST POOL,2026-01-06 16:00:00,2026-01-06 17:00:00,Swim
V2,0000002,HILLCREST POOL,2026-01-06 16:00:00,2026-01-06 17:00:00,Swim
V3,9999999,Hillcrest Pool,2026-01-07 08:00:00,2026-01-07 08:05:00,Swim
V4,0004242,Hillcrest Pool,2026-01-07 08:00:00,2026-01-07 09:00:00,Swim
V5,0000001,Riverside Leisure Centre,2026-02-01 10:00:00,2026-02-01 09:00:00,Gym
"""


def make_sources(tmp_path: Path) -> Path:
    data = tmp_path / "data"
    data.mkdir()
    (data / "centres.csv").write_text(CENTRES)
    (data / "members.csv").write_text(MEMBERS)
    (data / "visits.csv").write_text(VISITS)
    return data


def test_end_to_end_reconciles(spark, tmp_path):
    counts, tables = run(spark, make_sources(tmp_path), tmp_path / "out")
    assert counts == {"visits_in": 6, "duplicates": 1, "fact": 2, "quarantine": 3, "members": 2}
    reasons = sorted(r["reject_reason"] for r in tables["quarantine_visits"].collect())
    assert reasons == ["exit_not_after_entry", "test_card", "unknown_member"]


def test_rerun_gives_identical_output(spark, tmp_path):
    data, out = make_sources(tmp_path), tmp_path / "out"
    run(spark, data, out)
    first = pd.read_parquet(out / "fact_visit").sort_values("visit_id").reset_index(drop=True)
    run(spark, data, out)
    second = pd.read_parquet(out / "fact_visit").sort_values("visit_id").reset_index(drop=True)
    pd.testing.assert_frame_equal(first, second)
    assert len(second) == 2                     # not doubled
