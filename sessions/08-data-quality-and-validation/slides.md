---
marp: true
theme: default
paginate: true
header: "DE Learning Sessions · 08"
footer: "Data quality and validation"
---

<!-- _class: lead -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Data quality and validation

Session 08 · Module 2: Quality and reliability

---

## Today

1. What bad data costs
2. Testing code vs validating data
3. Data quality dimensions
4. Where to validate
5. Declarative validation with Pandera
6. Fail, quarantine or warn
7. **Exercise:** validate, quarantine, report

---

## What bad data costs

- A supplier changes a date format, the pipeline "succeeds", and a month of data lands as nulls.
- Excel strips leading zeros, so every industry code starting `0` is now invalid or, worse, maps to the wrong industry.
- A file is delivered twice, totals double, and no one notices until publication.
- A lookup table is out of date, so new codes silently drop out of a join (session 04!).

**None of these raise an error.** The code is fine. The **data** is wrong.

---

## Testing code vs validating data

| | **Testing** (sessions 06–07) | **Validating** (today) |
|---|---|---|
| Checks | Your **code** does what it should | The **data** is what you expect |
| Input | Small, hand-built, known | Real, incoming, unknown |
| When | Before deployment, in CI | **Every run**, in the pipeline |
| A failure means | A bug in the code | A problem in the data (or a changed assumption) |

You need **both**. Perfect code still produces wrong outputs from wrong inputs.

---

## Data quality dimensions

| Dimension | Question | Example check |
|---|---|---|
| **Completeness** | Is everything there? | No nulls in `employees`; expected row count |
| **Validity** | Does it follow the rules? | `period` is yyyymm; `sic_code` is 5 digits |
| **Uniqueness** | Is anything duplicated? | One return per `(ru_ref, period)` |
| **Consistency** | Do related values agree? | 0 employees **and** £5m turnover? |
| **Accuracy** | Does it match reality? | Hard to automate: compare with other sources |
| **Timeliness** | Is it fresh enough? | Latest period is last month |

---

## Where to validate

```
 source ──▶ [ VALIDATE INPUT ] ──▶ transform ──▶ [ CHECK OUTPUT ] ──▶ publish
              "is it what we           │            "does the result
               were promised?"         │             make sense?"
                                [ checks between stages ]
                                 row counts in = out?
```

- **At ingest:** catch supplier problems before they spread. This is the most valuable place.
- **Between stages:** row counts, join completeness, no unexpected nulls.
- **Before publishing:** totals within expected ranges, no disclosive cells.

---

## Declarative validation: Pandera

```python
import pandera as pa

schema = pa.DataFrameSchema(
    columns={
        "ru_ref":    pa.Column(str,   pa.Check.str_matches(r"^\d{11}$"), nullable=False),
        "period":    pa.Column(str,   pa.Check.isin(VALID_PERIODS)),
        "sic_code":  pa.Column(str,   pa.Check.str_matches(r"^\d{5}$")),
        "region":    pa.Column(str,   pa.Check.isin(REGIONS)),
        "employees": pa.Column(float, pa.Check.ge(0), nullable=False),
        "turnover":  pa.Column(float, pa.Check.ge(0), nullable=False),
    },
    unique=["ru_ref", "period"],
    strict=True,                       # no unexpected columns
)
```

The **rules are readable**. A business colleague can review this.

---

## Collect every failure, not just the first

```python
try:
    schema.validate(df, lazy=True)     # lazy: keep going, collect ALL failures
except pa.errors.SchemaErrors as err:
    failures = err.failure_cases       # a DataFrame: column, check, failure_case, index
```

```text
column    check                       failure_case  index
ru_ref    str_matches('^\d{11}$')     4990123456    17
sic_code  str_matches('^\d{5}$')      1110          42
region    isin([...])                 Londn         88
turnover  greater_than_or_equal_to(0) -51234.5      103
```

The failure report is useful **data**: count it, quarantine by `index`, send it to the supplier.

---

## Cross-field checks and warnings

```python
schema = pa.DataFrameSchema(
    columns={...},
    checks=[
        pa.Check(
            lambda df: ~((df["employees"] == 0) & (df["turnover"] > 1_000_000)),
            name="zero_employees_high_turnover",
            raise_warning=True,          # ← warn, don't fail
        ),
    ],
)
```

Some rules are **"definitely wrong"** and some are **"worth a human look"**. Treat them differently.

---

## Fail, quarantine or warn?

| Response | When | Example |
|---|---|---|
| **Fail the run** | The whole input is untrustworthy | Schema changed, file empty, wrong period delivered |
| **Quarantine rows** | Individual records are bad, the rest are fine | Invalid `ru_ref`, negative turnover |
| **Warn** | Plausible but unusual | Zero employees with high turnover |
| **Auto-fix** | Safe, agreed, **logged** | Trim whitespace, standardise case |

**Never silently drop rows.** Quarantined data must be counted, reported and followed up.

---

## The quiet killer: types on read

```python
pd.read_csv("returns.csv")                    # sic_code 01110 → 1110 (int)  💥
pd.read_csv("returns.csv", dtype={"sic_code": str, "ru_ref": str})   # ✅ "01110"
```

- IDs, codes and postcodes are **text**, even if they look like numbers.
- Information lost **on read** can't be recovered by any later check.
- In Spark, prefer an **explicit schema** over `inferSchema=True` for production reads.

---

## Same ideas, other tools

| Tool | Notes |
|---|---|
| **Pandera** | Python, lightweight, schemas as code. Supports **pandas and PySpark** |
| **Great Expectations** | Bigger framework: expectation suites, data docs, checkpoints |
| **Plain PySpark / SQL** | Row counts, `COUNT(*) FILTER (WHERE ...)`, anti-joins. Always available |
| **dbt tests / Dataplex** | Platform-level data quality (GCP) |

The tool matters less than **writing the rules down** and **running them every time**.

---

## CDP today → GCP tomorrow

| | CDP today | GCP tomorrow |
|---|---|---|
| Validation code | Pandera / custom PySpark checks in the job | Same code on Dataproc |
| Quarantine | A quarantine Hive table or HDFS folder | A quarantine **GCS prefix** or **BigQuery table** |
| Platform DQ | Mostly hand-built | **Dataplex data quality** scans, BigQuery assertions |
| Alerting | Team conventions, email | **Cloud Monitoring** alerts on failure counts |

**Carries over unchanged:** the dimensions, the schema, fail / quarantine / warn.
**Really changes:** more **built-in DQ and alerting** is available. Use it, but don't hand over thinking about the rules.

---

## Summary

- Testing checks **code**, validation checks **data**. You need both, every run.
- Think in **dimensions**: completeness, validity, uniqueness, consistency, accuracy, timeliness.
- Validate **at ingest** first.
- Write rules **declaratively** (Pandera) and collect **all** failures (`lazy=True`).
- **Fail, quarantine or warn**, and never silently drop rows.
- Read codes as **text**.

---

## Exercise (20 min, in pairs)

```bash
python exercise/validate_returns.py
```

- The starter schema catches 7 bad rows. **There are many more.**
- Complete the schema from the survey team's rules.
- For each problem: **auto-fix**, or **refer back**?
- Stretch: cross-field **warning** + an actionable failure report.

**Next session:** problem resolution: debugging and logging.
