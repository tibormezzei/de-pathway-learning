# Facilitator notes and example answers: session 17

## De-jargon warm-up: example answers

| Jargon | Plain English |
|---|---|
| "The join fans out because the lookup isn't unique on the key." | "One of our reference lists had a school listed twice, so its figures were being counted twice. We've fixed it and added a check." |
| "We quarantine rows that fail schema validation." | "Records that don't make sense, like more pupils present than on the roll, are set aside and reported back to the authority instead of going into the figures." |
| "The pipeline is idempotent, so we can backfill." | "If a council sends a correction next week, we can safely recalculate last week's figures with one command and nothing gets double-counted." |
| "Reconciliation balances but we've got a misallocation from the wrong lookup version." | "All the numbers add up, but three schools were assigned to the wrong area because we used this month's area list for last month. The totals are right, but the area figures aren't, and we're correcting them." |
| "It's an SCD type 2 dimension." | "We keep a history of which area each route belonged to over time, so past figures stay correct when things change." |

## Example opening lines by stakeholder

| Card | Weak opening | Strong opening |
|---|---|---|
| Deputy Director | "So, the pipeline ingests daily CSVs from SFTP…" | "Thursday publication is achievable. The main risk is a late council, and if that happens we publish without them and say so, which is what you asked for." |
| Statistician | "It's all automated, don't worry." | "The rate is total sessions attended divided by total possible, summed across the week. I'd like you to check week one against your spreadsheet before we go live." |
| LA data contact | "Your data has quality issues." | "We need one thing from you: if you resend a day, use the same filename with a later timestamp. Then corrections are picked up automatically." |
| DisCO | "We'll suppress small numbers." | "The smallest unsuppressed cell is N schools, using the threshold you set. We apply secondary suppression so totals can't reveal a hidden cell. A draft will be with you two weeks before go-live." |
| New team member | "It's in the README." | "If it fails on Thursday, check the alert email first. It says which step failed. There's a run book with what to do for each step, and you can re-run safely." |
| Migration lead | "It should be fine." | "All paths are in config and the I/O is in one module. The processing is plain PySpark, so the move is mainly configuration plus Composer scheduling." |

## Debrief points
- **Different stakeholders need different stories about the same pipeline.** Nobody wanted the architecture diagram except, possibly, the migration lead.
- **Lead with the answer.** Senior people often decide in the first 30 seconds.
- **"I don't know yet, I'll find out by X"** builds trust. Bluffing destroys it.
- The **defensive LA contact** responds to a specific, blame-free request, not to a list of their data's faults.
