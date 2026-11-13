# Example backlog: weekly school attendance (one good answer)

## Backlog, in order

| # | Story | Size | Sprint |
|---|---|---|---|
| 0 | **Spike** (time-boxed, 2 days): get one real-format sample file per LA and the register. How are resubmissions named? | S | 1 |
| 1 | As an **analyst**, I want the attendance rate for **one LA for one week**, all phases combined, as a CSV, so that I can check the method against my spreadsheet | M | 1 |
| 2 | As an analyst, I want **all 22 LAs** and a **national** figure for one week, so that I can see the full picture | S | 1 |
| 3 | As an analyst, I want the figures **by phase**, using the register **as at the date**, so that schools that changed phase are counted correctly | M | 1 |
| 4 | As the **statistician**, I want invalid rows **quarantined and reported** (attended > possible, unknown school), so that bad data never reaches the figures | M | 2 |
| 5 | As the statistician, I want **corrected resubmissions** to replace earlier files for that LA-day, so that published figures use the latest data | M | 2 |
| 6 | As the statistician, I want a **reconciliation and completeness report** (LAs reporting, sessions in = out + quarantined), so that I can sign off each week | S | 2 |
| 7 | As the **DisCO**, I want cells below the agreed threshold **suppressed** (with secondary suppression), so that no small school is identifiable | M | 2 |
| 8 | As the **analysis team**, I want the pipeline **scheduled for Thursday 06:00** with alerts on failure or a missing LA, so that publication is on time without manual runs | M | 3 |
| 9 | As an engineer, I want to **backfill any past week** with one command, so that late corrections and fixes are easy | S | 3 |
| 10 | As an engineer, I want all paths and tables **in config** and I/O in one module, so that the GCP move is a configuration change, not a rewrite | S | 3 |
| 11 | As a **user**, I want a data dictionary and dataset metadata published alongside the figures, so that I understand what they mean | S | 3 |

**MVP (end of sprint 1):** stories 1–3, the correct numbers for one week, all LAs, by phase, run by hand.

## Acceptance criteria examples

**Story 1**
1. **Given** a Cardiff file for each day 2–6 March with 3 schools, **when** the pipeline runs for week 2026-03-02, **then** the output has one row for Cardiff with Σ attended ÷ Σ possible over the 15 school-days.
2. **Given** the analyst's spreadsheet calculation for the same files, **when** the outputs are compared, **then** the rates match to 0.1 percentage points.

**Story 3**
1. **Given** school S123 changed from primary to special on 4 March, **when** the week of 2 March is processed, **then** S123's 2–3 March sessions count as primary and its 4–6 March sessions count as special.

**Story 5**
1. **Given** two Newport files for 3 March received at 07:00 and 15:00, **when** the week is processed, **then** only the 15:00 file is used for Newport on 3 March.
2. **Given** the week has already been processed, **when** a corrected file arrives and the week is re-run, **then** only Newport's figures change and the output has no duplicate rows.

## Why this order
- **Thin end-to-end first** (1): proves the method with the analyst early, which is the biggest risk.
- **Breadth before robustness** (2–3): a correct, complete happy path is the MVP.
- **Robustness and governance** (4–7) before **automation** (8–9): never automate something that might publish wrong figures.
- The **spike** (0) unblocks estimating story 5 and the ingestion details.
- Story 10 is cheap now and expensive later, so it's in, even though no user sees it.
