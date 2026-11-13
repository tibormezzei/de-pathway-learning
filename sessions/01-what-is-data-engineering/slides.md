---
marp: true
theme: default
paginate: true
header: "DE Learning Sessions · 01"
footer: "What data engineering is (and isn't)"
---

<!-- _class: lead -->
<!-- _header: "" -->
<!-- _footer: "" -->

# What data engineering is
## (and isn't)

Session 01 · Module 0: Orientation

---

## Today

1. Why data engineering exists
2. What a data engineer does
3. The data lifecycle
4. Five distinctions everyone should know
5. The component map: same building blocks, different names
6. **Exercise:** map a pipeline

<!--
Everyone here works on CDP. Say early that the series teaches concepts first so they carry over to GCP, and that each session ends with a "CDP today → GCP tomorrow" slide.
-->

---

## Why does data engineering exist?

Data is **created** in one place…
> survey collection apps, admin systems, APIs, spreadsheets

…is **needed** somewhere else…
> analysts, statistical outputs, dashboards, models

…and is needed **in a different shape**, **reliably**, **on time**, and **safely**.

**Data engineering is the work of getting it from one to the other.**

---

## What a data engineer does

From the ONS data engineer role profile:

- Implement **data flows** connecting operational systems, analytics and BI
- Document **source-to-target mappings**
- **Re-engineer manual flows** so they scale and can be repeated
- Support the build of **data streaming** systems
- Write **ETL** code that performs well
- Develop **reusable** BI reports
- Build **accessible data** for analysis

---

## …and what they don't do (mostly)

| Role | Main question | Typical output |
|---|---|---|
| **Data engineer** | *How do we get reliable data to the people who need it?* | Pipelines, tables, datasets |
| Data analyst | *What does the data say?* | Analysis, reports, statistics |
| Data scientist | *What can we predict or infer?* | Models, experiments |
| Data architect | *How should data be structured across the organisation?* | Models, standards, designs |

The boundaries blur. Data engineers **share 4 skills with data architects**: communicating, data analysis, data modelling and metadata.

---

## The data lifecycle

```
 GENERATE ──▶ INGEST ──▶ STORE ──▶ TRANSFORM ──▶ SERVE
 (sources)    (move)     (land)    (clean,       (tables, files,
                                    join, model)  APIs, dashboards)

 ════════════ underpinned by ════════════════════════════════════
   governance · metadata · security · quality · monitoring
```

Data engineers own **ingest → serve**, and they care about everything along the bottom line.

<!--
Ask: which stage do you spend most time in? It's usually transform. The bottom line is where problems hide.
-->

---

## Distinction 1: OLTP vs OLAP

| | **OLTP** (transactional) | **OLAP** (analytical) |
|---|---|---|
| Purpose | Run the business | Understand the business |
| Workload | Many small reads/writes | Few large scans and aggregations |
| Example | Survey collection app saving each response | "Response rate by region, per month, for 5 years" |
| Model | Normalised (see session 11) | Dimensional (see session 12) |

Data engineers usually move data **from OLTP systems to OLAP systems**.

---

## Distinction 2: batch vs streaming

**Batch:** process a bounded chunk of data on a schedule.
> "Every night at 2am, load yesterday's responses."

**Streaming:** process events continuously as they arrive.
> "Update the dashboard within seconds of each response."

- Batch is **simpler, cheaper and easier to test**, and it's what most ONS work is.
- Streaming is for when **latency really matters**.
- Ask: *how fresh does this data need to be?* The answer is rarely "real time".

---

## Distinction 3: ETL vs ELT

**ETL:** Extract → **Transform** → Load
> Clean and reshape *before* data lands in the target.

**ELT:** Extract → Load → **Transform**
> Land raw data first, then transform it *inside* the target, often with SQL.

| | ETL | ELT |
|---|---|---|
| Raw data kept? | Often not | Yes, so you can reprocess |
| Transform runs in | Pipeline code (e.g. PySpark) | Warehouse engine (e.g. SQL) |

In practice most pipelines are a **mix of both**.

---

## Distinction 4: where data lives

| | Holds | Good for |
|---|---|---|
| **Database** | Structured, current records | Applications (OLTP) |
| **Data warehouse** | Structured, modelled, historical | Analysis and reporting (OLAP) |
| **Data lake** | Anything (raw files, any format) | Cheap storage, raw landing, flexibility |
| **Lakehouse** | Files in a lake + warehouse-style tables on top | Both at once |

A common pattern is **raw → cleaned → curated**, often called the *bronze → silver → gold* layers.

---

## Distinction 5: file formats

| Format | Layout | Schema | Use it for |
|---|---|---|---|
| CSV | Row | None (everything is text) | Exchange with people and legacy systems |
| JSON | Nested | Loose | APIs, semi-structured data |
| **Parquet** | **Columnar** | Embedded, typed | **Analytics at scale** |

