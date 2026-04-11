# ============================================================
# beginner/02-control-flow/solutions/02-medium-solution.py
# ============================================================

# ----------------------------------------------------------
# Exercise 1 — Classify number (even/odd + sign)
# ----------------------------------------------------------
# APPROACH: Use nested if/elif to combine both classifications.
# Check divisibility with % 2, then compare with 0.

number = 7   # demo value

parity = "even" if number % 2 == 0 else "odd"
if number > 0:
    sign = "positive"
elif number < 0:
    sign = "negative"
else:
    sign = "zero"

print(f"{number} is {sign} and {parity}")


# ----------------------------------------------------------
# Exercise 2 — FizzBuzz 1–30
# ----------------------------------------------------------
# APPROACH: Always check divisibility by BOTH first (15),
# then check each individually. Order matters.

for n in range(1, 31):
    if n % 15 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)


# ----------------------------------------------------------
# Exercise 3 — Running total with while loop
# ----------------------------------------------------------
# APPROACH: Accumulate inside a while loop. Input "0" is
# the sentinel value that ends the loop.

print("\n--- Running Total (demo with hardcoded values) ---")
values = [10, 25, 5, 0]   # last 0 triggers stop
total = 0
for v in values:
    if v == 0:
        break
    total += v
    print(f"Added {v}. Running total: {total}")
print(f"Final total: {total}")


# ----------------------------------------------------------
# Exercise 4 — Numbers divisible by both 3 and 7 (1–100)
# ----------------------------------------------------------
# APPROACH: A number divisible by both 3 and 7 is divisible
# by their LCM = 21. Check with % 21 == 0.

print("\nNumbers 1–100 divisible by 3 and 7:")
for n in range(1, 101):
    if n % 3 == 0 and n % 7 == 0:
        print(n, end="  ")
print()


# ----------------------------------------------------------
# Exercise 5 — First number in 1–200 divisible by 13 and 17
# ----------------------------------------------------------
# APPROACH: Use for loop with break. Once found, print and
# stop. The loop's else clause runs if break was never hit.

print("\nFirst number 1–200 divisible by 13 and 17:")
for n in range(1, 201):
    if n % 13 == 0 and n % 17 == 0:
        print(n)   # 221 is outside range, so no result
        break
else:
    print("None found in range 1–200")
