"""Generate a synthetic food hygiene inspections extract for session 10.

Fully synthetic. Deliberately contains the kinds of quirks profiling should reveal.
Run:  python make_data.py      -> inspections.csv
"""

import csv
import random
from datetime import date, timedelta
from pathlib import Path

random.seed(10)
HERE = Path(__file__).parent

AUTHORITIES = ["Cardiff", "Newport", "Swansea", "Bristol", "Bath and North East Somerset"]
AUTH_VARIANTS = {"Newport": ["Newport", "Newport City Council", "NEWPORT"],
                 "Bath and North East Somerset": ["Bath and North East Somerset", "BANES"]}
TYPES = ["Restaurant/Cafe/Canteen", "Takeaway/sandwich shop", "Retailers - other",
         "Pub/bar/nightclub", "Mobile caterer", "School/college/university", "Hotel/B&B"]
PREFIX = {"Cardiff": "CF", "Newport": "NP", "Swansea": "SA", "Bristol": "BS",
          "Bath and North East Somerset": "BA"}
WORDS = ["Golden", "Corner", "Royal", "Happy", "Green", "Station", "Harbour", "Village", "Old", "New"]
NOUNS = ["Kitchen", "Cafe", "Bakery", "Diner", "Grill", "Deli", "Stores", "Bistro", "Inn", "Express"]


def postcode(auth: str) -> str:
    pc = f"{PREFIX[auth]}{random.randint(1, 30)} {random.randint(1, 9)}{random.choice('ABDEFGHJLNPQRSTUWXYZ')}{random.choice('ABDEFGHJLNPQRSTUWXYZ')}"
    r = random.random()
    if r < 0.10:
        return pc.replace(" ", "").lower()
    if r < 0.14:
        return ""
    return pc


def main() -> None:
    rows = []
    for est_id in range(100001, 101201):
        auth = random.choices(AUTHORITIES, [30, 15, 20, 25, 10])[0]
        btype = random.choices(TYPES, [30, 25, 15, 12, 6, 6, 6])[0]
        last = date(2021, 1, 1) + timedelta(days=random.randint(0, 1800))
        rating = random.choices(["5", "4", "3", "2", "1", "0", "Exempt", "AwaitingInspection"],
                                [50, 20, 10, 5, 3, 1, 6, 5])[0]
        inspected = rating not in ("Exempt", "AwaitingInspection")
        rows.append({
            "establishment_id": est_id,
            "business_name": f"{random.choice(WORDS)} {random.choice(NOUNS)}",
            "business_type": btype,
            "address_postcode": postcode(auth),
            "local_authority": random.choice(AUTH_VARIANTS.get(auth, [auth])),
            "rating_value": rating,
            "rating_date": last.isoformat() if inspected else random.choice(["", "1900-01-01"]),
            "hygiene_score": random.choice([0, 5, 10, 15, 20]) if inspected else "",
            "structural_score": random.choice([0, 5, 10, 15]) if inspected else "",
            "confidence_score": random.choice([0, 5, 10, 20]) if inspected else "",
            "scheme_type": "FHRS",
            "fax_number": "" if random.random() > 0.01 else f"01{random.randint(100000000, 999999999)}",
            "latitude": round(random.uniform(51.3, 51.7), 6) if random.random() > 0.08 else "",
            "longitude": round(random.uniform(-3.3, -2.3), 6) if random.random() > 0.08 else "",
        })
    # mis-keyed dates, a future date, and duplicated establishments re-sent with an updated name
    for r in random.sample(rows, 3):
        if r["rating_date"] not in ("", "1900-01-01"):
            r["rating_date"] = "2031-04-17"
    for r in random.sample(rows, 6):
        r["latitude"], r["longitude"] = 0.0, 0.0
    dupes = []
    for r in random.sample(rows, 12):
        d = dict(r)
        d["business_name"] = r["business_name"] + " Ltd"
        dupes.append(d)
    rows += dupes
    random.shuffle(rows)

    with (HERE / "inspections.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"inspections: {len(rows)} rows")


if __name__ == "__main__":
    main()
