"""All settings in one place. Nothing here is platform-specific: on CDP or GCP
only DATA_DIR / OUT_DIR change (HDFS path, gs:// bucket, ...)."""
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]          # capstone/
DATA_DIR = ROOT / "data"
OUT_DIR = ROOT / "output"

TEST_CARD = "9999999"
VALID_ACTIVITIES = ["Swim", "Gym", "Class"]
UNKNOWN_TYPE = "Unknown"

PERIOD_START = date(2026, 1, 1)
PERIOD_END = date(2026, 3, 31)
AGE_AS_OF = PERIOD_START                            # age bands are fixed at period start

# (label, min_age inclusive, max_age inclusive)
AGE_BANDS = [
    ("Under 16", 0, 15),
    ("16-24", 16, 24),
    ("25-44", 25, 44),
    ("45-64", 45, 64),
    ("65+", 65, 200),
]

# Order matters: a quarantined row gets the FIRST reason that applies.
REJECT_REASONS = [
    "test_card",
    "unknown_member",
    "unknown_centre",
    "missing_timestamp",
    "exit_not_after_entry",
    "unknown_activity",
]
