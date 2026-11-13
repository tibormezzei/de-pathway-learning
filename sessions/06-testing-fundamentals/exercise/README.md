# Exercise: test from the spec, find the bugs

**Time:** 20 minutes · **Work:** in pairs

`survey_utils.py` has four small functions used across a survey pipeline. **The docstrings are the specification.** Some of the implementations don't match them.

## Task

1. Run the starter tests (they pass):
   ```bash
   cd sessions/06-testing-fundamentals
   python -m pytest -v exercise
   ```
2. Read each docstring and add tests to `exercise/test_survey_utils.py` until you've covered the whole specification. Use:
   - `@pytest.mark.parametrize` for many input/output cases
   - `pytest.raises(...)` for the error cases
   - **boundary values**: the edges where behaviour changes
3. When a test fails, decide: **is the test wrong, or the code?** (The docstring is the judge.)
4. Fix the bugs in `survey_utils.py` until everything passes.

There are **4 bugs**. Some are obvious once tested and one is quite sneaky.

## Useful commands

```bash
python -m pytest exercise -v                 # verbose: one line per test
python -m pytest exercise -x                 # stop at the first failure
python -m pytest exercise -k age_band        # only tests whose name matches
python -m pytest exercise --lf               # re-run only the last failures
```

## Stretch
- Measure coverage: `pip install pytest-cov`, then `python -m pytest exercise --cov=survey_utils --cov-report=term-missing`. Is 100% coverage the same as "no bugs"? (Hint: what coverage did the buggy code already have?)
- Add `--doctest-modules` and see what happens to the examples in the docstring.
