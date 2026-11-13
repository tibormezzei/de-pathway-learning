"""Generate synthetic sources for session 13 (data integration).

Source A: practice registry
  practices.csv                practice_code, practice_name
  practice_board_v1.csv        practice_code, board_code   (valid 2026-01 .. 2026-03)
  practice_board_v2.csv        practice_code, board_code   (valid from 2026-04; 3 practices move to HB05)
  boards.csv                   board_code, board_name
  practice_mergers.csv         old_code, new_code, effective_month

Source B: appointment system (different team, different conventions)
  appointments.csv             org_code (messy!), month (yyyy-mm), appointments

Run:  python make_data.py
"""

import csv
import random
from pathlib import Path

random.seed(13)
HERE = Path(__file__).parent
MONTHS = [f"2026-{m:02d}" for m in range(1, 7)]


def write(name: str, rows: list[dict]) -> None:
    with (HERE / f"{name}.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"{name}: {len(rows)} rows")


def messy(code: str) -> str:
    r = random.random()
    if r < 0.15:
        return code.lower()
    if r < 0.25:
        return f" {code} "
    if r < 0.32:
        return f"{code[0]}-{code[1:]}"
    return code


def main() -> None:
    codes = [f"W{i:05d}" for i in range(1, 31)]
    practices = [{"practice_code": c, "practice_name": f"Practice {c[-2:]}"} for c in codes]
    boards = [{"board_code": f"HB0{i}", "board_name": n} for i, n in
              enumerate(["North Hills UHB", "Bay UHB", "Valley UHB", "City UHB", "Coast UHB"], start=1)]
    v1 = [{"practice_code": c, "board_code": f"HB0{(i % 4) + 1}"} for i, c in enumerate(codes)]
    moved = {"W00003", "W00007", "W00011"}
    v2 = [{"practice_code": r["practice_code"],
           "board_code": "HB05" if r["practice_code"] in moved else r["board_code"]} for r in v1]
    mergers = [{"old_code": "W00029", "new_code": "W00010", "effective_month": "2026-03"},
               {"old_code": "W00030", "new_code": "W00010", "effective_month": "2026-03"}]

    appointments = []
    for month in MONTHS:
        for c in codes:
            reported = c
            if c in ("W00029", "W00030") and month >= "2026-03":
                if random.random() < 0.5:
                    continue                      # some months reported under the new code already
            appointments.append({"org_code": messy(reported), "month": month,
                                 "appointments": random.randint(800, 4000)})
    appointments.append({"org_code": "W0001O", "month": "2026-02", "appointments": 1234})   # letter O
    appointments.append({"org_code": "X99999", "month": "2026-05", "appointments": 999})    # unknown
    random.shuffle(appointments)

    write("practices", practices)
    write("boards", boards)
    write("practice_board_v1", v1)
    write("practice_board_v2", v2)
    write("practice_mergers", mergers)
    write("appointments", appointments)


if __name__ == "__main__":
    main()
