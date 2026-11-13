# Exercise: branch, commit, conflict, resolve

**Time:** 20 minutes · **Work:** on your own, helping your neighbour when you're done

You've joined a team maintaining a cleaning config for survey responses. Two colleagues have changed the same file in different ways, and you need to combine their work and add your own change.

## 1. Create the practice repo

If you've never used git on this machine, set your identity first:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.name@ons.gov.uk"
```

```bash
python make_practice_repo.py
cd git-practice
```

## 2. Look around

```bash
git log --oneline --graph --all
git branch -a
cat cleaning_config.py
git diff main feature/colleague-b
```

❓ What did each colleague change? Which lines did they **both** change?

## 3. Make your own change on a branch

```bash
git switch -c feature/max-age
```

Change `MAX_AGE` from `120` to `110`, then:

```bash
git status
git diff
git add cleaning_config.py
git commit -m "Lower maximum plausible age to 110"
git switch main
git merge feature/max-age
```

❓ Why did this merge go through without a conflict?

## 4. Merge colleague B's branch

```bash
git merge feature/colleague-b
```

You'll get a **conflict**. Open `cleaning_config.py` and resolve it. The team has agreed that the final config should have:
- the **new minimum age** (18)
- **all** the regions both colleagues added
- your **new maximum age**
- the **new dedup columns**

Then:

```bash
git add cleaning_config.py
git commit            # accept the default merge message, or write a better one
git log --oneline --graph --all
```

Check there are no `<<<<<<<`, `=======` or `>>>>>>>` markers left:

```bash
grep -n "<<<<<<<\|=======\|>>>>>>>" cleaning_config.py   # should print nothing
python -c "import cleaning_config as c; print(c.MIN_AGE, c.MAX_AGE, c.VALID_REGIONS, c.DROP_DUPLICATES_ON)"
```

## 5. Write a merge request description

In a text file or on paper, write the MR description you'd submit for **colleague B's** change:
- **What** changed
- **Why**
- **How it was tested** (or how it should be)
- Anything the reviewer should look at closely

## Stretch: rebase instead of merge

```bash
cd .. && rm -rf git-practice && python make_practice_repo.py && cd git-practice
git switch feature/colleague-b
git rebase main            # resolve the conflict, then: git add ... && git rebase --continue
git switch main && git merge feature/colleague-b
git log --oneline --graph --all
```

❓ How does the history differ from the merge version? When would a team prefer each?
