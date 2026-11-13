# Homework: refactor a messy pipeline

**Time:** about 1.5–2 hours · **Due:** start of session 04 (bring your code to show a neighbour)

`messy_pipeline.py` calculates survey response rates by region and month. It works, but nobody wants to maintain it. Your job is to **refactor** it: improve the structure **without changing what it outputs**.

## Setup

```bash
cd homework
python messy_pipeline.py          # runs the original; writes ../output/response_rates.csv
```

## Task

Turn the script into a small package, for example:

```
survey_pipeline/
├── __init__.py
├── __main__.py      # entry point: python -m survey_pipeline --input ... --output ...
├── config.py        # business rules (age limits, aliases, date formats...)
├── clean.py         # cleaning functions
└── metrics.py       # response-rate calculation
```

Aim for:
- [ ] **Functions** that each do one thing, take inputs as parameters and return outputs, with no globals
- [ ] **No hard-coded paths**: input and output come from the command line
- [ ] **Business rules in config**, not magic numbers buried in the logic
- [ ] **Docstrings** and **type hints** on every function
- [ ] No bare `except:`, no commented-out code, no debugging `print`s (use `logging` if you want output)
- [ ] Loops over DataFrame rows replaced with vectorised pandas operations
- [ ] PEP 8 naming (`cleaned_df`, not `df3`)

## Check you haven't changed behaviour

```bash
python -m survey_pipeline --input ../data/survey_responses.csv --output ../output/response_rates.csv
python check_output.py ../output/response_rates.csv
```

You must see `PASS`. If not, your refactor changed the results, so find out why.

## Reflect (write 3–5 sentences)
1. Which change made the biggest difference to readability?
2. Did you spot anything in the original that looks like a **bug or questionable business rule**? (Keep it in your refactor so `check_output.py` still passes, but write it down. Spotting these is part of the job.)
3. Which function would you write a test for first, and why?

## Stretch
- Write 3 or more pytest tests for your cleaning functions (a preview of session 06).
- Run a formatter and linter over your code (`pip install ruff`, then `ruff format .` and `ruff check .`) and look at what it changes.
