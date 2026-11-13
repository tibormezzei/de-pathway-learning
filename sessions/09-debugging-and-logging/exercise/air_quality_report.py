"""Monthly air-quality report: mean PM2.5 and days over the limit, per station, for March 2026.

Run from the session folder:  python exercise/air_quality_report.py

It's broken. See exercise/README.md.
"""

from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[1] / "data"
DAILY_LIMIT = 15.0          # µg/m³
DETECTION_LIMIT_VALUE = 2.5  # agreed rule: "<5" (below detection) is reported as half the limit


def load_readings() -> pd.DataFrame:
    df = pd.read_csv(DATA / "readings.csv")
    df.columns = df.columns.str.lower()
    return df


def load_stations() -> pd.DataFrame:
    df = pd.read_csv(DATA / "stations.csv")
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    return df


def filter_month(df: pd.DataFrame, start: str, end: str) -> pd.DataFrame:
    return df[(df["reading_date"] > start) & (df["reading_date"] <= end)]


def summarise(readings: pd.DataFrame, stations: pd.DataFrame) -> pd.DataFrame:
    joined = readings.merge(stations, on="station_id", how="left")
    return (
        joined.groupby(["station_id", "station_name"], as_index=False)
        .agg(days=("pm25", "size"),
             mean_pm25=("pm25", "mean"),
             days_over_limit=("pm25", lambda s: (s > DAILY_LIMIT).sum()))
        .round({"mean_pm25": 1})
    )


def main() -> None:
    readings = load_readings()
    print("loaded")
    march = filter_month(readings, "2026-03-01", "2026-03-31")
    report = summarise(march, load_stations())
    print(report.to_string(index=False))


if __name__ == "__main__":
    main()
