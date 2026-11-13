"""Generate the synthetic library dataset for session 04.

Tables: branches, branch_opening_hours, members, books, loans (CSV files in this folder).
The traps are deliberate:
- some members have never borrowed anything (LEFT JOIN / anti-join)
- some loans reference books missing from the catalogue (orphans, lost rows on INNER JOIN)
- branch_opening_hours has 7 rows per branch (fan-out when joined carelessly)
- return_date is NULL for books still on loan

Run:  python make_data.py
"""

import csv
import random
from datetime import date, timedelta
from pathlib import Path

random.seed(4)
HERE = Path(__file__).parent

ADJECTIVES = ["Silent", "Hidden", "Last", "Northern", "Broken", "Golden", "Distant", "Little",
              "Winter", "Lost"]
NOUNS = ["River", "Garden", "Station", "Archive", "Harbour", "Orchard", "Lighthouse", "Census",
         "Bridge", "Map"]
GENRES = ["Fiction", "Crime", "History", "Science", "Children", "Biography"]
DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


def write(name: str, rows: list[dict]) -> None:
    with (HERE / f"{name}.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"{name}: {len(rows)} rows")


def main() -> None:
    branches = [
        {"branch_id": 1, "branch_name": "Central", "region": "Wales"},
        {"branch_id": 2, "branch_name": "Riverside", "region": "Wales"},
        {"branch_id": 3, "branch_name": "Hilltop", "region": "South West"},
        {"branch_id": 4, "branch_name": "Old Town", "region": "South West"},
        {"branch_id": 5, "branch_name": "Harbourside", "region": "South East"},
    ]
    hours = [
        {"branch_id": b["branch_id"], "day_of_week": d,
         "opens": "10:00" if d == "Sun" else "09:00", "closes": "16:00" if d in ("Sat", "Sun") else "19:00"}
        for b in branches for d in DAYS
    ]

    titles = sorted({f"The {a} {n}" for a in ADJECTIVES for n in NOUNS})
    books = [{"book_id": i, "title": t, "genre": random.choice(GENRES)}
             for i, t in enumerate(random.sample(titles, 80), start=1)]

    members = [{"member_id": i,
                "home_branch_id": random.randint(1, 5),
                "joined_date": (date(2023, 1, 1) + timedelta(days=random.randint(0, 900))).isoformat(),
                "age_band": random.choice(["0-15", "16-24", "25-44", "45-64", "65+"])}
               for i in range(1, 201)]

    active = random.sample(members, 170)   # 30 members never borrow
    popular = [b["book_id"] for b in books[:15]]
    loans = []
    for loan_id in range(1, 1501):
        m = random.choice(active)
        branch = m["home_branch_id"] if random.random() < 0.8 else random.randint(1, 5)
        book_id = random.choice(popular) if random.random() < 0.3 else random.randint(1, 80)
        if random.random() < 0.015:
            book_id = random.randint(900, 999)            # orphan: not in catalogue
        loan_date = date(2026, 1, 1) + timedelta(days=random.randint(0, 180))
        returned = loan_date + timedelta(days=random.randint(3, 40))
        loans.append({
            "loan_id": loan_id,
            "member_id": m["member_id"],
            "book_id": book_id,
            "branch_id": branch,
            "loan_date": loan_date.isoformat(),
            "return_date": "" if returned > date(2026, 7, 1) else returned.isoformat(),
        })

    write("branches", branches)
    write("branch_opening_hours", hours)
    write("books", books)
    write("members", members)
    write("loans", loans)


if __name__ == "__main__":
    main()
