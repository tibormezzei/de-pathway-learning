"""Run SQL against the session 04 CSVs using DuckDB.

Usage:
    python run_sql.py exercise/questions.sql      # run every query in a file
    python run_sql.py "SELECT * FROM loans LIMIT 5"

Each CSV in data/ is available as a table with the same name (loans, books, ...).
"""

import sys
from pathlib import Path

import duckdb

DATA = Path(__file__).parent / "data"


def connect() -> duckdb.DuckDBPyConnection:
    con = duckdb.connect()
    for csv in sorted(DATA.glob("*.csv")):
        con.execute(f"CREATE VIEW {csv.stem} AS SELECT * FROM read_csv_auto('{csv.as_posix()}')")
    return con


def statements(sql: str) -> list[str]:
    """Split a script into statements, ignoring ones that are only comments."""
    out = []
    for chunk in sql.split(";"):
        code = "\n".join(l for l in chunk.splitlines() if not l.strip().startswith("--")).strip()
        if code:
            out.append(chunk.strip())
    return out


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    sys.stdout.reconfigure(encoding="utf-8")   # DuckDB draws tables with box characters
    arg = sys.argv[1]
    sql = Path(arg).read_text() if arg.endswith(".sql") else arg
    con = connect()
    for stmt in statements(sql):
        print("\n" + "=" * 70)
        print(stmt)
        print("-" * 70)
        try:
            con.sql(stmt).show(max_rows=20)
        except duckdb.Error as err:
            print(f"ERROR: {err}")


if __name__ == "__main__":
    main()
