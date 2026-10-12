# Git & GitHub Guide

Notes from setting up this repo. Run all git commands from the `installation` folder (that is where `.git` lives).

## 1. Key ideas

| Term | Meaning |
|---|---|
| Repository (repo) | A folder tracked by git (has a hidden `.git` folder). |
| Commit | A saved snapshot of your changes, with a message. |
| Branch | A separate line of work. It is just a pointer to a commit, not a copy of files. |
| `main` | The stable branch that holds the working version of the code. |
| Remote / `origin` | The copy of the repo on GitHub. |
| Clone | A full copy of a repo on your computer. |
| Fork | Your own copy of someone else's repo on your GitHub account. |
| Pull request (PR) | A request on GitHub to merge one branch into another. |

Local and GitHub are two separate places. Commits and merges change your PC only. `git push` updates GitHub. `git pull` updates your PC from GitHub.

## 2. One-time setup

```
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global core.pager cat        # stops the (END) pager screen
```

Start a new repo and connect it to GitHub:

```
git init
git remote add origin https://github.com/<username>/<repo>.git
git branch -M main
```

Or copy an existing repo from GitHub:

```
git clone https://github.com/<username>/<repo>.git
```

## 3. Everyday workflow

| Command | Meaning |
|---|---|
| `git status` | Shows changed, new, and staged files. Safe to run any time. |
| `git add .` | Stages all changes for the next commit. |
| `git add file.py` | Stages just one file. |
| `git commit -m "message"` | Saves the staged changes as a commit (local only). |
| `git push` | Uploads your commits to GitHub. |
| `git pull` | Downloads new commits from GitHub and merges them. |

Typical routine:

```
git add .
git commit -m "Add weather chart"
git push
```

First push of a branch needs `-u` to link it to GitHub: `git push -u origin main`.

## 4. Looking around

```
git log --oneline       # list of past commits
git diff                # unstaged line changes
git diff --staged       # staged line changes
git show --stat HEAD    # what the latest commit changed
git branch              # list local branches (* = current)
git remote -v           # show the GitHub URL
```

Press `q` to leave a pager screen.

## 5. Branches

```
git checkout -b my-branch        # create a branch and switch to it
git switch -c my-branch          # same thing, newer syntax
git checkout main                # switch to main
git branch -d my-branch          # delete a merged local branch
git push -u origin my-branch     # push the branch to GitHub (first time)
```

- A new branch starts with everything from the branch it was created on.
- Switching branches swaps the files in your folder to match that branch.
- Changes on a branch do not appear in `main`, and changes in `main` do not appear in the branch, until you merge.

## 6. Merging

Merge a branch into `main` (locally):

```
git checkout main
git merge my-branch
git push
```

Bring the latest `main` into your branch:

```
git checkout my-branch
git merge main
```

- Merging adds only the branch's changes. `main` is not replaced.
- Fast-forward: if `main` has not moved since you branched, git just moves `main` forward. No new commit is made.
- Merge conflict: if two branches changed the same lines, git marks the file. Edit it to keep the right version, then `git add .` and `git commit`.

### Why push `main` again after merging?

Pushing a branch updates only that branch on GitHub. A local merge changes only your PC's `main`. So you push `main` too. If the branch was already pushed, git uploads no new data (`Total 0`). It only moves GitHub's `main` label (`bad04b7..6f989f1  main -> main`).

| Where you merge | Then run |
|---|---|
| Locally with `git merge` | `git push` |
| On GitHub (PR Merge button) | `git pull` |

## 7. Reading push output

```
Total 0 (delta 0), reused 0 ...      <- how much NEW data was uploaded
bad04b7..6f989f1  main -> main       <- GitHub's main moved to the new commit
```

- `Total 0` means GitHub already had the data, often because you pushed the branch first. It is not an error.
- Nonzero `Total` means new data was uploaded.
- An error shows `rejected` or `fatal:`.

## 8. Team workflow (feature branches)

1. Update: `git checkout main` then `git pull`
2. Branch: `git checkout -b feature-name`
3. Work: `git add .` and `git commit -m "..."` (repeat)
4. Push: `git push -u origin feature-name`
5. On GitHub, open a pull request into `main`.
6. Teammates review. Fix things by committing and pushing to the same branch.
7. Click **Merge pull request** on GitHub.
8. Update your local copy: `git checkout main` then `git pull`

## 9. Creating a pull request on GitHub

1. Push your branch. The output prints a link like `https://github.com/<user>/<repo>/pull/new/<branch>`. Open it, or click **Compare & pull request** on the repo page.
2. Set **base** = `main` and **compare** = your branch.
3. Add a title and description, then click **Create pull request**.
4. Check the **Files changed** tab. Reviewers can comment on lines.
5. Click **Merge pull request**, then **Confirm merge**. Optionally delete the branch.
6. Locally: `git checkout main` then `git pull`.

## 10. Contributing to someone else's repo

If you have no write access:

1. Click **Fork** on their repo page.
2. `git clone` your fork, make changes, `git push` (this goes to your fork).
3. On GitHub, click **Contribute → Open pull request**.
4. The owner reviews and chooses to merge or not.

Someone cloning your repo cannot affect it. Only people you add under Settings → Collaborators can push to it, and you can protect `main` under Settings → Branches so changes need a reviewed PR.

## 11. `.gitignore`

Lists files git should not track. This repo ignores:

```
.venv/
venv/
.env
__pycache__/
*.pyc
.DS_Store
```

- Never commit virtual environments (`venv/`), they are huge. Share dependencies with `requirements.txt` instead (`pip freeze > requirements.txt`).
- Never commit secrets such as `.env` files or API keys.
- `.gitignore` does not affect files already tracked. Untrack them first (keeps the file on disk):

```
git rm -r --cached venv
git commit -m "Stop tracking venv"
```

## 12. Fixing common problems

| Problem | Fix |
|---|---|
| `fatal: not a git repository` | You are in the wrong folder. `cd` to `installation`. |
| `'orgin' does not appear to be a git repository` | Typo. The remote is spelled `origin`. |
| Stuck on `(END)` / `~` lines | Press `q`. Set `git config --global core.pager cat`. |
| Push is slow or times out | Check you did not commit `venv/` or other huge folders. |
| Push `rejected` (non-fast-forward) | GitHub has newer commits. Run `git pull`, then `git push`. |
| Wrong commit message on last commit (not pushed) | `git commit --amend -m "new message"` |
| Undo staging a file | `git restore --staged file.py` |
| Discard unsaved edits to a file | `git restore file.py` (this cannot be undone) |
| Check what is on GitHub vs local | `git status` and `git log --oneline` |

Avoid `git push --force` and `git reset --hard` unless you are sure. They can destroy work, especially on shared branches.
