# Session 11: Data modelling I: conceptual, logical and physical

| | |
|---|---|
| Module | 3: Analysis and design |
| Wiki skill(s) | Data modelling (Working): ERDs, conceptual/logical/physical models, notation, normalisation, reverse engineering |
| HEO target level | Working |
| Duration | 60 min (~35 concept / ~20 exercise / ~5 Q&A) |
| Follow-up | **Exercise** (in session, group whiteboard) |
| Prerequisites | Session 04 (keys, joins, grain) |
| Dataset | `data/case_visits_flat.csv`: a flat spreadsheet export (52 visits), plus `exercise/scenario.md` |

## Learning outcomes
By the end of the session, participants can:
1. Explain why we model data and who each kind of model is for.
2. Identify entities, attributes and relationships from a business description, and draw them with crow's foot notation.
3. Distinguish conceptual, logical and physical models.
4. Normalise a flat table to 3NF and explain each step.
5. Reverse-engineer a model from an existing table or system.

## Concept outline
| Min | Section |
|---|---|
| 0–4 | Top finding from session 10 homework, one sentence each (optional) |
| 4–8 | Why model: shared understanding, fewer bugs, easier change |
| 8–14 | Entities, attributes, relationships, cardinality; crow's foot notation |
| 14–19 | Conceptual → logical → physical |
| 19–23 | Keys: natural, surrogate, composite, foreign |
| 23–30 | Normalisation: anomalies, 1NF, 2NF, 3NF |
| 30–32 | Reverse engineering |
| 32–35 | CDP today → GCP tomorrow |
| 35–55 | Exercise (groups) |
| 55–60 | Compare models; reveal the reference |

## Exercise
- **Task:** build a conceptual model of a survey field operation from a narrative, then a 3NF logical model by normalising a flat export.
- **Starting files:** `exercise/README.md`, `exercise/scenario.md`, `data/case_visits_flat.csv`
- **Done when:** entities and relationships with cardinality are drawn, and the flat file is split into 3NF tables with keys.
- **Stretch:** physical DDL in DuckDB; load the data and prove the result is lossless.
- **Reference:** `solutions/README.md` (Mermaid ERDs + discussion), `solutions/schema.sql`, `solutions/load_and_check.py`

## Further learning (from the wiki)
- [YouTube: Introduction to data modelling](https://www.youtube.com/watch?v=qKWnFRnjkA0) (2 min)
- Hoberman, *Data Modelling Made Simple* (Percipio, or borrow a copy)
- [YouTube playlist: Erwin Data Modeler tutorial](https://www.youtube.com/playlist?list=PLdWyZdkgKpTWy_24ldyMY0vLEfTS_5eYP) (Erwin is the tool used at ONS)
- [Poolparty resource library](https://www.poolparty.biz/resource-library)
- DAMA-DMBOK2, chapter 5 (ONS Data Architecture SharePoint) · [BCS systems modelling resources](https://www.bcs.org/qualifications-and-certifications/certifications-for-professionals/solution-development/bcs-practitioner-certificate-in-systems-modelling-techniques/)

## Facilitator notes
- Data architects (DAB) are natural guests for this session. Invite one to join the exercise debrief.
- Most groups model `ADDRESS` and skip `CASE` at first. Ask "where does the interviewer go if an address is in two surveys?"
- The exercise is pen and paper, deliberately. Tools come later, and the thinking is the skill.
