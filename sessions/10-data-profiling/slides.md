---
marp: true
theme: default
paginate: true
header: "DE Learning Sessions · 10"
footer: "Data profiling and source system analysis"
---

<!-- _class: lead -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Data profiling
## and source system analysis

Session 10 · Module 3: Analysis and design

---

## Today

1. Why profile?
2. Profiling vs validation
3. What to look at
4. Data smells
5. Source system analysis
6. From findings to insight
7. **Homework:** profile a new source and report what matters

---

## Assumptions are the most expensive bugs

"The ID is unique."
"Dates are all valid."
"Every row has a local authority."
"The supplier sends a full extract."

Each of these is a **guess** until you've looked. A pipeline designed on guesses gets **redesigned later**, or publishes wrong numbers.

**Profiling = looking at the data before you design anything.**

---

## Profiling vs validation

| | **Profiling** (today) | **Validation** (session 08) |
|---|---|---|
| Question | *What is actually in this data?* | *Does this data meet our rules?* |
| When | Once, at the start, and when a source changes | Every run |
| Output | Findings, questions, **draft rules** | Pass, fail, quarantine |
| Mindset | Curious, exploratory | Strict |

Profiling **discovers** the rules that validation later **enforces**.

---

## Read everything as text first

```python
df = pd.read_csv("inspections.csv", dtype=str, keep_default_na=False)
```

- Typing on read **hides problems**: `"01110"` → 1110, `"n/a"` → NaN, `"Exempt"` → error or NaN.
- As text you see **exactly what was sent**, then you decide the types.
- In Spark: `spark.read.csv(path, header=True)` with **no** `inferSchema` gives all strings.

---

## What to look at: every column

| Check | Question | Tool |
|---|---|---|
| **Completeness** | How many blanks? What does blank *mean*? | `blank_%` |
| **Type** | Is it really numeric or a date? Mixed? | `numeric_%`, patterns |
| **Cardinality** | Constant? Unique? A handful of categories? | `distinct`, `unique_%` |
| **Range** | Min and max plausible? Future dates? Negatives? | `min`, `max` |
| **Values** | Spelling variants? Sentinels? | `value_counts()` |
| **Patterns** | What shapes do codes take? | `patterns()` |
| **Keys** | Is the "ID" unique? | `.duplicated().sum()` |
| **Relationships** | Do columns agree with each other? | cross-tabs |

---

## Pattern profiling

```python
patterns(df["address_postcode"])
```

```text
AA99 9AA    722
AA9 9AA     317
aa999aa      95      ← lower case, no space
<blank>      44
aa99aa       34
```

Replace letters with `A`/`a` and digits with `9`, then count the **shapes**. It finds format problems in codes, IDs, postcodes and dates in seconds.

---

## Data smells

| Smell | Example | Usually means |
|---|---|---|
| **Sentinel values** | `1900-01-01`, `9999`, `-1`, `"N/A"` | "Unknown", disguised as a real value |
| **Mixed types** | Rating: `5`, `4`, `Exempt` | A category pretending to be a number |
| **Spelling variants** | `Newport` / `NEWPORT` / `Newport City Council` | Free-text entry, totals will split |
| **Constant column** | `scheme_type` = `FHRS` everywhere | No information |
| **Nearly empty** | `fax_number` 99% blank | Unused field (and data you may not need) |
| **Impossible values** | Dates in 2031; lat/long `0, 0` | Keying or processing errors |
| **Broken key** | Duplicate `establishment_id` | Re-sends, merges, or a wrong grain assumption |

---

## Source system analysis

Profiling tells you about **this file**. SSA tells you about **the system it came from**.

| Question | Why it matters |
|---|---|
| **Structure:** what's the grain and the key? | Joins, dedup, counts |
| **Update pattern:** full or incremental? How often? | Replace vs merge, scheduling |
| **History:** current state only, or changes over time? | What you can and can't publish |
| **Quality at source:** who enters it, and how? | Where problems come from, and who can fix them |
| **Access and ownership:** who do you ask? | Every finding needs an owner |

---

## From findings to insight

❌ "`local_authority` has 8 distinct values with 3 Newport variants and a 10.6% postcode pattern mismatch."

✅ "**Newport is recorded three different ways.** If we published today, Newport's figures would be split across three rows. We can fix this in processing and will ask the supplier to standardise."

- Lead with the **decision or impact**.
- **Plain English**, with meaningful numbers ("1 in 10 postcodes").
- Separate **what we'll fix** from **what we need from others**.
- Three key findings beat thirty minor ones.

---

## CDP today → GCP tomorrow

| | CDP today | GCP tomorrow |
|---|---|---|
| Quick profiling | pandas on a sample, or PySpark `describe()` / `summary()` in CML | Same on Dataproc, or SQL in **BigQuery** |
| Big tables | Spark aggregates per column | BigQuery `COUNT(DISTINCT)`, `APPROX_` functions, **table preview is free** |
| Automated profiles | ydata-profiling (pandas or Spark) | **Dataplex data profiling** scans |
| Cost to watch | Cluster time | BigQuery bytes scanned: profile **selected columns** or a **sample** |

**Carries over unchanged:** the checklist, smells, SSA questions and write-up. All of today.
**Really changes:** built-in profiling tools exist, but **someone still has to interpret them**.

---

## Summary

- **Profile before you design.** Assumptions are expensive.
- Read **as text first**, then go through **every column**: completeness, type, cardinality, range, values, patterns, keys, relationships.
- Learn the **smells**: sentinels, mixed types, variants, constants, impossible values, broken keys.
- **Source system analysis**: grain, update pattern, history, quality at source, ownership.
- Write findings as **impact and decisions**, in plain English.

---

## Homework

`homework/README.md`

1. **Profile** `data/inspections.csv` with `profile_tools.py`: every column.
2. **Source system analysis** using `data/supplier_note.md`, plus 3 or more questions for the supplier.
3. **One page** for the service manager: 3 findings, why they matter, what you recommend.

Bring your top finding to session 11. You'll present it in one sentence.

**Next session:** data modelling I: conceptual, logical and physical.
