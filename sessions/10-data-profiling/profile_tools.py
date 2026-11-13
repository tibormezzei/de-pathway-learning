"""Lightweight profiling helpers for session 10 (pandas only, no extra installs).

    from profile_tools import profile, patterns, value_counts
    df = pd.read_csv("data/inspections.csv", dtype=str, keep_default_na=False)
    print(profile(df))
    print(patterns(df["address_postcode"]))
"""

import re

import pandas as pd


def _blank(s: pd.Series) -> pd.Series:
    return s.isna() | s.astype(str).str.strip().eq("")


def profile(df: pd.DataFrame) -> pd.DataFrame:
    """One row per column: completeness, cardinality, numeric range and the most common values.

    Read the file with dtype=str first. Profiling before typing shows what's really there.
    """
    rows = []
    for col in df.columns:
        s = df[col]
        blank = _blank(s)
        filled = s[~blank]
        numeric = pd.to_numeric(filled, errors="coerce")
        top = filled.value_counts().head(3)
        rows.append({
            "column": col,
            "rows": len(s),
            "blank_%": round(blank.mean() * 100, 1),
            "distinct": filled.nunique(),
            "unique_%": round(filled.nunique() / max(len(filled), 1) * 100, 1),
            "numeric_%": round(numeric.notna().mean() * 100, 1) if len(filled) else 0.0,
            "min": numeric.min() if numeric.notna().any() else filled.min() if len(filled) else None,
            "max": numeric.max() if numeric.notna().any() else filled.max() if len(filled) else None,
            "top_values": ", ".join(f"{v} ({n})" for v, n in top.items()),
        })
    return pd.DataFrame(rows).set_index("column")


def to_pattern(value: str) -> str:
    """'NP10 8XG' -> 'AA99 9AA'. Letters become A or a, digits become 9, everything else stays."""
    value = re.sub(r"[A-Z]", "A", str(value))
    value = re.sub(r"[a-z]", "a", value)
    return re.sub(r"[0-9]", "9", value)


def patterns(s: pd.Series, top: int = 10) -> pd.Series:
    """The most common shapes in a text column. Great for codes, postcodes, dates, IDs."""
    return s.fillna("<null>").map(lambda v: "<blank>" if str(v).strip() == "" else to_pattern(v)) \
            .value_counts().head(top)


def value_counts(s: pd.Series, top: int = 15) -> pd.Series:
    """Value counts including blanks, so missing values are never hidden."""
    return s.fillna("<null>").replace("", "<blank>").value_counts(dropna=False).head(top)
