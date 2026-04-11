# Mini-Project 02 — Contact Book

## Description

A terminal-based contact book. The user can add, search, edit, delete, and list contacts through a menu-driven interface. All data lives in memory during the session.

## Concepts Used

| Concept | Where |
|---|---|
| `03-data-structures` | List of dicts as the contact database |
| `04-functions` | One function per operation (add, search, delete…) |
| `05-string-manipulation` | f-string table, strip, lower for search |
| `02-control-flow` | Main menu loop, input validation |

## How to Run

```bash
python main.py
```

No external libraries required — pure Python 3.

## Features

- Add contacts (name, phone, email)
- Search by name — partial match, case-insensitive
- Edit any field of an existing contact
- Delete a contact
- List all contacts in a formatted table
- Basic email validation (must contain `@` and `.`)

## Example Output

```
=============================
        CONTACT BOOK
=============================
[1] Add contact
[2] Search
[3] List all
[4] Edit contact
[5] Delete contact
[0] Exit
> 1

Name:  Alice Smith
Phone: +55 11 99999-0000
Email: alice@email.com
Contact added!

> 3

Name             Phone                Email
-------------------------------------------------
Alice Smith      +55 11 99999-0000    alice@email.com
```

## Challenge Yourself

- Save contacts to a `.txt` or `.csv` file so data persists between runs
- Add a "favorite" flag and a command to list only favorites
- Sort the contact list alphabetically
