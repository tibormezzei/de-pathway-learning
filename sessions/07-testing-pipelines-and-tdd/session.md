# Session 07: Testing data pipelines and TDD

| | |
|---|---|
| Module | 2: Quality and reliability |
| Wiki skill(s) | Programming & build (Testing): TDD, TDDA, pytest fixtures, mocks; Data analysis & synthesis: dummy vs synthetic data |
| HEO target level | Working (TDD itself is closer to Practitioner; aim for confident use of the cycle) |
| Duration | 60 min (~35 concept / ~20 exercise / ~5 Q&A) |
| Follow-up | **Exercise** (in session) |
| Prerequisites | Sessions 05 (PySpark) and 06 (pytest) |
| Dataset | Hand-built test DataFrames (smart-meter readings). No files: that's the point |

## Learning outcomes
By the end of the session, participants can:
1. Write unit tests for PySpark transformations using a session-scoped Spark fixture and small inline DataFrames.
2. Compare DataFrames with `assertDataFrameEqual`.
3. Explain the TDD cycle (red → green → refactor) and use it in a pair.
4. Tell dummy from synthetic test data and choose between them.
5. Structure pipeline code so I/O is at the edges, and explain why fakes usually beat mocks.

## Concept outline
| Min | Section |
|---|---|
| 0–4 | Why pipeline code is hard to test, and how to make it easy |
| 4–10 | Functional core, I/O at the edges |
| 10–16 | Testing PySpark: the fixture, inline DataFrames, `assertDataFrameEqual` |
| 16–21 | Test data: dummy vs synthetic, and what each is for |
| 21–28 | TDD: the cycle, why it works, ping-pong pairing |
| 28–31 | Mocks vs fakes |
| 31–35 | CDP today → GCP tomorrow + summary |
| 35–55 | Exercise: ping-pong TDD |
| 55–60 | Compare routes; discuss the R4 business rule |

## Exercise
- **Task:** build a PySpark meter-reading cleaning module test-first, swapping roles after every test.
- **Starting files:** `exercise/README.md`, `exercise/meter_cleaning.py`, `exercise/test_meter_cleaning.py`, `exercise/conftest.py`
- **Done when:** R1–R4 are implemented, each driven by a test that failed first.
- **Reference solution:** `solutions/` (13 tests)

## Further learning (from the wiki)
- [IBM: 5 steps of test-driven development](https://developer.ibm.com/articles/5-steps-of-test-driven-development/) · [Test-Driven Data Analysis (TDDA) blog](https://www.tdda.info/pages/about.html)
- [Five advanced pytest fixture patterns](https://www.inspiredpython.com/article/five-advanced-pytest-fixture-patterns) · [Ed's pytest examples](https://github.com/EdCussONS/pytest_examples)
- [Book: Obey the Testing Goat](https://www.obeythetestinggoat.com/pages/book.html) · [Book: Cosmic Python](https://www.cosmicpython.com/book/preface.html)
- [Video: Stop using mocks (for a while)](https://www.youtube.com/watch?v=rk-f3B-eMkI) · [Video: Stop mocking, start testing](https://www.youtube.com/watch?v=Xu5EhKVZdV8)
- Synthetic data tools: [Faker](https://pypi.org/project/Faker/), [Mockaroo](https://www.mockaroo.com/), [SMOTE](https://imbalanced-learn.org/stable/references/generated/imblearn.over_sampling.SMOTE.html)

## Facilitator notes
- Spark start-up takes about 10s on the first run. Ask people to run `python -m pytest exercise` at the start of the session so it's warmed up and any setup problems show early.
- Be strict about the rules in the first two rounds (one test, simplest code). People naturally write the whole function at once.
- Most pairs reach R3 in 20 minutes. R4 is good homework.
