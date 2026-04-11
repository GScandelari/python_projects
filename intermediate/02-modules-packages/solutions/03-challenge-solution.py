# ============================================================
# intermediate/02-modules-packages/solutions/03-challenge-solution.py
# ============================================================
# APPROACH: The myutils package lives in solutions/myutils/.
# We import from it using relative package imports.
# The CLI uses a simple while loop + if/elif menu.

import sys
import os

# Add the solutions directory to path so we can import myutils
sys.path.insert(0, os.path.dirname(__file__))

from myutils import reverse, is_palindrome, word_count, clamp, is_prime, factors


def string_tools():
    text = input("Enter a word or phrase: ").strip()
    print(f"  Reversed   : {reverse(text)}")
    print(f"  Palindrome : {is_palindrome(text)}")
    print(f"  Word count : {word_count(text)}")


def number_tools():
    while True:
        raw = input("Enter an integer: ").strip()
        if raw.lstrip("-").isdigit():
            n = int(raw)
            break
        print("  Please enter a valid integer.")

    print(f"  Is prime      : {is_prime(n)}")
    print(f"  Factors       : {factors(abs(n)) if n > 0 else 'N/A (negative)'}")
    print(f"  Clamped(1-100): {clamp(n, 1, 100)}")


def main():
    print("\n" + "=" * 40)
    print("        myutils CLI Tool")
    print("=" * 40)

    while True:
        print("\n[1] String tools\n[2] Number tools\n[0] Exit")
        choice = input("> ").strip()

        if choice == "1":
            string_tools()
        elif choice == "2":
            number_tools()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
