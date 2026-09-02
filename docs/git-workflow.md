# Git Workflow

## 1. Clone

The repository was cloned from GitHub to the local machine.

```bash
git clone <repo-url>
```

## 2. Create a Feature Branch

A separate feature branch was created so development could be done without directly changing the `main` branch.

```bash
git switch -c feature/day2-profile or we will also use git checkout -d feature/day2-profile
```

## 3. Check Status

`git status` was used to check the current branch and identify modified or untracked files.

```bash
git status
```

## 4. Add

`git add` was used to stage files before committing them.

```bash
git add .
```

## 5. Commit

`git commit` was used to save meaningful changes in the local Git history.

```bash
git commit -m "Add intern profile data"
```

## 6. Push

The feature branch was pushed to the remote GitHub repository.

```bash
git push -u origin feature/day2-profile
```

## 7. Pull

`git pull` downloads changes from the remote repository and integrates them into the current branch.

```bash
git pull
```

## 8. Fetch

`git fetch` downloads information about changes from the remote repository without merging them into the current branch.

```bash
git fetch
```

## 9. Merge

`git merge` combines changes from one branch into another branch.

```bash
git merge <branch-name>
```

## 10. Pull Request

A Pull Request is created to propose merging the feature branch into `main`. Team members review the changes before the PR is approved and merged.

## 11. Code Review

Code review is the process of checking code for correctness, readability, maintainability, security, and project standards.

## 12. Merge Conflict

A merge conflict occurs when Git cannot automatically combine changes from different branches. The developer must resolve the conflicting changes manually and then commit the resolution. It gives us three options to solve the conflict that is accept current changes, accept incomming changes or keep both changes.

## 13. .gitignore

`.gitignore` specifies files and directories that should not be tracked by Git, such as Python cache files or venv or env files.

## 14. README

The README file provides information about the project's purpose, structure, setup, and usage.
