# Curriculum (draft)

There are 18 sessions in 5 modules, plus an optional capstone. Each session is a concept presentation followed by **one** of these:
- **Exercise (E):** a short guided task done during the session.
- **Homework (H):** a take-home task, reviewed at the start of the next session.

Each session is **60 minutes**: about 35 min of concepts, then about 20 min of exercise or homework briefing and Q&A. Each session uses **its own dataset**, chosen to suit the topic. The datasets are small, synthetic or public, and stored in the session's `data/` folder.

Everyone currently works on **CDP**. Each session ends with a **"CDP today → GCP tomorrow"** slide that shows what carries over, what only changes name, and what really changes on GCP (cost, IAM, ephemeral compute, infrastructure as code).

## Coverage map: wiki skill → sessions

| Wiki skill | HEO target | Sessions |
|---|---|---|
| Technical understanding (moving to the homepage) | – | 1 |
| Programming & build (incl. Testing) | Working | 2, 3, 5, 6, 7, 15 |
| Data analysis & synthesis | Working | 4, 5, 10 |
| Data development process | Working | 8, 15 |
| Data integration design | Working | 13 |
| Data modelling | Working | 11, 12 |
| Metadata management | Working | 14 |
| Problem resolution (incl. Agile) | Awareness | 9, 16 |
| Communicating tech ↔ non-tech | Awareness | 17 (and presentation tasks throughout) |
| Data innovation | Awareness | 18 |

---

## Module 0: Orientation

### 1. What data engineering is (and isn't)
- **Concepts:** the data lifecycle; the jobs a DE does (from the role profile); OLTP vs OLAP; batch vs streaming; ETL vs ELT; data lake vs warehouse vs lakehouse. Also the **component map**: storage, compute, orchestration, version control. It shows that CDP and GCP are different names for the same building blocks.
- **Code:** none. This session is concepts only.
- **E:** take a pipeline you work on (or a made-up one) and map it onto the components.

## Module 1: Foundations of building

### 2. The working environment and version control
- **Concepts:** command-line basics; IDEs; virtual environments and dependencies; the git mental model (commits, branches, remotes); PR workflow and code review etiquette.
- **E:** branch, commit, open a PR, then resolve a merge conflict on purpose.

### 3. Writing maintainable Python for data
- **Concepts:** PEP 8 and PEP 20; functions vs scripts; modules and packages; when OOP helps and when it doesn't; project structure (ons-python-template); docstrings and type hints.
- **H:** refactor a 200-line notebook-style script into a small, tidy package.

### 4. SQL for data engineers
- **Concepts:** set-based thinking; join types and how they go wrong (fan-out, lost rows); aggregation; CTEs; window functions; a simple mental model of what the engine does.
- **E:** answer 6 business questions on a small multi-table dataset using DuckDB.

### 5. From pandas to PySpark: thinking distributed
- **Concepts:** when to pick pandas, PySpark or SQL; single-machine vs distributed processing; lazy evaluation; partitions; shuffles and why joins and groupBys are expensive; the DataFrame API as a common language.
- **E:** write the same transformation three ways (pandas, PySpark, SQL) and compare them.

## Module 2: Quality and reliability

### 6. Testing fundamentals
- **Concepts:** why we test; unit vs integration vs end-to-end tests; pytest basics; fixtures; parametrisation; positive vs negative tests; coverage and what it doesn't tell you.
- **E:** write tests for an existing function and find the bug they expose.

### 7. Testing data pipelines and TDD
- **Concepts:** testing PySpark transformations; building small test DataFrames; dummy vs synthetic test data; the TDD cycle (red, green, refactor); why fakes are often better than mocks.
- **E:** ping-pong TDD in pairs to build a cleaning function.

### 8. Data quality and validation
- **Concepts:** data quality dimensions (completeness, validity, uniqueness, consistency, timeliness); schema vs content validation; where checks belong in a pipeline; what to do when a check fails (fail, quarantine or warn); Pandera and Great Expectations as examples.
- **E:** write a validation schema for a messy dataset and catch the planted problems.

### 9. Problem resolution: debugging and logging
- **Concepts:** reading tracebacks and Spark errors; working out how severe a problem is and what else it affects; debugging techniques (print statements, debugger, rubber ducking, shrinking the input); logging levels and what to log; using AI assistants responsibly, in line with ONS policy.
- **E:** a broken pipeline with several bugs to find and fix, then add logging to it.

## Module 3: Analysis and design

### 10. Data profiling and source system analysis
- **Concepts:** what profiling is for; profiling metrics; source system analysis (structure, update frequency, access, quality); turning findings into insights; quick profiling tools (ydata-profiling).
- **H:** profile a new source and write up the 3 most important findings for a non-technical stakeholder.

### 11. Data modelling I: conceptual, logical and physical
- **Concepts:** why we model; entities, attributes and relationships; ERD notation (with a nod to UML); conceptual vs logical vs physical models; normalisation up to 3NF; reverse-engineering a model from an existing system.
- **E:** model a simple business domain as a group (e.g. a library or a survey operation), from conceptual through to logical.

### 12. Data modelling II: dimensional modelling
- **Concepts:** OLTP vs analytical models; facts and dimensions; grain; star vs snowflake schemas; slowly changing dimensions (types 1 and 2); conformed dimensions.
- **H:** design a star schema from a supplied operational dataset to answer a given business question (e.g. "response rate by region per month").

### 13. Data integration design
- **Concepts:** combining sources; primary, foreign, natural and surrogate keys; schema mismatches; deduplication; awareness-level record linkage; full vs incremental loads; idempotency; source-to-target mappings. The ONS libraries (de-utils, plumb-etl, DLH_Utils) are covered as examples of reusable integration code.
- **E:** integrate two sources that have mismatched keys and a lookup table that changes version.

### 14. Metadata and data governance
- **Concepts:** kinds of metadata (descriptive, structural, administrative, operational); data dictionaries; lineage; catalogues; standards at awareness level (DCAT, Dublin Core, GSIM); governance roles (IAO, DisCO); PII and GDPR basics.
- **H:** write a data dictionary and a source-to-target mapping for session 13's output.

## Module 4: Delivering and working with people

### 15. The data development process: from requirements to production
- **Concepts:** the wiki's end-to-end lifecycle (objectives → sources → requirements → model → tech choice → ETL design → governance → prototype → maintenance). Also orchestration concepts (DAGs, scheduling, retries, backfills), CI/CD, and awareness of containers and infrastructure as code. All platform-neutral.
- **H:** write a one-page design doc for a small pipeline.

### 16. Ways of working: Agile in data teams
- **Concepts:** Agile vs waterfall; Scrum and Kanban; user stories for data work; estimation; definition of done; working with Jira; documentation as a deliverable; pair programming styles.
- **E:** split a vague data request into stories with acceptance criteria.

### 17. Communicating across technical and non-technical audiences
- **Concepts:** gathering requirements; translating technical ideas for different audiences; managing expectations; communicating risks; presenting in slides, reports and posters; accessible content; PACE graded assertiveness.
- **E:** a 3-minute explanation of your design-doc pipeline to a "non-technical stakeholder" (role-play), with peer feedback.

### 18. Data innovation and ethics
- **Concepts:** data ethics frameworks; how to evaluate a new tool (and when to adopt it); horizon scanning; communities of practice.
- **H:** evaluate one emerging tool or technique against a simple template.

## Capstone (optional)

- **H:** build a small tested pipeline that combines two supplied sources. It should include validation, logging, a dimensional output model, a data dictionary and a 5-minute presentation. It brings together all four modules.
