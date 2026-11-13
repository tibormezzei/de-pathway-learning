---
marp: true
theme: default
paginate: true
header: "DE Learning Sessions · 15"
footer: "The data development process"
---

<!-- _class: lead -->
<!-- _header: "" -->
<!-- _footer: "" -->

# The data development process
## from requirements to production

Session 15 · Module 4: Delivering and working with people

---

## Today

1. Why designs fail
2. The lifecycle
3. Requirements
4. Orchestration
5. CI/CD and environments
6. Containers and infrastructure as code
7. Design documents
8. **Demo** + **homework:** design a real pipeline

---

## Why designs fail

Most pipeline designs handle the **happy path**:
> file arrives → transform → publish ✅

Production is mostly the **awkward cases**:
- the file is **late**, or **sent twice**, or **corrected** next week
- the reference data **changed** last month
- the job **failed halfway** and someone re-ran it
- one supplier's data is **missing** on publication day

**A good design is mostly about the awkward cases.** Modules 1–3 gave you the tools, and today puts them together.

---

## The lifecycle

From the wiki's data development process, condensed:

| # | Step | Sessions |
|---|---|---|
| 1 | **Business objectives**: what question, for whom, by when? | 17 |
| 2 | **Identify and analyse sources** | 10 |
| 3 | **Define data requirements**: dictionary, history, granularity, rules | 14 |
| 4 | **Design the data model** | 11–12 |
| 5 | **Select technology** | 01, today |
| 6 | **Design ETL**: cleansing, scheduling, **failure handling** | 08, 13, today |
| 7 | **Governance and quality** standards | 08, 14 |
| 8 | **Prototype / MVP** on a subset, then validate with stakeholders | 16 |
| 9 | **Plan for scale and maintenance**: monitoring, alerting, recovery | 09, today |

---

## Requirements

| Type | Example (school attendance) |
|---|---|
| **Functional**: what it produces | Weekly attendance rate by LA and phase |
| **Quality**: how good, how reliable | Reproducible for any past week; missing LAs flagged |
| **Constraint**: limits | Thursday 09:30; CDP now, GCP next year; six weeks |
| **Out of scope**: what it *won't* do | No school-level figures |

- **Number them** (R1, R2…) so designs, tests and stories can refer back to them.
- Writing down **out of scope** prevents scope creep and arguments later.
- Ambiguity becomes an **open question with an owner**.

---

## Orchestration: what and why

An orchestrator runs your pipeline's tasks:
- **in the right order** (dependencies form a **DAG**: a directed acyclic graph)
- **on a schedule**, or when data arrives
- **for a given date** (the run date is a parameter)
- **retrying** transient failures
- **alerting** someone when it really fails
- **backfilling** past dates on request

```
extract ──▶ validate ──▶ transform ──▶ publish
```

Examples: Airflow / **Cloud Composer**, Jenkins jobs, CML jobs, cron (the minimal version).

---

## Retries: transient vs data failures

| Failure | Example | Retry? |
|---|---|---|
| **Transient** | Network timeout, cluster busy | ✅ Yes, with back-off |
| **Data** | Invalid records, empty file, schema changed | ❌ No. It'll fail the same way. **Stop and alert** |
| **Code** | A bug | ❌ No. Fix and re-run |

When a task fails, **downstream tasks must not run** on missing or partial inputs.

---

## Backfills and idempotency (again)

A **backfill** re-runs the pipeline for past dates:
- a corrected file arrived for last Tuesday
- a bug fix changes how last month should have been calculated
- a new pipeline needs a year of history

That only works if every task is **idempotent** (session 13):

```python
def transform(run_date):
    data = read(run_date, "validated")         # reads only that date's input
    write(run_date, "output", result)          # overwrites only that date's output
```

**Parameterise by date, read one partition, overwrite one partition.**

---

## The same DAG in Airflow (Cloud Composer)

```python
with DAG("school_attendance", schedule="0 6 * * THU", catchup=False,
         default_args={"retries": 0}) as dag:

    extract = PythonOperator(task_id="extract", python_callable=extract,
                             retries=3, retry_delay=timedelta(minutes=5))
    validate  = PythonOperator(task_id="validate",  python_callable=validate)
    transform = PythonOperator(task_id="transform", python_callable=transform)
    publish   = PythonOperator(task_id="publish",   python_callable=publish)

    extract >> validate >> transform >> publish
```

The **concepts** from the demo map one-to-one. The tool provides the scheduler, UI, logs and alerting.

---

## CI/CD and environments

**Continuous integration:** every merge request runs tests and checks automatically (session 06).
**Continuous delivery / deployment:** merged code is packaged and deployed automatically.

```
 MR ──▶ CI: lint + tests ──▶ merge ──▶ deploy to DEV ──▶ TEST ──▶ PROD
```

| Environment | Data | Who |
|---|---|---|
| **Dev** | Synthetic or sample | Engineers, freely |
| **Test / pre-prod** | Realistic, controlled | Engineers + QA, with sign-off |
| **Prod** | Real | Automated deployments only |

---

## Containers and infrastructure as code (awareness)

**Containers (Docker):** package code **and** its dependencies into one image that runs the same everywhere.
> No more "works on my machine". The machine comes with the code.

**Infrastructure as code (Terraform):** buckets, datasets, clusters and permissions defined in **version-controlled files**, not clicked together in a console.

```hcl
resource "google_storage_bucket" "raw" {
  name     = "attendance-raw-dev"
  location = "europe-west2"
}
```

Both are more prominent on **GCP**, where teams own more of their infrastructure.

---

## Design documents

A short document written **before** building, reviewed by the team and the stakeholder:

1. Objective and requirements
2. Sources (grain, owner, delivery, issues)
3. Output
4. Design: steps, data model, **quality**, **late and corrected data**
5. Orchestration and operations
6. Technology: **CDP now, GCP later**
7. Governance
8. Testing
9. Risks and **open questions with owners**

Changing a design doc is cheap. Changing a pipeline in production is expensive.

---

## CDP today → GCP tomorrow

| | CDP today | GCP tomorrow |
|---|---|---|
| Orchestration | Team schedulers, CML jobs, Jenkins | **Cloud Composer** (managed Airflow) |
| Compute per run | Long-running shared cluster | **Ephemeral** Dataproc clusters / **Dataproc Serverless** |
| CI/CD | GitLab CI | **GitHub Actions** → deploy to Composer / Artifact Registry |
| Infrastructure | Provided by the platform team | **Terraform**, owned by the team |
| Packaging | Code in the CML project | **Wheels or container images** |

**Carries over unchanged:** the lifecycle, requirements, DAG thinking, idempotency, design docs.
**Really changes:** you own more of the stack, and the orchestrator **will** retry and backfill, so your design must expect it.

---

## Summary

- Good designs are mostly about the **awkward cases**.
- Follow the **lifecycle**: objectives → sources → requirements → model → tech → ETL → governance → MVP → operate.
- Requirements: **functional, quality, constraints, out of scope**, numbered.
- Orchestration: **DAG**, run date as a parameter, **retry transient failures only**, **stop downstream on failure**, **backfill** idempotently.
- CI/CD, environments, containers and IaC: you'll meet them more on GCP.
- **Write a design doc first.**

---

## Demo, then homework

```bash
python demo/mini_orchestrator.py --backfill
python demo/mini_orchestrator.py --rerun
```

**Homework** (`homework/README.md`): design **weekly school attendance statistics** from a stakeholder email.
- Late and corrected files, a changing register, small schools, a fixed publication time, and the move to GCP.

We'll use your design docs in **session 16** (stories) and **session 17** (explaining it).
