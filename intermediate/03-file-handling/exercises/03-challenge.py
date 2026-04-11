# ============================================================
# intermediate/03-file-handling/exercises/03-challenge.py
# Topic: File Handling — advanced patterns
# Difficulty: Challenge
# ============================================================

import csv
import json
import os
from pathlib import Path
from datetime import datetime

EXERCISES_DIR = Path(os.path.dirname(__file__))


# Exercise 1 — CSV Merger and Transformer
# -----------------------------------------
# Create two CSV files:
#   "sales_jan.csv": product,units,price_per_unit
#                    Notebook,50,2500.00 / Mouse,120,89.90 / Keyboard,75,199.90
#   "sales_feb.csv": same columns
#                    Notebook,65,2500.00 / Monitor,30,1899.00 / Mouse,95,89.90
#
# Then write code to:
#   a) Read both files and merge the data
#   b) If a product appears in both months, SUM the units
#   c) Calculate total revenue per product (units * price)
#   d) Sort by total revenue descending
#   e) Write the result to "sales_combined.csv" with columns:
#      product, total_units, price_per_unit, total_revenue
#   f) Print the combined report to the console
#
# Expected:
#   product    | total_units | price/unit | total_revenue
#   Notebook   | 115         | 2500.00    | 287500.00
#   Monitor    | 30          | 1899.00    |  56970.00
#   ...

# Write your code here


# Exercise 2 — JSON Database (CRUD)
# -----------------------------------
# Build a simple file-based "database" for contacts stored as JSON.
# The database is a JSON file: "contacts_db.json"
# Format: { "contacts": [ {id, name, email, phone}, ... ], "next_id": 1 }
#
# Implement these functions:
#   load_db(path)             → loads and returns the database dict
#   save_db(path, db)         → saves the database dict to file
#   create(db, name, email, phone) → adds a new contact, auto-increments id
#   read_all(db)              → returns list of all contacts
#   update(db, id, **fields)  → updates fields of contact with given id
#   delete(db, id)            → removes contact with given id
#
# Then demonstrate all operations:
#   - Create 3 contacts
#   - List all
#   - Update one contact's phone
#   - Delete one contact
#   - List all again

# Write your code here


# Exercise 3 — File Backup Utility
# ----------------------------------
# Write a function backup(source_path, backup_dir) that:
#   a) Reads a source text file
#   b) Creates the backup_dir if it doesn't exist
#   c) Names the backup: originalname_YYYYMMDD_HHMMSS.ext
#      (e.g. notes_20260411_143000.txt)
#   d) Writes the backup file
#   e) Returns the path to the backup file
#
# Also write a function list_backups(backup_dir, original_name) that:
#   - Lists all backup files matching the original name
#   - Prints them sorted by date (newest first)
#   - Prints the size of each backup in bytes
#
# Demonstrate by:
#   1. Creating a "notes.txt" file with some content
#   2. Backing it up 3 times (modify content between backups)
#   3. Listing all backups

# Write your code here
