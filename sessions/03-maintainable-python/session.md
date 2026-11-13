# Session 03: Writing maintainable Python for data

| | |
|---|---|
| Module | 1: Foundations of building |
| Wiki skill(s) | Programming & build: concepts (PEP 8/20, OOP vs FP), packaging, ons-python-template |
| HEO target level | Working |
| Duration | 60 min (~35 concept / ~20 homework briefing + live refactor demo / ~5 Q&A) |
| Follow-up | **Homework** (refactoring takes longer than 20 minutes) |
| Prerequisites | Session 02 (venv set up from `requirements.txt`) |
| Dataset | `data/survey_responses.csv`: 625 synthetic survey rows, regenerate with `data/make_data.py` |

## Learning outcomes
By the end of the session, participants can:
1. Apply PEP 8 naming and layout, and explain the main ideas of PEP 20.
2. Break a script into small, single-purpose, testable functions with docstrings and type hints.
3. Organise code into modules and a package with a clear entry point, keeping config separate from logic.
4. Decide when a class helps and when plain functions are better for data work.
5. Refactor safely by checking that behaviour hasn't changed.

## Concept outline
| Min | Section |
|---|---|
| 0–4 | Why maintainability: code is read far more than it's written |
| 4–9 | PEP 8 and PEP 20, plus formatters and linters |
| 9–17 | Good functions: one job, parameters in, values out, no globals, docstrings, type hints |
| 17–22 | Vectorise instead of looping |
| 22–27 | Modules, packages, project layout, config, entry points |
| 27–31 | Functions vs classes for data work |
| 31–35 | Refactoring safely + CDP today → GCP tomorrow |
| 35–55 | Homework briefing + **live demo**: refactor the date-parsing block together |
| 55–60 | Q&A |

## Homework
- **Task:** refactor `homework/messy_pipeline.py` into a package without changing its output.
- **Starting files:** `homework/README.md`, `homework/messy_pipeline.py`, `homework/check_output.py`
- **Done when:** `check_output.py` prints PASS and the checklist in the README is met.
- **Stretch:** pytest tests, ruff.
- **Reference solution:** `solutions/` (package + tests + a "what changed" table)

## Further learning (from the wiki)
- [PEP 20: The Zen of Python](https://peps.python.org/pep-0020/) · [PEP 8](https://peps.python.org/pep-0008/)
- [YouTube: FP vs OOP](https://www.youtube.com/watch?v=08CWw_VD45w)
- [Learning Hub: Loops and Functions](https://learninghub.ons.gov.uk/course/view.php?id=1222) · [Intro to OOP in Python](https://learninghub.ons.gov.uk/course/view.php?id=567) · [Packaging Code with Python](https://learninghub.ons.gov.uk/course/view.php?id=533)
- [CS50P Week 8: OOP](https://cs50.harvard.edu/python/2022/weeks/8/) · [Python design patterns](https://python-patterns.guide/)
- [ONSdigital/ons-python-template](https://github.com/ONSdigital/ons-python-template)
- [Real Python: documenting Python code](https://realpython.com/documenting-python-code/)

## Facilitator notes
- In the live demo, refactor the triple-nested `try/except` date block into `parse_date()` while the room watches, then run `check_output.py`. It shows the whole refactoring loop in about 5 minutes.
- Start the next session by having people swap homework with a neighbour for 5 minutes as a mini code review, which reinforces session 02.
- The homework's reflection question 2 (spotting questionable business rules) matters more than it looks. Raise it in the next session.
