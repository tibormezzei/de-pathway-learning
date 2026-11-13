---
marp: true
theme: default
paginate: true
header: "DE Learning Sessions · 14"
footer: "Metadata and data governance"
---

<!-- _class: lead -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Metadata and data governance

Session 14 · Module 3: Analysis and design

---

## Today

1. Why metadata matters
2. Kinds of metadata
3. Data dictionaries and source-to-target mappings
4. Lineage and catalogues
5. Standards
6. Governance: roles, personal data, disclosure
7. Metadata as code
8. **Homework:** document the integrated dataset

---

## "What does this column mean?"

You've seen this already in this series:
- `rating_value` mixes numbers and text (session 10)
- "Appointments": booked, or attended? (session 13)
- Which board-mapping version applies to March? (session 13)

Without metadata, every user **rediscovers** the same things or, worse, **guesses**.

> Data without metadata is a liability, not an asset.

---

## Kinds of metadata

| Kind | Answers | Examples |
|---|---|---|
| **Descriptive** | What is it? | Title, description, keywords, coverage |
| **Structural** | How is it organised? | Columns, types, keys, relationships, grain |
| **Administrative** | Who, rules, rights? | Owner, IAO, classification, licence, retention |
| **Operational** | What happened in the run? | Run time, row counts, lookup version used, quarantine totals |

Engineers produce **all four**. Operational metadata usually comes free from good logging (session 09).

---

## The data dictionary

| column_name | data_type | description | nullable | example | source | transformation |
|---|---|---|---|---|---|---|
| board_code | string | Health board responsible for the practice **in that month** | no | HB05 | practice_board_v1/v2 | Lookup version valid for the month (v1 Jan–Mar, v2 from Apr) |
| appointments | bigint | Total GP appointments recorded by practices in the board that month. **Excludes quarantined rows** | no | 16660 | appointments.appointments | Cast to integer, summed |

Write descriptions **for someone who's never seen the pipeline**. State the business rules.

---

## Source-to-target mapping

For **each target column**: where it comes from and what happens to it.

| Target | Source | Rule |
|---|---|---|
| board_code | practice_board_v1 / v2 | Join on standardised + merger-mapped code, version by month |
| practices | appointments.org_code | Standardise → map mergers → count distinct |

Plus **row-level rules** (exclusions, quarantine) and **what must reconcile**.

It's in the ONS data engineer role profile: *"Document source-to-target mappings."*

---

## Lineage and catalogues

**Lineage** answers *"where did this number come from?"*

```
appointments.csv ──┐
practice_mergers ──┼─▶ integrate ──▶ appointments_by_board ──▶ health dashboard
practice_board v1/v2┘        │
                         quarantine
```

- Needed for **impact analysis**: "the registry is changing its codes; what breaks?"
- Needed for **trust**: "can we explain this published figure?"

**Catalogues** are searchable inventories of datasets with their metadata, so people can **find** data and **understand** it before asking.

---

## Standards (awareness level)

| Standard | For |
|---|---|
| **Dublin Core**, **DCAT** | Describing datasets: title, publisher, coverage, distributions |
| **SKOS** | Code lists, classifications, thesauri |
| **GSIM / GSBPM** | Statistical information and the statistical business process (UNECE) |
| **PROV-O** | Provenance and lineage |
| **ISO/IEC 11179** | Metadata registries and data element definitions |
| **Schema.org** | Making published data findable on the web |

Recognise the names, and know that **DAB** (data architecture) can advise on which apply.

---

## Governance roles

| Role | Responsible for |
|---|---|
| **Information Asset Owner (IAO)** | Accountable for a data asset: approves uses, sharing and risks |
| **Data steward** | Day-to-day quality, definitions and metadata |
| **DisCO** (Disclosure Control) | Checks outputs leaving secure environments aren't disclosive |
| **Data engineer** | Implements the controls, documents and flags issues. **Doesn't decide** uses or access |

When in doubt about whether data *can* be used for something, the answer comes from the **IAO**, not from the pipeline.

---

## Personal data and protection basics

- **Personal data:** anything relating to an identifiable living person, directly or indirectly.
- **Data minimisation:** only take, keep and pass on what's needed. (That 99%-empty `fax_number` column? Drop it.)
- **Purpose limitation:** use data only for the approved purpose.
- **Security classification:** OFFICIAL / OFFICIAL-SENSITIVE. Follow the handling rules.
- **Retention:** keep data only as long as needed, then delete it.
- **Never** in logs, tests, repos or AI prompts (sessions 02, 07, 09).

---

## Disclosure

Aggregates can still reveal individuals:
- small counts ("1 person aged 95+ in this area")
- differencing two tables
- combining with other published data

Board-level appointment counts are **low risk**. A **practice-level** or small-area version needs a **DisCO** check before release.

Record disclosure considerations in the **metadata**, so the next person doesn't have to rediscover them.

---

## Metadata as code

```bash
python homework/check_dictionary.py homework/data_dictionary.csv
```

```text
FAIL: dictionary and data disagree:
  - practices: in the output but not documented
  - appointments: documented as 'int', actual type 'bigint'
```

- Keep metadata **in the repo**, next to the code it describes.
- **Test it against the real output**, so documentation can't silently drift.
- Generate what you can (schemas, row counts, lineage). Write what only people know (meaning, rules, caveats).

---

## CDP today → GCP tomorrow

| | CDP today | GCP tomorrow |
|---|---|---|
| Table metadata | Hive metastore (structure), wiki or SharePoint docs | **BigQuery** column descriptions and labels |
| Catalogue | Mostly documents | **Dataplex Catalog** (formerly Data Catalog): search, tags, business glossary |
| Lineage | Hand-drawn | **Automatic lineage** for BigQuery and Dataproc jobs, viewable in Dataplex |
| Access control | Platform team, Ranger policies | **IAM** roles on datasets, column- and row-level security, policy tags |

**Carries over unchanged:** dictionaries, mappings, governance roles, the thinking.
**Really changes:** the platform can **store and show** much more metadata automatically. **Descriptions and business rules still have to be written by people.**

---

## Summary

- Metadata turns data from a liability into an **asset**.
- Four kinds: **descriptive, structural, administrative, operational**.
- **Data dictionary** + **source-to-target mapping**, written for newcomers.
- **Lineage** for impact and trust. **Catalogues** for finding data.
- Governance: **IAO** decides uses, **DisCO** checks outputs, engineers implement and flag.
- **Metadata as code**: in the repo, tested against the data.

---

## Homework

`homework/README.md`

1. **Data dictionary** for session 13's output, checked against the real data until **PASS**.
2. **Source-to-target mapping**: columns, row rules, reconciliation.
3. **Dataset metadata**, including governance: IAO, personal data, disclosure, quality notes.

**Next session (Module 4):** the data development process: from requirements to production.
