# beginner/03-data-structures/exercises/03-challenge.py
# Topic: Lists, Tuples, Dictionaries, Sets — Challenge Exercises
# Complete each exercise by replacing the placeholder with your code.

# =============================================================================
# Exercise 1 — Phonebook (interactive)
# Build a simple command-line phone book backed by a dictionary where:
#   - Keys are contact names (strings)
#   - Values are phone numbers (strings)
#
# The program should loop and present a menu:
#   1. Add contact      → prompt for name and number, store in dict
#   2. Search contact   → prompt for name, print number or "Not found"
#   3. Delete contact   → prompt for name, remove from dict or "Not found"
#   4. Quit             → exit the loop
#
# Example session:
#   --- Phonebook ---
#   1. Add  2. Search  3. Delete  4. Quit
#   Choice: 1
#   Name: Alice
#   Number: 555-1234
#   Contact added.
#
#   Choice: 2
#   Name: Alice
#   Alice -> 555-1234
#
#   Choice: 3
#   Name: Alice
#   Alice deleted.
#
#   Choice: 4
#   Goodbye!
# =============================================================================

# Write your code here


# =============================================================================
# Exercise 2 — Top-5 Word Frequency Counter
# Given the paragraph string below (already assigned — do not change it),
# count how many times each word appears.
# Normalise by converting to lowercase and stripping punctuation manually
# (replace commas, periods, exclamation marks, and question marks with "").
# Print the 5 most frequent words in descending order of frequency.
# Hint: sort the dictionary items by value before printing.
#
# Expected output (exact counts depend on the paragraph):
#   the      -> 7
#   of       -> 5
#   ...
# =============================================================================

paragraph = (
    "To be or not to be that is the question whether tis nobler in the mind "
    "to suffer the slings and arrows of outrageous fortune or to take arms "
    "against a sea of troubles and by opposing end them to die to sleep no "
    "more and by a sleep to say we end the heartache and the thousand natural "
    "shocks that flesh is heir to tis a consummation devoutly to be wished"
)

# Write your code here


# =============================================================================
# Exercise 3 — Shopping Cart with Discount
# You have a list of items, each represented as a dictionary with the keys:
#   "name"  (str)  — product name
#   "price" (float) — unit price
#   "qty"   (int)  — quantity
#
# Steps:
#   1. Calculate the subtotal for each item  (price × qty)
#   2. Sum all subtotals to get the cart total
#   3. If the total exceeds 100, apply a 10% discount
#   4. Print a receipt: one line per item, then the total (and discount if any)
#
# cart = [
#     {"name": "Apple",    "price": 0.50, "qty": 6},
#     {"name": "Notebook", "price": 12.99, "qty": 3},
#     {"name": "Pen",      "price": 1.75,  "qty": 10},
#     {"name": "Backpack", "price": 49.90, "qty": 1},
# ]
#
# Expected output:
#   Apple      x6   =  $3.00
#   Notebook   x3   = $38.97
#   Pen        x10  = $17.50
#   Backpack   x1   = $49.90
#   --------------------------------
#   Subtotal:        $109.37
#   Discount (10%):  -$10.94
#   Total:           $98.43
# =============================================================================

cart = [
    {"name": "Apple",    "price": 0.50,  "qty": 6},
    {"name": "Notebook", "price": 12.99, "qty": 3},
    {"name": "Pen",      "price": 1.75,  "qty": 10},
    {"name": "Backpack", "price": 49.90, "qty": 1},
]

# Write your code here
