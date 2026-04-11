# ============================================================
# intermediate/03-file-handling/solutions/02-medium-solution.py
# ============================================================

import csv
import json
import os
from pathlib import Path
from datetime import datetime

SOLUTIONS_DIR = Path(os.path.dirname(os.path.abspath(__file__)))


# ----------------------------------------------------------
# Exercise 1 — Write and Read a CSV file
# ----------------------------------------------------------
# APPROACH: csv.writer for writing rows, csv.DictReader for
# reading back with named column access. Status based on grade int.

csv_path = SOLUTIONS_DIR / "students.csv"

rows = [
    {"name": "Alice", "grade": 92, "city": "São Paulo"},
    {"name": "Bob",   "grade": 78, "city": "Rio de Janeiro"},
    {"name": "Carol", "grade": 85, "city": "Curitiba"},
    {"name": "Dave",  "grade": 91, "city": "Belo Horizonte"},
    {"name": "Eve",   "grade": 67, "city": "Fortaleza"},
]

with open(csv_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "grade", "city"])
    writer.writeheader()
    writer.writerows(rows)

print("--- Student grades ---")
with open(csv_path, "r", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        grade = int(row["grade"])
        status = "Pass" if grade >= 70 else "Fail"
        print(f"  {row['name']:<8} | {grade:>2} | {status}")


# ----------------------------------------------------------
# Exercise 2 — JSON Config File
# ----------------------------------------------------------
# APPROACH: Write default → load → mutate → write → reload → print.

settings_path = SOLUTIONS_DIR / "settings.json"

default = {
    "theme": "light",
    "font_size": 12,
    "language": "pt-BR",
    "autosave": True,
    "recent_files": [],
}

settings_path.write_text(json.dumps(default, indent=2), encoding="utf-8")

settings = json.loads(settings_path.read_text(encoding="utf-8"))
settings["theme"] = "dark"
settings["font_size"] = 14
settings["recent_files"].append("notes.txt")

settings_path.write_text(json.dumps(settings, indent=2), encoding="utf-8")

final = json.loads(settings_path.read_text(encoding="utf-8"))
print("\n--- Final settings ---")
for key, value in final.items():
    print(f"  {key:<12}: {value}")


# ----------------------------------------------------------
# Exercise 3 — CSV Statistics Report
# ----------------------------------------------------------
# APPROACH: Re-read the students.csv written in Exercise 1.
# Accumulate grades into a list, then compute all stats in one pass.

report_path = SOLUTIONS_DIR / "report.txt"

with open(csv_path, "r", encoding="utf-8") as f:
    students = [(r["name"], int(r["grade"])) for r in csv.DictReader(f)]

grades = [g for _, g in students]
avg    = sum(grades) / len(grades)
top    = max(students, key=lambda t: t[1])
low    = min(students, key=lambda t: t[1])
passed = sum(1 for g in grades if g >= 70)

report = (
    "=== CLASS REPORT ===\n"
    f"Students     : {len(students)}\n"
    f"Average grade: {avg:.1f}\n"
    f"Highest      : {top[0]} — {top[1]}\n"
    f"Lowest       : {low[0]} — {low[1]}\n"
    f"Passed       : {passed} / {len(students)}\n"
)

report_path.write_text(report, encoding="utf-8")
print("\n" + report, end="")


# ----------------------------------------------------------
# Exercise 4 — Log File
# ----------------------------------------------------------
# APPROACH: Append-mode open ensures entries accumulate.
# Filter ERROR lines by simple string membership when reading.

log_path = SOLUTIONS_DIR / "app.log"
log_path.unlink(missing_ok=True)  # start fresh each run

def log(message, level="INFO"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] [{level}] {message}\n")

log("Application started")
log("Loading configuration")
log("Disk space low", level="WARNING")
log("Something went wrong!", level="ERROR")
log("Retrying operation", level="WARNING")

print("--- ERROR lines ---")
for line in log_path.read_text(encoding="utf-8").splitlines():
    if "ERROR" in line:
        print(f"  {line}")


# ----------------------------------------------------------
# Exercise 5 — Count files by extension with pathlib
# ----------------------------------------------------------
# APPROACH: project root is two levels above SOLUTIONS_DIR.
# Path.rglob("*.ext") walks recursively. len(list(...)) counts.

project_root = SOLUTIONS_DIR.parent.parent.parent  # solutions/ → exercises' parent → module → intermediate → root

py_count    = len(list(project_root.rglob("*.py")))
md_count    = len(list(project_root.rglob("*.md")))
ipynb_count = len(list(project_root.rglob("*.ipynb")))

print("\n--- File counts ---")
print(f"  .py files   : {py_count}")
print(f"  .md files   : {md_count}")
print(f"  .ipynb files: {ipynb_count}")

# Cleanup generated files
for p in [csv_path, settings_path, report_path, log_path]:
    p.unlink(missing_ok=True)
