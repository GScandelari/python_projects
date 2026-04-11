# ============================================================
# Mini-Project 01 — Number Guessing Game (SOLUTION)
# ============================================================

import random


LEVELS = {
    "1": ("Easy",   1,  50, 10),
    "2": ("Medium", 1, 100,  7),
    "3": ("Hard",   1, 200,  5),
}


def get_difficulty():
    """Display difficulty menu and return (label, low, high, max_attempts)."""
    print("\nSelect difficulty:")
    print("  1. Easy   (1-50,  10 attempts)")
    print("  2. Medium (1-100,  7 attempts)")
    print("  3. Hard   (1-200,  5 attempts)")
    while True:
        choice = input("> ").strip()
        if choice in LEVELS:
            label, low, high, max_att = LEVELS[choice]
            return label, low, high, max_att
        print("Please enter 1, 2 or 3.")


def get_secret_number(low, high):
    """Return a random integer between low and high (inclusive)."""
    return random.randint(low, high)


def get_player_guess(low, high, attempt, max_attempts):
    """Prompt the player for a valid integer guess within range."""
    while True:
        raw = input(f"\n[Attempt {attempt}/{max_attempts}] Your guess: ").strip()
        if not raw.isdigit() and not (raw.startswith("-") and raw[1:].isdigit()):
            print(f"  Please enter a whole number between {low} and {high}.")
            continue
        guess = int(raw)
        if guess < low or guess > high:
            print(f"  Out of range! Guess between {low} and {high}.")
            continue
        return guess


def rate_performance(attempts_used, max_attempts):
    """Return a performance rating string based on attempts used."""
    ratio = attempts_used / max_attempts
    if ratio <= 0.33:
        return "Legendary!"
    if ratio <= 0.50:
        return "Excellent!"
    if ratio <= 0.75:
        return "Good job!"
    return "Better luck next time."


def play_game():
    """Run one full round of the guessing game."""
    print("\n" + "=" * 35)
    print("      NUMBER GUESSING GAME")
    print("=" * 35)

    label, low, high, max_attempts = get_difficulty()
    secret = get_secret_number(low, high)
    history = []

    for attempt in range(1, max_attempts + 1):
        guess = get_player_guess(low, high, attempt, max_attempts)
        history.append(guess)

        if guess == secret:
            print(f"\nCorrect! The number was {secret}.")
            print(f"Attempts used: {attempt} / {max_attempts}")
            print(f"Rating: {rate_performance(attempt, max_attempts)}")
            return

        hint = "Too low! " if guess < secret else "Too high!"
        remaining = max_attempts - attempt
        print(f"{hint} History: {history}  ({remaining} attempt(s) left)")

    print(f"\nOut of attempts! The number was {secret}.")
    print("Rating: Better luck next time.")


def main():
    """Main loop — play until the user decides to quit."""
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("\nThanks for playing. Goodbye!")
            break


if __name__ == "__main__":
    main()
