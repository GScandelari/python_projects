# ============================================================
# beginner/01-fundamentals/solutions/02-medium-solution.py
# ============================================================

# ----------------------------------------------------------
# Exercise 1 — Reading and displaying user input
# ----------------------------------------------------------
# APPROACH: input() always returns str. Convert age to int
# before embedding in the f-string arithmetic.

# name = input("Enter your name: ")
# age  = int(input("Enter your age: "))
# print(f"Hello, {name}! You are {age} years old.")

# Demo (hardcoded to avoid blocking):
name, age = "Maria", 30
print(f"Hello, {name}! You are {age} years old.")


# ----------------------------------------------------------
# Exercise 2 — Area of a rectangle
# ----------------------------------------------------------
# APPROACH: float() accepts decimal input. :.2f in the
# f-string rounds and pads to exactly 2 decimal places.

width, height = 5.5, 3.0
area      = width * height
perimeter = 2 * (width + height)
print(f"Area     : {area:.2f}")
print(f"Perimeter: {perimeter:.2f}")


# ----------------------------------------------------------
# Exercise 3 — Type conversion practice
# ----------------------------------------------------------
# APPROACH: int("42") → 42, float("3.14") → 3.14,
# bool(int("1")) → True. type() returns the class object.

str_integer = "42"
str_float   = "3.14"
str_bool    = "1"

converted_int   = int(str_integer)
converted_float = float(str_float)
converted_bool  = bool(int(str_bool))

print(converted_int,   type(converted_int))
print(converted_float, type(converted_float))
print(converted_bool,  type(converted_bool))


# ----------------------------------------------------------
# Exercise 4 — f-string formatting
# ----------------------------------------------------------
# APPROACH: Multi-line f-string using \n inside the string,
# or three separate print() calls. :.2f formats the price.

product = "Laptop"
price   = 999.9
stock   = 5

print(f"Product : {product}\nPrice   : ${price:.2f}\nIn stock: {stock} unit(s)")


# ----------------------------------------------------------
# Exercise 5 — Tip calculator
# ----------------------------------------------------------
# APPROACH: Convert inputs to float. Calculate tip and total,
# then format each with :.2f. Embed the percentage in the label.

bill       = 85.50
tip_pct    = 18.0
tip_amount = bill * (tip_pct / 100)
grand      = bill + tip_amount

print(f"Bill total : ${bill:.2f}")
print(f"Tip ({tip_pct}%): ${tip_amount:.2f}")
print(f"Grand total: ${grand:.2f}")
