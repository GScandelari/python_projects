# ============================================================
# Mini-Project 01 — Number Guessing Game
# Build a complete terminal game using only beginner concepts.
# ============================================================
#
# HOW TO APPROACH THIS PROJECT:
#   1. Read the README.md for the full feature list
#   2. Break the problem into small functions (one task each)
#   3. Test each function before wiring them together
#   4. Check solution.py only after you have a working version
#
# SUGGESTED FUNCTIONS TO BUILD:
#   - get_difficulty()       → returns (min_val, max_val, max_attempts)
#   - get_secret_number(...) → returns a random int in range
#   - get_player_guess(...)  → returns a validated integer from input()
#   - rate_performance(...)  → returns a string rating based on attempts used
#   - play_game()            → runs one full round
#   - main()                 → main loop with play-again logic
#
# HINT — generating a random number without importing random:
#   Python has a built-in module: import random
#   secret = random.randint(low, high)   # inclusive on both ends
#
# DIFFICULTY LEVELS:
#   Easy:   range 1–50,  max 10 attempts
#   Medium: range 1–100, max  7 attempts
#   Hard:   range 1–200, max  5 attempts
#
# PERFORMANCE RATINGS (based on attempts used vs max):
#   ≤ 33% of attempts → "Legendary!"
#   ≤ 50%             → "Excellent!"
#   ≤ 75%             → "Good job!"
#   otherwise         → "Better luck next time."
# ============================================================

import random

# Write your code here


if __name__ == "__main__":
    main()
