# Exercise: from a vague request to a first sprint

**Time:** 20 minutes · **Work:** in groups of 3–4 (one person is the **product owner** and answers questions in role)

The request (from session 15's brief, as the product owner said it out loud in a meeting):

> "We need the weekly attendance stats pipeline. 22 authorities, by phase, national figures, published Thursdays, quality assured, disclosure-checked, on CDP but ready for GCP. Six weeks. Can you just get on with it?"

## Part 1: split it (about 8 min)

Split the work into **user stories**. Aim for **vertical slices**: each story delivers something end to end that someone could look at, even if it's small.

```
As a <who>, I want <what>, so that <why>.
```

❌ Horizontal: "Build ingestion", "Build validation", "Build aggregation" (nothing usable until all three are done)
✅ Vertical: "Attendance rate for **one LA, one week**, all phases, as a CSV the analyst can check"

Hints: start with the **thinnest possible end-to-end slice**, then add **breadth** (more LAs, phases), **robustness** (late files, resends), **governance** (disclosure), **operations** (scheduling, alerting).

## Part 2: acceptance criteria (about 7 min)

For your **top 3** stories, write acceptance criteria in **Given / When / Then** form:

```
Given  a daily file for Cardiff for 2 March with 3 schools
When   the pipeline runs for the week of 2 March
Then   the output has one row for Cardiff with sessions attended / possible summed over the 3 schools
```

Each criterion should be **testable**, and ideally it becomes an automated test.

## Part 3: size and order (about 5 min)

- Size each story: **S / M / L**. Anything **L** should be split again.
- Order the backlog: what goes in **sprint 1** (2 weeks)? What's the MVP?
- Agree a **definition of done** for the team (start from `definition_of_done.md`).

## Templates
- `story_template.md`
- `definition_of_done.md`

## Discuss
- Which stories carry the most **risk**? Should they come earlier or later?
- Where are the **spikes** (time-boxed investigations) needed before you can estimate?
