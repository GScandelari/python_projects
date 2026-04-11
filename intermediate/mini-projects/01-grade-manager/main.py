# ============================================================
# Intermediate Mini-Project 01 — Student Grade Manager
# ============================================================
#
# HOW TO APPROACH THIS PROJECT:
#   1. Read the README.md for the full feature list
#   2. Define the custom exceptions first (they're used everywhere)
#   3. Build Student → Subject → GradeBook in that order
#   4. Implement JSON save/load
#   5. Wire up the menu loop last
#   6. Check solution.py only after you have a working version
#
# SUGGESTED CLASS STRUCTURE:
#
# class StudentNotFoundError(Exception): ...
# class SubjectNotFoundError(Exception): ...
# class InvalidGradeError(Exception): ...
# class DuplicateError(Exception): ...
#
# class Student:
#     def __init__(self, name): ...
#     def add_grade(self, subject, grade, description=""):
#         # stores {subject: [{grade, date, description}, ...]}
#     def average(self, subject=None): ...  # None = overall average
#     def status(self): ...  # "Pass" if average >= 6.0
#     def to_dict(self): ...  # for JSON serialization
#     @classmethod
#     def from_dict(cls, data): ...  # for JSON deserialization
#
# class GradeBook:
#     def __init__(self): ...
#     def add_student(self, name): ...
#     def add_subject(self, name): ...
#     def record_grade(self, student_name, subject, grade, description=""): ...
#     def get_student(self, name): ...
#     def ranking(self): ...  # sorted by overall average, desc
#     def export_csv(self, path): ...
#     def save(self, path): ...
#     def load(self, path): ...
#
# PERSISTENCE FORMAT (gradebook.json):
# {
#   "subjects": ["Math", "Python", "English"],
#   "students": [
#     {
#       "name": "Alice",
#       "grades": {
#         "Math": [{"grade": 8.5, "date": "2026-04-11", "description": "Exam 1"}]
#       }
#     }
#   ]
# }
# ============================================================

import json
import csv
import os
from datetime import date

DB_PATH = os.path.join(os.path.dirname(__file__), "gradebook.json")
REPORT_PATH = os.path.join(os.path.dirname(__file__), "report.csv")
PASS_GRADE = 6.0

# Write your code here


if __name__ == "__main__":
    main()
