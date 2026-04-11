# Mini-Project 01 — Number Guessing Game

## Description

A terminal-based number guessing game where the player tries to guess a secret number. The program gives "too high" / "too low" hints after each attempt and tracks performance.

## Concepts Used

| Concept | Where |
|---|---|
| `01-fundamentals` | Variables, input(), type conversion |
| `02-control-flow` | while loop, if/elif/else, break |
| `04-functions` | Modular design, return values, docstrings |
| `03-data-structures` | List for guess history |

## How to Run

```bash
python main.py
```

No external libraries required — pure Python 3.

## Features

- 3 difficulty levels (Easy / Medium / Hard)
- Attempt limit per level
- Guess history shown each round
- Performance rating at the end
- Option to play again

## Difficulty Levels

| Level | Range | Max Attempts |
|---|---|---|
| Easy | 1 – 50 | 10 |
| Medium | 1 – 100 | 7 |
| Hard | 1 – 200 | 5 |

## Example Output

```
=============================
   NUMBER GUESSING GAME
=============================
Select difficulty:
  1. Easy   (1-50,  10 attempts)
  2. Medium (1-100,  7 attempts)
  3. Hard   (1-200,  5 attempts)
> 2

[Attempt 1/7] Your guess: 50
Too low!  History: [50]

[Attempt 2/7] Your guess: 75
Too high! History: [50, 75]

[Attempt 3/7] Your guess: 63
Correct! The number was 63.

Attempts used: 3 / 7
Rating: Excellent!
Play again? (y/n):
```

## Challenge Yourself

After completing `main.py`, try extending it:
- Add a scoring system that saves the best score
- Allow the player to set a custom range
- Add a "give up" option that reveals the number
