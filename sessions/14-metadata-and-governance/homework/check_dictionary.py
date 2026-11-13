"""Check a data dictionary against the real output of the session 13 pipeline ("metadata as code").

Usage (from the session 14 folder):
    python homework/check_dictionary.py homework/data_dictionary.csv

Checks: every output column is documented, nothing documented is missing from the output,
types match, required fields are filled in, and allowed values are respected.
"""

import importlib.util
import os
import sys
from pathlib import Path

import pandas as pd

os.environ.setdefault("PYSPARK_PYTHON", sys.executable)
SESSION_13 = Path(__file__).resolve().parents[2] / "13-data-integration-design" / "solutions" / "integrate.py"
REQUIRED = ["column_name", "data_type", "description", "nullable", "example", "source", "transformation"]


def pipeline_output() -> pd.DataFrame:
    from pyspark.sql import SparkSession

    spec = importlib.util.spec_from_file_location("integrate", SESSION_13)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    spark = (SparkSession.builder.master("local[1]")
             .config("spark.ui.showConsoleProgress", "false").getOrCreate())
    spark.sparkContext.setLogLevel("ERROR")
    result, _, _ = module.integrate(spark)
    schema = {f.name: f.dataType.simpleString() for f in result.schema.fields}
    data = result.toPandas()
    spark.stop()
    return data, schema


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    dictionary = pd.read_csv(sys.argv[1], dtype=str).fillna("")
    problems = []

    missing_cols = [c for c in REQUIRED if c not in dictionary.columns]
    if missing_cols:
        sys.exit(f"FAIL: dictionary is missing these headings: {missing_cols}")

    for _, row in dictionary.iterrows():
        empty = [c for c in REQUIRED if not row[c].strip()]
        if empty:
            problems.append(f"{row['column_name'] or '<blank>'}: empty {empty}")

    data, schema = pipeline_output()
    documented = set(dictionary["column_name"])
    for col in schema:
        if col not in documented:
            problems.append(f"{col}: in the output but not documented")
    for col in documented - set(schema):
        problems.append(f"{col}: documented but not in the output")

    for _, row in dictionary.iterrows():
        col = row["column_name"]
        if col in schema and row["data_type"].strip().lower() != schema[col]:
            problems.append(f"{col}: documented as {row['data_type']!r}, actual type {schema[col]!r}")
        if col in data and row["nullable"].strip().lower() in ("no", "false", "n") and data[col].isna().any():
            problems.append(f"{col}: documented as not nullable, but has nulls")
        allowed = row.get("allowed_values", "").strip()
        if col in data and allowed:
            permitted = {v.strip() for v in allowed.split("|")}
            bad = set(data[col].dropna().astype(str)) - permitted
            if bad:
                problems.append(f"{col}: values not in allowed_values: {sorted(bad)}")

    if problems:
        print("FAIL: dictionary and data disagree:")
        for p in problems:
            print(f"  - {p}")
        sys.exit(1)
    print(f"PASS: all {len(schema)} output columns documented and consistent with the data.")


if __name__ == "__main__":
    main()
