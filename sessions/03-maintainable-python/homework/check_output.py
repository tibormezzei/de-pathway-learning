"""Check that your refactored pipeline produces the same output as the original.

Usage:
    python check_output.py path/to/your/response_rates.csv

Refactoring means changing the structure without changing the behaviour, so
your output must match expected_response_rates.csv exactly.
"""

import sys
from pathlib import Path

import pandas as pd

EXPECTED = Path(__file__).parent / "expected_response_rates.csv"


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    actual = pd.read_csv(sys.argv[1])
    expected = pd.read_csv(EXPECTED)
    try:
        pd.testing.assert_frame_equal(actual, expected, check_dtype=False)
    except AssertionError as err:
        sys.exit(f"FAIL: output differs from the original:\n{err}")
    print("PASS: output matches the original. Behaviour preserved.")


if __name__ == "__main__":
    main()
