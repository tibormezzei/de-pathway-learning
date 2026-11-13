---
marp: true
theme: default
paginate: true
header: "DE Learning Sessions · 03"
footer: "Writing maintainable Python for data"
---

<!-- _class: lead -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Writing maintainable Python
## for data

Session 03 · Module 1: Foundations of building

---

## Today

1. Why maintainability matters
2. Style: PEP 8, PEP 20 and tools that enforce them
3. Good functions
4. Vectorise, don't loop
5. Modules, packages and config
6. Functions or classes?
7. Refactoring safely
8. **Homework:** refactor a messy pipeline

---

## Code is read far more than it's written

The pipeline you write today will be:
- **read** in code review next week
- **debugged** at 4pm on a release day in six months
- **handed over** when you move teams
- **migrated** to GCP

> "Works on my machine, do not touch" isn't a finished pipeline.

Maintainable code is **cheaper, safer and kinder** to your colleagues and your future self.

---

## PEP 20: The Zen of Python (highlights)

```text
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Readability counts.
Errors should never pass silently.
In the face of ambiguity, refuse the temptation to guess.
```

`import this` in any Python shell shows the full list.

---

## PEP 8: style in 30 seconds

| Thing | Convention | Example |
|---|---|---|
| Variables, functions | `snake_case` | `cleaned_responses`, `parse_date()` |
| Constants | `UPPER_SNAKE` | `MIN_AGE = 16` |
| Classes | `PascalCase` | `PipelineStage` |
| Line length | ≤ 88–100 chars (team choice) | |
| Imports | top of file: stdlib, third-party, local | |

**Don't argue about style. Automate it:**
```bash
ruff format .     # formats your code
ruff check .      # finds bugs and style problems
```

---

## Names are documentation

```python
# ❌
df2 = df[df["age"] >= 16]
df3 = df2.drop_duplicates(subset=["case_id"])
rr = round((c + p * 0.5) / n * 100, 1)
```

```python
# ✅
adults = responses[responses["age"] >= MIN_AGE]
unique_cases = adults.drop_duplicates(subset=["case_id"])
response_rate = round(weighted_responses / issued * 100, 1)
```

If you need a comment to explain what a variable *is*, rename it.

---

## Good functions: one job

```python
def parse_date(value: str) -> datetime | None:
    """Parse a date in any accepted format, or return None."""
    for fmt in DATE_FORMATS:
        try:
            return datetime.strptime(value, fmt)
        except (TypeError, ValueError):
            continue
    return None
```

- **One job**, described by its name
- **Inputs as parameters, outputs as return values**, with no globals and no hidden reading or writing
- **Docstring** says *what*, **type hints** say *with what*
- Catch **specific** exceptions, never a bare `except:`

---

## Pure functions are easy to test and reuse

```python
# ❌ reads a global, mutates its input, returns nothing
def clean():
    df["region"] = df["region"].str.strip().str.title()

# ✅ data in → new data out
def standardise_region(df: pd.DataFrame) -> pd.DataFrame:
    """Trim and title-case the region column."""
    return df.assign(region=df["region"].str.strip().str.title())
```

Chain the steps into a readable pipeline:

```python
cleaned = (
    raw.pipe(standardise_region)
       .pipe(parse_interview_dates)
       .pipe(filter_valid_ages)
       .pipe(drop_duplicate_cases)
)
```

---

## Vectorise, don't loop

```python
# ❌ Python loop over rows: slow, verbose, doesn't translate to Spark
for i in range(len(df)):
    if df.loc[i, "region"] == "sth":
        df.loc[i, "region"] = "south"

# ✅ one vectorised operation on the whole column
df["region"] = df["region"].replace({"sth": "south", "wst": "west"})
```

```python
# ❌ nested loops filtering for every region × month
# ✅
df.groupby(["region", "month"]).agg(issued=("case_id", "size"))
```

**Think in columns and groups, not rows.** It's also how PySpark thinks (session 05).

---

## Modules and packages

```
survey_pipeline/
├── __init__.py      # makes it a package
├── __main__.py      # entry point: python -m survey_pipeline ...
├── config.py        # business rules: MIN_AGE, aliases, date formats
├── clean.py         # cleaning functions
└── metrics.py       # response-rate calculation
tests/
└── test_clean.py
```

- Group code by **responsibility**.
- **Config is separate from logic**, so business rules are visible and easy to change.
- **No hard-coded paths**: take them as arguments or from config.
- For new repos, start from **ons-python-template**.

---

## An entry point

```python
def run(input_path: Path, output_path: Path) -> pd.DataFrame:
    raw = pd.read_csv(input_path, dtype=str)
    result = response_rates(clean(raw))
    result.to_csv(output_path, index=False)
    return result


if __name__ == "__main__":
    main()     # parses --input / --output, then calls run()
```

```bash
python -m survey_pipeline --input data/raw.csv --output out/rates.csv
```

The same command runs on a laptop, in a CML job and on Dataproc.

---

## Functions or classes?

| Use **functions** when… | Use a **class** when… |
|---|---|
| You transform data in, data out | You have **state + behaviour** that belong together |
| Steps are independent and composable | Many objects share one interface (e.g. pipeline stages) |
| Most DataFrame cleaning and transforms | Config objects, connections, clients |

```python
class PipelineStage:                      # e.g. the plumb-etl style
    def run(self, df: DataFrame) -> DataFrame: ...
```

**Default to functions.** Reach for a class when it removes repetition or groups things that really belong together, not to look "proper".

---

## Refactoring safely

> Refactoring = changing the **structure** without changing the **behaviour**.

1. **Capture current behaviour first**: save the output, or write a test.
2. Change **one small thing**.
3. **Check** the output is identical.
4. Commit. Repeat.

Spot something that looks like a **bug or odd business rule**? **Write it down and ask.** Don't quietly "fix" it in the middle of a refactor.

---

## CDP today → GCP tomorrow

| | CDP today | GCP tomorrow |
|---|---|---|
| How code runs | Scripts and notebooks in a CML project | Jobs **submitted** to Dataproc, Cloud Run, Composer |
| Packaging | Nice to have | **Needed**: wheels / `--py-files` / containers |
| Paths | HDFS / S3 paths | `gs://` paths, from config, never hard-coded |
| Notebooks | Often used for production runs | Exploring only; production is scripted |

**Carries over unchanged:** everything on these slides.
**Really changes:** a **packaged, parameterised entry point** goes from good practice to **essential**.

---

## Summary

- Code is read far more than it's written, so optimise for the reader.
- **PEP 8 + a formatter**; names that explain themselves.
- **Small, pure functions** with docstrings and type hints.
- **Vectorise**: think in columns and groups.
- **Package** it: modules by responsibility, config separate, an entry point with no hard-coded paths.
- **Refactor safely**: capture behaviour, change little, check, commit.

---

## Homework: refactor a messy pipeline

`homework/messy_pipeline.py` works but is hard to maintain.

1. Refactor it into a package (checklist in `homework/README.md`).
2. Prove you haven't changed behaviour: `python check_output.py <your output>` → **PASS**.
3. Write down anything that looks like a bug or questionable rule.

Bring it to session 04, where we'll swap with a neighbour for a quick code review.

**Next session:** SQL for data engineers.
