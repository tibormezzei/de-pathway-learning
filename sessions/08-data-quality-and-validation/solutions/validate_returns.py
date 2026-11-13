"""Session 08 reference solution: validate business survey returns with Pandera, then quarantine.

Run from the session folder:  python solutions/validate_returns.py
"""

import warnings
from pathlib import Path

import pandas as pd
import pandera as pa

DATA = Path(__file__).resolve().parents[1] / "data" / "returns.csv"

REGIONS = ["Wales", "Scotland", "Northern Ireland", "North East", "North West", "London",
           "South East", "South West"]
VALID_PERIODS = [f"2026{m:02d}" for m in range(1, 7)]       # the survey covers Jan–Jun 2026


def read_returns(path: Path = DATA) -> pd.DataFrame:
    """Read codes as text so leading zeros survive; let numbers be numbers."""
    return pd.read_csv(path, dtype={"ru_ref": str, "period": str, "sic_code": str, "region": str})


schema = pa.DataFrameSchema(
    columns={
        "ru_ref":    pa.Column(str, pa.Check.str_matches(r"^\d{11}$"), nullable=False),
        "period":    pa.Column(str, pa.Check.isin(VALID_PERIODS), nullable=False),
        "sic_code":  pa.Column(str, pa.Check.str_matches(r"^\d{5}$"), nullable=False),
        "region":    pa.Column(str, pa.Check.isin(REGIONS), nullable=False),
        "employees": pa.Column(float, [pa.Check.ge(0),
                                       pa.Check(lambda s: s == s.round(), error="whole number")],
                               nullable=False),
        "turnover":  pa.Column(float, pa.Check.ge(0), nullable=False),
    },
    checks=[
        # Cross-field plausibility: WARN, don't fail. A human should look at these.
        pa.Check(lambda df: ~((df["employees"] == 0) & (df["turnover"] > 1_000_000)),
                 name="zero_employees_high_turnover", raise_warning=True),
    ],
    unique=["ru_ref", "period"],
    report_duplicates="all",
    strict=True,             # unexpected extra columns are an error
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
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        valid, quarantined, failures = validate(df)

    print(f"Read {len(df)} rows: {len(valid)} valid, {len(quarantined)} quarantined\n")
    print("Failures by check:")
    print(failures.groupby(["column", "check"], dropna=False).size().to_string(), "\n")
    for w in caught:
        if "zero_employees_high_turnover" in str(w.message):
            print("WARNING (not quarantined): zero employees but turnover > 1m. Refer for review.")


if __name__ == "__main__":
    main()
