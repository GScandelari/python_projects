# ============================================================
# intermediate/03-file-handling/solutions/03-challenge-solution.py
# ============================================================

import csv
import json
import os
from pathlib import Path
from datetime import datetime

SOLUTIONS_DIR = Path(os.path.dirname(os.path.abspath(__file__)))


# ----------------------------------------------------------
# Exercise 1 — CSV Merger and Transformer
# ----------------------------------------------------------
# APPROACH: Read both CSVs into a dict keyed by product. Merge
# by summing units; keep the price from whichever file has it.
# Sort by total revenue desc, then write combined CSV.

jan_path  = SOLUTIONS_DIR / "sales_jan.csv"
feb_path  = SOLUTIONS_DIR / "sales_feb.csv"
out_path  = SOLUTIONS_DIR / "sales_combined.csv"

jan_data = [
    {"product": "Notebook", "units": 50,  "price_per_unit": 2500.00},
    {"product": "Mouse",    "units": 120, "price_per_unit": 89.90},
    {"product": "Keyboard", "units": 75,  "price_per_unit": 199.90},
]
feb_data = [
    {"product": "Notebook", "units": 65, "price_per_unit": 2500.00},
    {"product": "Monitor",  "units": 30, "price_per_unit": 1899.00},
    {"product": "Mouse",    "units": 95, "price_per_unit": 89.90},
]

for path, data in [(jan_path, jan_data), (feb_path, feb_data)]:
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["product", "units", "price_per_unit"])
        writer.writeheader()
        writer.writerows(data)

# Merge
merged = {}
for path in [jan_path, feb_path]:
    with open(path, "r", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            p = row["product"]
            units = int(row["units"])
            price = float(row["price_per_unit"])
            if p in merged:
                merged[p]["total_units"] += units
            else:
                merged[p] = {"total_units": units, "price_per_unit": price}

combined = []
for product, info in merged.items():
    revenue = info["total_units"] * info["price_per_unit"]
    combined.append({
        "product": product,
        "total_units": info["total_units"],
        "price_per_unit": info["price_per_unit"],
        "total_revenue": revenue,
    })

combined.sort(key=lambda r: r["total_revenue"], reverse=True)

with open(out_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["product", "total_units", "price_per_unit", "total_revenue"])
    writer.writeheader()
    writer.writerows(combined)

print("--- Sales Combined ---")
print(f"  {'product':<12} | {'units':>5} | {'price/unit':>10} | {'revenue':>12}")
print("  " + "-" * 48)
for row in combined:
    print(f"  {row['product']:<12} | {row['total_units']:>5} | "
          f"{row['price_per_unit']:>10.2f} | {row['total_revenue']:>12.2f}")


# ----------------------------------------------------------
# Exercise 2 — JSON Database (CRUD)
# ----------------------------------------------------------
# APPROACH: The database is a plain dict written to JSON. Each
# CRUD function takes the in-memory db dict — callers are
# responsible for load/save. Auto-increments next_id.

db_path = SOLUTIONS_DIR / "contacts_db.json"

def load_db(path):
    if Path(path).exists():
        return json.loads(Path(path).read_text(encoding="utf-8"))
    return {"contacts": [], "next_id": 1}

def save_db(path, db):
    Path(path).write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")

def create(db, name, email, phone):
    contact = {"id": db["next_id"], "name": name, "email": email, "phone": phone}
    db["contacts"].append(contact)
    db["next_id"] += 1
    return contact

def read_all(db):
    return db["contacts"]

def update(db, contact_id, **fields):
    for c in db["contacts"]:
        if c["id"] == contact_id:
            c.update(fields)
            return c
    raise KeyError(f"Contact id={contact_id} not found.")

def delete(db, contact_id):
    db["contacts"] = [c for c in db["contacts"] if c["id"] != contact_id]

# Demo
db = load_db(db_path)
create(db, "Alice",  "alice@email.com",  "+55 11 99999-0001")
create(db, "Bob",    "bob@email.com",    "+55 21 98888-0002")
create(db, "Carol",  "carol@email.com",  "+55 31 97777-0003")
save_db(db_path, db)

print("\n--- All contacts ---")
for c in read_all(db):
    print(f"  {c}")

update(db, 2, phone="+55 21 99000-0002")
delete(db, 3)
save_db(db_path, db)

print("\n--- After update & delete ---")
for c in read_all(db):
    print(f"  {c}")


# ----------------------------------------------------------
# Exercise 3 — File Backup Utility
# ----------------------------------------------------------
# APPROACH: backup() reads source, builds a timestamped filename,
# writes to backup_dir. list_backups() uses rglob + sorted by
# name (timestamps make lexicographic == chronological).

import time

backup_dir = SOLUTIONS_DIR / "backups"

def backup(source_path, backup_dir):
    source = Path(source_path)
    dest   = Path(backup_dir)
    dest.mkdir(parents=True, exist_ok=True)
    content = source.read_text(encoding="utf-8")
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"{source.stem}_{stamp}{source.suffix}"
    backup_path = dest / backup_name
    backup_path.write_text(content, encoding="utf-8")
    return backup_path

def list_backups(backup_dir, original_name):
    backups = sorted(
        Path(backup_dir).glob(f"{original_name}_*"),
        key=lambda p: p.name,
        reverse=True,
    )
    print(f"\n--- Backups for '{original_name}' ---")
    for p in backups:
        print(f"  {p.name}  ({p.stat().st_size} bytes)")

notes = SOLUTIONS_DIR / "notes.txt"
for i, content in enumerate(["First version.", "Second version.", "Third version."], 1):
    notes.write_text(content, encoding="utf-8")
    bp = backup(notes, backup_dir)
    print(f"Backup {i}: {bp.name}")
    time.sleep(1)  # ensure unique timestamps

list_backups(backup_dir, "notes")

# Cleanup
notes.unlink(missing_ok=True)
for f in backup_dir.glob("*"):
    f.unlink()
backup_dir.rmdir()
for p in [jan_path, feb_path, out_path, db_path]:
    p.unlink(missing_ok=True)
