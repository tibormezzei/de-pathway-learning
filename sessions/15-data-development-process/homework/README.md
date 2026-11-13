# Homework: write a design document

**Time:** about 2 hours · **Due:** start of session 16 (we'll use it in sessions 16 and 17)

Read `brief.md`, an email asking for weekly school attendance statistics. Write a design document using `design_doc_template.md`.

## Guidance
- **Two to four pages.** A design doc is a thinking tool and a conversation starter, not a specification of every line.
- Use everything from the series so far: profiling questions (10), grain and keys (11–12), versioned reference data and idempotency (13), validation and quarantine (08), logging and alerting (09), metadata and governance (14), testing (06–07).
- **Make the hard parts explicit.** For this brief, those are:
  - files that are **late**, and **corrected resubmissions**
  - a school register that **changes over time**
  - **small special schools** (disclosure)
  - a **fixed publication time**, with missing authorities published as such
  - a **CDP → GCP** move next year
- Where you don't know something, list it as an **open question** with an owner. Don't guess.

## The orchestration demo
Run it before you design the scheduling section:

```bash
python demo/mini_orchestrator.py --backfill
python demo/mini_orchestrator.py --rerun
```

Which task is retried, and which isn't? Why? What happens downstream of a failure?

## Self-check before submitting (`rubric.md`)
- [ ] Could a new team member build from this?
- [ ] Could the stakeholder see their requirements in it?
- [ ] Is every failure mode handled (late, resent, invalid, missing, re-run)?
- [ ] Is the CDP → GCP move considered?
- [ ] Are open questions listed with owners?
