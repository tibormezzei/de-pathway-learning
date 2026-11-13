# Session 01: What data engineering is (and isn't)

| | |
|---|---|
| Module | 0: Orientation |
| Wiki skill(s) | Technical understanding (moving to the homepage); Home: role profile responsibilities and the platforms table |
| HEO target level | Awareness, used as a shared vocabulary for the rest of the series |
| Duration | 60 min (~35 concept / ~20 exercise / ~5 Q&A) |
| Follow-up | **Exercise** (in session) |
| Prerequisites | None |
| Dataset | None. This session is concepts only |

## Learning outcomes
By the end of the session, participants can:
1. Explain what a data engineer does and how the role differs from analysts, data scientists and data architects.
2. Describe the stages of the data lifecycle and place common activities in them.
3. Distinguish OLTP from OLAP, batch from streaming, ETL from ELT, and database from warehouse, lake and lakehouse.
4. Break any data pipeline down into platform-neutral components (storage, compute, orchestration, version control, metadata, monitoring) and name the matching service on CDP, GCP or a laptop.

## Concept outline (slides.md)
| Min | Section |
|---|---|
| 0–3 | Why data engineering exists |
| 3–8 | What a DE does, and how it compares with neighbouring roles |
| 8–13 | The data lifecycle |
| 13–25 | Key distinctions: OLTP/OLAP, batch/streaming, ETL/ELT, storage types, file formats |
| 25–32 | The component map: same building blocks, different names |
| 32–35 | What good looks like + series roadmap |
| 35–55 | Exercise: map a pipeline |
| 55–60 | Share-back and Q&A |

## Exercise
- **Task:** Map a real pipeline you work on, or the fictional scenario provided, onto the component map, then answer the reflection questions.
- **Starting files:** `exercise/README.md` (worksheet + scenario)
- **Done when:** every lifecycle stage has a component and a named tool, and there is at least one risk or weakness noted.
- **CDP → GCP:** redraw the pipeline for GCP and say what only changes name and what really changes. **Stretch:** a laptop version.
- **Facilitator answer:** `solutions/scenario_answer.md`

## Further learning (from the wiki)
- [Data engineering vault](https://www.ssp.sh/brain/data-engineering/): concept glossary
- [Data Knowledge Hub](https://officenationalstatistics.sharepoint.com/sites/onswiki/SitePages/Data-Knowledge-Hub.aspx): where DE fits in the ONS (internal)
- [roadmap.sh: data engineer](https://roadmap.sh/) and [r/dataengineering wiki](https://dataengineering.wiki/Learning+Resources)
- [GDD data engineer role](https://ddat-capability-framework.service.gov.uk/role/data-engineer)

## Facilitator notes
- Keep it light. This session sets up vocabulary and the "same blocks, different names" idea that the rest of the series relies on.
- Everyone works on CDP. Explain early that the series is concept-first so it carries over to GCP, and that every session ends with a "CDP today → GCP tomorrow" slide. The exercise's section 4 is where people first try the move to GCP.
- The CDP/GCP table comes from the wiki homepage. Services change, so check it before each run.
- Have people work in pairs in the exercise. If anyone doesn't have a pipeline they can describe, give them the fictional scenario.
