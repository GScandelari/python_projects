# ============================================================
# Mini-Project 02 — Contact Book
# Build a menu-driven contact manager using beginner concepts.
# ============================================================
#
# HOW TO APPROACH THIS PROJECT:
#   1. Read the README.md for the full feature list
#   2. Choose a data structure to store contacts (hint: list of dicts)
#   3. Build one function per operation, test each independently
#   4. Wire everything into a main menu loop
#   5. Check solution.py only after you have a working version
#
# DATA STRUCTURE SUGGESTION:
#   contacts = [
#       {"name": "Alice Smith", "phone": "+55 11 99999-0000", "email": "alice@email.com"},
#       ...
#   ]
#
# SUGGESTED FUNCTIONS TO BUILD:
#   - add_contact(contacts)          → adds a new contact dict to the list
#   - search_contacts(contacts, query) → returns list of matches (partial, case-insensitive)
#   - list_contacts(contacts)        → prints a formatted table
#   - edit_contact(contacts)         → lets user pick a contact and edit a field
#   - delete_contact(contacts)       → removes a contact by name
#   - validate_email(email)          → returns True if email contains '@' and '.'
#   - show_menu()                    → prints the menu options
#   - main()                         → main loop
#
# FORMATTING HINT — aligned table with f-strings:
#   print(f"{'Name':<20} {'Phone':<20} {'Email':<30}")
# ============================================================

# Write your code here


if __name__ == "__main__":
    main()
