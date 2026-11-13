# Reference solution: session 09

```bash
python solutions/air_quality_report.py           # INFO and above
python solutions/air_quality_report.py --debug   # plus DEBUG
```

Correct output: 10 stations, 31 days each. S01 Castle Street mean 7.7, … S10 Ring Road mean 20.5.

## The 4 bugs, in the order people usually meet them

| # | Symptom | Cause | Fix | Kind |
|---|---|---|---|---|
| 1 | `KeyError: 'reading_date'` | `load_readings` lower-cases headers but keeps the space: `"reading date"` | Snake-case column names consistently (one shared function) | Crash |
| 2 | `TypeError: agg function failed [how->mean,dtype->object]` | `"<5"` makes the whole `PM25` column **text** | Replace `"<5"` with 2.5 (agreed rule), then `to_numeric(errors="raise")` | Crash |
| 3 | Runs, but **30 days** per station | `> "2026-03-01"` excludes 1 March | `between(start, end)` (inclusive) | **Silent** |
| 4 | Runs, but **S04 appears twice** (Corn Market and Old Market) with the same numbers | `stations.csv` has a historical row for S04, so the join **fans out** | Join only current rows; `validate="many_to_one"`; check the row count | **Silent** |

After fixes 1 and 2, the output **looks plausible**. That's the trap. Only checking against expectations (31 days, 10 stations) shows bugs 3 and 4.

## Teaching points
- **Read tracebacks bottom-up**, then find the last frame in **our** code. The pandas internals above it are rarely where the problem is.
- **Check your hypothesis against the data**: `df.columns`, `df.dtypes` and `.unique()` find most bugs in seconds.
- **Silent bugs need expectations.** Write them down ("31 days", "10 stations") and turn them into checks in the code: `validate=`, row-count assertions, validation (session 08).
- **Severity:** bug 4 would have published a duplicated station in an official report. That's a reputational issue, not just a technical one. Bug 3 understates every monthly mean slightly. Both matter more than the crashes, which nobody could miss.
- **Logging vs print:** levels let you turn detail on and off without editing code. Timestamps and logger names help on shared platforms, and platform log tools collect them.
- **Never log personal data.** Log counts and IDs of *problems*, not records' contents.
