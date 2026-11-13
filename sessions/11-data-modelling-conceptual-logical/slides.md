---
marp: true
theme: default
paginate: true
header: "DE Learning Sessions · 11"
footer: "Data modelling I: conceptual, logical and physical"
---

<!-- _class: lead -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Data modelling I
## conceptual, logical and physical

Session 11 · Module 3: Analysis and design

---

## Today

1. Why model data?
2. Entities, attributes, relationships
3. Conceptual → logical → physical
4. Keys
5. Normalisation
6. Reverse engineering
7. **Exercise:** model a survey field operation

---

## Why model data?

A data model is a **picture of what the data means** and how it fits together.

- **Shared understanding** between the business, architects, engineers and analysts
- **Fewer bugs**: grain, keys and relationships are decided up front, not discovered in a join
- **Easier change**: you can see the impact of a new requirement
- **Documentation** that outlives the people who built the system

At ONS, data architects (DAB) lead on modelling, but **every data engineer needs to read, question and contribute to models**.

---

## Entities, attributes, relationships

| Concept | Is | Example |
|---|---|---|
| **Entity** | A thing the business cares about | Survey, Address, Interviewer, Visit |
| **Attribute** | A fact about an entity | `survey_name`, `visit_date` |
| **Relationship** | How entities connect (a verb) | An interviewer *makes* visits |
| **Cardinality** | How many on each side | One case *receives* one-or-many visits |

Find entities by listening for **nouns** in the business description, and relationships by listening for **verbs**.

---

## Crow's foot notation

```
  SURVEY ||──────o{ CASE         one survey issues zero-or-many cases
  CASE   ||──────|{ VISIT        one case receives one-or-many visits
  PERSON ||──────|| PASSPORT     one-to-one (rare)

  ||  exactly one       o|  zero or one
  |{  one or many       o{  zero or many
```

**Many-to-many** (e.g. surveys ↔ addresses) usually hides an entity. Here it's the **case**.

UML class diagrams show the same ideas with different symbols. Recognise both.

---

## Three levels of model

| | **Conceptual** | **Logical** | **Physical** |
|---|---|---|---|
| Audience | Business | Analysts, architects, engineers | Engineers, DBAs |
| Shows | Entities + relationships | + attributes, keys, normalised structure | + types, indexes, partitions, platform specifics |
| Technology | None | None | **Specific**: Hive, BigQuery, SQL Server |
| Example | "Cases receive visits" | `VISIT(case_id FK, visit_no, visit_date, outcome_code FK)` | `CREATE TABLE visit (... DATE NOT NULL ...)` |

Logical models are **platform-neutral**, so the same logical model works on CDP and on GCP.

---

## Keys

| Key | What | Example |
|---|---|---|
| **Primary key** | Uniquely identifies a row | `case_id` |
| **Natural key** | A real-world identifier | `survey_code`, `ru_ref`, postcode? |
| **Surrogate key** | A meaningless generated ID | `address_id` 1, 2, 3… |
| **Composite key** | Several columns together | `(case_id, visit_no)` |
| **Foreign key** | Points to another table's primary key | `visit.case_id → case.case_id` |

Use a surrogate key when the natural key is **missing, unstable or not unique** (addresses!).

---

## Why normalise? Anomalies

One row per visit, everything repeated:

| case_id | survey_name | interviewer_name | visit_no | outcome_description |
|---|---|---|---|---|
| C0001 | Labour Force Survey | D. Evans | 1 | No contact |
| C0001 | Labour Force Survey | D. Evans | 2 | No contact |
| C0001 | Labour Force Survey | D. Evans | 3 | No contact |

- **Update anomaly:** an interviewer changes name, and hundreds of rows need editing.
- **Insert anomaly:** you can't record a new interviewer until they make a visit.
- **Delete anomaly:** delete the last visit and you lose the case.
- **Drift:** "No contact" vs "No Contact" vs "Non-contact".

---

## Normal forms

> Every non-key attribute depends on **the key** (1NF), **the whole key** (2NF), and **nothing but the key** (3NF).

| Form | Rule | Survey example |
|---|---|---|
| **1NF** | Atomic values, no repeating groups | No `visit1_date, visit2_date, …` columns |
| **2NF** | No dependency on *part* of a composite key | `survey_name` depends on `case_id` only, not `(case_id, visit_no)`, so move it |
| **3NF** | No dependency on a non-key column | `region_name` depends on `region_code`, so give it its own table |

Operational systems (OLTP) are usually 3NF. Analytical models **deliberately denormalise** (next session).

---

## Reverse engineering

Often the system already exists, and you have to work out its model:

1. List the tables and columns (`DESCRIBE`, `information_schema`, Hive metastore, Erwin's reverse-engineer feature).
2. **Profile** (session 10): which columns are unique (keys)? Which values match another table (foreign keys)?
3. Infer the **relationships and cardinality** from the data, then **confirm with the owners**.
4. Draw it.

```sql
-- candidate key?
SELECT COUNT(*), COUNT(DISTINCT case_id) FROM visits;
-- foreign key?
SELECT COUNT(*) FROM visits v LEFT JOIN cases c USING (case_id) WHERE c.case_id IS NULL;
```

---

## CDP today → GCP tomorrow

| | CDP today | GCP tomorrow |
|---|---|---|
| Conceptual and logical | Erwin (DAB), diagrams | **Same models**, platform-neutral |
| Physical | Hive / Impala tables, SQL Server | **BigQuery**: partitioning, clustering, nested and repeated fields |
| Keys enforced? | Hive: no; SQL Server: yes | BigQuery: PK/FK are **informational only**, not enforced |
| Consequence | Validate keys in the pipeline | **Even more** important to validate keys yourself (session 08) |

**Carries over unchanged:** entities, relationships, normalisation, logical models.
**Really changes:** the physical design. BigQuery often **denormalises** with nested fields, and it doesn't enforce keys for you.

---

## Summary

- Models create **shared understanding**. Learn to read, question and contribute to them.
- **Entities** (nouns), **relationships** (verbs), **cardinality** (crow's feet).
- **Conceptual** (business) → **logical** (keys, platform-neutral) → **physical** (platform).
- Keys: natural, surrogate, composite, foreign.
- **Normalise to 3NF** to remove anomalies: the key, the whole key, nothing but the key.
- Reverse-engineer with **profiling and the owners**.

---

## Exercise (20 min, groups)

`exercise/scenario.md` + `data/case_visits_flat.csv`

1. **Conceptual:** entities, relationships and cardinality, from the narrative.
2. **Logical:** normalise the flat file to **3NF** and choose keys.
3. Stretch: **physical** DDL in DuckDB, then prove the load is lossless.

Key question: **is a case the same thing as an address?**

**Next session:** data modelling II: dimensional modelling.
