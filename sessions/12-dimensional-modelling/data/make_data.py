"""Generate a synthetic bus ticketing system (operational, 3NF-ish) for session 12.

operators.csv       operator_id, operator_name
stops.csv           stop_id, stop_name, area, fare_zone
route_operator.csv  route_id, route_name, operator_id, valid_from, valid_to   (route 7 changes operator!)
fare_types.csv      fare_type_code, fare_type_name, is_concession
tickets.csv         ticket_id, sold_at, route_id, boarding_stop_id, fare_type_code, price_gbp, payment_method

Run:  python make_data.py
"""

import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

random.seed(12)
HERE = Path(__file__).parent


def write(name: str, rows: list[dict]) -> None:
    with (HERE / f"{name}.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"{name}: {len(rows)} rows")


def main() -> None:
    operators = [{"operator_id": "OP1", "operator_name": "Valley Buses"},
                 {"operator_id": "OP2", "operator_name": "Coastline Travel"},
                 {"operator_id": "OP3", "operator_name": "CityLink"}]
    areas = ["City Centre", "North", "East", "Coast"]
    stops = [{"stop_id": f"ST{i:03d}", "stop_name": f"Stop {i}", "area": areas[i % 4],
              "fare_zone": 1 if i % 4 == 0 else 2} for i in range(1, 41)]
    routes = []
    for r in range(1, 11):
        op = ["OP1", "OP2", "OP3"][r % 3]
        if r == 7:
            routes.append({"route_id": 7, "route_name": "Route 7", "operator_id": "OP1",
                           "valid_from": "2020-01-01", "valid_to": "2026-03-31"})
            routes.append({"route_id": 7, "route_name": "Route 7", "operator_id": "OP2",
                           "valid_from": "2026-04-01", "valid_to": ""})
        else:
            routes.append({"route_id": r, "route_name": f"Route {r}", "operator_id": op,
                           "valid_from": "2020-01-01", "valid_to": ""})
    fare_types = [{"fare_type_code": "ADS", "fare_type_name": "Adult single", "is_concession": False},
                  {"fare_type_code": "ADR", "fare_type_name": "Adult return", "is_concession": False},
                  {"fare_type_code": "CHS", "fare_type_name": "Child single", "is_concession": True},
                  {"fare_type_code": "OAP", "fare_type_name": "Older person pass", "is_concession": True},
                  {"fare_type_code": "DAY", "fare_type_name": "Day ticket", "is_concession": False}]
    prices = {"ADS": 2.0, "ADR": 3.6, "CHS": 1.2, "OAP": 0.0, "DAY": 5.5}

    tickets = []
    start = datetime(2026, 1, 1, 6, 0)
    for tid in range(1, 20_001):
        route = random.choices(range(1, 11), [3, 2, 2, 1, 1, 2, 4, 1, 1, 2])[0]
        fare = random.choices(list(prices), [40, 15, 12, 20, 13])[0]
        tickets.append({
            "ticket_id": tid,
            "sold_at": (start + timedelta(minutes=random.randint(0, 181 * 24 * 60 - 6 * 60 - 1))).isoformat(sep=" "),
            "route_id": route,
            "boarding_stop_id": f"ST{random.randint(1, 40):03d}",
            "fare_type_code": fare,
            "price_gbp": prices[fare],
            "payment_method": "pass" if fare == "OAP" else random.choice(["cash", "contactless", "app"]),
        })

    write("operators", operators)
    write("stops", stops)
    write("route_operator", routes)
    write("fare_types", fare_types)
    write("tickets", tickets)


if __name__ == "__main__":
    main()
