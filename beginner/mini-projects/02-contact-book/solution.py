# ============================================================
# Mini-Project 02 — Contact Book (SOLUTION)
# ============================================================


def validate_email(email):
    """Return True if email contains '@' and at least one '.' after '@'."""
    if "@" not in email:
        return False
    local, _, domain = email.partition("@")
    return "." in domain and len(local) > 0


def add_contact(contacts):
    """Prompt the user for contact details and add to the list."""
    print()
    name = input("Name:  ").strip().title()
    if not name:
        print("Name cannot be empty.")
        return

    phone = input("Phone: ").strip()

    while True:
        email = input("Email: ").strip().lower()
        if validate_email(email):
            break
        print("  Invalid email. Must contain '@' and a domain (e.g. user@mail.com).")

    contacts.append({"name": name, "phone": phone, "email": email})
    print(f"Contact '{name}' added!")


def search_contacts(contacts, query):
    """Return contacts whose name contains the query (case-insensitive)."""
    query = query.lower()
    return [c for c in contacts if query in c["name"].lower()]


def list_contacts(contacts):
    """Print all contacts as a formatted table."""
    if not contacts:
        print("  No contacts found.")
        return

    print()
    print(f"{'Name':<22} {'Phone':<22} {'Email':<30}")
    print("-" * 74)
    for c in sorted(contacts, key=lambda x: x["name"]):
        print(f"{c['name']:<22} {c['phone']:<22} {c['email']:<30}")


def edit_contact(contacts):
    """Let the user select a contact and edit one or more fields."""
    if not contacts:
        print("  No contacts to edit.")
        return

    query = input("Search contact to edit: ").strip()
    results = search_contacts(contacts, query)

    if not results:
        print("  No contacts found.")
        return

    for i, c in enumerate(results, 1):
        print(f"  {i}. {c['name']} — {c['phone']} — {c['email']}")

    try:
        idx = int(input("Select number: ")) - 1
        contact = results[idx]
    except (ValueError, IndexError):
        print("  Invalid selection.")
        return

    print(f"Editing '{contact['name']}' — leave blank to keep current value.")
    new_name = input(f"  Name  [{contact['name']}]: ").strip().title()
    new_phone = input(f"  Phone [{contact['phone']}]: ").strip()
    new_email = input(f"  Email [{contact['email']}]: ").strip().lower()

    if new_name:
        contact["name"] = new_name
    if new_phone:
        contact["phone"] = new_phone
    if new_email:
        if validate_email(new_email):
            contact["email"] = new_email
        else:
            print("  Invalid email — email not updated.")

    print("Contact updated!")


def delete_contact(contacts):
    """Remove a contact selected by the user."""
    if not contacts:
        print("  No contacts to delete.")
        return

    query = input("Search contact to delete: ").strip()
    results = search_contacts(contacts, query)

    if not results:
        print("  No contacts found.")
        return

    for i, c in enumerate(results, 1):
        print(f"  {i}. {c['name']} — {c['phone']}")

    try:
        idx = int(input("Select number: ")) - 1
        contact = results[idx]
    except (ValueError, IndexError):
        print("  Invalid selection.")
        return

    confirm = input(f"Delete '{contact['name']}'? (y/n): ").strip().lower()
    if confirm == "y":
        contacts.remove(contact)
        print("Contact deleted.")
    else:
        print("Cancelled.")


def show_menu():
    """Print the main menu."""
    print("\n" + "=" * 35)
    print("         CONTACT BOOK")
    print("=" * 35)
    print("  [1] Add contact")
    print("  [2] Search")
    print("  [3] List all")
    print("  [4] Edit contact")
    print("  [5] Delete contact")
    print("  [0] Exit")


def main():
    """Main menu loop."""
    contacts = []

    actions = {
        "1": lambda: add_contact(contacts),
        "2": lambda: list_contacts(
            search_contacts(contacts, input("Search by name: ").strip())
        ),
        "3": lambda: list_contacts(contacts),
        "4": lambda: edit_contact(contacts),
        "5": lambda: delete_contact(contacts),
    }

    while True:
        show_menu()
        choice = input("> ").strip()
        if choice == "0":
            print("\nGoodbye!")
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("  Invalid option. Choose 0–5.")


if __name__ == "__main__":
    main()
