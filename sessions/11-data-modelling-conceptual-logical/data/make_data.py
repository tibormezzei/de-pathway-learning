"""Generate the flat 'case visits' spreadsheet export for session 11.

One row per visit, with everything repeated on every row, which is typical of a spreadsheet
export. Fully synthetic. Run:  python make_data.py
"""

import csv
import random
from datetime import date, timedelta
from pathlib import Path

random.seed(11)
HERE = Path(__file__).parent

SURVEYS = [("LFS", "Labour Force Survey"), ("LCF", "Living Costs and Food Survey")]
REGIONS = [("W92", "Wales"), ("E12", "South West")]
INTERVIEWERS = [("I101", "A. Jones", "W92"), ("I102", "B. Patel", "W92"),
                ("I201", "C. Smith", "E12"), ("I202", "D. Evans", "E12")]
OUTCOMES = [("110", "Full interview"), ("210", "Partial interview"), ("310", "Refusal"),
            ("410", "No contact"), ("510", "Ineligible address")]
STREETS = ["High Street", "Church Road", "Mill Lane", "Station Road", "Park Avenue"]


def main() -> None:
    rows = []
    case_no = 0
    for survey_code, survey_name in SURVEYS:
        for period in ["2026-03", "2026-04"]:
            for _ in range(6):
                case_no += 1
                region_code, region_name = random.choice(REGIONS)
                iv = random.choice([i for i in INTERVIEWERS if i[2] == region_code])
                prefix = "CF" if region_code == "W92" else "BS"
                address = f"{random.randint(1, 120)} {random.choice(STREETS)}"
                pc = f"{prefix}{random.randint(1, 30)} {random.randint(1, 9)}AB"
                day = date.fromisoformat(f"{period}-01") + timedelta(days=random.randint(0, 10))
                n_visits = random.randint(1, 4)
                for visit_no in range(1, n_visits + 1):
                    last = visit_no == n_visits
                    outcome = random.choice(OUTCOMES[:3] + OUTCOMES[4:]) if last else OUTCOMES[3]
                    rows.append({
                        "case_id": f"C{case_no:04d}",
                        "survey_code": survey_code, "survey_name": survey_name,
                        "period": period,
                        "address_line": address, "postcode": pc,
                        "region_code": region_code, "region_name": region_name,
                        "interviewer_id": iv[0], "interviewer_name": iv[1],
                        "visit_no": visit_no,
                        "visit_date": (day + timedelta(days=3 * (visit_no - 1))).isoformat(),
                        "outcome_code": outcome[0], "outcome_description": outcome[1],
                    })

    with (HERE / "case_visits_flat.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"case_visits_flat: {len(rows)} rows, {case_no} cases")


if __name__ == "__main__":
    main()
