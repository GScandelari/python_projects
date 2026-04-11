# ============================================================
# Intermediate Mini-Project 01 — Student Grade Manager (SOLUTION)
# ============================================================

import json
import csv
import os
from datetime import date

DB_PATH = os.path.join(os.path.dirname(__file__), "gradebook.json")
REPORT_PATH = os.path.join(os.path.dirname(__file__), "report.csv")
PASS_GRADE = 6.0


# ── Custom Exceptions ─────────────────────────────────────

class GradeManagerError(Exception):
    pass

class StudentNotFoundError(GradeManagerError):
    def __init__(self, name):
        super().__init__(f"Student not found: '{name}'")

class SubjectNotFoundError(GradeManagerError):
    def __init__(self, subject):
        super().__init__(f"Subject not registered: '{subject}'")

class InvalidGradeError(GradeManagerError):
    def __init__(self, grade):
        super().__init__(f"Grade must be between 0.0 and 10.0, got {grade}")

class DuplicateError(GradeManagerError):
    pass


# ── Student ───────────────────────────────────────────────

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}   # {subject: [{grade, date, description}]}

    def add_grade(self, subject, grade, description=""):
        if not 0.0 <= grade <= 10.0:
            raise InvalidGradeError(grade)
        if subject not in self.grades:
            self.grades[subject] = []
        self.grades[subject].append({
            "grade": grade,
            "date": str(date.today()),
            "description": description,
        })

    def average(self, subject=None):
        if subject:
            entries = self.grades.get(subject, [])
            if not entries:
                return None
            return round(sum(e["grade"] for e in entries) / len(entries), 2)
        all_grades = [e["grade"] for entries in self.grades.values() for e in entries]
        if not all_grades:
            return None
        return round(sum(all_grades) / len(all_grades), 2)

    def status(self):
        avg = self.average()
        if avg is None:
            return "No grades"
        return "Pass" if avg >= PASS_GRADE else "Fail"

    def to_dict(self):
        return {"name": self.name, "grades": self.grades}

    @classmethod
    def from_dict(cls, data):
        s = cls(data["name"])
        s.grades = data.get("grades", {})
        return s

    def __str__(self):
        avg = self.average()
        avg_str = f"{avg:.1f}" if avg is not None else "N/A"
        return f"Student({self.name}) — avg: {avg_str} — {self.status()}"


# ── GradeBook ─────────────────────────────────────────────

class GradeBook:
    def __init__(self):
        self.subjects = []
        self.students = {}   # {name: Student}

    def add_student(self, name):
        key = name.strip().title()
        if key in self.students:
            raise DuplicateError(f"Student '{key}' already exists.")
        self.students[key] = Student(key)
        print(f"  Student '{key}' added.")

    def add_subject(self, name):
        key = name.strip().title()
        if key in self.subjects:
            raise DuplicateError(f"Subject '{key}' already registered.")
        self.subjects.append(key)
        print(f"  Subject '{key}' added.")

    def get_student(self, name):
        key = name.strip().title()
        if key not in self.students:
            raise StudentNotFoundError(key)
        return self.students[key]

    def record_grade(self, student_name, subject, grade, description=""):
        subject = subject.strip().title()
        if subject not in self.subjects:
            raise SubjectNotFoundError(subject)
        student = self.get_student(student_name)
        student.add_grade(subject, grade, description)
        print(f"  Grade {grade:.1f} recorded for {student.name} in {subject}.")

    def ranking(self):
        ranked = []
        for s in self.students.values():
            avg = s.average()
            ranked.append((s, avg if avg is not None else -1))
        return sorted(ranked, key=lambda x: x[1], reverse=True)

    def export_csv(self, path):
        with open(path, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            header = ["Name"] + self.subjects + ["Average", "Status"]
            writer.writerow(header)
            for s, _ in self.ranking():
                row = [s.name]
                for sub in self.subjects:
                    avg = s.average(sub)
                    row.append(f"{avg:.1f}" if avg is not None else "-")
                row += [
                    f"{s.average():.1f}" if s.average() is not None else "-",
                    s.status(),
                ]
                writer.writerow(row)
        print(f"  Report exported to {path}")

    def save(self, path):
        data = {
            "subjects": self.subjects,
            "students": [s.to_dict() for s in self.students.values()],
        }
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def load(self, path):
        if not os.path.exists(path):
            return
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.subjects = data.get("subjects", [])
        self.students = {
            d["name"]: Student.from_dict(d)
            for d in data.get("students", [])
        }


# ── Menu helpers ──────────────────────────────────────────

def show_menu():
    print("\n" + "=" * 35)
    print("        GRADE MANAGER")
    print("=" * 35)
    print("  [1] Add student")
    print("  [2] Add subject")
    print("  [3] Record grade")
    print("  [4] View student report")
    print("  [5] Class ranking")
    print("  [6] Export CSV report")
    print("  [0] Save & Exit")


def pick_subject(gb):
    if not gb.subjects:
        print("  No subjects registered.")
        return None
    for i, s in enumerate(gb.subjects, 1):
        print(f"  {i}. {s}")
    try:
        idx = int(input("Select subject number: ")) - 1
        return gb.subjects[idx]
    except (ValueError, IndexError):
        print("  Invalid selection.")
        return None


def main():
    gb = GradeBook()
    gb.load(DB_PATH)
    print("Grade Manager loaded.")

    actions = {
        "1": lambda: gb.add_student(input("Student name: ")),
        "2": lambda: gb.add_subject(input("Subject name: ")),
        "3": grade_menu,
        "4": student_report,
        "5": show_ranking,
        "6": lambda: gb.export_csv(REPORT_PATH),
    }

    while True:
        show_menu()
        choice = input("> ").strip()
        if choice == "0":
            gb.save(DB_PATH)
            print("Saved. Goodbye!")
            break
        action = actions.get(choice)
        if action:
            try:
                if choice in ("3", "4", "5"):
                    action(gb)
                else:
                    action()
            except GradeManagerError as e:
                print(f"  Error: {e}")
        else:
            print("  Invalid option.")


def grade_menu(gb):
    name = input("Student name: ")
    subject = pick_subject(gb)
    if not subject:
        return
    while True:
        try:
            grade = float(input(f"Grade for {subject} (0.0–10.0): "))
            break
        except ValueError:
            print("  Please enter a number.")
    desc = input("Description (optional): ").strip()
    gb.record_grade(name, subject, grade, desc)


def student_report(gb):
    name = input("Student name: ")
    try:
        s = gb.get_student(name)
    except StudentNotFoundError as e:
        print(f"  {e}")
        return
    print(f"\n=== Report: {s.name} ===")
    if not s.grades:
        print("  No grades recorded.")
        return
    for subject, entries in s.grades.items():
        avg = s.average(subject)
        print(f"\n  {subject} — avg: {avg:.1f}")
        for e in entries:
            print(f"    {e['date']}  {e['grade']:.1f}  {e['description']}")
    print(f"\n  Overall: {s.average():.1f} — {s.status()}")


def show_ranking(gb):
    print("\n=== CLASS RANKING ===")
    if not gb.students:
        print("  No students.")
        return
    for i, (s, avg) in enumerate(gb.ranking(), 1):
        avg_str = f"{avg:.1f}" if avg >= 0 else "N/A"
        symbol = "✓" if s.status() == "Pass" else "✗"
        print(f"  {i}. {s.name:<15} avg: {avg_str:>4}  {symbol} {s.status()}")


if __name__ == "__main__":
    main()
