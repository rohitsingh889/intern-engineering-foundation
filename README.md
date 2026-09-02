# Intern Engineering Foundation

This repository contains my Day 2 – Git & Version Control assignment for the Project Nexelis Intern-to-Engineer Bootcamp.

![Git and GitHub](https://miro.medium.com/v2/resize:fit:720/format:webp/1*qwFrTMnFkcd3U9rFKwwacw.png)

## Objective

The objective of this project is to demonstrate basic Git and version-control practices, including feature branches, meaningful commits, pushing changes, testing, documentation, and Pull Requests.

## Project Structure

```text
intern-engineering-foundation/
├── README.md
├── .gitignore
├── docs/
│   └── git-workflow.md
├── src/
│   ├── __init__.py
│   └── profile.py
└── tests/
    ├── __init__.py
    ├── test_profile.py
    └── test_profile2.py
```

## Application

The project contains a simple Python intern profile with:

* Intern name
* Role
* Department
* Skills
* Profile display function

## Testing

The project includes tests to verify that the intern profile data is correct.

Tests can be executed using:

```bash
python3 -m tests.test_profile  and python3 -m tests2.test_profile
```

## Git Workflow

Development was performed using the feature branch:

```text
feature/day2-profile
```

The workflow followed was:

```text
Clone → Branch → Add → Commit → Push → Pull Request → Code Review → Merge
```

The repository demonstrates meaningful commits, feature-branch development, testing, documentation, and Git version-control practices.
