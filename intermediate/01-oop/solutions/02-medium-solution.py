# ============================================================
# intermediate/01-oop/solutions/02-medium-solution.py
# ============================================================

# ----------------------------------------------------------
# Exercise 1 — BankAccount (encapsulation)
# ----------------------------------------------------------
# APPROACH: Protected _balance with controlled access through
# deposit/withdraw. Raise ValueError for invalid operations.

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amount

    def get_balance(self):
        return self._balance

    def __str__(self):
        return f"Account[{self.owner}]: R$ {self._balance:.2f}"

acc = BankAccount("Alice", 500)
acc.deposit(200)
acc.withdraw(100)
print(acc.get_balance())  # 600
print(acc)                # Account[Alice]: R$ 600.00


# ----------------------------------------------------------
# Exercise 2 — Student with class attribute
# ----------------------------------------------------------
# APPROACH: Class attribute `school` shared across all instances.
# average() guards against empty grades list with or condition.

class Student:
    school = "Python Academy"

    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average(self):
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def status(self):
        return "Pass" if self.average() >= 6.0 else "Fail"

    def __str__(self):
        return f"Student({self.name}) — avg: {self.average():.1f} — {self.status()}"

s = Student("Bob")
print(Student.school)  # Python Academy
s.add_grade(7.5)
s.add_grade(8.0)
s.add_grade(5.0)
print(s)               # Student(Bob) — avg: 6.8 — Pass


# ----------------------------------------------------------
# Exercise 3 — Shape hierarchy (inheritance)
# ----------------------------------------------------------
# APPROACH: Base Shape provides describe() using self.area() and
# type(self).__name__ for the class name — subclasses just override area().

class Shape:
    def area(self):
        return 0

    def describe(self):
        return f"I am a {type(self).__name__} with area {self.area():.2f}"


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def __str__(self):
        return f"Circle(radius={self.radius})"


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def __str__(self):
        return f"Triangle(base={self.base}, height={self.height})"


c = Circle(7)
t = Triangle(6, 4)
print(c.describe())  # I am a Circle with area 153.94
print(t.describe())  # I am a Triangle with area 12.00
print(c)             # Circle(radius=7)
print(t)             # Triangle(base=6, height=4)
