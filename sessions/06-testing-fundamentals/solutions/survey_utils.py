"""Small utility functions used across a survey pipeline.

Fixed version (session 06 reference solution). Four bugs corrected:
normalise_postcode with tabs/newlines, age_band(64), response_rate with issued == 0,
and parse_bool case-sensitivity.
"""


def normalise_postcode(raw: str) -> str:
    """Return a UK postcode in standard form: upper case, one space before the last 3 characters.

    Leading, trailing and internal whitespace is ignored.

    >>> normalise_postcode("  np10 8xg ")
    'NP10 8XG'
    >>> normalise_postcode("np108xg")
    'NP10 8XG'
    """
    compact = "".join(raw.split()).upper()
    return f"{compact[:-3]} {compact[-3:]}"


def age_band(age: int) -> str:
    """Return the age band for an age in whole years.

    Bands: "0-15", "16-24", "25-44", "45-64", "65+".
    Raises ValueError for negative ages.
    """
    if age < 0:
        raise ValueError(f"age cannot be negative: {age}")
    if age <= 15:
        return "0-15"
    if age <= 24:
        return "16-24"
    if age <= 44:
        return "25-44"
    if age <= 64:
        return "45-64"
    return "65+"


def response_rate(complete: int, issued: int) -> float | None:
    """Return complete / issued as a percentage, rounded to 1 decimal place.

    Returns None when issued is 0 (a rate can't be calculated).
    Raises ValueError if complete is greater than issued, or if either is negative.
    """
    if complete < 0 or issued < 0:
        raise ValueError("counts cannot be negative")
    if complete > issued:
        raise ValueError("complete cannot exceed issued")
    if issued == 0:
        return None
    return round(complete / issued * 100, 1)


def parse_bool(value: str) -> bool:
    """Parse a yes/no style answer. Case-insensitive; surrounding whitespace is ignored.

    True:  "y", "yes", "true", "1"
    False: "n", "no", "false", "0"
    Anything else raises ValueError.
    """
    cleaned = value.strip().lower()
    if cleaned in {"y", "yes", "true", "1"}:
        return True
    if cleaned in {"n", "no", "false", "0"}:
        return False
    raise ValueError(f"not a yes/no value: {value!r}")
