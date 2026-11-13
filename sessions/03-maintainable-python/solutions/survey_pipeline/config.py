"""Business rules, kept in one place and separate from the logic that uses them."""

MIN_AGE = 16
MAX_AGE = 120

REGION_ALIASES = {"sth": "south", "wst": "west"}

DATE_FORMATS = ("%Y-%m-%d", "%d/%m/%Y", "%d-%b-%Y")

DEDUP_KEYS = ["case_id"]

# A partial interview counts as half a response.
OUTCOME_WEIGHTS = {"complete": 1.0, "partial": 0.5}
