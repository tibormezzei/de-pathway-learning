"""Session 08 exercise: validate business survey returns with Pandera, then quarantine bad rows.

Run from the session folder:  python exercise/validate_returns.py

Rules from the survey team:
    ru_ref     11 digits, required
    period     yyyymm, Jan–Jun 2026 only (202601..202606), required
    sic_code   exactly 5 digits (as text), required
    region     one of REGIONS, required
    employees  whole number, >= 0, required
    turnover   >= 0, required
    (ru_ref, period) must be unique
    No unexpected extra columns
    Zero employees with turnover over £1m is suspicious: WARN, don't fail (stretch)
"""

from pathlib import Path

import pandas as pd
import pandera as pa

DATA = Path(__file__).resolve().parents[1] / "data" / "returns.csv"

REGIONS = ["Wales", "Scotland", "Northern Ireland", "North East", "North West", "London",
           "South East", "South West"]
VALID_PERIODS = [f"2026{m:02d}" for m in range(1, 7)]


def read_returns(path: Path = DATA) -> pd.DataFrame:
    """Read codes as text so leading zeros survive; let numbers be numbers."""
    return pd.read_csv(path, dtype={"ru_ref": str, "period": str, "sic_code": str, "region": str})


schema = pa.DataFrameSchema(
    columns={
        "ru_ref": pa.Column(str, pa.Check.str_matches(r"^\d{11}$"), nullable=False),
        "turnover": pa.Column(float, pa.Check.ge(0), nullable=False),
        # TODO period, sic_code, region, employees
        # Useful: pa.Check.isin([...]), pa.Check.str_matches(regex), pa.Check.ge(0),
        #         pa.Check(lambda s: <boolean Series>, error="message")
    },
    # TODO uniqueness of (ru_ref, period): unique=[...], report_duplicates="all"
    # TODO strict=True
)


def validate(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Return (valid rows, quarantined rows, failure report). Never raises on bad data."""
    try:
        schema.validate(df, lazy=True)          # lazy=True: collect ALL failures, not just the first
        return df, df.iloc[0:0], pd.DataFrame()
    except pa.errors.SchemaErrors as err:
        failures = err.failure_cases
        bad_index = failures["index"].dropna().astype(int).unique()
        return df.drop(index=bad_index), df.loc[bad_index], failures


def main() -> None:
    df = read_returns()
    valid, quarantined, failures = validate(df)
    print(f"Read {len(df)} rows: {len(valid)} valid, {len(quarantined)} quarantined\n")
    if len(failures):
        print("Failures by check:")
        print(failures.groupby(["column", "check"], dropna=False).size().to_string())


if __name__ == "__main__":
    main()
