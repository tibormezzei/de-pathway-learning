# Session 15: The data development process: from requirements to production

| | |
|---|---|
| Module | 4: Delivering and working with people |
| Wiki skill(s) | Data development process (Working): the 9-step lifecycle; Programming & build: CI, containers, IaC (awareness); Data integration: orchestration |
| HEO target level | Working |
| Duration | 60 min (~35 concept / ~15 demo + homework briefing / ~10 Q&A) |
| Follow-up | **Homework** (design doc) |
| Prerequisites | Modules 1–3. This session pulls them together |
| Dataset | None. `demo/mini_orchestrator.py` generates its own toy data |

## Learning outcomes
By the end of the session, participants can:
1. Describe the end-to-end lifecycle of a data product, from business objectives to maintenance.
2. Capture requirements and turn them into a design that handles real-world failure modes.
3. Explain orchestration concepts: DAGs, scheduling, dependencies, retries, backfills, alerting.
4. Explain CI/CD, containers and infrastructure as code at awareness level.
5. Write a design document that a team and a stakeholder can both review.

## Concept outline
| Min | Section |
|---|---|
| 0–5 | Why designs fail: they skip the awkward cases |
| 5–12 | The lifecycle (the wiki's 9 steps, condensed) |
| 12–16 | Requirements: functional, quality, constraints, out of scope |
| 16–24 | Orchestration: DAGs, schedules, retries, backfills, idempotency |
| 24–28 | CI/CD, environments (dev / test / prod) |
| 28–31 | Containers and infrastructure as code (awareness) |
| 31–35 | CDP today → GCP tomorrow + design docs |
| 35–45 | **Demo**: `mini_orchestrator.py` (single run, backfill with a bad-data day, re-run) |
| 45–50 | Homework briefing |
| 50–60 | Q&A |

## Homework
- **Task:** write a 2–4 page design doc for weekly school attendance statistics, from a stakeholder email.
- **Starting files:** `homework/README.md`, `homework/brief.md`, `homework/design_doc_template.md`, `homework/rubric.md`, `demo/mini_orchestrator.py`
- **Done when:** every template section is addressed, the hard parts (late or resent files, register changes, small schools, fixed time, GCP move) are handled explicitly, and open questions have owners.
- **Reference answer:** `solutions/reference_design.md`

## Further learning (from the wiki)
- The wiki's **Data development process** page: the 9-step lifecycle this session follows
- [Learning Hub: Introduction to Continuous Integration](https://learninghub.ons.gov.uk/course/view.php?id=568) · [Jenkins](https://learninghub.ons.gov.uk/course/view.php?id=543)
- [Docker overview](https://docs.docker.com/guides/docker-overview/) · [YouTube: Containerise Python applications with Docker](https://www.youtube.com/watch?v=0TFWtfFY87U)
- [YouTube: Getting started with Terraform for Google Cloud](https://www.youtube.com/watch?v=BUPenAjobjw)
- [Cloud Skills Boost: Basic Airflow lab](https://www.cloudskillsboost.google/focuses/3528) · [Building batch data pipelines on Google Cloud](https://www.cloudskillsboost.google/course_templates/53)
- DAMA-DMBOK2, chapter 3: data governance considerations

## Facilitator notes
- The demo is the anchor. Run `--backfill` and pause on 5 March: the timeout is retried, the bad record isn't, and downstream tasks are skipped. Ask "why not retry validation?"
- Session 16 uses the design docs for story-splitting, and session 17 uses them for the 3-minute explanation, so make sure everyone does the homework.
- Tool names on the GCP slide (Composer, Dataproc Serverless, Terraform) are for awareness only. Don't teach them here.
