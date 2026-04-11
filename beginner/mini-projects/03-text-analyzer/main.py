# ============================================================
# Mini-Project 03 — Text Analyzer
# Analyze a text and print a full statistical report.
# ============================================================
#
# HOW TO APPROACH THIS PROJECT:
#   1. Read the README.md for the full feature list
#   2. Build one function per metric — keep them pure (no print inside)
#   3. Collect all results in main() and print the report there
#   4. Check solution.py only after you have a working version
#
# SUGGESTED FUNCTIONS TO BUILD:
#   - count_characters(text)       → returns (total, no_spaces)
#   - count_words(text)            → returns (total_words, unique_words)
#   - count_sentences(text)        → returns int (count '.', '!', '?')
#   - count_paragraphs(text)       → returns int (split on '\n\n')
#   - word_frequency(text)         → returns dict {word: count}, excluding stopwords
#   - top_n_words(freq_dict, n)    → returns list of (word, count) sorted by count desc
#   - longest_shortest_word(text)  → returns (longest, shortest)
#   - avg_word_length(text)        → returns float rounded to 2 decimals
#   - words_per_sentence(text)     → returns float rounded to 1 decimal
#   - print_report(text)           → calls all functions and prints the formatted report
#   - main()                       → gets text from user, calls print_report
#
# STOPWORDS TO EXCLUDE FROM FREQUENCY:
STOPWORDS = {
    "the", "a", "an", "and", "or", "but", "is", "in", "on",
    "at", "to", "for", "of", "with", "it", "its", "as", "by",
    "that", "this", "are", "was", "were", "be", "been", "have",
    "has", "do", "does", "from", "not", "so", "if", "no", "we"
}
#
# INPUT HINT — collecting multi-line text from the user:
#   print("Paste your text (press Enter twice to finish):")
#   lines = []
#   while True:
#       line = input()
#       if line == "":
#           break
#       lines.append(line)
#   text = " ".join(lines)
# ============================================================

# Write your code here


if __name__ == "__main__":
    main()
