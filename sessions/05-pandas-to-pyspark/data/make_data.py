"""Generate the synthetic city bike-hire dataset for session 05.

stations.csv : 20 docking stations
trips.csv    : 60,000 trips (a few data issues: zero/negative and extreme durations)

Run:  python make_data.py
"""

import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

random.seed(5)
HERE = Path(__file__).parent

AREAS = ["Docks", "Castle", "University", "Station", "Market", "Park", "Bay", "Hospital",
         "Stadium", "Museum"]


def main() -> None:
    stations = [{"station_id": i, "station_name": f"{AREAS[(i - 1) % 10]} {'North' if i <= 10 else 'South'}",
                 "capacity": random.choice([10, 15, 20, 25])} for i in range(1, 21)]

    weights = [random.uniform(0.3, 3.0) for _ in stations]
    start = datetime(2026, 4, 1)
    trips = []
    for trip_id in range(1, 60_001):
        member_type = "member" if random.random() < 0.65 else "casual"
        duration = round(random.lognormvariate(2.6 if member_type == "member" else 3.1, 0.6), 1)
        r = random.random()
        if r < 0.004:
            duration = random.choice([0.0, -3.0])          # bad records
        elif r < 0.008:
            duration = round(random.uniform(300, 3000), 1)  # bike not docked properly
        trips.append({
            "trip_id": trip_id,
            "start_station_id": random.choices(range(1, 21), weights)[0],
            "end_station_id": random.randint(1, 20),
            "start_time": (start + timedelta(minutes=random.randint(0, 60 * 24 * 30))).isoformat(sep=" "),
            "duration_min": duration,
            "member_type": member_type,
        })

    for name, rows in [("stations", stations), ("trips", trips)]:
        with (HERE / f"{name}.csv").open("w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
        print(f"{name}: {len(rows)} rows")


if __name__ == "__main__":
    main()
