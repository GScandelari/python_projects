# ============================================================
# intermediate/01-oop/solutions/03-challenge-solution.py
# ============================================================

# ----------------------------------------------------------
# Exercise 1 — Vector2D (dunder methods)
# ----------------------------------------------------------
# APPROACH: Implement each arithmetic dunder by creating a new
# Vector2D from the result. magnitude uses manual ** 0.5.

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector2D({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector2D(x={self.x}, y={self.y})"

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def magnitude(self):
        return round((self.x ** 2 + self.y ** 2) ** 0.5, 4)

v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)
print(v1 + v2)               # Vector2D(4, 6)
print(v1 - v2)               # Vector2D(2, 2)
print(v1 * 3)                # Vector2D(9, 12)
print(v1.magnitude())        # 5.0
print(v1 == Vector2D(3, 4))  # True


# ----------------------------------------------------------
# Exercise 2 — Vehicle → Car → ElectricCar
# ----------------------------------------------------------
# APPROACH: Each level calls super().__init__ to chain attribute
# initialisation. ElectricCar forces fuel_type="electric" by
# passing it directly to Car's __init__.

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        return f"{self.make} {self.model} engine started."

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type="gasoline"):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type

    def start(self):
        return f"{self.make} {self.model} ({self.fuel_type}) engine started."

    def refuel(self, liters):
        return f"Refueled {liters}L of {self.fuel_type}."


class ElectricCar(Car):
    def __init__(self, make, model, year, battery_kw):
        super().__init__(make, model, year, fuel_type="electric")
        self.battery_kw = battery_kw

    def start(self):
        return f"{self.make} {self.model} motor humming silently."

    def recharge(self, kw):
        return f"Charged {kw} kW."

    def range_km(self):
        return self.battery_kw * 6


car = Car("Toyota", "Corolla", 2022)
ev  = ElectricCar("Tesla", "Model 3", 2023, battery_kw=75)
print(car)              # 2022 Toyota Corolla
print(car.start())      # Toyota Corolla (gasoline) engine started.
print(ev.start())       # Tesla Model 3 motor humming silently.
print(ev.recharge(50))  # Charged 50 kW.
print(ev.range_km())    # 450


# ----------------------------------------------------------
# Exercise 3 — Library system (composition)
# ----------------------------------------------------------
# APPROACH: Book carries its own availability flag. Library holds
# a list of Book objects. checkout/return_book locate by title
# using next() with a default of None — clean and Pythonic.

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.available = True

    def __str__(self):
        return f'"{self.title}" by {self.author} ({self.year})'


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def _find(self, title):
        return next((b for b in self.books if b.title.lower() == title.lower()), None)

    def checkout(self, title):
        book = self._find(title)
        if book is None:
            raise ValueError(f"'{title}' not found in {self.name}.")
        if not book.available:
            raise ValueError(f"'{title}' is currently unavailable.")
        book.available = False
        return book

    def return_book(self, title):
        book = self._find(title)
        if book:
            book.available = True

    def list_available(self):
        available = [b for b in self.books if b.available]
        print(f"\n{self.name} — available books:")
        for i, book in enumerate(available, 1):
            print(f"  {i}. {book}")

    def search(self, query):
        q = query.lower()
        return [b for b in self.books
                if q in b.title.lower() or q in b.author.lower()]


lib = Library("City Library")
lib.add_book(Book("Python Crash Course", "Matthes", 2019))
lib.add_book(Book("Clean Code", "Martin", 2008))
lib.add_book(Book("Fluent Python", "Ramalho", 2022))

lib.list_available()
lib.checkout("Clean Code")
lib.list_available()   # Clean Code no longer shown

results = lib.search("python")
print(f"\nSearch 'python': {[str(b) for b in results]}")
