# Session 04: SQL for data engineers

| | |
|---|---|
| Module | 1: Foundations of building |
| Wiki skill(s) | Data analysis & synthesis (Working): SQL |
| HEO target level | Working |
| Duration | 60 min (~35 concept / ~20 exercise / ~5 Q&A) |
| Follow-up | **Exercise** (in session; Q5–Q7 can be finished afterwards) |
| Prerequisites | Session 02 (venv). Basic `SELECT … FROM … WHERE` helps; the slides recap it quickly |
| Dataset | Synthetic library service: `data/*.csv` (5 tables), regenerate with `data/make_data.py`. Query with `run_sql.py` (DuckDB) |

## Learning outcomes
By the end of the session, participants can:
1. Think in **sets**: describe what a query returns in terms of rows and grain.
2. Choose the right join and spot the two classic join bugs: **lost rows** and **fan-out**.
3. Aggregate with `GROUP BY` / `HAVING`, and handle `NULL`s correctly.
4. Structure longer queries with **CTEs**.
5. Use **window functions** (`ROW_NUMBER`, `RANK`, `LAG`, running totals) for "top N per group" and period-on-period questions.

## Concept outline
| Min | Section |
|---|---|
| 0–3 | Code review swap of session 03 homework (5 min, optional; take it from the exercise if needed) |
| 3–7 | Why SQL still matters for DEs; the logical order a query runs in |
| 7–10 | Grain: the most important question |
| 10–18 | Joins, plus lost rows and fan-out |
| 18–22 | Aggregation and NULLs |
| 22–25 | CTEs |
| 25–31 | Window functions |
| 31–35 | CDP today → GCP tomorrow + summary |
| 35–55 | Exercise |
| 55–60 | Go through Q3/Q4 together |

## Exercise
- **Task:** answer 7 business questions about a library service, including a broken query to debug.
- **Starting files:** `exercise/README.md`, `exercise/questions.sql`, `run_sql.py`
- **Done when:** Q1–Q4 answered and sanity-checked against total row counts.
- **Stretch:** Q5–Q7 (window functions, CTE + LAG).
- **Reference answers:** `solutions/answers.sql`, `solutions/README.md` (expected numbers + teaching points)

## Further learning (from the wiki)
- [Learning Hub: Foundations of SQL](https://learninghub.ons.gov.uk/course/view.php?id=1162), with [SQLite Online](https://sqliteonline.com) for practice
- [YouTube: SQL full course (3h)](https://www.youtube.com/watch?v=7S_tz1z_5bA)
- [SQL Noir](https://www.sqlnoir.com/) · [SQL Premier League](https://sqlpremierleague.com/): practice through puzzles
- [Cloud Skills Boost](https://www.cloudskillsboost.google/): BigQuery SQL labs (GCP preparation)

## Facilitator notes
- DuckDB is used because it runs locally with no setup and its SQL is close to both Hive/Impala and BigQuery. Mention dialect differences, but don't dwell on them.
- Q4 is the highlight. Let pairs struggle for a minute, then ask "what's one row in `branch_opening_hours`?"
- If the room is new to SQL, spend longer on slides 5–9 and treat Q5–Q7 as homework.