Columnar = read only the columns you need, plus much better compression.

```python
df.write.parquet("responses/")   # what you'll usually want for analysis
```

---

## The component map

Every pipeline, on any platform, is built from the same blocks:

| Component | Job |
|---|---|
| **Storage** | Where data lands and lives |
| **Compute** | What runs the transformations |
| **Orchestration** | What runs it, when, in what order, and what happens on failure |
| **Version control** | Where the code lives and how changes are reviewed |
| **Metadata / catalogue** | What the data is, where it came from, who owns it |
| **Monitoring / logging** | How you find out it broke |

---

## Same building blocks, different names

| Component | Laptop | ONS CDP | GCP |
|---|---|---|---|
| Data lake | Local folder | S3 via HUE | Cloud Storage |
| Warehouse | DuckDB / SQLite | HDFS + Hive, SQL Server | BigQuery |
| Transformation | pandas / PySpark local | PySpark in Cloudera ML | PySpark on Dataproc |
| Orchestration | cron / a script | *(varies by team)* | Cloud Composer (Airflow), Cloud Functions |
| Version control | git | GitLab | GitHub |

**Learn the concepts once, then map them onto whatever platform you're using.** That's why this series is platform-neutral.

<!--
Table adapted from the wiki homepage. Services change, so check it before presenting.
-->

---

## CDP today → GCP tomorrow

We work on **CDP today**. GCP is coming, and the move is mostly about **names and responsibilities**, not new concepts.

| | CDP (Cloudera on AWS) | GCP |
|---|---|---|
| Who manages infrastructure? | Cloudera does most of it | More of it is **ours**: IAM, buckets, clusters, cost |
| Spark | Long-running cluster sessions in CML | Often **ephemeral** clusters (Dataproc) or serverless |
| SQL warehouse | Hive / Impala on HDFS | **BigQuery** (serverless, pay per query) |
| Code | GitLab | GitHub |
| New things to care about | | **Cost**, permissions (IAM), infrastructure as code |

**What carries over unchanged:** PySpark, SQL, git, testing, data modelling, validation, design thinking. That's most of this series.

<!--
The aim is to reassure people. Most of what they know carries over. The genuinely new parts on GCP are cost awareness, IAM and owning more of the infrastructure, and later sessions will point these out.
-->

---

## Worked example

*Survey responses → monthly management information dashboard*

| Stage | Component | Example |
|---|---|---|
| Generate | Source system | Survey collection app (OLTP) |
| Ingest | Orchestration + compute | Nightly batch job extracts new responses |
| Store | Lake (raw) | Parquet files, partitioned by date |
| Transform | Compute | PySpark: clean, deduplicate, join to reference data |
| Serve | Warehouse | Star schema tables → dashboard |
| Underpinning | Metadata, monitoring | Data dictionary, row-count checks, failure alerts |

---

## What good looks like

Over this series we'll work towards pipelines that are:

- **Reproducible:** same input, same output (version control, environments)
- **Tested:** we know it works and find out when it stops working
- **Validated:** bad data is caught, not passed on
- **Idempotent:** safe to re-run
- **Observable:** logs and alerts tell us what happened
- **Documented:** someone else can pick it up
- **Understood:** stakeholders know what they're getting

---

## The series

| Module | Sessions |
|---|---|
| 0 · Orientation | 1 |
| 1 · Foundations of building | 2–5: environment & git, Python, SQL, pandas → PySpark |
| 2 · Quality & reliability | 6–9: testing, TDD, data validation, debugging & logging |
| 3 · Analysis & design | 10–14: profiling, modelling ×2, integration, metadata |
| 4 · Delivering & people | 15–18: dev process, Agile, communicating, innovation |

---

## Exercise: map a pipeline (20 min, in pairs)

1. Pick a pipeline **you work on**, or use the **fictional scenario** on the worksheet.
2. Fill in the worksheet: for each lifecycle stage, give the **component** and **tool**.
3. Classify it: OLTP→OLAP? Batch or streaming? ETL or ELT?
4. Note **one risk or weakness**. Where would it break, and how would you find out?
5. **CDP → GCP:** redraw it for GCP. What only changes name, and what really changes?

📄 `exercise/README.md`

---

## Summary

- Data engineering gets data **from where it's created to where it's needed**, in the right shape, reliably.
- Lifecycle: **generate → ingest → store → transform → serve**, with governance underneath.
- Know the distinctions: **OLTP/OLAP · batch/streaming · ETL/ELT · database/warehouse/lake · row/columnar**.
- Every platform is **the same building blocks with different names**.

**Next session:** the working environment and version control.
