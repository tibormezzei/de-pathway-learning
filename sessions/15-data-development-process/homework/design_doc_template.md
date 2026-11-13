# Design: <pipeline name>

**Author:** · **Date:** · **Status:** draft / in review / agreed · **Reviewers:**

## 1. Objective
What business question does this answer, for whom, by when? (2–3 sentences)

## 2. Requirements
| # | Requirement | Type (functional / quality / constraint) | Source |
|---|---|---|---|
| R1 | | | |

**Out of scope:**

## 3. Sources
| Source | Owner | Format and delivery | Grain | Update pattern | Known issues and questions |
|---|---|---|---|---|---|

## 4. Output
Tables or files, grain, key columns, who uses them. Link to the data dictionary (session 14).

## 5. Design
Diagram + steps (ingest → validate → transform → publish). For each step: what it does, inputs and outputs, failure behaviour.

```
source ──▶ ... ──▶ output
```

### Data model
Grain, keys, history handling (SCD / versioned reference data).

### Data quality
Validation rules; fail / quarantine / warn; reconciliation.

### Late and corrected data
How does the design handle late files and resubmissions? Is it idempotent?

## 6. Orchestration and operations
Schedule, dependencies, retries, alerting, backfills, who gets alerted, run book.

## 7. Technology
| Component | CDP today | GCP later |
|---|---|---|

What has to change at migration? What have you done now to make that easier?

## 8. Governance and security
Personal data? Disclosure? IAO? Access? Retention?

## 9. Testing
Unit, integration, end-to-end; test data.

## 10. Risks, assumptions and open questions
| Item | Type (risk / assumption / question) | Impact | Mitigation / owner |
|---|---|---|---|
