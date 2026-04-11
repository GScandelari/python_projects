# Mini-Project 03 — Text Analyzer

## Description

Paste any text and receive a complete statistical report: character counts, word frequency, longest/shortest words, readability index, and more.

## Concepts Used

| Concept | Where |
|---|---|
| `05-string-manipulation` | split, lower, strip, replace, f-strings |
| `03-data-structures` | Dict for word frequency, list for sorting |
| `04-functions` | One function per metric |
| `02-control-flow` | Loops for counting, sorting |

## How to Run

```bash
python main.py
```

No external libraries required — pure Python 3.

## Features

- Total characters (with and without spaces)
- Word count and unique word count
- Sentence count (`.` `!` `?`)
- Paragraph count
- Top 5 most frequent words (excluding common stopwords)
- Longest and shortest word
- Average word length
- Simple readability score (words per sentence)
- Full formatted report printed to terminal

## Example Output

```
============================================================
                      TEXT ANALYSIS REPORT
============================================================
Characters (total)   :  312
Characters (no spaces):  261
Words                :   52
Unique words         :   38
Sentences            :    4
Paragraphs           :    2
------------------------------------------------------------
Longest word         :  programming  (11 chars)
Shortest word        :  is  (2 chars)
Average word length  :  5.02 chars
Words per sentence   :  13.0
------------------------------------------------------------
Top 5 words:
  1. python       — 4 times
  2. language     — 3 times
  3. easy         — 2 times
  4. developers   — 2 times
  5. amazing      — 1 time
============================================================
```

## Challenge Yourself

- Let the user input text interactively line by line (end with empty line)
- Add detection of the most common character
- Export the report to a `.txt` file
