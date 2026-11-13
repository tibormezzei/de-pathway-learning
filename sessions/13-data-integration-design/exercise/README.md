# Exercise: integrate two sources that don't quite fit

**Time:** 20 minutes · **Work:** in pairs

The health analysis team wants **GP appointments per health board per month**. Two teams own the data:

| Source | Owner | Files | Quirks |
|---|---|---|---|
| **A: practice registry** | Registry team | `practices`, `boards`, `practice_board_v1`, `practice_board_v2`, `practice_mergers` | Practice-to-board mapping **changed in April** (v1 → v2). Two practices **merged** into W00010 in March |
| **B: appointment system** | Primary care team | `appointments` | `org_code` typed by hand: `w00012`, `" W00012 "`, `W-00012`. Some months still use pre-merger codes |

## Task

`exercise/integrate.py` has the pipeline and reconciliation. Complete the three steps:

1. **`standardise_code`:** make B's codes match A's format.
2. **`apply_mergers`:** from the effective month, map merged practices to their successor.
3. **`attach_board`:** join to the **lookup version valid for that month**.

```bash
python exercise/integrate.py
```

## You're done when the reconciliation says

```
appointments_in               424013
appointments_out              421780
appointments_quarantined        2233     ← 2 rows: a typo (W0001O, letter O) and an unknown code
in == out + quarantined:  True
idempotent (re-run gives identical output): True
```

and **HB05 Coast UHB appears only from April**.

## Experiments (if you have time)
What happens to the totals if you…
1. …skip `standardise_code`?
2. …join to **v2 only** for every month?
3. …join to **both** versions **without** the month condition?

For each one: would anyone notice from the output alone? Which check catches it?

## Discuss
- Should the typo `W0001O` be fixed automatically (it's "obviously" `W00010`)? Who decides?
- The appointment team keeps sending pre-merger codes. Whose problem is that to fix: ours, theirs, or both?
