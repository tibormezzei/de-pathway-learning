"""Generate the capstone data: leisure centre memberships + turnstile visits.

Two sources from two different systems that don't quite agree:
  centres.csv   reference list of leisure centres (clean)
  members.csv   membership CRM export (has duplicates and messy codes)
  visits.csv    turnstile system export, Jan-Mar 2026 (different ID format,
                centre *names* not codes, plus planted quality problems)

Run:  python capstone/data/make_data.py
"""
from __future__ import annotations

import csv
import random
from datetime import date, datetime, timedelta
from pathlib import Path

OUT = Path(__file__).parent
rng = random.Random(2026)

CENTRES = [
    ("LC01", "Riverside Leisure Centre", "Northshire", "2009-05-01"),
    ("LC02", "Hillcrest Pool", "Northshire", "1998-09-14"),
    ("LC03", "Market Street Gym", "Northshire", "2015-01-10"),
    ("LC04", "Parkside Sports Hub", "Eastvale", "2012-03-22"),
    ("LC05", "Eastvale Aquatics", "Eastvale", "2018-07-01"),
    ("LC06", "Westbrook Leisure", "Westbrook", "2004-11-30"),
    ("LC07", "Canal Side Fitness", "Westbrook", "2020-02-17"),
    ("LC08", "Old Mill Sports Centre", "Westbrook", "1991-06-05"),
]
CENTRE_WEIGHTS = [18, 10, 9, 14, 8, 15, 12, 6]
MEMBERSHIP_TYPES = [("Standard", 60), ("Concession", 25), ("Junior", 15)]
DISTRICTS = ["NS1", "NS2", "NS3", "NS4", "EV1", "EV2", "EV3", "WB1", "WB2", "WB3"]
ACTIVITIES = {"Swim": 35, "Gym": 45, "Class": 20}

N_MEMBERS = 1500
N_VISITS = 30000
START = datetime(2026, 1, 1)
DAYS = 90  # 1 Jan - 31 Mar 2026


def weighted(options):
    names, weights = zip(*options)
    return rng.choices(names, weights=weights, k=1)[0]


def write(name, header, rows):
    with open(OUT / name, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)
    print(f"wrote {name}: {len(rows):,} rows")


def main():
    write("centres.csv", ["centre_code", "centre_name", "local_authority", "opened_date"], CENTRES)

    # ---- members (CRM) ----------------------------------------------------
    members = []
    for i in range(1, N_MEMBERS + 1):
        mtype = weighted(MEMBERSHIP_TYPES)
        if mtype == "Junior":
            birth_year = rng.randint(2009, 2018)
        elif mtype == "Concession":
            birth_year = rng.choice([rng.randint(1940, 1961), rng.randint(2000, 2008)])
        else:
            birth_year = rng.randint(1962, 2007)
        centre = rng.choices([c[0] for c in CENTRES], weights=CENTRE_WEIGHTS, k=1)[0]
        joined = date(2015, 1, 1) + timedelta(days=rng.randint(0, 3990))  # up to Dec 2025
        updated = datetime.combine(joined, datetime.min.time()) + timedelta(days=rng.randint(0, 60))
        code = centre
        r = rng.random()
        if r < 0.05:
            code = centre.lower()                    # planted: lowercase code
        elif r < 0.08:
            code = f" {centre} "                     # planted: padded code
        members.append([f"M{i:05d}", birth_year, rng.choice(DISTRICTS), code, mtype,
                        joined.isoformat(), updated.isoformat(sep=" ")])

    # planted: 40 members have an older + newer version (moved home centre / type)
    for m in rng.sample(members, 40):
        newer = list(m)
        newer[3] = rng.choice([c[0] for c in CENTRES])
        newer[6] = (datetime.fromisoformat(m[6]) + timedelta(days=rng.randint(30, 400))).isoformat(sep=" ")
        members.append(newer)
    # planted: 12 members with missing membership type
    for m in rng.sample(members[:N_MEMBERS], 12):
        m[4] = ""
    rng.shuffle(members)
    write("members.csv", ["member_id", "birth_year", "home_district", "home_centre_code",
                          "membership_type", "joined_date", "updated_at"], members)

    # ---- visits (turnstile) -----------------------------------------------
    names = [c[1] for c in CENTRES]
    visits = []
    for v in range(1, N_VISITS + 1):
        member_no = rng.randint(1, N_MEMBERS)
        card = f"{member_no:07d}"
        # members mostly visit their home centre, but not always
        centre_name = rng.choices(names, weights=CENTRE_WEIGHTS, k=1)[0]
        entry = START + timedelta(minutes=rng.randint(6 * 60, DAYS * 24 * 60 - 3 * 60))
        entry = entry.replace(hour=max(6, min(entry.hour, 21)))
        activity = weighted(list(ACTIVITIES.items()))
        stay = {"Swim": (30, 90), "Gym": (25, 120), "Class": (45, 75)}[activity]
        exit_ = entry + timedelta(minutes=rng.randint(*stay))
        r = rng.random()
        if r < 0.04:
            centre_name = centre_name.upper()            # planted: inconsistent case
        elif r < 0.07:
            centre_name = centre_name + "  "             # planted: trailing spaces
        visits.append([f"V{v:06d}", card, centre_name, entry.isoformat(sep=" "),
                       exit_.isoformat(sep=" "), activity])

    # planted: 300 orphan cards (lost / temporary cards not in CRM)
    for v in rng.sample(visits, 300):
        v[1] = f"{rng.randint(N_MEMBERS + 1, N_MEMBERS + 400):07d}"
    # planted: 150 visits from the engineers' test card
    for v in rng.sample(visits, 150):
        v[1] = "9999999"
    # planted: 80 visits whose exit is before entry (clock reset)
    for v in rng.sample(visits, 80):
        entry = datetime.fromisoformat(v[3])
        v[4] = (entry - timedelta(minutes=rng.randint(5, 120))).isoformat(sep=" ")
    # planted: 60 visits with an unknown activity code
    for v in rng.sample(visits, 60):
        v[5] = "UNK"
    # planted: 250 exact duplicate rows (turnstile re-sent a batch)
    visits.extend([list(v) for v in rng.sample(visits, 250)])
    rng.shuffle(visits)
    write("visits.csv", ["visit_id", "card_number", "centre", "entry_ts", "exit_ts", "activity"], visits)


if __name__ == "__main__":
    main()
