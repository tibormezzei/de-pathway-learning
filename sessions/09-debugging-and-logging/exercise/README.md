# Exercise: fix the report, then make it observable

**Time:** 20 minutes · **Work:** in pairs (one drives, one navigates; swap after each bug)

The environmental monitoring team's March air-quality report is broken, and it's due today.

```bash
cd sessions/09-debugging-and-logging
python exercise/air_quality_report.py
```

## What correct output looks like

The team lead says the report should have:
- **one row per station: 10 stations**
- **31 days** for every station (March has 31 days and every station reported daily)
- readings recorded as `"<5"` (below detection) counted as **2.5**, as agreed

## Part 1: fix it (about 12 min)

There are **4 bugs**. Two crash the script and two **don't**.

For each bug:
1. **Read** the error (if there is one). Which line of *our* code? What value was it working on?
2. **Form a hypothesis**, then **check it** by inspecting the data: `print(df.columns)`, `df.dtypes`, `df["col"].unique()`, or `breakpoint()`.
3. **Fix it**, rerun, and repeat.

When it stops crashing, you're **not** done. Compare the output with "what correct looks like".

## Part 2: make it observable (about 8 min)

Replace the `print("loaded")` debugging with **logging**:
- `logger = logging.getLogger(__name__)` and `logging.basicConfig(level=logging.INFO, ...)` in `main()`
- **INFO**: row counts after loading, filtering and joining
- **WARNING**: how many `"<5"` values were replaced
- Optional **DEBUG**: the first few rows after filtering, shown only with a `--debug` flag

Then add one **safeguard** so the silent join bug could never happen again unnoticed. Hint: `merge(..., validate="many_to_one")`, or compare row counts before and after.

## Discuss
- Which bugs were hardest to find, the crashing ones or the silent ones? Why?
- How serious would it have been if bug 4 reached publication? Who would be affected?
