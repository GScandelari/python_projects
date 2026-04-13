# Git — Cheat Sheet

## Daily Workflow

```bash
git status                    # what changed?
git diff                      # unstaged changes
git diff --staged             # staged changes

git add file.py               # stage specific file
git add .                     # stage everything (careful with secrets)
git commit -m "Add: feature"  # commit with message
git push origin main          # push to remote
git pull                      # fetch + merge
```

---

## Branching

```bash
git branch                    # list local branches
git branch feature/login      # create branch
git checkout feature/login    # switch to branch
git checkout -b feature/login # create + switch (shortcut)
git switch feature/login      # modern alternative to checkout

git merge feature/login       # merge into current branch
git rebase main               # rebase onto main (linear history)

git branch -d feature/login   # delete merged branch
git branch -D feature/login   # force delete
git push origin --delete feature/login  # delete remote branch
```

---

## Undoing Things

```bash
# Unstage a file (keep changes in working tree)
git restore --staged file.py

# Discard changes in working tree (DESTRUCTIVE)
git restore file.py

# Amend the last commit (before push)
git commit --amend -m "New message"

# Undo last commit, keep changes staged
git reset --soft HEAD~1

# Undo last commit, keep changes unstaged
git reset HEAD~1

# Undo last commit, DISCARD changes (DESTRUCTIVE)
git reset --hard HEAD~1

# Revert a commit (safe — creates new commit)
git revert <commit-hash>

# Unstage all
git reset HEAD
```

---

## Viewing History

```bash
git log                       # full log
git log --oneline             # compact log
git log --oneline --graph     # with branch graph
git log --oneline -10         # last 10
git log --author="Alice"      # by author
git log -- path/to/file       # commits touching a file

git show <hash>               # show a commit's diff
git diff main..feature        # diff between branches
git blame file.py             # who changed each line
```

---

## Remote

```bash
git remote -v                 # list remotes
git remote add origin <url>   # add remote
git fetch origin              # fetch without merging
git pull origin main          # fetch + merge main
git push -u origin feature    # push + set upstream
git push --force-with-lease   # safer force push (checks remote)
```

---

## Stash

```bash
git stash                     # save dirty state
git stash push -m "WIP: login"# stash with name
git stash list                # list stashes
git stash pop                 # apply + drop latest
git stash apply stash@{1}     # apply specific stash
git stash drop stash@{0}      # delete stash
git stash clear               # delete all stashes
```

---

## Tags

```bash
git tag                       # list tags
git tag v1.0.0                # lightweight tag
git tag -a v1.0.0 -m "Release 1.0"  # annotated tag
git push origin v1.0.0        # push single tag
git push origin --tags        # push all tags
git tag -d v1.0.0             # delete local tag
```

---

## .gitignore Patterns

```gitignore
# Folders
node_modules/
__pycache__/
.venv/
dist/
build/

# Files
*.pyc
*.log
*.env
.DS_Store
Thumbs.db

# Secrets
.env
*.pem
credentials.json
secrets.yaml
```

---

## Commit Message Convention

```
<type>: <short summary>

<optional body — what and why, not how>
```

| Type | When to use |
|---|---|
| `Add:` | New feature or file |
| `Update:` | Enhancement to existing feature |
| `Fix:` | Bug fix |
| `Refactor:` | Code change without behaviour change |
| `Remove:` | Deletion |
| `Docs:` | Documentation only |
| `Test:` | Tests only |
| `Chore:` | Build, CI, dependencies |
