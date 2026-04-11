# ============================================================
# Mini-Project 03 — Text Analyzer (SOLUTION)
# ============================================================

STOPWORDS = {
    "the", "a", "an", "and", "or", "but", "is", "in", "on",
    "at", "to", "for", "of", "with", "it", "its", "as", "by",
    "that", "this", "are", "was", "were", "be", "been", "have",
    "has", "do", "does", "from", "not", "so", "if", "no", "we"
}


def clean_word(word):
    """Strip punctuation from both ends of a word and lowercase it."""
    cleaned = word.lower()
    while cleaned and not cleaned[0].isalpha():
        cleaned = cleaned[1:]
    while cleaned and not cleaned[-1].isalpha():
        cleaned = cleaned[:-1]
    return cleaned


def count_characters(text):
    """Return (total_chars, chars_without_spaces)."""
    return len(text), len(text.replace(" ", ""))


def count_words(text):
    """Return (total_words, unique_words)."""
    raw_words = text.split()
    cleaned = [clean_word(w) for w in raw_words if clean_word(w)]
    return len(cleaned), len(set(cleaned))


def count_sentences(text):
    """Count sentence-ending punctuation: . ! ?"""
    return sum(1 for ch in text if ch in ".!?")


def count_paragraphs(text):
    """Count paragraphs separated by blank lines."""
    parts = [p.strip() for p in text.split("\n\n") if p.strip()]
    return max(len(parts), 1)


def word_frequency(text):
    """Return {word: count} dict excluding stopwords."""
    freq = {}
    for raw in text.split():
        word = clean_word(raw)
        if word and word not in STOPWORDS:
            freq[word] = freq.get(word, 0) + 1
    return freq


def top_n_words(freq_dict, n=5):
    """Return list of (word, count) sorted by count descending."""
    return sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)[:n]


def longest_shortest_word(text):
    """Return (longest_word, shortest_word) ignoring punctuation."""
    words = [clean_word(w) for w in text.split() if clean_word(w)]
    if not words:
        return "", ""
    longest = max(words, key=len)
    shortest = min(words, key=len)
    return longest, shortest


def avg_word_length(text):
    """Return average word length rounded to 2 decimal places."""
    words = [clean_word(w) for w in text.split() if clean_word(w)]
    if not words:
        return 0.0
    return round(sum(len(w) for w in words) / len(words), 2)


def words_per_sentence(text):
    """Return average words per sentence rounded to 1 decimal place."""
    sentences = count_sentences(text)
    total, _ = count_words(text)
    if sentences == 0:
        return 0.0
    return round(total / sentences, 1)


def print_report(text):
    """Print the full analysis report for the given text."""
    total_chars, no_space_chars = count_characters(text)
    total_words, unique_words = count_words(text)
    sentences = count_sentences(text)
    paragraphs = count_paragraphs(text)
    longest, shortest = longest_shortest_word(text)
    avg_len = avg_word_length(text)
    wps = words_per_sentence(text)
    freq = word_frequency(text)
    top = top_n_words(freq)

    sep = "=" * 60
    thin = "-" * 60

    print(f"\n{sep}")
    print(f"{'TEXT ANALYSIS REPORT':^60}")
    print(sep)
    print(f"{'Characters (total)':<25}: {total_chars:>6}")
    print(f"{'Characters (no spaces)':<25}: {no_space_chars:>6}")
    print(f"{'Words':<25}: {total_words:>6}")
    print(f"{'Unique words':<25}: {unique_words:>6}")
    print(f"{'Sentences':<25}: {sentences:>6}")
    print(f"{'Paragraphs':<25}: {paragraphs:>6}")
    print(thin)
    print(f"{'Longest word':<25}: {longest}  ({len(longest)} chars)")
    print(f"{'Shortest word':<25}: {shortest}  ({len(shortest)} chars)")
    print(f"{'Average word length':<25}: {avg_len:>6} chars")
    print(f"{'Words per sentence':<25}: {wps:>6}")
    print(thin)
    if top:
        print("Top 5 words:")
        for i, (word, count) in enumerate(top, 1):
            label = "time" if count == 1 else "times"
            print(f"  {i}. {word:<15} — {count} {label}")
    print(sep)


def get_text_from_user():
    """Prompt the user to paste multi-line text (blank line to finish)."""
    print("Paste your text below (press Enter on an empty line to finish):")
    print("-" * 60)
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    return " ".join(lines)


def main():
    """Entry point — get text and print the report."""
    text = get_text_from_user()
    if not text.strip():
        print("No text provided.")
        return
    print_report(text)


if __name__ == "__main__":
    main()
