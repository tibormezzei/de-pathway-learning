---
marp: true
theme: default
paginate: true
header: "DE Learning Sessions · 16"
footer: "Ways of working: Agile in data teams"
---

<!-- _class: lead -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Ways of working
## Agile in data teams

Session 16 · Module 4: Delivering and working with people

---

## Today

1. Waterfall vs Agile
2. Scrum and Kanban
3. User stories for data work
4. Acceptance criteria
5. Estimation, spikes, MVP, definition of done
6. Jira, and ONS roles
7. **Exercise:** from a vague request to a first sprint

---

## Waterfall vs Agile

| | **Waterfall** | **Agile** |
|---|---|---|
| Plan | Everything up front | Enough to start, refined continuously |
| Delivery | One big release at the end | Small, working increments |
| Change | Expensive, resisted | Expected, welcomed |
| Feedback | At the end (too late) | Every sprint |
| Suits | Well-understood, stable problems | **Uncertain** problems |

Data work is **full of uncertainty**: what's really in the source (session 10)? What does "attendance" mean? Will the method match the analyst's?

**Find out early, with something working.**

---

## Scrum in one slide

**Roles**
- **Product owner:** owns the backlog and priorities, and represents users
- **Delivery manager / Scrum master:** removes blockers, protects the process
- **Team:** engineers, analysts, testers, who decide *how*

**Events** (in a 2-week sprint)
- **Planning:** what can we finish this sprint?
- **Daily stand-up:** progress, plan, blockers (15 minutes)
- **Review:** show working output to stakeholders
- **Retrospective:** how can we work better?

**Artefacts:** product backlog · sprint backlog · **increment** (working output)

---

## Kanban

```
 To do │ In progress (max 3) │ In review (max 2) │ Done
───────┼─────────────────────┼───────────────────┼─────
 ▢ ▢ ▢ │  ▣ ▣                │  ▣                │ ▣ ▣ ▣
```

- **Continuous flow**, with no fixed sprints.
- **Work-in-progress limits**: stop starting, start finishing.
- Good for **operational** work: run support, incoming data requests, bug fixes.

Many ONS data teams use **Scrum for build** and **Kanban for run**.

---

## User stories

```
As a  <who>
I want <what>
so that <why>
```

> As an **analyst**, I want the attendance rate for **one LA for one week** as a CSV,
> so that **I can check the method against my spreadsheet**.

Good stories are **INVEST**:
**I**ndependent · **N**egotiable · **V**aluable · **E**stimable · **S**mall · **T**estable

---

## Slice vertically, not horizontally

```
              HORIZONTAL stories          VERTICAL stories
              (one per layer)             (one per thin slice)

               S1     S2     S3            S1     S2     S3
 ingest       ████                         █      █      █
 validate            ████                  █      █      █
 aggregate                  ████           █      █      █
 output                     ████           █      █      █

              usable only after S3        usable after S1
```

Slice 1: **one LA, one week, all phases.** Then add breadth (22 LAs, phases), then robustness (late files, resends), then governance (disclosure), then automation (scheduling).

---

## Acceptance criteria: Given / When / Then

```
Given  two Newport files for 3 March, received at 07:00 and 15:00
When   the pipeline runs for the week of 2 March
Then   only the 15:00 file is used for Newport on 3 March
```

Each criterion becomes a **test**:

```python
def test_latest_resubmission_wins(spark):
    # Given
    files = make_files(("NWP", "2026-03-03", "07:00", 100), ("NWP", "2026-03-03", "15:00", 120))
    # When
    result = latest_per_la_day(files)
    # Then
    assert result.collect()[0]["sessions_attended"] == 120
```

Stories, tests and the definition of done connect (sessions 06–07).

---

## Estimation, spikes and MVP

- **Size relatively:** S / M / L (or story points). If it's **L, split it**.
- **Spike:** a time-boxed investigation when you can't estimate yet.
  > "2 days: get sample files from every LA and find out how resubmissions are named."
- **MVP (minimum viable product):** the smallest thing that delivers value and tests the riskiest assumptions.
  > Correct numbers for one week, all LAs, by phase, run by hand.
- **Order by value and risk:** do the riskiest things early, while there's time to change course.

---

## Definition of done

A shared checklist. A story isn't done until **all** of it is true:

- [ ] Reviewed merge request on `main`
- [ ] Tests written, CI green
- [ ] Validation and reconciliation pass
- [ ] Logging in place
- [ ] Data dictionary and mapping updated
- [ ] No real data or secrets committed
- [ ] Shown to the product owner
- [ ] Safe to re-run

It stops "done, apart from the tests and docs", which in practice means not done.

---

## Jira in practice

| Jira | Means |
|---|---|
| **Epic** | A large goal: "Weekly attendance publication" |
| **Story** | A user-facing slice with acceptance criteria |
| **Task / sub-task** | Technical work inside a story |
| **Bug** | Something that doesn't meet its criteria |
| **Spike** | A time-boxed investigation |

- Link commits and merge requests to tickets (e.g. `ATT-42` in the branch name).
- **Update the board yourself.** It's how the team knows what's happening without asking.
- Write tickets so someone else could pick them up.

---

## ONS roles alongside Agile

| Role | Where they appear |
|---|---|
| **IAO** | Approves data use. A dependency for stories that need new data or sharing |
| **DisCO** | Signs off outputs leaving secure environments. Include them in acceptance criteria for publishing stories |
| **Data architect** | Reviews models and designs |
| **Methodologist / statistician** | Agrees methods, and is often the "user" in stories |

These sign-offs take **time**. Put them **in the backlog**, not as a surprise at the end.

---

## CDP today → GCP tomorrow

| | CDP today | GCP tomorrow |
|---|---|---|
| Backlog | Jira | Jira (unchanged) |
| Code + review | GitLab merge requests | GitHub pull requests |
| CI | GitLab CI | GitHub Actions |
| New story types | | Infrastructure (Terraform), IAM, cost monitoring, migration stories |

**Carries over unchanged:** everything today.
**Really changes:** the **migration itself** is a project to slice vertically. Move **one pipeline end to end** first, not "all ingestion" first.

---

## Summary

- Agile suits **uncertain** work, and data work is uncertain.
- **Scrum** for build, **Kanban** for run, both making work **visible**.
- Stories as **vertical slices**: something usable after the first one.
- **Given / When / Then** acceptance criteria → automated tests.
- **Spikes** for unknowns, an **MVP** for the riskiest assumptions, and a shared **definition of done**.
- Put IAO, DisCO and other sign-offs **in the backlog**.

---

## Exercise (20 min, groups)

The product owner says:
> "Weekly attendance pipeline. 22 LAs, by phase, national, Thursdays, QA'd, disclosure-checked, CDP but GCP-ready. Six weeks. Just get on with it."

1. **Split** into vertical-slice stories
2. **Given / When / Then** for the top 3
3. **Size**, **order**, plan **sprint 1**, agree a **definition of done**

**Next session:** communicating across technical and non-technical audiences.
