# Session 02: The working environment and version control

| | |
|---|---|
| Module | 1: Foundations of building |
| Wiki skill(s) | Programming & build: IDEs, command line, git/version control, RAP |
| HEO target level | Working |
| Duration | 60 min (~35 concept / ~20 exercise / ~5 Q&A) |
| Follow-up | **Exercise** (in session) |
| Prerequisites | Session 01. Laptop with git and Python 3.11 installed |
| Dataset | None. The exercise script builds a practice git repo |

## Learning outcomes
By the end of the session, participants can:
1. Use the essential Linux shell commands they'll meet in a CML terminal (and on GCP).
2. Explain why virtual environments and pinned dependencies matter, and create one.
3. Describe git's model (working tree → staging area → commits → branches → remote) and use the daily workflow.
4. Resolve a merge conflict and raise a merge/pull request that's easy to review.
5. Know what must **never** be committed: data, credentials, outputs.

## Concept outline
| Min | Section |
|---|---|
| 0–7 | The command line: why it matters, essential commands, Windows vs Linux |
| 7–12 | IDEs and where code runs |
| 12–18 | Virtual environments and dependencies |
| 18–28 | Git: the model, daily workflow, branches, conflicts |
| 28–32 | Merge requests and code review etiquette; what never to commit |
| 32–35 | CDP today → GCP tomorrow + summary |
| 35–55 | Exercise: branch, commit, conflict, resolve |
| 55–60 | Q&A |

## Exercise
- **Task:** run a script that creates a practice repo where two "colleagues" have changed the same file. Then make your own branch, merge, resolve the conflict, and write a merge request description.
- **Starting files:** `exercise/README.md`, `exercise/make_practice_repo.py`
- **Done when:** `main` contains both changes, merged correctly, with a clean `git log --graph` and no conflict markers left.
- **Stretch:** do it again with `git rebase` instead of `git merge` and compare the histories.
- **Facilitator answer:** `solutions/README.md`

## Further learning (from the wiki)
- [Learning Hub: Command line basics](https://learninghub.ons.gov.uk/course/view.php?id=1166) and the [Linux vs Windows commands list](https://www.geeksforgeeks.org/linux-vs-windows-commands/)
- [Learning Hub: Introduction to Git](https://learninghub.ons.gov.uk/course/view.php?id=1165)
- [Make Git Happen (presentation)](https://josephcrispell.github.io/standalone/gov-uk-rap-materials_make-git-happen.html)
- [Git cheat sheet](https://education.github.com/git-cheat-sheet-education.pdf) · [GitHub Skills](https://skills.github.com/) · [Oh My Git](https://ohmygit.org/) (off-network laptops only)
- [ASAP getting-started guide](https://gitlab-app-l-01/ASAP/coding-getting-started-guide/-/wikis/home) (internal, VPN)
- [Learning Hub: Introduction to RAP](https://learninghub.ons.gov.uk/course/view.php?id=1236)

## Facilitator notes
- Check before the session that everyone can run `git --version` and `python --version`. Setup problems eat into exercise time.
- The exercise runs locally, so nobody needs GitLab access. If your team has a sandbox GitLab project, the stretch can include pushing a branch and opening a real MR.
- Spend time on "never commit data or secrets". It's the most important ONS-specific point in the session.
