---
marp: true
theme: default
paginate: true
header: "DE Learning Sessions · 02"
footer: "The working environment and version control"
---

<!-- _class: lead -->
<!-- _header: "" -->
<!-- _footer: "" -->

# The working environment
## and version control

Session 02 · Module 1: Foundations of building

---

## Today

1. The command line
2. IDEs and where code runs
3. Virtual environments and dependencies
4. Git: the model and the daily workflow
5. Merge requests, code review, and what never to commit
6. **Exercise:** branch, commit, conflict, resolve

---

## Why the command line?

- CML terminals, Dataproc clusters and Cloud Shell are all **Linux shells**, with no Windows Explorer.
- Git, Python environments and Spark jobs are all started from a shell.
- Scripts in a shell are **repeatable**. Clicking through a UI isn't.

You don't need to be a shell wizard. About 15 commands cover nearly everything.

---

## The essential commands

| Linux / bash | Windows (cmd) | Does |
|---|---|---|
| `pwd` | `cd` | Where am I? |
| `ls -la` | `dir` | What's here? |
| `cd path` / `cd ..` | `cd path` | Move around |
| `mkdir -p a/b` | `mkdir a\b` | Make folders |
| `cp`, `mv`, `rm` | `copy`, `move`, `del` | Copy / move / delete (**no recycle bin!**) |
| `cat`, `head`, `less` | `type`, `more` | Look inside a file |
| `grep "text" file` | `findstr` | Search in files |
| `cmd1 \| cmd2` | `cmd1 \| cmd2` | Pipe output into the next command |

```bash
head -5 responses.csv          # peek at a file without opening it
wc -l responses.csv            # how many rows?
grep -c "ERROR" job.log        # how many errors?
```

<!--
Point out that rm is permanent, and that paths use / on Linux and \ on Windows. Git Bash gives you Linux commands on a Windows laptop.
-->

---

## IDEs and where code runs

| Tool | Good for | Watch out for |
|---|---|---|
| **VS Code** | Packages, tests, git integration, linting | Needs a service desk request on ONS laptops |
| **Jupyter / CML sessions** | Exploring data, quick checks | Hidden state, running cells out of order, hard to test and review |
| **Spyder** | Python with a variable explorer | Less common for pipeline work |

**Rule of thumb:** explore in notebooks, **build in `.py` files**.
Pipelines that go to production live in version-controlled modules, not notebooks.

---

## Virtual environments: why?

Without them:
> "It works on my machine."
> Project A needs `pandas 1.5`, project B needs `pandas 2.2`. 💥

A **virtual environment** is an isolated set of packages for **one project**.

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

---

## Pin your dependencies

```text
# requirements.txt
pandas==2.2.3
pyspark==3.5.9
pytest==8.3.4
```

- `==` pins an **exact** version, so everyone gets the same environment.
- Unpinned (`pandas`) means "whatever's latest today", which isn't reproducible.
- Keep the PySpark version the **same as the cluster's Spark version**.
- Commit `requirements.txt`, and **never commit `.venv/`**.

Reproducible environment + version-controlled code = **RAP** (Reproducible Analytical Pipeline).

---

## Git: the mental model

```
 working tree ──git add──▶ staging area ──git commit──▶ local repo ──git push──▶ remote
  (your files)              (next commit)                (history)               (GitLab/GitHub)
                                                              ◀──────git pull────────
```

- A **commit** is a snapshot of the whole project, with a message and an author.
- A **branch** is a movable label pointing at a commit.
- The **remote** is the shared copy everyone pushes to and pulls from.

---

## The daily workflow

```bash
git switch main && git pull                 # start from the latest main
git switch -c feature/dedup-responses       # new branch for your change

# ... edit files ...
git status                                  # what changed?
git diff                                    # how did it change?
git add src/dedup.py tests/test_dedup.py    # stage specific files
git commit -m "Deduplicate responses on case_id and submission time"

git push -u origin feature/dedup-responses  # share it, then open a merge request
```

**Small branches, small commits, clear messages.**

---

## Good commit messages

❌ `fix` · `changes` · `wip` · `asdf`

✅ `Handle null postcodes in address cleaning`
✅ `Add test for duplicate submissions on same day`

- Describe **what the change does**, in the imperative mood ("Add", "Fix", "Remove").
- One logical change per commit. If you need the word "and", consider splitting it.
- Someone reading `git log` in a year should understand the history.

---

## Merge conflicts

Two branches changed **the same lines**. Git can't choose, so it asks you:

```text
<<<<<<< HEAD
MIN_AGE = 16
=======
MIN_AGE = 18
>>>>>>> feature/age-rules
```

1. Open the file and decide what the code **should** be. It may need parts of both versions.
2. Delete the markers.
3. `git add` the file, then `git commit` (or `git merge --continue`).
4. **Run the tests.** A merge that git accepts can still be wrong.

Conflicts are normal. Pull from `main` often to keep them small.

---

## Merge requests and code review

A **merge request** (GitLab) or **pull request** (GitHub) asks for a branch to be merged into `main` after review.

**As the author**
- Keep it small, ideally reviewable in about 15 minutes.
- Description: *what* changed, *why*, *how you tested it*.
- Review your own diff first.

**As the reviewer**
- Comment on the code, not the person. Ask questions rather than giving orders.
- Check correctness, tests and readability before style.
- Approve when it's good enough. It doesn't need to be how you'd have written it.

---

## ⚠️ Never commit

- **Data**: real records, extracts, samples of real data. Not even "just for testing".
- **Credentials**: passwords, tokens, keys, connection strings.
- **Outputs**: generated files, logs, `.parquet` results.
- **Environments**: `.venv/`, `__pycache__/`.

```gitignore
# .gitignore
.venv/
__pycache__/
data/
*.parquet
*.csv
.env
```

Git keeps **everything forever**. Deleting a file in a later commit doesn't remove it from the history.

<!--
If something sensitive is committed, tell your lead straight away. It isn't fixed just by deleting the file.
-->

---

## CDP today → GCP tomorrow

| | CDP today | GCP tomorrow |
|---|---|---|
| Git host | **GitLab**: merge requests | **GitHub**: pull requests |
| CI | GitLab CI (`.gitlab-ci.yml`) | GitHub Actions (`.github/workflows/`) |
| Shell | CML session terminal | Cloud Shell, Dataproc / Workbench terminals |
| Environment | Packages installed in the CML project or session | Packages baked into **Dataproc images / init actions** or containers |
| Secrets | Platform-managed, team conventions | **Secret Manager** + IAM service accounts |

**Carries over unchanged:** the shell, git commands, branching, code review, `.gitignore` discipline.
**Really changes:** environments need to be **fully scripted**, because ephemeral clusters don't remember what you installed by hand.

---

## Summary

- About 15 shell commands get you a long way, and the platforms you'll use are Linux.
- **Explore in notebooks, build in `.py` files.**
- One project → one **virtual environment** → **pinned** `requirements.txt`.
- Git: **working tree → staging → commit → push**, on short-lived branches.
- Small merge requests, kind reviews, **never commit data or secrets**.

**Next session:** writing maintainable Python for data.
