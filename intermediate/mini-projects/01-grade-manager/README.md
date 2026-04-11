# Mini-Project 01 — Student Grade Manager

## Description

A terminal-based grade management system. Manages students, subjects, and grades with full JSON persistence and CSV report export.

## Concepts Used

| Concept | Where |
|---|---|
| `01-oop` | `Student`, `Subject`, `GradeBook` classes, custom exceptions |
| `03-file-handling` | JSON persistence, CSV report export |
| `04-error-handling` | `StudentNotFoundError`, `InvalidGradeError`, input validation |
| `02-modules-packages` | `json`, `csv`, `datetime`, `os` |

## How to Run

```bash
python main.py
```

Data is saved automatically to `gradebook.json` and loaded on startup.

## Features

- Add / remove students and subjects
- Record grades (0.0–10.0) with date and description
- View grade history per student per subject
- Compute average, highest, lowest grade per student
- Class ranking (sorted by overall average)
- Pass/fail status (cutoff: 6.0)
- Export full class report to `report.csv`
- JSON persistence (auto-save on exit, auto-load on start)

## Custom Exceptions

| Exception | When |
|---|---|
| `StudentNotFoundError` | Student name not in gradebook |
| `SubjectNotFoundError` | Subject not registered |
| `InvalidGradeError` | Grade outside 0.0–10.0 range |
| `DuplicateError` | Adding a student/subject that already exists |

## Example Output

```
=============================
     GRADE MANAGER
=============================
[1] Add student
[2] Add subject
[3] Record grade
[4] View student report
[5] Class ranking
[6] Export CSV report
[0] Save & Exit

> 5

=== CLASS RANKING ===
1. Alice    avg: 8.7  ✓ Pass
2. Carol    avg: 7.2  ✓ Pass
3. Bob      avg: 5.8  ✗ Fail
```
