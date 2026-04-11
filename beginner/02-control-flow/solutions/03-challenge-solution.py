# ============================================================
# beginner/02-control-flow/solutions/03-challenge-solution.py
# ============================================================

# ----------------------------------------------------------
# Exercise 1 — Multiplication table
# ----------------------------------------------------------
# APPROACH: Nested f-string with :>3 aligns numbers right.
# Use a single for loop from 1 to 10.

def multiplication_table(n):
    print(f"\n--- Multiplication table for {n} ---")
    for i in range(1, 11):
        print(f"  {n} x {i:2} = {n * i:3}")

multiplication_table(7)


# ----------------------------------------------------------
# Exercise 2 — Number guessing game
# ----------------------------------------------------------
# APPROACH: while True loop with break on correct guess.
# Count attempts and give directional hints each round.

def guessing_game_demo():
    """Demo version with hardcoded guesses (avoids input())."""
    secret = 42
    guesses = [25, 60, 42]   # simulate user guesses
    attempts = 0

    print("\n--- Guessing Game (demo) ---")
    for guess in guesses:
        attempts += 1
        print(f"Guess: {guess}")
        if guess == secret:
            print(f"Correct! You got it in {attempts} attempt(s).")
            break
        elif guess < secret:
            print("Too low!")
        else:
            print("Too high!")

guessing_game_demo()


# ----------------------------------------------------------
# Exercise 3 — Star triangle
# ----------------------------------------------------------
# APPROACH: For height H, row i (1-indexed) contains i stars.
# Use a nested loop or string multiplication.

def star_triangle(height):
    print(f"\n--- Triangle (height={height}) ---")
    for i in range(1, height + 1):
        print("*" * i)

star_triangle(5)
star_triangle(3)
