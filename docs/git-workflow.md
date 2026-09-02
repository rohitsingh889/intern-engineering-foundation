# Git Workflow

## 1. Clone

The repository was cloned from GitHub to the local machine.

```bash
git clone <repo-url>
```

Cloning creates a local copy of the remote repository so that development can be performed on the local machine.

---

## 2. Create a Feature Branch

A separate feature branch was created so development could be done without directly changing the `main` branch.

```bash
git switch -c feature/day2-profile
```

The alternative older command is:

```bash
git checkout -b feature/day2-profile
```

The `-c` option with `git switch` and the `-b` option with `git checkout` create a new branch.

---

## 3. Check Status

`git status` was used to check the current branch and identify modified, staged, or untracked files.

```bash
git status
```

This helps the developer understand the current state of the working directory before making or committing changes.

---

## 4. Pull / Fetch Latest Changes

Before starting development, the latest information from the remote repository can be obtained.

### Pull

`git pull` downloads changes from the remote repository and integrates them into the current branch.

```bash
git pull origin <branch-name>
```

### Fetch

`git fetch` downloads information about changes from the remote repository without automatically merging them into the current branch.

```bash
git fetch origin
```

`fetch` is useful when the developer wants to inspect remote changes before integrating them.

---

## 5. Make Changes

The required files are created or modified in the working directory.

For example:

- Add intern profile information
- Add profile functionality
- Add tests
- Update README
- Add Git documentation

---

## 6. Add

`git add` stages the required changes so they can be included in the next commit.

```bash
git add .
```

The staging area allows the developer to select which changes should be included in a commit.

---

## 7. Commit

`git commit` saves the staged changes as a snapshot in the local Git history.

```bash
git commit -m "Add intern profile data"
```

Commit messages should be meaningful and clearly describe the change.

Examples:

```text
feat: add intern profile data
test: add intern profile tests
docs: update Git workflow
```

---

## 8. Pull / Fetch Before Push

Before pushing the local commits, the developer should check whether the remote branch has received new changes.

```bash
git fetch origin
```

If the remote branch contains changes that need to be integrated, they can be pulled:

```bash
git pull origin <branch-name>
```

This helps reduce the possibility of conflicts and ensures the local branch is synchronized with the remote branch before pushing.

---

## 9. Push

The feature branch is pushed to the remote GitHub repository.

```bash
git push -u origin feature/day2-profile
```

`push` uploads the local commits to the remote repository.

---

## 10. Pull Request

A Pull Request (PR) is created to propose merging the feature branch into the `main` branch.

```text
feature/day2-profile → main
```

The Pull Request allows team members to review the changes before they are merged into the main branch.

---

## 11. Code Review

Code review is the process of examining the changes in a Pull Request.

Reviewers check the code for:

- Correctness
- Readability
- Maintainability
- Security
- Coding standards
- Possible bugs

Reviewers can provide comments or request changes before the Pull Request is merged.

---

## 12. Merge

After the Pull Request is reviewed and approved, the feature branch can be merged into `main`.

Using Git commands:

```bash
git switch main
git pull origin main
git merge feature/day2-profile
git push origin main
```

`git merge` combines the changes from the feature branch into the target branch.

---

## 13. Merge Conflict

A merge conflict occurs when Git cannot automatically combine changes from different branches.

The developer must manually resolve the conflicting sections and then stage and commit the resolution.

Git or development tools may provide options such as:

- Accept Current Change
- Accept Incoming Change
- Accept Both Changes

The correct option depends on which version of the code should be retained.

After resolving the conflict:

```bash
git add .
git commit -m "Resolve merge conflict"
```

---

## 14. .gitignore

`.gitignore` specifies files and directories that should not be tracked by Git.

For example:

```gitignore
__pycache__/
*.pyc
venv/
.venv/
.env
```

These files are commonly excluded because they are generated files, local environments, or files containing environment-specific configuration.

---

## 15. README

The `README.md` file provides important information about the project, such as:

- Project purpose
- Project structure
- Setup instructions
- Usage
- Testing
- Git workflow

A clear README helps other developers understand and work with the project.

---

# Overall Git Workflow

The overall development workflow followed in this project can be summarized as:

```text
Clone → Branch → Checkout/Switch → Pull/Fetch → Add → Commit
       → Pull/Fetch → Push → Pull Request → Code Review → Merge
```

This workflow helps developers work safely in feature branches, keep their local repository synchronized with the remote repository, maintain meaningful Git history, and use Pull Requests and code reviews before integrating changes into `main`.
