# Exercise: map a pipeline

**Time:** 20 minutes · **Work in:** pairs

Pick **one** of these:
- **Option A:** a pipeline you work on, or one you know well.
- **Option B:** the fictional scenario below.

---

## Option B: fictional scenario

> A government department runs a **business register survey**. Businesses submit returns through a web form, which writes each return to a transactional database. Every Monday, analysts download the previous week's returns as CSV, clean them by hand in Excel, combine them with an industry classification lookup that the classifications team emails over as a spreadsheet, and paste the results into a quarterly report template.
>
> The analysts are spending two days a week on this. Duplicate submissions sometimes get through, and last quarter an out-of-date lookup was used without anyone noticing.
>
> You've been asked to replace the manual process with a pipeline.

Design the pipeline you would build. The worksheet below applies to both options.

---

## 1. Lifecycle → component → tool

| Stage | What happens here? | Component | Tool / service (name your platform) |
|---|---|---|---|
| Generate | | Source system | |
| Ingest | | | |
| Store (raw) | | | |
| Transform | | | |
| Store (curated) / Serve | | | |
| Orchestration | *What triggers it, how often, and what happens on failure?* | | |
| Version control | | | |
| Metadata | | | |
| Monitoring | | | |

## 2. Classify it

| Question | Answer | Why? |
|---|---|---|
| Moving from OLTP to OLAP? | | |
| Batch or streaming? | | |
| ETL, ELT, or a mix? | | |
| Which file format(s)? | | |

## 3. Risks

Name at least one:
- Where could this pipeline break, or quietly produce wrong data?
- How would you find out?

## 4. CDP → GCP

You've probably filled in section 1 for CDP. Now redraw the **Tool / service** column for **GCP**.
- Which components only **change name**?
- Which ones **really change** something you'd have to do or think about (cost, permissions, who manages the cluster)?

**Stretch:** redraw it for a laptop. What's the smallest working version of this pipeline?

---

## Share-back (5 min)

Each pair gives one thing in 30 seconds: something surprising, a risk they spotted, or a component they couldn't name.
