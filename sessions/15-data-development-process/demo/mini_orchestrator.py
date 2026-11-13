"""A toy orchestrator showing the ideas behind Airflow / Cloud Composer, with no installs needed.

    python demo/mini_orchestrator.py                 # run for one date
    python demo/mini_orchestrator.py --backfill      # run for a range of dates
    python demo/mini_orchestrator.py --rerun         # run the same date twice: idempotency

Concepts: tasks, dependencies (a DAG), run date as a parameter, retries, idempotent outputs,
and backfills. Real orchestrators add scheduling, a UI, alerting and distributed workers.
"""

import argparse
import json
import random
import shutil
import tempfile
import time
from datetime import date, timedelta
from graphlib import TopologicalSorter
from pathlib import Path

OUT = Path(tempfile.gettempdir()) / "mini_orchestrator_demo"
random.seed(15)


# --- Tasks: each takes the run date and writes ONE output for that date (idempotent) ---

def extract(run_date: date) -> None:
    if random.random() < 0.3:                       # a flaky source, like real life
        raise ConnectionError("source API timed out")
    source = random.Random(run_date.toordinal())    # same date -> same source data
    rows = [{"school": f"S{i}", "present": source.randint(150, 300), "on_roll": 300} for i in range(5)]
    if run_date == date(2026, 3, 5):
        rows[2]["present"] = 412                     # a bad record arrives on 5 March
    write(run_date, "raw", rows)


def validate(run_date: date) -> None:
    rows = read(run_date, "raw")
    bad = [r for r in rows if not 0 <= r["present"] <= r["on_roll"]]
    if bad:
        raise ValueError(f"{len(bad)} invalid rows")   # a data problem: retrying won't help
    write(run_date, "validated", rows)


def transform(run_date: date) -> None:
    rows = read(run_date, "validated")
    rate = sum(r["present"] for r in rows) / sum(r["on_roll"] for r in rows)
    write(run_date, "attendance_rate", [{"date": run_date.isoformat(), "rate": round(rate, 3)}])


def publish(run_date: date) -> None:
    print(f"      published {read(run_date, 'attendance_rate')[0]}")


# The DAG: task -> the tasks it depends on
DAG = {"extract": set(), "validate": {"extract"}, "transform": {"validate"}, "publish": {"transform"}}
TASKS = {"extract": extract, "validate": validate, "transform": transform, "publish": publish}
RETRIES = {"extract": 3}                            # retry only where failures are transient


# --- Storage: one file per (dataset, date), so overwriting is safe ----------------------------

def path(run_date: date, dataset: str) -> Path:
    return OUT / dataset / f"date={run_date.isoformat()}.json"


def write(run_date: date, dataset: str, rows: list[dict]) -> None:
    p = path(run_date, dataset)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(rows))                  # overwrite, never append: idempotent


def read(run_date: date, dataset: str) -> list[dict]:
    return json.loads(path(run_date, dataset).read_text())


# --- The orchestrator ---------------------------------------------------------------

def run_task(name: str, run_date: date) -> None:
    attempts = RETRIES.get(name, 0) + 1
    for attempt in range(1, attempts + 1):
        try:
            TASKS[name](run_date)
            print(f"   OK   {name}" + (f" (attempt {attempt})" if attempt > 1 else ""))
            return
        except ConnectionError as err:
            print(f"   FAIL {name} attempt {attempt}/{attempts}: {err}")
            time.sleep(0.2 * attempt)               # back off a little more each time
    raise RuntimeError(f"{name} failed after {attempts} attempts")


def run_dag(run_date: date) -> bool:
    print(f"Run for {run_date}:")
    for name in TopologicalSorter(DAG).static_order():   # dependency order
        try:
            run_task(name, run_date)
        except Exception as err:                          # stop downstream tasks; alert in real life
            print(f"   STOP {name} FAILED: {err}. Downstream tasks skipped.")
            return False
    return True


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--backfill", action="store_true")
    parser.add_argument("--rerun", action="store_true")
    args = parser.parse_args()
    shutil.rmtree(OUT, ignore_errors=True)

    if args.backfill:
        start = date(2026, 3, 2)
        results = {start + timedelta(days=d): run_dag(start + timedelta(days=d)) for d in range(5)}
        print("\nBackfill summary:", {d.isoformat(): "ok" if ok else "FAILED" for d, ok in results.items()})
    elif args.rerun:
        d = date(2026, 3, 2)
        run_dag(d)
        run_dag(d)
        files = sorted(p.relative_to(OUT).as_posix() for p in OUT.rglob("*.json"))
        print(f"\nFiles after running the same date twice ({len(files)}, no duplicates):", files)
    else:
        run_dag(date(2026, 3, 2))


if __name__ == "__main__":
    main()
