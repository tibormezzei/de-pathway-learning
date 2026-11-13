"""Load the operational CSVs, build the star schema and answer the questions.

Run from the session folder:  python solutions/build_star.py
"""

import sys
from pathlib import Path

import duckdb

HERE = Path(__file__).resolve().parent
DATA = HERE.parent / "data"


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    con = duckdb.connect()
    for csv in sorted(DATA.glob("*.csv")):
        con.execute(f"CREATE VIEW {csv.stem} AS SELECT * FROM read_csv_auto('{csv.as_posix()}')")

    con.execute((HERE / "build_star.sql").read_text())

    tickets = con.sql("SELECT COUNT(*) FROM tickets").fetchone()[0]
    facts = con.sql("SELECT COUNT(*) FROM fact_ticket_sale").fetchone()[0]
    print(f"tickets: {tickets}, fact rows: {facts}, match: {tickets == facts}")
    con.sql("SELECT * FROM dim_route WHERE route_id = 7").show()

    for stmt in (HERE / "questions.sql").read_text().split(";"):
        if stmt.strip():
            print(next(l for l in stmt.splitlines() if l.startswith("-- Q")))
            con.sql(stmt).show(max_rows=40)


if __name__ == "__main__":
    main()
