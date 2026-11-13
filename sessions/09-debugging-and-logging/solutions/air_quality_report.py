"""Monthly air-quality report: mean PM2.5 and days over the limit, per station, for March 2026.

Session 09 reference solution: 4 bugs fixed, logging added.
Run from the session folder:  python solutions/air_quality_report.py [--debug]
"""

import argparse
import logging
from pathlib import Path

import pandas as pd

logger = logging.getLogger("air_quality_report")

DATA = Path(__file__).resolve().parents[1] / "data"
DAILY_LIMIT = 15.0           # µg/m³
DETECTION_LIMIT_VALUE = 2.5  # agreed rule: "<5" (below detection) is reported as half the limit


def snake_case_columns(df: pd.DataFrame) -> pd.DataFrame:
    # FIX 1: readings had "Reading Date" -> "reading date" (space kept) -> KeyError 'reading_date'.
    return df.rename(columns=lambda c: c.strip().lower().replace(" ", "_"))


def load_readings() -> pd.DataFrame:
    df = snake_case_columns(pd.read_csv(DATA / "readings.csv", dtype={"PM25": str}))

    # FIX 2: "<5" made pm25 a text column -> TypeError comparing str with float.
    below_limit = df["pm25"].eq("<5")
    if below_limit.any():
        logger.warning("%d readings below detection limit; using %.1f per agreed rule",
                       below_limit.sum(), DETECTION_LIMIT_VALUE)
    df["pm25"] = pd.to_numeric(df["pm25"].mask(below_limit, str(DETECTION_LIMIT_VALUE)),
                               errors="raise")
    logger.info("Loaded %d readings for %d stations", len(df), df["station_id"].nunique())
    return df


def load_current_stations() -> pd.DataFrame:
    df = snake_case_columns(pd.read_csv(DATA / "stations.csv"))
    # FIX 4: S04 has two rows (renamed). Joining both doubled its readings. Keep the current row.
    current = df[df["valid_to"].isna()]
    if current["station_id"].duplicated().any():
        raise ValueError("stations lookup has more than one current row for a station")
    logger.info("Loaded %d current stations (%d historical rows ignored)",
                len(current), len(df) - len(current))
    return current


def filter_month(df: pd.DataFrame, start: str, end: str) -> pd.DataFrame:
    # FIX 3: `> start` dropped 1 March. Both ends inclusive for a calendar month.
    result = df[df["reading_date"].between(start, end)]
    logger.info("Filtered to %s..%s: %d rows", start, end, len(result))
    return result


def summarise(readings: pd.DataFrame, stations: pd.DataFrame) -> pd.DataFrame:
    joined = readings.merge(stations, on="station_id", how="left", validate="many_to_one")
    if len(joined) != len(readings):
        raise ValueError(f"join changed row count: {len(readings)} -> {len(joined)}")
    if joined["station_name"].isna().any():
        logger.warning("Readings for unknown stations: %s",
                       sorted(joined.loc[joined["station_name"].isna(), "station_id"].unique()))
    return (
        joined.groupby(["station_id", "station_name"], as_index=False)
        .agg(days=("pm25", "size"),
             mean_pm25=("pm25", "mean"),
             days_over_limit=("pm25", lambda s: (s > DAILY_LIMIT).sum()))
        .round({"mean_pm25": 1})
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action="store_true", help="show DEBUG messages")
    args = parser.parse_args()
    logging.basicConfig(level=logging.DEBUG if args.debug else logging.INFO,
                        format="%(asctime)s %(levelname)-7s %(name)s: %(message)s")

    march = filter_month(load_readings(), "2026-03-01", "2026-03-31")
    logger.debug("First rows after filter:\n%s", march.head())
    report = summarise(march, load_current_stations())
    logger.info("Report has %d stations", len(report))
    print(report.to_string(index=False))


if __name__ == "__main__":
    main()
