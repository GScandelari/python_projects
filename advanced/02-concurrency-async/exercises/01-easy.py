# ============================================================
# advanced/02-concurrency-async/exercises/01-easy.py
# Topic: Concurrency — threading and asyncio basics
# Difficulty: Easy
# ============================================================

import threading
import time
import asyncio

# Exercise 1 — Basic threading
# ------------------------------
# Create 5 threads that each print a message with their thread number
# and sleep for a random time between 0.1 and 0.5 seconds.
# Use threading.Thread with a target function.
# Print "All threads done" after all threads complete.
#
# Expected (order varies):
#   Thread 1 starting
#   Thread 3 starting
#   ...
#   Thread 2 done
#   Thread 5 done
#   All threads done

import random
# Write your code here


# Exercise 2 — Thread with return value
# ---------------------------------------
# Python threads don't natively return values. Write a function
# threaded_square(n, results, index) that computes n**2 and
# stores it in results[index]. Run 5 threads to square [1,2,3,4,5]
# and print the results in order after all threads finish.
#
# Expected:
#   [1, 4, 9, 16, 25]

# Write your code here


# Exercise 3 — asyncio hello world
# ----------------------------------
# Write an async function greet(name, delay) that waits `delay`
# seconds then prints "Hello, {name}!".
# Write an async main() that calls greet() for three names with
# different delays SEQUENTIALLY (using await one by one).
# Note the total time — it should be the sum of all delays.
#
# Expected:
#   Hello, Alice!    (after 0.5s)
#   Hello, Bob!      (after 1.0s more)
#   Hello, Carol!    (after 0.3s more)
#   Total: ~1.8s

# Write your code here


# Exercise 4 — asyncio gather (concurrent)
# ------------------------------------------
# Copy greet() from above and modify main() to run all three
# greetings CONCURRENTLY using asyncio.gather().
# Note the total time — it should be ≈ max(delays), not sum.
#
# Expected:
#   All three names printed in ~0.5s (the longest delay)

# Write your code here
