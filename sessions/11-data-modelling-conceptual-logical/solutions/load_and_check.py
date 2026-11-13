"""Session 11 reference (stretch): build the 3NF schema in DuckDB, load it from the flat export,
and prove nothing was lost by rebuilding the flat view with joins.

Run from the session folder:  python solutions/load_and_check.py
"""

import sys
from pathlib import Path

import duckdb

HERE = Path(__file__).resolve().parent
FLAT = (HERE.parent / "data" / "case_visits_flat.csv").as_posix()

LOAD = f"""
CREATE TEMP VIEW flat AS SELECT * FROM read_csv_auto('{FLAT}', all_varchar=true);

INSERT INTO region      SELECT DISTINCT region_code, region_name FROM flat;
INSERT INTO survey      SELECT DISTINCT survey_code, survey_name FROM flat;
INSERT INTO outcome     SELECT DISTINCT outcome_code, outcome_description FROM flat;
INSERT INTO interviewer SELECT DISTINCT interviewer_id, interviewer_name, region_code FROM flat;
INSERT INTO address
    SELECT ROW_NUMBER() OVER (ORDER BY postcode, address_line), address_line, postcode, region_code
    FROM (SELECT DISTINCT address_line, postcode, region_code FROM flat);
INSERT INTO survey_case
    SELECT DISTINCT f.case_id, f.survey_code, f.period, a.address_id, f.interviewer_id
    FROM flat f JOIN address a USING (address_line, postcode);
INSERT INTO visit
    SELECT case_id, CAST(visit_no AS INTEGER), CAST(visit_date AS DATE), outcome_code FROM flat;
"""

REBUILD = """
SELECT c.case_id, s.survey_code, s.survey_name, c.period, a.address_line, a.postcode,
       r.region_code, r.region_name, i.interviewer_id, i.interviewer_name,
       CAST(v.visit_no AS VARCHAR) AS visit_no, CAST(v.visit_date AS VARCHAR) AS visit_date,
       o.outcome_code, o.outcome_description
FROM visit v
JOIN survey_case c USING (case_id)
JOIN survey s      USING (survey_code)
JOIN address a     USING (address_id)
JOIN region r      ON a.region_code = r.region_code
JOIN interviewer i USING (interviewer_id)
JOIN outcome o     USING (outcome_code)
"""


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    con = duckdb.connect()
    con.execute((HERE / "schema.sql").read_text())
    con.execute(LOAD)

    for table in ["region", "survey", "outcome", "interviewer", "address", "survey_case", "visit"]:
        print(f"{table:<12} {con.sql(f'SELECT COUNT(*) FROM {table}').fetchone()[0]:>4} rows")

    diff = con.sql(f"(SELECT * FROM flat EXCEPT ALL ({REBUILD})) UNION ALL "
                   f"(({REBUILD}) EXCEPT ALL SELECT * FROM flat)").fetchall()
    print("\nRebuilt flat view identical to the original:", not diff)

    print("\nFinal outcome per case (the question the flat file made awkward):")
    con.sql("""
        SELECT s.survey_name, c.period, o.outcome_description, COUNT(*) AS cases
        FROM survey_case c
        JOIN visit v   ON v.case_id = c.case_id
        JOIN survey s  USING (survey_code)
        JOIN outcome o USING (outcome_code)
        WHERE v.visit_no = (SELECT MAX(visit_no) FROM visit WHERE case_id = c.case_id)
        GROUP BY ALL ORDER BY ALL
    """).show()


if __name__ == "__main__":
    main()
