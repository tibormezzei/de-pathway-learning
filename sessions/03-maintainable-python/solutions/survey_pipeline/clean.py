"""Cleaning steps. Each function takes a DataFrame and returns a new one."""

from datetime import datetime

import pandas as pd

from survey_pipeline import config


def standardise_region(df: pd.DataFrame) -> pd.DataFrame:
    """Trim, fix known abbreviations and title-case the region column."""
    region = df["region"].str.strip().str.lower().replace(config.REGION_ALIASES)
    return df.assign(region=region.str.title())


def parse_date(value: str) -> datetime | None:
    """Parse a date in any of the accepted formats, or return None."""
    for fmt in config.DATE_FORMATS:
        try:
            return datetime.strptime(value, fmt)
        except (TypeError, ValueError):
            continue
    return None


def parse_interview_dates(df: pd.DataFrame) -> pd.DataFrame:
    """Convert interview_date strings to datetimes."""
    return df.assign(interview_date=pd.to_datetime(df["interview_date"].map(parse_date)))


def filter_valid_ages(
    df: pd.DataFrame, min_age: int = config.MIN_AGE, max_age: int = config.MAX_AGE
) -> pd.DataFrame:
    """Keep rows with a numeric age in [min_age, max_age]; drop blanks and out-of-range values."""
    age = pd.to_numeric(df["age"], errors="coerce")
    return df.assign(age=age)[age.between(min_age, max_age)]


def drop_duplicate_cases(df: pd.DataFrame, keys: list[str] = config.DEDUP_KEYS) -> pd.DataFrame:
    """Keep the first submission for each case."""
    return df.drop_duplicates(subset=keys, keep="first")


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """Run all cleaning steps in order."""
    return (
        df.pipe(standardise_region)
        .pipe(parse_interview_dates)
        .pipe(filter_valid_ages)
        .pipe(drop_duplicate_cases)
    )
