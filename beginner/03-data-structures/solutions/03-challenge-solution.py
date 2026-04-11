# ============================================================
# beginner/03-data-structures/solutions/03-challenge-solution.py
# ============================================================

# ----------------------------------------------------------
# Exercise 1 — Phonebook (dict-based)
# ----------------------------------------------------------
# APPROACH: Use a dict {name: {"phone": ..., "email": ...}}.
# Normalize names with .title() for case-insensitive lookup.

def phonebook_demo():
    book = {}

    def add(name, phone, email=""):
        book[name.title()] = {"phone": phone, "email": email}
        print(f"  Added: {name.title()}")

    def search(name):
        contact = book.get(name.title())
        if contact:
            print(f"  {name.title()}: {contact}")
        else:
            print(f"  '{name}' not found.")

    def delete(name):
        key = name.title()
        if key in book:
            del book[key]
            print(f"  Deleted: {key}")
        else:
            print(f"  '{name}' not found.")

    print("--- Phonebook demo ---")
    add("Alice", "+55 11 99999-0001", "alice@email.com")
    add("Bob",   "+55 21 98888-0002")
    add("Carol", "+55 31 97777-0003", "carol@email.com")

    search("alice")    # found
    search("dave")     # not found

    delete("bob")
    search("bob")      # not found after deletion
    print(f"  Contacts remaining: {list(book.keys())}")

phonebook_demo()


# ----------------------------------------------------------
# Exercise 2 — Word frequency counter (top 5)
# ----------------------------------------------------------
# APPROACH: split() → frequency dict → sort by count desc → top 5.

paragraph = (
    "Python is amazing and Python is fun. "
    "Many developers love Python. "
    "Python makes programming easy and fun."
)

words = paragraph.lower().replace(".", "").split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

top5 = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:5]
print("\n--- Top 5 words ---")
for i, (word, count) in enumerate(top5, 1):
    print(f"  {i}. {word:<12} — {count} time(s)")


# ----------------------------------------------------------
# Exercise 3 — Shopping cart
# ----------------------------------------------------------
# APPROACH: Compute total by summing price*qty. Apply 10%
# discount only if total exceeds 100. Format as a receipt.

cart = [
    {"name": "Notebook", "price": 2500.00, "qty": 1},
    {"name": "Mouse",    "price":   89.90, "qty": 2},
    {"name": "Keyboard", "price":  199.90, "qty": 1},
]

print("\n--- Shopping Cart ---")
subtotal = 0
for item in cart:
    line_total = item["price"] * item["qty"]
    subtotal += line_total
    print(f"  {item['name']:<12} x{item['qty']}  R$ {line_total:>8.2f}")

print("-" * 35)
if subtotal > 100:
    discount = subtotal * 0.10
    total = subtotal - discount
    print(f"  Subtotal           R$ {subtotal:>8.2f}")
    print(f"  Discount (10%)   - R$ {discount:>8.2f}")
else:
    total = subtotal
    discount = 0

print(f"  TOTAL              R$ {total:>8.2f}")
