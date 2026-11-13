# Homework: profile a new source and report what matters

**Time:** about 1.5 hours · **Due:** start of session 11 (bring your one-page write-up)

Your team has been asked to build a pipeline that publishes **food hygiene ratings by local authority**. Before anyone designs anything, you've been asked to profile the first extract and do a quick **source system analysis**.

Inputs:
- `data/inspections.csv`: the extract (1,212 rows)
- `data/supplier_note.md`: what the supplier told you about it

## Part 1: profile (about 45 min)

```python
import pandas as pd
from profile_tools import profile, patterns, value_counts

pd.set_option("display.width", 250)
pd.set_option("display.max_columns", None)

df = pd.read_csv("data/inspections.csv", dtype=str, keep_default_na=False)   # everything as text first
print(profile(df))
print(patterns(df["address_postcode"]))
print(value_counts(df["local_authority"]))
```

Work through **every column**. For each one, note:
- Is it **complete**? What does "blank" mean here?
- Is the **type** what you'd expect? Are there mixed types?
- What do the **values** and **patterns** look like? Any sentinels, outliers or impossible values?
- Is anything that **should be unique** actually unique?
- Is the column **useful** at all?

Record your findings in a table like `findings_template.md`.

## Part 2: source system analysis (about 15 min)

From the supplier note and your profile, answer:
1. **Structure:** what's the grain? What's the key? Can you trust the key?
2. **Update pattern:** full or incremental? How often? What does that mean for the pipeline?
3. **History:** what *can't* this extract tell you? Does that matter for the publication?
4. **Access and ownership:** who do you ask when something's wrong?
5. **Questions for the supplier:** write at least **3** specific questions.

## Part 3: write it up for a non-technical stakeholder (about 30 min)

One page for the **service manager** (not a data person) who has to decide whether the publication can go ahead:
- The **3 most important findings**, in plain English, each with **why it matters** for the publication.
- What you **recommend** (e.g. what to fix in the pipeline vs what to ask the supplier).
- No code, no jargon. If you use a number, make it meaningful ("1 in 10 postcodes" rather than "10.6% pattern mismatch").

## Stretch
- Install `ydata-profiling` (`pip install ydata-profiling`) and generate an HTML report. What does it find that you didn't, and what did you find that it didn't?
