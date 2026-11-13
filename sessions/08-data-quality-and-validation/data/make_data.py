"""Generate synthetic business survey returns for session 08, with planted data quality problems.

Run:  python make_data.py      -> returns.csv (and prints the answer key)
"""

import csv
import random
from pathlib import Path

random.seed(8)
HERE = Path(__file__).parent

REGIONS = ["Wales", "Scotland", "Northern Ireland", "North East", "North West", "London",
           "South East", "South West"]
SIC_CODES = ["01110", "10710", "41201", "47110", "56101", "62012", "68100", "86101"]
PERIODS = ["202601", "202602", "202603", "202604", "202605", "202606"]


def good_row(ru_ref: str, period: str) -> dict:
    employees = random.choice([0, 1, 3, 8, 15, 40, 120, 600])
    turnover = round(employees * random.uniform(40_000, 120_000) + random.uniform(5_000, 60_000), 2)
    return {"ru_ref": ru_ref, "period": period, "sic_code": random.choice(SIC_CODES),
            "region": random.choice(REGIONS), "employees": employees, "turnover": turnover}


def main() -> None:
    refs = [f"4990{random.randint(1000000, 9999999)}" for _ in range(80)]
    rows = [good_row(r, p) for r in refs for p in random.sample(PERIODS, 5)]
    random.shuffle(rows)

    key = {}
    def plant(name, n, fn):
        targets = random.sample(range(len(rows)), n)
        for i in targets:
            fn(rows[i])
        key[name] = n

    plant("ru_ref not 11 digits", 4, lambda r: r.update(ru_ref=r["ru_ref"][:-1]))
    plant("period invalid", 3, lambda r: r.update(period=random.choice(["202613", "2026-03", "202612"])))
    plant("sic_code lost leading zero", 5, lambda r: r.update(sic_code="1110"))
    plant("region misspelt", 4, lambda r: r.update(region=random.choice(["Londn", "wales", "Scotland "])))
    plant("employees missing", 6, lambda r: r.update(employees=""))
    plant("turnover negative", 3, lambda r: r.update(turnover=-abs(float(r["turnover"]))))
    plant("zero employees but turnover > 1m (suspicious)", 3,
          lambda r: r.update(employees=0, turnover=round(random.uniform(1.2e6, 5e6), 2)))

    dupes = [dict(r) for r in random.sample(rows, 4)]
    rows += dupes
    key["duplicate (ru_ref, period)"] = len(dupes)
    random.shuffle(rows)

    with (HERE / "returns.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"returns: {len(rows)} rows. Planted problems (facilitator key):")
    for k, v in key.items():
        print(f"  {v:>2}  {k}")


if __name__ == "__main__":
    main()
