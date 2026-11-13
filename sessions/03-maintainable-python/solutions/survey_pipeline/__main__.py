"""Command-line entry point.

    python -m survey_pipeline --input data/survey_responses.csv --output output/response_rates.csv
"""

import argparse
import logging
from pathlib import Path

import pandas as pd

from survey_pipeline.clean import clean
from survey_pipeline.metrics import response_rates

logger = logging.getLogger(__name__)


def run(input_path: Path, output_path: Path) -> pd.DataFrame:
    """Read raw responses, clean them, compute response rates and write the result."""
    raw = pd.read_csv(input_path, dtype=str)
    cleaned = clean(raw)
    logger.info("Read %d rows, %d remain after cleaning", len(raw), len(cleaned))

    result = response_rates(cleaned)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    result.to_csv(output_path, index=False)
    logger.info("Wrote %d rows to %s", len(result), output_path)
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    run(args.input, args.output)


if __name__ == "__main__":
    main()
