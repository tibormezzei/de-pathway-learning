"""Create a local practice git repo for the session 02 exercise.

Usage:
    python make_practice_repo.py [target_dir]

It creates a repo (default ./git-practice) with:
- main: a small cleaning config, plus a later commit from "colleague A"
- feature/colleague-b: a branch from "colleague B" that changes the same lines

Merging feature/colleague-b into main produces a conflict for you to resolve.
"""

import subprocess
import sys
from pathlib import Path

CONFIG_V1 = '''"""Cleaning rules for survey responses."""

MIN_AGE = 16
MAX_AGE = 120
VALID_REGIONS = ["North", "South", "East", "West"]
DROP_DUPLICATES_ON = ["case_id"]
'''

# Colleague A (on main): Wales and Scotland added, age rule unchanged
CONFIG_A = CONFIG_V1.replace(
    'VALID_REGIONS = ["North", "South", "East", "West"]',
    'VALID_REGIONS = ["North", "South", "East", "West", "Wales", "Scotland"]',
)

# Colleague B (on a branch): new age rule, and the same list line edited differently
CONFIG_B = CONFIG_V1.replace("MIN_AGE = 16", "MIN_AGE = 18").replace(
    'VALID_REGIONS = ["North", "South", "East", "West"]',
    'VALID_REGIONS = ["North", "South", "East", "West", "Northern Ireland"]',
).replace(
    'DROP_DUPLICATES_ON = ["case_id"]',
    'DROP_DUPLICATES_ON = ["case_id", "submitted_at"]',
)

README = "# Survey cleaning\n\nPractice repo for session 02.\n"
GITIGNORE = ".venv/\n__pycache__/\ndata/\n*.csv\n*.parquet\n.env\n"


def git(*args: str, cwd: Path) -> None:
    subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True)


def commit(cwd: Path, message: str, author: str) -> None:
    git("add", "-A", cwd=cwd)
    git(
        "-c", f"user.name={author}",
        "-c", f"user.email={author.lower().replace(' ', '.')}@example.com",
        "commit", "-m", message,
        cwd=cwd,
    )


def main() -> None:
    target = Path(sys.argv[1] if len(sys.argv) > 1 else "git-practice").resolve()
    if target.exists():
        sys.exit(f"{target} already exists. Delete it or choose another folder.")

    target.mkdir(parents=True)
    git("init", "-b", "main", cwd=target)

    (target / "README.md").write_text(README)
    (target / ".gitignore").write_text(GITIGNORE)
    (target / "cleaning_config.py").write_text(CONFIG_V1)
    commit(target, "Add initial cleaning config", "Team Lead")

    git("switch", "-c", "feature/colleague-b", cwd=target)
    (target / "cleaning_config.py").write_text(CONFIG_B)
    commit(target, "Raise minimum age to 18 and dedupe on submission time", "Colleague B")

    git("switch", "main", cwd=target)
    (target / "cleaning_config.py").write_text(CONFIG_A)
    commit(target, "Add Wales and Scotland to valid regions", "Colleague A")

    print(f"Practice repo created at {target}")
    print("Next: cd into it and follow exercise/README.md, starting at step 2.")


if __name__ == "__main__":
    main()
