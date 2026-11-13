"""Generate synthetic air-quality data for session 09.

readings.csv : daily PM2.5 readings for 10 stations, 15 Feb – 15 Apr 2026.
               Values below the detection limit are recorded as "<5".
stations.csv : station lookup. Station S04 was renamed on 1 March 2026, so it has two rows
               (valid_from / valid_to): the current one has an empty valid_to.

Run:  python make_data.py
"""

import csv
import random
from datetime import date, timedelta
from pathlib import Path

random.seed(9)
HERE = Path(__file__).parent

NAMES = ["Castle Street", "Docks Road", "Park Lane", "Old Market", "Hospital Gate",
         "Bridge End", "Station Square", "Hill Top", "Riverside", "Ring Road"]


def main() -> None:
    stations = []
    for i, name in enumerate(NAMES, start=1):
        sid = f"S{i:02d}"
        if sid == "S04":
            stations.append({"Station ID": sid, "Station Name": "Corn Market", "Area": "Centre",
                             "valid_from": "2020-01-01", "valid_to": "2026-02-28"})
            stations.append({"Station ID": sid, "Station Name": name, "Area": "Centre",
                             "valid_from": "2026-03-01", "valid_to": ""})
        else:
            stations.append({"Station ID": sid, "Station Name": name,
                             "Area": random.choice(["Centre", "North", "South"]),
                             "valid_from": "2020-01-01", "valid_to": ""})

    readings = []
    day = date(2026, 2, 15)
    while day <= date(2026, 4, 15):
        for i in range(1, 11):
            base = 6 + i * 1.5
            value = round(random.gauss(base, 4), 1)
            readings.append({"Station ID": f"S{i:02d}", "Reading Date": day.isoformat(),
                             "PM25": "<5" if value < 5 else value})
        day += timedelta(days=1)

    for name, rows in [("stations", stations), ("readings", readings)]:
        with (HERE / f"{name}.csv").open("w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
        print(f"{name}: {len(rows)} rows")


if __name__ == "__main__":
    main()
