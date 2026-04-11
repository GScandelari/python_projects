# ============================================================
# intermediate/01-oop/exercises/02-medium.py
# Topic: OOP — encapsulation, class attributes, inheritance
# Difficulty: Medium
# ============================================================

# Exercise 1
# ----------
# Create a class called BankAccount with:
#   - Protected attribute: _balance (starts at 0 by default)
#   - Attribute: owner (str)
#   - Method: deposit(amount) → adds amount if > 0, else raises ValueError
#   - Method: withdraw(amount) → subtracts if amount <= _balance and > 0,
#                                else raises ValueError
#   - Method: get_balance() → returns current _balance
#   - __str__ → returns "Account[{owner}]: R$ {balance:.2f}"
#
# Expected:
#   acc = BankAccount("Alice", 500)
#   acc.deposit(200)
#   acc.withdraw(100)
#   print(acc.get_balance())   → 600
#   print(acc)                 → Account[Alice]: R$ 600.00

# Write your code here


# Exercise 2
# ----------
# Create a class called Student with a CLASS attribute `school = "Python Academy"`.
#   - Instance attributes: name, grades (list of floats, starts empty)
#   - Method: add_grade(grade) → appends grade to grades list
#   - Method: average() → returns average of grades (0.0 if no grades)
#   - Method: status() → returns "Pass" if average >= 6.0 else "Fail"
#   - __str__ → returns "Student({name}) — avg: {average:.1f} — {status}"
#
# Expected:
#   s = Student("Bob")
#   print(Student.school)    → Python Academy
#   s.add_grade(7.5)
#   s.add_grade(8.0)
#   s.add_grade(5.0)
#   print(s)                 → Student(Bob) — avg: 6.8 — Pass

# Write your code here


# Exercise 3
# ----------
# Create a base class called Shape with:
#   - Abstract-style method area() → returns 0 (to be overridden)
#   - Method describe() → returns "I am a {classname} with area {area:.2f}"
#
# Then create TWO subclasses:
#   Circle(radius) → area = π * r²  (use 3.14159)
#   Triangle(base, height) → area = 0.5 * base * height
#
# Both must override area() and __str__.
#
# Expected:
#   c = Circle(7)
#   t = Triangle(6, 4)
#   print(c.describe())    → I am a Circle with area 153.94
#   print(t.describe())    → I am a Triangle with area 12.00
#   print(c)               → Circle(radius=7)
#   print(t)               → Triangle(base=6, height=4)

# Write your code here
