---
marp: true
theme: default
paginate: true
header: "DE Learning Sessions · 09"
footer: "Problem resolution: debugging and logging"
---

<!-- _class: lead -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Problem resolution
## debugging and logging

Session 09 · Module 2: Quality and reliability

---

## Today

1. When things break: severity and impact
2. Reading errors
3. A debugging method
4. Silent bugs
5. Logging
6. AI assistants, used responsibly
7. **Exercise:** fix the report, then make it observable

---

## First: how bad is it?

Before diving into code, ask:

| Question | Why |
|---|---|
| **Who is affected?** | Just you? The team? Published statistics? |
| **Has wrong data already gone out?** | Stopping the spread may matter more than the fix |
| **Is it getting worse?** | A failing nightly job vs a one-off |
| **Who needs to know?** | Your lead, the product owner, downstream users |

The wiki calls these **operational, tactical and strategic** problems. A crash at 10am is annoying, but a **wrong number published** is serious.

---

## Reading a Python traceback

```text
Traceback (most recent call last):
  File "air_quality_report.py", line 52, in main
    march = filter_month(readings, "2026-03-01", "2026-03-31")
  File "air_quality_report.py", line 32, in filter_month          ← last frame in OUR code
    return df[(df["reading_date"] > start) & ...]
  File ".../pandas/core/frame.py", line 4102, in __getitem__
  File ".../pandas/core/indexes/base.py", line 3812, in get_loc
    raise KeyError(key) from err
KeyError: 'reading_date'                                          ← start here
```

1. Read the **last line**: the error type and value.
2. Go up to the **last frame in your code**.
3. Ask: **what was the data at that point?**

---

## Reading a PySpark error

```text
py4j.protocol.Py4JJavaError: An error occurred while calling o54.collectToPython.
: org.apache.spark.SparkException: Job aborted due to stage failure: ...
    at org.apache.spark.scheduler.DAGScheduler ...        ← 80 lines of Java
    ...
Caused by: org.apache.spark.api.python.PythonException:
  File "/my_job.py", line 18, in parse_reading           ← THE USEFUL BIT
ValueError: could not convert string to float: 'n/a'
```

- Spark is **lazy**, so the error appears at the **action** (`collect`, `write`), not where the bug is.
- Search for **`Caused by:`** and **`PythonException`**, or for your own file names.
- `AnalysisException: cannot resolve 'colname'` means a **column name problem**, found at plan time.

---

## A debugging method

1. **Reproduce** it reliably, ideally on a **small** input.
2. **Read** the error properly (previous slides).
3. **Hypothesise**: "I think `pm25` is text because of the `<5` values."
4. **Inspect** to test the hypothesis: `df.dtypes`, `df.columns`, `df["x"].unique()`, `df.printSchema()`.
5. **Fix** one thing.
6. **Verify**: rerun and compare against **what correct looks like**.

Stuck for 30 minutes? **Change technique**: explain it to a rubber duck, ask a colleague to pair, take a screen break.

---

## Techniques

| Technique | When |
|---|---|
| **Print / inspect** | Quick look at shapes, columns, types, values |
| **`breakpoint()`** | Pause *inside* the code and explore interactively (`p df.dtypes`, `n`, `c`) |
| **Shrink the input** | Filter to one station or one day, so the problem becomes obvious |
| **Binary search** | Comment out half the steps. Which half breaks? (`git bisect` does this across commits) |
| **Rubber duck** | Explaining step by step exposes the wrong assumption |
| **Pair programming** | A fresh pair of eyes, and a navigator who sees what the driver misses |

---

## Silent bugs

The worst bugs **don't crash**:
- a filter that's off by one day
- a join that fans out (session 04)
- a type conversion that turns bad values into NaN

You can only catch them if you **know what correct looks like**:

```python
assert report["station_id"].is_unique, "one row per station"
assert (report["days"] == 31).all(), "every station should have 31 days in March"

joined = readings.merge(stations, on="station_id", validate="many_to_one")   # raises on fan-out
```

**Write expectations down, then turn them into checks** (session 08).

---

## Logging: why not `print`?

| `print` | `logging` |
|---|---|
| Always on, or deleted by hand | **Levels**: turn detail up or down without editing code |
| No timestamp, no source | Timestamp, level and module name automatically |
| Only goes to the console | Console, files, **platform log tools** |
| Mixed with real output | Kept apart from the program's results |

```python
import logging
logger = logging.getLogger(__name__)

logger.info("Filtered to March: %d rows", len(march))
logger.warning("%d readings below detection limit; using %.1f", n, 2.5)
```

---

## Levels and what to log

| Level | Use for | Example |
|---|---|---|
| `DEBUG` | Detail while developing | First 5 rows after the filter |
| `INFO` | Normal milestones | "Loaded 600 rows", "Wrote 10 rows to …" |
| `WARNING` | Unexpected but handled | "29 values below detection limit replaced" |
| `ERROR` | A step failed | "Join changed row count 310 → 341" |

```python
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(name)s: %(message)s")
```

**Log:** row counts at each stage, decisions taken, things you quarantined.
**Never log:** personal data, record contents, credentials.

---

## AI assistants, used responsibly

**Good uses**
- Explaining an unfamiliar error or a piece of code
- Suggesting hypotheses to test ("what could cause this TypeError?")
- Drafting tests and docstrings, **which you then check**

**Risks**
- Confident and wrong: invented functions, references and causes
- Code that runs but doesn't do what you meant

**Rules**
- Follow the **UKSA AI policy** and use approved tools only (e.g. GitHub Copilot, Microsoft Copilot).
- **Never paste sensitive data**, real records or credentials into a prompt.
- **You're responsible** for what you commit. AI doesn't replace critical thinking.

---

## CDP today → GCP tomorrow

| | CDP today | GCP tomorrow |
|---|---|---|
| Where logs go | CML session or job output, Spark UI | **Cloud Logging** (Dataproc, Composer, Cloud Run all send there) |
| Finding a failed run | CML job history | Dataproc job page, Composer task logs, Logs Explorer queries |
| Spark UI | Session's Spark UI | Dataproc web interfaces, persistent history server |
| Alerts | Mostly manual checks | **Log-based alerts** in Cloud Monitoring, e.g. on `severity>=ERROR` |

**Carries over unchanged:** the method, reading errors, `logging` in your code.
**Really changes:** nobody is watching an ephemeral cluster's console, so **good log messages are the only record** of what happened. Write them for the person reading them at 9am.

---

## Summary

- Judge **severity and impact** first. Wrong published numbers matter most.
- Tracebacks: read the **last line**, then the **last frame in your code**. For Spark, look for **`Caused by:`**.
- Method: **reproduce → read → hypothesise → inspect → fix → verify**.
- Silent bugs: **write down what correct looks like** and turn it into checks.
- **`logging`, not `print`**: levels, counts, decisions, and no personal data.
- Use AI to help you think, not to think for you.

---

## Exercise (20 min, in pairs)

```bash
python exercise/air_quality_report.py
```

- The March air-quality report is broken and due today.
- **4 bugs.** Fix them until the output matches "what correct looks like".
- Then add **logging** and one **safeguard**.

**Next session (Module 3):** data profiling and source system analysis.
