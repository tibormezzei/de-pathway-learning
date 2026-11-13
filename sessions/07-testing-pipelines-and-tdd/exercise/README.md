# Exercise: ping-pong TDD on a PySpark cleaning module

**Time:** 20 minutes · **Work:** in pairs, swapping roles after every test

An energy supplier sends daily smart-meter readings. Build `meter_cleaning.py` **test-first**.

## The ping-pong loop

```
 A: write ONE small failing test  →  RED
 B: write the SIMPLEST code that passes it  →  GREEN
 A + B: tidy up the code and tests, which must stay green  →  REFACTOR
 swap roles, repeat
```

Rules: **no production code without a failing test first**, and **one test at a time**.

```bash
cd sessions/07-testing-pipelines-and-tdd
python -m pytest -v exercise
```

The first test is already written and fails. Start by making it pass.

## Requirements

| # | Function | Requirement |
|---|---|---|
| R1 | `parse_reading` | Convert `reading_kwh` text to a **double**. Allow thousands separators (`"1,234.5"`) and surrounding whitespace. Anything that isn't a number becomes **null**. |
| R2 | `flag_invalid` | Add a boolean `is_valid`: **True** only if `reading_kwh` is not null **and** ≥ 0. |
| R3 | `latest_per_meter_day` | Suppliers resubmit corrections. Keep only the reading with the **latest `submitted_at`** for each `(meter_id, reading_date)`. Leave no helper columns behind. |
| R4 | `clean_readings` | Run parse → latest → flag. **If the latest submission is junk, keep it (flagged invalid). Don't fall back to an older reading.** |

## Tips
- Build tiny DataFrames inline: `spark.createDataFrame([("M1", "12.5")], "meter_id string, reading_kwh string")`
- Compare whole DataFrames with `assertDataFrameEqual(actual, expected)`. It ignores row order.
- The `spark` fixture in `conftest.py` starts Spark **once** for the whole run.
- Useful functions: `F.regexp_replace`, `F.trim`, `F.when`, `.rlike(...)`, `.cast("double")`, `F.coalesce`, `F.row_number().over(Window...)`

## Discuss afterwards
- Did writing the test first change *how* you wrote the function?
- R4 is a **business rule**. Where should it be recorded, besides the test?
