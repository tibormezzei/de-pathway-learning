"""Generate the synthetic survey_responses.csv used in session 03.

Fully synthetic, with no real data. The messiness is deliberate.
Run:  python make_data.py
"""

import csv
import random
from datetime import date, timedelta
from pathlib import Path

random.seed(42)

REGION_SPELLINGS = {
    "North": ["North", "north", "NORTH", " North "],
    "South": ["South", "south", "SOUTH ", "Sth"],
    "East": ["East", "east", " EAST"],
    "West": ["West", "west", "WEST", "Wst"],
}
OUTCOMES = ["complete"] * 5 + ["partial"] * 2 + ["refusal"] * 2 + ["noncontact"] * 3


def messy_date(d: date) -> str:
    style = random.random()
    if style < 0.6:
        return d.isoformat()                  # 2026-01-05
    if style < 0.9:
        return d.strftime("%d/%m/%Y")         # 05/01/2026
    return d.strftime("%d-%b-%Y")             # 05-Jan-2026


def messy_age() -> str:
    r = random.random()
    if r < 0.04:
        return ""
    if r < 0.07:
        return str(random.choice([-1, 0, 999, 150, 7]))
    return str(random.randint(16, 95))


def main() -> None:
    rows = []
    start = date(2026, 1, 1)
    for i in range(1, 601):
        region = random.choice(list(REGION_SPELLINGS))
        rows.append({
            "case_id": f"C{i:05d}",
            "interviewer_id": f"INT{random.randint(1, 12):03d}",
            "region": random.choice(REGION_SPELLINGS[region]),
            "interview_date": messy_date(start + timedelta(days=random.randint(0, 89))),
            "age": messy_age(),
            "outcome": random.choice(OUTCOMES),
        })
    # duplicate submissions: same case sent twice
    rows += [dict(r) for r in random.sample(rows, 25)]
    random.shuffle(rows)

    out = Path(__file__).parent / "survey_responses.csv"
    with out.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} rows to {out}")


if __name__ == "__main__":
    main()
