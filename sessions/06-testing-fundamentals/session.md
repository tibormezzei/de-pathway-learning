# Session 06: Testing fundamentals

| | |
|---|---|
| Module | 2: Quality and reliability |
| Wiki skill(s) | Programming & build (Testing merged in): pytest, unit tests, positive/negative testing, coverage |
| HEO target level | Working |
| Duration | 60 min (~35 concept / ~20 exercise / ~5 Q&A) |
| Follow-up | **Exercise** (in session) |
| Prerequisites | Session 03 (small, pure functions) |
| Dataset | None. The functions under test are in `exercise/survey_utils.py` |

## Learning outcomes
By the end of the session, participants can:
1. Explain why we test, and the difference between unit, integration and end-to-end tests.
2. Write pytest tests using the Arrange–Act–Assert structure.
3. Use **parametrisation**, **fixtures** and **`pytest.raises`**.
4. Choose test cases well: typical, **boundary**, **negative** and error cases.
5. Explain what coverage does and doesn't tell you.

## Concept outline
| Min | Section |
|---|---|
| 0–5 | Why test: confidence to change code, documentation that runs, catching bugs early |
| 5–9 | The test pyramid: unit, integration, end-to-end |
| 9–15 | pytest basics: discovery, `assert`, Arrange–Act–Assert, running and reading output |
| 15–20 | Parametrisation |
| 20–24 | Testing errors: `pytest.raises` |
| 24–28 | Fixtures |
| 28–31 | Choosing test cases: equivalence classes, boundaries, positive and negative |
| 31–35 | Coverage, CI + CDP today → GCP tomorrow |
| 35–55 | Exercise |
| 55–60 | Reveal the four bugs; discuss the sneaky one |

## Exercise
- **Task:** write tests from the docstrings of four utility functions, find the 4 bugs, fix them.
- **Starting files:** `exercise/README.md`, `exercise/survey_utils.py`, `exercise/test_survey_utils.py`
- **Done when:** the spec is covered by tests and everything passes after the fixes.
- **Stretch:** coverage report; doctests.
- **Reference solution:** `solutions/` (`--buggy` flag shows the tests failing on the original code)

## Further learning (from the wiki)
- [PyTest docs](https://docs.pytest.org/en/stable/) · [Real Python: Getting started with testing](https://realpython.com/python-testing/)
- [Writing good unit tests in Python with ease](https://mitches-got-glitches.medium.com/writing-good-unit-tests-in-python-with-ease-5fb6d7aa2b77)
- [Learning Hub: Introduction to Unit Testing](https://learninghub.ons.gov.uk/course/view.php?id=1171)
- [CS50P Week 5: Unit tests](https://cs50.harvard.edu/python/2022/weeks/5/) · [YouTube: How to write unit tests in Python](https://www.youtube.com/watch?v=YbpKMIUjvK8)
- [Different types of testing in Python](https://www.bitecode.dev/p/testing-with-python-part-5-the-different) · [Positive vs negative testing](https://www.geeksforgeeks.org/software-engineering/difference-between-positive-testing-and-negative-testing/)
- [Useful pytest flags](https://adamj.eu/tech/2019/10/03/my-most-used-pytest-commandline-flags/) · [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/reporting.html)

## Facilitator notes
- Don't reveal the number of bugs per function. Let pairs find them.
- If pairs finish early, point them at the stretch coverage question. Seeing high coverage on buggy code is a memorable lesson.
- Session 07 builds directly on this with PySpark, so make sure everyone can run pytest before they leave.
