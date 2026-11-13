# Session 10: Data profiling and source system analysis

| | |
|---|---|
| Module | 3: Analysis and design |
| Wiki skill(s) | Data analysis & synthesis (Working): data profiling, source system analysis, presenting insights; Communicating |
| HEO target level | Working |
| Duration | 60 min (~35 concept / ~20 homework briefing + live profiling demo / ~5 Q&A) |
| Follow-up | **Homework** (profiling a whole source and writing it up takes longer than 20 min) |
| Prerequisites | Sessions 03–04, 08 (quality dimensions) |
| Dataset | Synthetic food hygiene inspections: `data/inspections.csv` (1,212 rows), `data/supplier_note.md`, regenerate with `data/make_data.py`. Helper: `profile_tools.py` |

## Learning outcomes
By the end of the session, participants can:
1. Explain what profiling is for, and why it comes **before** design and validation rules.
2. Profile a dataset systematically: completeness, types, cardinality, ranges, patterns, uniqueness, relationships.
3. Recognise common data smells: sentinels, mixed types, spelling variants, constant columns, impossible values, broken keys.
4. Carry out a basic **source system analysis**: grain, key, update pattern, history, ownership.
5. Turn findings into a short, decision-focused write-up for a non-technical stakeholder.

## Concept outline
| Min | Section |
|---|---|
| 0–4 | Why profile: assumptions are the most expensive bugs |
| 4–8 | Profiling vs validation (session 08): discover first, then enforce |
| 8–18 | What to look at: the column checklist, with examples |
| 18–23 | Data smells gallery |
| 23–28 | Source system analysis: the five questions |
| 28–32 | From findings to insight: writing for stakeholders |
| 32–35 | CDP today → GCP tomorrow |
| 35–52 | **Live demo**: profile `inspections.csv` together for 10 min, then the homework briefing |
| 52–60 | Q&A |

## Homework
- **Task:** profile the inspections extract, answer the source system analysis questions, and write a one-page findings note for a service manager.
- **Starting files:** `homework/README.md`, `homework/findings_template.md`, `profile_tools.py`, `data/`
- **Done when:** every column has been looked at, at least 3 supplier questions are written, and there's a one-page plain-English write-up.
- **Stretch:** compare with a `ydata-profiling` report.
- **Reference answers:** `solutions/README.md` (findings table, SSA, example write-up)

## Further learning (from the wiki)
- [Article: Data profiling (IBM)](https://www.ibm.com/topics/data-profiling)
- [ydata-profiling](https://github.com/ydataai/ydata-profiling): quick automated profiles (works with PySpark too)
- [Learning Hub: Data Visualisation in Python](https://learninghub.ons.gov.uk/course/view.php?id=1195): quick plots for understanding
- [Coffee & Coding](https://teams.microsoft.com/l/team/19%3AqULwEkDAmExr95ouE5mVDMRkzhF3uV8cMMYQRgbyw2U1%40thread.tacv2/conversations?groupId=8ad6b255-e0da-4d21-9659-5fdeca628904&tenantId=078807bf-ce82-4688-bce0-0d811684dc46) and the RAP network: see how others present findings

## Facilitator notes
- In the live demo, show only `profile()` and one `patterns()` call, and stop once the postcode shapes appear. Leave the rest for the homework.
- Start session 11 by having two or three people read out their top finding to the room, as a practice in plain-English communication (links to session 17).
- The best write-ups lead with a decision. Praise those, even if they found fewer issues.
