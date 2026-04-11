# =============================================================================
# Difficulty : Easy  —  SOLUTIONS
# Topic      : Data Structures — Lists, Tuples, Dictionaries, Sets
# Description: Full solutions for all 5 easy exercises with approach comments.
# =============================================================================


# -----------------------------------------------------------------------------
# Exercise 1 - List of fruits — first and last item via indexing
# -----------------------------------------------------------------------------
# PROMPT:
#   Create a list named 'fruits' that contains exactly 5 fruit names (strings).
#   Then print:
#     - The first item using a positive index.
#     - The last item using a negative index.
#
# Expected output (example with the list below):
#   apple
#   mango

# APPROACH:
#   Python lists are zero-indexed, so the first element is always at index 0.
#   Negative indices count from the end: -1 is the last element, -2 is the
#   second to last, and so on. Using -1 is preferred over len(fruits) - 1
#   because it is shorter and works regardless of the list length.

fruits = ["apple", "banana", "cherry", "orange", "mango"]

print(fruits[0])    # First item  → apple
print(fruits[-1])   # Last item   → mango


# -----------------------------------------------------------------------------
# Exercise 2 - Modify a list: add two fruits, remove one, print the result
# -----------------------------------------------------------------------------
# PROMPT:
#   Starting with the list from Exercise 1, perform these steps IN ORDER:
#     1. Add "grape" to the end of the list.
#     2. Add "pineapple" to the end of the list.
#     3. Remove "banana" from the list.
#   Print the final list.
#
# Expected output:
#   ['apple', 'cherry', 'orange', 'mango', 'grape', 'pineapple']

# APPROACH:
#   .append(item) adds a single item to the end of the list (O(1) operation).
#   .remove(value) searches for the first occurrence of the given value and
#   deletes it; it raises ValueError if the value is not found, so only call
#   it when you are sure the item exists. Because lists are mutable, all three
#   methods modify the list in place and return None — do not assign the result.

fruits = ["apple", "banana", "cherry", "orange", "mango"]  # fresh copy

fruits.append("grape")
fruits.append("pineapple")
fruits.remove("banana")

print(fruits)


# -----------------------------------------------------------------------------
# Exercise 3 - Tuple with (x, y, z) coordinates — unpack and print each axis
# -----------------------------------------------------------------------------
# PROMPT:
#   Create a tuple named 'point' that stores three numbers representing a
#   3-D coordinate: x = 4, y = -2, z = 7.
#   Use tuple unpacking to assign each value to its own variable, then print
#   each axis on a separate line in the format "x: 4", "y: -2", "z: 7".
#
# Expected output:
#   x: 4
#   y: -2
#   z: 7

# APPROACH:
#   Tuple unpacking (also called destructuring) assigns each element of the
#   tuple to a matching variable in a single statement. The number of variables
#   on the left must equal the number of elements in the tuple, otherwise Python
#   raises a ValueError. This is more readable than accessing elements by index
#   (point[0], point[1], …) and documents the intent clearly.

point = (4, -2, 7)

x, y, z = point   # unpack all three values in one line

print(f"x: {x}")
print(f"y: {y}")
print(f"z: {z}")


# -----------------------------------------------------------------------------
# Exercise 4 - Dictionary with name/age/city — print each value by key
# -----------------------------------------------------------------------------
# PROMPT:
#   Create a dictionary named 'person' with these three key-value pairs:
#     - "name"  → "Alice"
#     - "age"   → 30
#     - "city"  → "São Paulo"
#   Print each value by accessing it with its key.
#
# Expected output:
#   Alice
#   30
#   São Paulo

# APPROACH:
#   Dictionary values are retrieved with square-bracket notation: dict[key].
#   This raises a KeyError if the key does not exist, which is intentional here
#   because we know all three keys are present. An alternative is .get(key),
#   which returns None (or a default you supply) instead of raising — useful
#   when the key might be absent.

person = {
    "name": "Alice",
    "age" : 30,
    "city": "São Paulo",
}

print(person["name"])
print(person["age"])
print(person["city"])


# -----------------------------------------------------------------------------
# Exercise 5 - Set with duplicate numbers — demonstrate deduplication
# -----------------------------------------------------------------------------
# PROMPT:
#   Create a set named 'numbers' from the following sequence (which contains
#   duplicates): 3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5
#   Print the set and its length to show that duplicates were removed.
#
# Expected output (order will vary — sets are unordered):
#   {1, 2, 3, 4, 5, 6, 9}
#   7

# APPROACH:
#   A set is a collection of UNIQUE elements. When you construct a set from a
#   sequence that has duplicates, Python automatically discards the extras —
#   each value appears at most once. Sets are also unordered, so the printed
#   order may differ between runs or Python versions (though CPython tends to
#   sort small integer sets consistently). Use len() to confirm the count of
#   unique values.

numbers = {3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5}

print(numbers)        # only unique values remain
print(len(numbers))   # 7 unique numbers
