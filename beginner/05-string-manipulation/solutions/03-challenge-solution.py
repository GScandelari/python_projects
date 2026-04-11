# ============================================================
# beginner/05-string-manipulation/solutions/03-challenge-solution.py
# ============================================================

# ----------------------------------------------------------
# Exercise 1 — title_case without .title() / .capitalize()
# ----------------------------------------------------------
# APPROACH: Split the text into words. For each word, take the
# first character with [0].upper() and the rest with [1:].lower().
# Rejoin with a space.

def title_case(text):
    result = []
    for word in text.split():
        result.append(word[0].upper() + word[1:].lower())
    return " ".join(result)

print(title_case("hello world"))          # Hello World
print(title_case("the QUICK brown FOX"))  # The Quick Brown Fox
print(title_case("python is great!"))     # Python Is Great!


# ----------------------------------------------------------
# Exercise 2 — Run-length encoding (compress)
# ----------------------------------------------------------
# APPROACH: Walk the string tracking the current character and
# its count. When the character changes, emit the char + count
# (omitting the count when it equals 1).

def compress(text):
    if not text:
        return ""
    result = []
    current = text[0]
    count = 1
    for ch in text[1:]:
        if ch == current:
            count += 1
        else:
            result.append(current if count == 1 else current + str(count))
            current = ch
            count = 1
    result.append(current if count == 1 else current + str(count))
    return "".join(result)

print(compress("aabbbcccc"))  # a2b3c4
print(compress("hello"))      # hel2o
print(compress("aaabbaaa"))   # a3b2a3
print(compress("abc"))        # abc


# ----------------------------------------------------------
# Exercise 3 — word_stats
# ----------------------------------------------------------
# APPROACH: One pass for character/word stats. Split on spaces
# for word list. Scan for sentence-ending punctuation manually.
# Frequency dict built with .get(). Longest word via max() with
# key=len.

paragraph = (
    "Python is an amazing language. "
    "Python makes programming fun and easy! "
    "Many developers love Python. "
    "Is Python the best language?"
)

def word_stats(text):
    chars_total   = len(text)
    chars_no_space = len(text.replace(" ", ""))
    sentences     = sum(1 for ch in text if ch in ".!?")
    words         = text.replace(".", " ").replace("!", " ").replace("?", " ").split()
    word_count    = len(words)

    # frequency (case-insensitive)
    freq = {}
    for w in words:
        key = w.lower()
        freq[key] = freq.get(key, 0) + 1

    longest = max(words, key=len)
    most_freq_word = max(freq, key=freq.get)
    avg_len = round(sum(len(w) for w in words) / word_count, 2)

    print(f"Characters (total)   : {chars_total}")
    print(f"Characters (no spaces): {chars_no_space}")
    print(f"Words                : {word_count}")
    print(f"Sentences            : {sentences}")
    print(f"Longest word         : {longest}")
    print(f"Most frequent word   : {most_freq_word} ({freq[most_freq_word]})")
    print(f"Average word length  : {avg_len}")

print("\n--- Word Stats ---")
word_stats(paragraph)
