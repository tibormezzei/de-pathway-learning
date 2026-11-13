"""Response-rate calculation."""

import pandas as pd

from survey_pipeline import config


def response_rates(df: pd.DataFrame) -> pd.DataFrame:
    """Issued, complete, partial and weighted response rate (%) per region and month."""
    counts = (
        df.assign(month=df["interview_date"].dt.strftime("%Y-%m"))
        .assign(
            complete=lambda d: d["outcome"].eq("complete"),
            partial=lambda d: d["outcome"].eq("partial"),
        )
        .groupby(["region", "month"], as_index=False)
        .agg(issued=("case_id", "size"), complete=("complete", "sum"), partial=("partial", "sum"))
    )
    weighted = (
        counts["complete"] * config.OUTCOME_WEIGHTS["complete"]
        + counts["partial"] * config.OUTCOME_WEIGHTS["partial"]
    )
    return counts.assign(response_rate=(weighted / counts["issued"] * 100).round(1))
