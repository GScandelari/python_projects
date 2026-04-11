# ============================================================
# intermediate/01-oop/exercises/03-challenge.py
# Topic: OOP — dunder methods, inheritance chains, composition
# Difficulty: Challenge
# ============================================================

# Exercise 1
# ----------
# Create a class called Vector2D that represents a 2D vector.
# Implement:
#   - __init__(x, y)
#   - __str__ → "Vector2D(x, y)"
#   - __repr__ → "Vector2D(x=x, y=y)"
#   - __add__ → adds two vectors component-wise
#   - __sub__ → subtracts two vectors
#   - __mul__(scalar) → multiplies vector by a scalar (int or float)
#   - __eq__ → True if x and y are equal
#   - magnitude() → returns √(x²+y²) rounded to 4 decimal places
#                   (compute manually: (x**2 + y**2) ** 0.5)
#
# Expected:
#   v1 = Vector2D(3, 4)
#   v2 = Vector2D(1, 2)
#   print(v1 + v2)        → Vector2D(4, 6)
#   print(v1 - v2)        → Vector2D(2, 2)
#   print(v1 * 3)         → Vector2D(9, 12)
#   print(v1.magnitude()) → 5.0
#   print(v1 == Vector2D(3, 4))  → True

# Write your code here


# Exercise 2
# ----------
# Build an inheritance chain: Vehicle → Car → ElectricCar
#
# Vehicle:
#   - Attributes: make (str), model (str), year (int)
#   - Method: start() → returns "{make} {model} engine started."
#   - __str__ → "{year} {make} {model}"
#
# Car(Vehicle):
#   - Additional attribute: fuel_type (str, default "gasoline")
#   - Override start() → "{make} {model} ({fuel_type}) engine started."
#   - Method: refuel(liters) → returns "Refueled {liters}L of {fuel_type}."
#
# ElectricCar(Car):
#   - fuel_type is always "electric" (set via super().__init__)
#   - Additional attribute: battery_kw (int)
#   - Override start() → "{make} {model} motor humming silently."
#   - Override refuel → renamed to recharge(kw) → "Charged {kw} kW."
#   - Method: range_km() → returns battery_kw * 6  (simplified estimate)
#
# Expected:
#   car = Car("Toyota", "Corolla", 2022)
#   ev = ElectricCar("Tesla", "Model 3", 2023, battery_kw=75)
#   print(car)              → 2022 Toyota Corolla
#   print(car.start())      → Toyota Corolla (gasoline) engine started.
#   print(ev.start())       → Tesla Model 3 motor humming silently.
#   print(ev.recharge(50))  → Charged 50 kW.
#   print(ev.range_km())    → 450

# Write your code here


# Exercise 3
# ----------
# Create a simple Library system using COMPOSITION (a class that
# contains instances of another class).
#
# Book:
#   - Attributes: title, author, year
#   - Property: available (bool, starts True)
#   - __str__ → '"{title}" by {author} ({year})'
#
# Library:
#   - Attribute: name, books (list, starts empty)
#   - Method: add_book(book) → adds a Book to the collection
#   - Method: checkout(title) → marks book as unavailable, returns Book
#                               raises ValueError if not found or unavailable
#   - Method: return_book(title) → marks book as available
#   - Method: list_available() → prints available books as a numbered list
#   - Method: search(query) → returns list of books where query matches
#                              title or author (case-insensitive, partial)
#
# Expected:
#   lib = Library("City Library")
#   lib.add_book(Book("Python Crash Course", "Matthes", 2019))
#   lib.add_book(Book("Clean Code", "Martin", 2008))
#   lib.add_book(Book("Fluent Python", "Ramalho", 2022))
#   lib.list_available()
#   lib.checkout("Clean Code")
#   lib.list_available()    # Clean Code no longer shown

# Write your code here
