# =============================================================================
# 02-Control Flow | Easy Exercises — Solutions
# =============================================================================
# Each solution includes the original exercise prompt, an APPROACH comment
# explaining the concept used, and clean, working code.
# =============================================================================


# -----------------------------------------------------------------------------
# Exercise 1: Check if a number is positive, negative, or zero
# -----------------------------------------------------------------------------
# PROMPT: Given number = -7, print whether it is positive, negative, or zero.

# APPROACH: Use an if/elif/else chain. Python evaluates each condition from top
# to bottom and executes the first branch whose condition is True. The else
# clause acts as a catch-all for any case not covered above it.

number = -7

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# Output: The number is negative.


# -----------------------------------------------------------------------------
# Exercise 2: Print numbers 1–10 using for + range()
# -----------------------------------------------------------------------------
# PROMPT: Use a for loop with range() to print every integer from 1 to 10,
# each on its own line.

# APPROACH: range(start, stop) generates integers from start up to (but NOT
# including) stop. To include 10 we pass range(1, 11). The for loop variable
# takes each value in turn — no manual incrementing is needed.

print("\nNumbers 1 to 10:")
for n in range(1, 11):
    print(n)


# -----------------------------------------------------------------------------
# Exercise 3: Print even numbers 1–20 using range() with step
# -----------------------------------------------------------------------------
# PROMPT: Print all even numbers between 1 and 20 (inclusive) using range()
# with a step argument. Do not use an if statement inside the loop.

# APPROACH: range(start, stop, step) skips by step each iteration. Starting at
# 2 and stepping by 2 lands on every even number. Using range(2, 21, 2) covers
# 2, 4, 6, … 20. The step does the filtering work so no if is needed.

print("\nEven numbers 1–20:")
for even in range(2, 21, 2):
    print(even)


# -----------------------------------------------------------------------------
# Exercise 4: Countdown from 5 to 1 with a while loop, then print "Go!"
# -----------------------------------------------------------------------------
# PROMPT: Use a while loop to count down from 5 to 1, printing each number.
# After the loop finishes, print "Go!".

# APPROACH: A while loop keeps running as long as its condition is True. We
# initialise a counter at 5 and print it, then decrement by 1 each iteration.
# When the counter reaches 0 the condition (counter > 0) becomes False and
# Python exits the loop, then executes the line after it — "Go!".

print("\nCountdown:")
counter = 5
while counter > 0:
    print(counter)
    counter -= 1
print("Go!")


# -----------------------------------------------------------------------------
# Exercise 5: Print each character of "Python" on its own line
# -----------------------------------------------------------------------------
# PROMPT: Iterate over the string "Python" and print every character
# individually, one per line.

# APPROACH: In Python, strings are iterable sequences of characters. A for
# loop over a string yields one character at a time, left to right, without
# needing indexing or len(). This works identically to iterating over a list.

print("\nCharacters in 'Python':")
for char in "Python":
    print(char)
