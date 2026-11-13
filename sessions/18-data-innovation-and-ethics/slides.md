---
marp: true
theme: default
paginate: true
header: "DE Learning Sessions · 18"
footer: "Data innovation and ethics"
---

<!-- _class: lead -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Data innovation and ethics

Session 18 · Module 4: Delivering and working with people

---

## Today

1. What innovation means here
2. Data ethics
3. **Scenarios** (pairs)
4. Evaluating a new tool, and when to adopt it
5. Hype vs value
6. Horizon scanning and communities
7. Homework + series wrap-up

---

## Innovation in a public sector data team

Two kinds:
- **New tools:** a faster engine, a better test framework, a new platform (GCP!)
- **New uses of data:** linking, new sources (admin data, web data), new methods

What's different for us:
- **Public trust** is the product. One misstep costs more than ten wins gain.
- **Approval routes** exist for good reasons (security, procurement, legal basis).
- Value comes from **better, faster, cheaper statistics**, not novelty.

<!-- Innovation isn't the same as "using the newest thing". Most innovation in a DE team is removing toil. -->

---

## Data ethics: the questions to ask

UK Statistics Authority ethics principles (summarised):

| Principle | Ask |
|---|---|
| **Public good** | Is there a clear benefit to the public? |
| **Confidentiality & security** | Is data protected; could anyone be identified? |
| **Methods & quality** | Are the methods sound and the limits understood? |
| **Legal compliance** | Is there a legal basis; does it fit the agreement? |
| **Public views & engagement** | Would the public expect and accept this use? |
| **Transparency** | Could we openly explain what we did? |

Tools: UKSA **ethics self-assessment**, the government **Data Ethics Framework**, the ONS DALI Data Ethics team.

---

## Ethics traps engineers actually hit

- Pasting **real data into an online/AI tool**
- **Purpose creep:** "we have the data, so let's link it"
- **Production data in dev** because synthetic data is "not realistic"
- **Proxies** that discriminate (postcode → deprivation)
- **Quietly fixing** a published error
- **Opaque** processing nobody can reproduce or explain

Most aren't malicious. They're **shortcuts under time pressure**.

---

## Scenarios (10 min, pairs)

`homework/ethics_scenarios.md`

For each: **Is there an issue? Which principle? What would you do?**

1. The helpful assistant · 2. The clever linkage · 3. The quiet fix
4. The proxy · 5. The synthetic shortcut · 6. The new shiny

<!-- Reveal answers from solutions/example_evaluation.md (facilitator notes). Link #3 back to PACE (session 17). -->

---

## Evaluating a new tool

| Criterion | Question |
|---|---|
| **Fit** | Which problem *of ours* does it solve? |
| **Maturity** | Stable? Who else uses it? Will it exist in 3 years? |
| **Skills** | How long for the team to become productive? |
| **Integration** | Does it work with CDP today **and** GCP tomorrow? |
| **Cost** | Licence, compute, *maintenance* |
| **Security** | Licence type, does data leave, approval route |
| **Exit cost** | How hard is it to stop using it? |

No problem to solve? **Then the answer is "not now".**

---

## Timing: a tech radar

```
               ┌──────────────────────────────────┐
               │  HOLD   don't start new work     │
               │  ┌────────────────────────────┐  │
               │  │ ASSESS  explore, learn     │  │
               │  │  ┌──────────────────────┐  │  │
               │  │  │ TRIAL  one real,     │  │  │
               │  │  │ low-risk project     │  │  │
               │  │  │  ┌────────────────┐  │  │  │
               │  │  │  │ ADOPT standard │  │  │  │
               │  │  │  └────────────────┘  │  │  │
               │  │  └──────────────────────┘  │  │
               │  └────────────────────────────┘  │
               └──────────────────────────────────┘
```

Adopt **too early** and you carry immature tools. Adopt **too late** and you carry toil and skills gaps.
A team radar, refreshed quarterly, makes the timing a **shared decision**.

---

## Hype vs value

Hype signals:
- "It will replace X entirely"
- Demos on perfect data, no talk of failure modes
- A solution looking for a problem

Run a **safe trial**:
1. Synthetic or public data **only**
2. A specific success measure ("profiling 3× faster, same results")
3. Time-boxed with a review date
4. Write it up, **including** "it wasn't worth it"

<!-- Negative results are valuable. They stop the next person spending the same week. -->

---

## Keeping up without drowning

- **Communities of practice:** ONS/government DE and Python communities, internal show-and-tells
- **Meetups:** PyData Southampton, Cardiff, Manchester, London
- **Podcasts and blogs:** Data Skeptic, Towards Data Science, engineering blogs
- **Release notes** of the tools you already use (Spark, pandas, Airflow)
- **Practitioner+:** arXiv alerts, industry reports

**Habit:** 30 minutes a week, and share one thing a month. Teaching is the best filter.

---

## CDP today → GCP tomorrow

The migration **is** an innovation decision, already made at organisational level.
The decisions left to *your team* are the small ones:

| Decision | Use the template |
|---|---|
| BigQuery SQL or Spark on Dataproc for this pipeline? | Fit, skills, cost |
| Dataproc Serverless or a cluster? | Cost, ops effort |
| Adopt Dataplex for quality and lineage? | Maturity, integration, exit cost |
| Keep running a pipeline unchanged ("lift & shift") or redesign it? | Timing, value |

**Carries over unchanged:** ethics principles, evaluation criteria, safe trials.
**Really changes:** more managed services and pay-per-use. **Cost** becomes an evaluation criterion you can measure.

---

## Series wrap-up

| Module | You can now… |
|---|---|
| 0 | Explain the DE role and work in a reproducible, version-controlled way |
| 1 | Write maintainable Python, SQL and PySpark, and test and debug it |
| 2 | Validate, profile and model data (3NF, star, SCD2) |
| 3 | Design integration, metadata and governance |
| 4 | Plan, deliver, communicate and innovate responsibly |

**Next:** the optional **capstone**, the wiki's Practitioner resources, and your team's own CDP → GCP work.

---

## Homework

**Evaluate one emerging tool or technique** with `homework/evaluation_template.md`:
- Try it hands-on (synthetic or public data **only**)
- Score fit, maturity, community, skills, integration, cost, security and exit cost
- **Ethics and risks** section
- A recommendation: **Adopt / Trial / Assess / Hold**, with *why now*
- A 2-minute summary for the team

Worked example: `solutions/example_evaluation.md` (Polars)
