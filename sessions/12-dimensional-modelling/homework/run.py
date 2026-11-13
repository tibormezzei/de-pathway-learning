"""Load the operational CSVs as tables, run your star-schema SQL, then your question queries.

Run from the session folder:
    python homework/run.py homework/my_star.sql homework/my_questions.sql
"""

import sys
from pathlib import Path

import duckdb

DATA = Path(__file__).resolve().parents[1] / "data"


def main() -> None:
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    sys.stdout.reconfigure(encoding="utf-8")
    con = duckdb.connect()
    for csv in sorted(DATA.glob("*.csv")):
        con.execute(f"CREATE VIEW {csv.stem} AS SELECT * FROM read_csv_auto('{csv.as_posix()}')")

    con.execute(Path(sys.argv[1]).read_text())
    print("Tables built:")
    con.sql("SELECT table_name, estimated_size AS approx_rows FROM duckdb_tables() ORDER BY 1").show()

    for stmt in Path(sys.argv[2]).read_text().split(";"):
        code = "\n".join(l for l in stmt.splitlines() if not l.strip().startswith("--")).strip()
        if code:
            print(stmt.strip())
            con.sql(code).show(max_rows=40)


if __name__ == "__main__":
    main()
