# Capstone rubric

Each row is scored **Not yet / Working / Strong**. "Working" in every row is a pass at HEO level.

| Area | Not yet | Working | Strong |
|---|---|---|---|
| **Profiling** (10) | Jumped straight to code | The main issues in each source are found and listed | Issues are quantified, each with a decision and reason |
| **Code structure** (03) | One long script | Functions, config separate from logic | A small package with I/O isolated from transforms; easy to point at new paths |
| **Integration** (13) | Joins lose or duplicate rows | Keys standardised; no fan-out; no silent loss | Explicit lookup rules; join choices explained |
| **Validation** (08) | Bad rows dropped silently | A quarantine with a reason per row | Rule order deliberate; null-safe; warn vs quarantine justified |
| **Reconciliation** (13) | None | Counts logged; in = out + rejected | The run fails when it doesn't balance; grain checks too |
| **Testing** (06, 07) | No tests | Unit tests for the main rules | Tests for edge cases and nulls, plus an end-to-end test; written test-first |
| **Logging and debugging** (09) | `print` everywhere | Logging with levels and row counts | Useful warnings; a debug mode; a clear failure message |
| **Modelling** (12) | Flat output | Fact plus dimensions with a stated grain | Answers the "later" questions; SCD choice discussed |
| **Metadata** (14) | None | A data dictionary for the output tables | Source-to-target rules documented; matches the real schema |
| **Idempotency** (15) | Re-run duplicates output | Re-run gives the same output | Shown with a test |
| **Version control** (02) | One commit at the end | Regular commits | Meaningful messages; a branch or PR reviewed by a peer |
| **README** (03, 14) | Missing | How to run it plus the main decisions | Trade-offs and limitations stated honestly |
| **Presentation** (17) | Walks through code | The answer first; findings explained | Tailored to a mixed audience; honest about limitations; GCP slide |

## Peer review prompts
- Could you run it from the README alone?
- Pick one rejected row. Can you find out *why* it was rejected?
- Does in = out + rejected? Where is that checked?
- What would break first if next quarter's file had a new centre?
