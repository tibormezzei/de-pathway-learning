# Capstone (optional): leisure centre visits pipeline

**Effort:** about 8–12 hours over 2–4 weeks · **Work:** on your own or in pairs · **Ends with:** a 5-minute presentation

This brings together all four modules: maintainable Python and PySpark, testing, data quality, debugging and logging, profiling, dimensional modelling, integration, metadata, and communicating.

## The scenario

A council's leisure service wants to know **how its centres are used**. Two systems hold the data, and they were never designed to talk to each other:

| File | System | What it holds |
|---|---|---|
| `data/centres.csv` | Reference list | 8 leisure centres, their codes and local authority |
| `data/members.csv` | Membership CRM | One row per member *version*: birth year, home district, home centre, membership type |
| `data/visits.csv` | Turnstile system | One row per swipe: card number, centre **name**, entry/exit time, activity (Jan–Mar 2026) |

Generate the data first:

```bash
python capstone/data/make_data.py
```

The service manager's question:

> "For each local authority and month, how many visits were there by Standard, Concession and Junior members? I'd also like to look at it by activity, age group and time of day later, so build it so we can."

## Requirements

| # | Requirement |
|---|---|
| R1 | Combine the visits with the member and centre data |
| R2 | Each visit counted **once** |
| R3 | Records that can't be trusted are **not** in the figures, but are **kept and explained** |
| R4 | Every input row is accounted for: in = loaded + rejected (+ any removed duplicates) |
| R5 | Re-running the pipeline gives the same result |
| R6 | The output can answer the manager's question **and** the "later" questions without rebuilding |
| R7 | Someone else can understand and run it |

We deliberately aren't telling you what's wrong with the data. **Profile it first** (session 10).

## Deliverables

1. **Profiling notes** (short): what you found in each source and what you decided to do about it.
2. **Pipeline code**, in Python and PySpark (pandas is acceptable if you justify it), structured as a small package with config separate from logic.
3. **Validation**, with a quarantine output and a reason per rejected row.
4. **Logging** of row counts at each step, warnings for data issues, and a reconciliation check that **fails the run** if it doesn't balance.
5. **Tests**: unit tests for each cleaning and validation rule, plus at least one end-to-end test.
6. **A dimensional output model**: a fact table with a stated grain, and dimensions. Include a diagram.
7. **A data dictionary** for your output tables (column, type, description, source, rule).
8. **A README**: how to run it, design decisions and trade-offs, limitations.
9. **A 5-minute presentation** to a mixed audience (session 17): the answer first, then what you found, how you know it's right, and next steps. Include one slide on what would change on GCP.

## Suggested plan

| Week | Focus | Sessions to revisit |
|---|---|---|
| 1 | Profile the three files; write down the problems and decisions; sketch the star schema | 10, 11, 12 |
| 2 | Build standardisation and validation **test-first**; get reconciliation balancing | 06, 07, 08, 13 |
| 3 | Build the model, logging, data dictionary and README | 09, 12, 14 |
| 4 | Presentation; tidy up; peer review of someone else's repo | 02, 16, 17 |

## Rules
- Work in a Git repo with small, meaningful commits (session 02).
- Don't edit the source CSVs by hand. Every fix must be in code.
- Use `capstone/output/` for outputs (it's gitignored).
- **Windows:** Spark's Parquet writer needs `hadoop.dll`. Either install it alongside `winutils.exe`, or write small outputs through pandas and pyarrow (see how `solution/leisure_pipeline/io.py` does it).

## Assessment
See `rubric.md`. A reference solution is in `solution/`. **Don't open it until you've presented.**
