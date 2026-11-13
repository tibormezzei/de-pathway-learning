# Source-to-target mapping: appointments by health board (reference)

**Target:** `appointments_by_board`, one row per board per month (27 rows for Jan–Jun 2026)

| Target column | Source system | Source table.column | Transformation / business rule | Notes |
|---|---|---|---|---|
| month | Appointment system | `appointments.month` | Unchanged | yyyy-mm text |
| board_code | Practice registry | `practice_board_v1.board_code` (Jan–Mar), `practice_board_v2.board_code` (from Apr) | Join on standardised and merger-mapped `practice_code` **and** month within the version's validity | HB05 exists only from Apr 2026 |
| board_name | Practice registry | `boards.board_name` | Join on `board_code` | |
| appointments | Appointment system | `appointments.appointments` | Cast to integer; **sum** by month and board | Excludes quarantined rows |
| practices | Appointment system | `appointments.org_code` | Standardise (trim, upper case, remove spaces/hyphens) → map merged codes → **count distinct** by month and board | W00029/W00030 count as W00010 from Mar 2026 |

## Row-level rules
- **Key standardisation:** `org_code` → trim → upper case → remove spaces and hyphens → `practice_code`.
- **Mergers:** from `practice_mergers.effective_month` onwards, `old_code` is replaced by `new_code`.
- **Lookup versioning:** v1 applies to months 2026-01..2026-03 and v2 from 2026-04.
- **Exclusions:** rows whose practice code isn't in the registry, or has no board for that month, go to **quarantine** with their appointments. They're reported, not dropped. (Jan–Jun 2026: 2 rows, 2,233 appointments.)

## Reconciliation (every run)
- Σ appointments in source = Σ appointments in target + Σ appointments in quarantine.
- Re-running with the same inputs gives an identical target (idempotent).
