# Facilitator answer: session 02 exercise

## Step 2
- **Colleague A (main):** added `"Wales", "Scotland"` to `VALID_REGIONS`.
- **Colleague B (branch):** `MIN_AGE` 16 → 18, added `"Northern Ireland"` to `VALID_REGIONS`, and added `"submitted_at"` to `DROP_DUPLICATES_ON`.
- **Both** changed the `VALID_REGIONS` line, which is where the conflict comes from.

## Step 3
`feature/max-age` was branched from the current `main`, and `main` hadn't changed since, so git just moves `main` forward (a **fast-forward** merge). No combining is needed.

## Step 4: resolved file

```python
"""Cleaning rules for survey responses."""

MIN_AGE = 18
MAX_AGE = 110
VALID_REGIONS = ["North", "South", "East", "West", "Wales", "Scotland", "Northern Ireland"]
DROP_DUPLICATES_ON = ["case_id", "submitted_at"]
```

The check prints:
```
18 110 ['North', 'South', 'East', 'West', 'Wales', 'Scotland', 'Northern Ireland'] ['case_id', 'submitted_at']
```

Teaching point: the right answer is **neither side** of the conflict but a combination of both. That's why resolving conflicts takes understanding, not just picking "ours" or "theirs".

Because the changed lines are next to each other, git puts all four lines into **one conflict block**:

```text
<<<<<<< HEAD
MIN_AGE = 16
MAX_AGE = 110
VALID_REGIONS = ["North", "South", "East", "West", "Wales", "Scotland"]
DROP_DUPLICATES_ON = ["case_id"]
=======
MIN_AGE = 18
MAX_AGE = 120
VALID_REGIONS = ["North", "South", "East", "West", "Northern Ireland"]
DROP_DUPLICATES_ON = ["case_id", "submitted_at"]
>>>>>>> feature/colleague-b
```

**The trap:** "accept incoming" (B's side) looks almost right, but it silently puts `MAX_AGE` back to 120 and drops Wales and Scotland. Ask the room who fell for it. It shows why you resolve conflicts line by line against what the code *should* do.

## Step 5: example MR description

> **Raise minimum age to 18 and deduplicate on submission time**
>
> **What:** `MIN_AGE` 16 → 18; adds Northern Ireland to valid regions; deduplication now uses `case_id` + `submitted_at`.
> **Why:** the survey scope changed to adults only (link to decision/ticket). Some respondents legitimately submit twice for different reference periods, so `case_id` alone dropped valid records.
> **Testing:** cleaning unit tests updated for 16- and 17-year-olds; reran on last month's test extract, and 312 previously dropped records are now kept.
> **Reviewer:** please check the dedup change. Does anything downstream assume `case_id` is unique?

## Stretch: merge vs rebase
- **Merge** keeps the true history, with a merge commit joining the branches. It's safe for shared branches.
- **Rebase** replays the branch commits on top of `main`, giving a linear history with no merge commit. It's cleaner to read, but it **rewrites commits**, so never rebase a branch other people have pulled.
- Many teams rebase their own feature branch onto `main` before opening the MR, then merge (or squash-merge) the MR.
