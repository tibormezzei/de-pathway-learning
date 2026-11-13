"""Run the pipeline end to end.

    cd capstone/solution
    python -m leisure_pipeline              # normal run
    python -m leisure_pipeline --debug      # more logging
"""
from __future__ import annotations

import argparse
import logging
import os
import sys
from pathlib import Path

os.environ.setdefault("PYSPARK_PYTHON", sys.executable)
os.environ.setdefault("PYSPARK_DRIVER_PYTHON", sys.executable)

from pyspark.sql import SparkSession, functions as F  # noqa: E402

from . import config, io, model, transform, validate  # noqa: E402

log = logging.getLogger("leisure_pipeline")


class ReconciliationError(Exception):
    pass


def run(spark: SparkSession, data_dir: Path, out_dir: Path) -> tuple[dict[str, int], dict]:
    src = io.read_sources(spark, data_dir)

    # --- members -----------------------------------------------------------
    members_in = src["members"].count()
    members = transform.standardise_members(src["members"]).cache()
    n_members = members.count()
    n_unknown_type = members.filter(F.col("membership_type") == config.UNKNOWN_TYPE).count()
    log.info("members: %d rows in, %d after keeping latest version", members_in, n_members)
    if n_unknown_type:
        log.warning("members: %d with missing membership_type -> '%s'", n_unknown_type, config.UNKNOWN_TYPE)

    # --- visits ------------------------------------------------------------
    visits_in = src["visits"].count()
    deduped = src["visits"].dropDuplicates()
    n_dupes = visits_in - deduped.count()
    log.info("visits: %d rows in, %d exact duplicates removed", visits_in, n_dupes)

    visits = transform.standardise_visits(deduped, src["centres"])
    valid, quarantine = validate.split_valid(visits, members)
    valid, quarantine = valid.cache(), quarantine.cache()

    # --- model -------------------------------------------------------------
    tables = {
        "fact_visit": model.build_fact_visit(valid),
        "dim_member": model.build_dim_member(members),
        "dim_centre": model.build_dim_centre(src["centres"]),
        "dim_date": model.build_dim_date(spark),
        "quarantine_visits": quarantine,
    }
    n_fact = tables["fact_visit"].count()
    n_quarantine = quarantine.count()

    for row in quarantine.groupBy("reject_reason").count().orderBy(F.desc("count")).collect():
        log.warning("quarantine: %-22s %6d", row["reject_reason"], row["count"])

    # --- checks before writing ---------------------------------------------
    if visits_in != n_dupes + n_fact + n_quarantine:
        raise ReconciliationError(
            f"{visits_in} in != {n_dupes} dupes + {n_fact} fact + {n_quarantine} quarantined")
    log.info("reconciliation OK: %d = %d duplicates + %d fact + %d quarantined",
             visits_in, n_dupes, n_fact, n_quarantine)

    fact = tables["fact_visit"]
    if fact.select("visit_id").distinct().count() != n_fact:
        raise ReconciliationError("fact_visit grain broken: visit_id not unique")
    orphan_dates = fact.join(tables["dim_date"], "date_key", "left_anti").count()
    if orphan_dates:
        raise ReconciliationError(f"{orphan_dates} fact rows have no dim_date row")

    io.write_tables(tables, out_dir)
    log.info("wrote %d tables to %s", len(tables), out_dir)

    counts = {"visits_in": visits_in, "duplicates": n_dupes, "fact": n_fact,
              "quarantine": n_quarantine, "members": n_members}
    return counts, tables


def summary(t: dict) -> None:
    """The business question: monthly visits by local authority and membership type.

    Analysts would query the written star schema (Hive on CDP, BigQuery on GCP);
    here we use the in-memory tables to keep the local run simple.
    """
    report = (
        t["fact_visit"]
        .join(t["dim_date"], "date_key")
        .join(t["dim_centre"], "centre_code")
        .join(t["dim_member"], "member_id")
        .groupBy("local_authority", "year_month")
        .pivot("membership_type", ["Standard", "Concession", "Junior", "Unknown"])
        .count()
        .na.fill(0)
        .orderBy("local_authority", "year_month")
    )
    report.show(truncate=False)


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--data-dir", type=Path, default=config.DATA_DIR)
    p.add_argument("--out-dir", type=Path, default=config.OUT_DIR)
    p.add_argument("--debug", action="store_true")
    args = p.parse_args(argv)

    logging.basicConfig(level=logging.DEBUG if args.debug else logging.INFO,
                        format="%(asctime)s %(levelname)-7s %(name)s: %(message)s")
    logging.getLogger("py4j").setLevel(logging.WARNING)

    spark = (SparkSession.builder.master("local[2]").appName("leisure_pipeline")
             .config("spark.sql.shuffle.partitions", "4")
             .config("spark.sql.session.timeZone", "UTC")
             .config("spark.ui.showConsoleProgress", "false")
             .getOrCreate())
    spark.sparkContext.setLogLevel("ERROR")
    try:
        _, tables = run(spark, args.data_dir, args.out_dir)
        summary(tables)
    except ReconciliationError:
        log.exception("checks failed: nothing written")
        return 1
    finally:
        spark.stop()
    return 0


if __name__ == "__main__":
    sys.exit(main())
