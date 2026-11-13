# Data Engineering Learning Sessions

A series of learning sessions that teach the core data engineering skills that don't depend on any one platform. The topics are based on the ONS Data Engineering Learning Pathway wiki (reference copy in `reference/ons_de_wiki/`).

> Status: **DRAFT structure.** Sessions are outlined but no content has been written yet.

## Decisions so far

| Area | Decision |
|---|---|
| Audience | Data Engineers at **HEO** grade |
| Target level | The level the wiki expects for HEO within 3–6 months in role. This is **Working** for most skills and **Awareness** for Communicating, Innovation and Problem resolution |
| Format | Concept presentation, then **either** a short in-session exercise **or** homework, whichever fits the topic better |
| Style | **Concept first, with some code**. Ideas stay platform-neutral, and code is there to illustrate them |
| Stack for code | Python, SQL and PySpark, all run locally. Exercises use pandas, PySpark (local mode), DuckDB for SQL, pytest and git |
| Scope | Every skill the wiki covers (see the mapping in `CURRICULUM.md`) |
| Session length | **60 min, weekly**: about 35 min of concepts, then about 20 min of exercise or homework briefing and Q&A. The 18 sessions take roughly 4–5 months |
| Slides | **Markdown (Marp)** stored in the repo, rendered to HTML/PDF/PPTX |
| Data | **Each session has its own dataset**, chosen to suit its topic. There is no shared case study |
| Platforms | Everyone works on **CDP today**, and the series also **prepares them for GCP**. Concepts are taught platform-neutral, then every session ends with a **"CDP today → GCP tomorrow"** bridge slide that shows how the idea maps onto each platform and what changes |

## Local setup

```bash
# Python 3.11 + Java 17/21 (for PySpark)
python -m venv .venv
.venv\Scripts\activate          # Windows  (source .venv/bin/activate on Linux/macOS)
pip install -r requirements.txt
```

Exercises run locally (pandas, PySpark in local mode, DuckDB, pytest), so they work the same whichever platform a learner uses at work.

**Setup gotchas (Windows):**
- Spark starts Python workers with whatever `python` is on PATH, not your venv's Python. The session scripts and `conftest.py` files set `PYSPARK_PYTHON` for you. If you write your own Spark scripts, set it yourself (`os.environ["PYSPARK_PYTHON"] = sys.executable`) or you'll get `Connection reset` errors.
- PySpark 3.5 needs **NumPy < 2** and **PyArrow** for `pyspark.testing`. Both are pinned in `requirements.txt`.
- The Windows console can't show some characters. The scripts avoid emoji in output.
- Spark's Parquet **writer** (and directory listing on read) needs `hadoop.dll` next to `winutils.exe`. The capstone writes through pandas and pyarrow on Windows instead.

## Repo layout

```
learning_pathway/
├── README.md              # this file
├── CURRICULUM.md          # the session-by-session structure
├── templates/
│   └── session_template.md
├── sessions/
│   └── NN-short-name/     # 01–18, all written
│       ├── session.md     # facilitator plan
│       ├── slides.md      # Marp presentation
│       ├── data/          # this session's own dataset
│       ├── exercise/      # in-session exercise, if this session has one
│       ├── homework/      # take-home task, if this session has one
│       └── solutions/
├── capstone/              # optional end-of-series project (brief, rubric, data, reference solution)
├── wiki/                  # GENERATED from the slides. Don't edit (see below)
├── tools/
│   └── build_wiki.py      # slides.md → wiki/ pages, Home and sidebar
├── .github/workflows/
│   └── publish-wiki.yml   # checks wiki/ on PRs, publishes to the GitHub Wiki on merge to main
└── reference/
    └── ons_de_wiki/       # snapshot of the source wiki
```

## The wiki

The GitHub Wiki has one page per session, made from that session's `slides.md`. Speaker notes are left out. `Home.md` and `_Sidebar.md` are built from the modules in `CURRICULUM.md`.

- **Don't edit `wiki/` or the live wiki by hand.** Edit the slides, then run `python tools/build_wiki.py` and commit the regenerated `wiki/` with your change.
- On a PR, the `publish-wiki` action runs `build_wiki.py --check` and fails if `wiki/` is out of date.
- On merge to `main`, it rebuilds the pages and replaces the whole live wiki with them, so any edits made directly on GitHub are lost.
- **One-time setup:** enable the wiki in the repo settings and create any first page in the web UI. GitHub doesn't create the `.wiki.git` repo until then, and the action can't push before it exists.
