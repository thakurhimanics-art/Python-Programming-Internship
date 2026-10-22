"""
Task 3: Persistent Contact Book
Author: Himani Thakur
Description:
    A command-line contact management system that allows users to add, view,
    search, update, and delete contacts. Contacts are persistently saved in
    a JSON file with graceful handling of missing or corrupted data.
"""

import json
import os
import re

# Default contacts file in the same directory as this script
DEFAULT_STORAGE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "contacts.json")


def load_contacts(filepath: str = DEFAULT_STORAGE_FILE) -> dict:
    """
    Load contacts dictionary from a JSON file.
    If the file does not exist or is corrupted, returns an empty dictionary.
    """
    if not os.path.exists(filepath):
        return {}

    try:
        with open(filepath, mode="r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, dict):
                return data
            return {}
    except (json.JSONDecodeError, OSError):
        # File was corrupted or unreadable; return empty dict safely
        return {}


def save_contacts(filepath: str, contacts: dict) -> bool:
    """
    Save the contacts dictionary to a JSON file.
    Returns True if successful, False otherwise.
    """
    try:
        os.makedirs(os.path.dirname(os.path.abspath(filepath)), exist_ok=True)
        with open(filepath, mode="w", encoding="utf-8") as file:
            json.dump(contacts, file, indent=4, ensure_ascii=False)
        return True
    except OSError as e:
        print(f"[Storage Error] Could not save contacts: {e}")
        return False


def validate_phone(phone: str) -> bool:
    """Ensure phone number contains at least 7 digits and valid phone characters."""
    digits = re.sub(r"\D", "", phone)
    return len(digits) >= 7


def add_contact(contacts: dict, name: str, phone: str, email: str = "") -> tuple[bool, str]:
    """
    Add a new contact to the contacts dictionary.
    Returns (success, message).
    """
    name_clean = name.strip()
    phone_clean = phone.strip()
    email_clean = email.strip()

    if not name_clean:
        return False, "Contact name cannot be empty."

    if not phone_clean or not validate_phone(phone_clean):
        return False, "Invalid phone number. It must contain at least 7 digits."

    # Case-insensitive name collision check
    for existing_name in contacts:
        if existing_name.lower() == name_clean.lower():
            return False, f"Contact '{name_clean}' already exists. Use update option instead."

    contacts[name_clean] = {
        "phone": phone_clean,
        "email": email_clean,
    }
    return True, f"Contact '{name_clean}' added successfully."


def search_contacts(contacts: dict, query: str) -> dict:
    """
    Search contacts matching name, phone number, or email.
    Returns a dictionary of matched contacts.
    """
    q = query.strip().lower()
    if not q:
        return contacts

    results = {}
    for name, info in contacts.items():
        if (q in name.lower() or
            q in info.get("phone", "").lower() or
            q in info.get("email", "").lower()):
            results[name] = info
    return results


def update_contact(contacts: dict, name: str, new_phone: str = None, new_email: str = None) -> tuple[bool, str]:
    """
    Update an existing contact's phone and/or email.
    Returns (success, message).
    """
    name_clean = name.strip()
    target_key = None
    for existing_name in contacts:
        if existing_name.lower() == name_clean.lower():
            target_key = existing_name
            break

    if not target_key:
        return False, f"Contact '{name_clean}' not found."

    if new_phone is not None and new_phone.strip():
        if not validate_phone(new_phone):
            return False, "Invalid new phone number format."
        contacts[target_key]["phone"] = new_phone.strip()

    if new_email is not None and new_email.strip():
        contacts[target_key]["email"] = new_email.strip()

    return True, f"Contact '{target_key}' updated successfully."


def delete_contact(contacts: dict, name: str) -> tuple[bool, str]:
    """
    Delete a contact by name.
    Returns (success, message).
    """
    name_clean = name.strip()
    target_key = None
    for existing_name in contacts:
        if existing_name.lower() == name_clean.lower():
            target_key = existing_name
            break

    if not target_key:
        return False, f"Contact '{name_clean}' not found."

    del contacts[target_key]
    return True, f"Contact '{target_key}' deleted successfully."


def display_contacts(contacts: dict):
    """Print contacts in a clean, tabular format."""
    if not contacts:
        print("\n[Notice] No contacts found.")
        return

    print("\n" + "-" * 60)
    print(f"{'Name':<20} | {'Phone':<18} | {'Email':<18}")
    print("-" * 60)
    for name, info in sorted(contacts.items()):
        phone = info.get("phone", "N/A")
        email = info.get("email", "N/A") or "N/A"
        print(f"{name:<20} | {phone:<18} | {email:<18}")
    print("-" * 60)
    print(f"Total contacts: {len(contacts)}")


def main():
    storage_path = DEFAULT_STORAGE_FILE
    contacts = load_contacts(storage_path)

    # If first run with empty storage, provide 2 fictional demo contacts
    if not contacts and not os.path.exists(storage_path):
        add_contact(contacts, "Alice Sharma", "+91 98765 43210", "alice.sharma@example.com")
        add_contact(contacts, "Bob Patel", "+91 91234 56789", "bob.patel@example.com")
        save_contacts(storage_path, contacts)

    print("=" * 50)
    print("             CONTACT BOOK APPLICATION            ")
    print("=" * 50)

    while True:
        print("\n--- Main Menu ---")
        print("1. View All Contacts")
        print("2. Add New Contact")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("\nEnter choice (1-6): ").strip()

        if choice == "1":
            display_contacts(contacts)

        elif choice == "2":
            print("\n--- Add New Contact ---")
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address (optional, press Enter to skip): ")

            success, msg = add_contact(contacts, name, phone, email)
            print(f">>> {msg}")
            if success:
                save_contacts(storage_path, contacts)

        elif choice == "3":
            print("\n--- Search Contacts ---")
            query = input("Enter search term (name, phone, or email): ")
            matched = search_contacts(contacts, query)
            display_contacts(matched)

        elif choice == "4":
            print("\n--- Update Contact ---")
            name = input("Enter exact name of contact to update: ")
            print("Leave blank to keep existing value.")
            new_phone = input("Enter new phone number: ")
            new_email = input("Enter new email address: ")

            phone_arg = new_phone if new_phone.strip() else None
            email_arg = new_email if new_email.strip() else None

            success, msg = update_contact(contacts, name, phone_arg, email_arg)
            print(f">>> {msg}")
            if success:
                save_contacts(storage_path, contacts)

        elif choice == "5":
            print("\n--- Delete Contact ---")
            name = input("Enter name of contact to delete: ")
            confirm = input(f"Are you sure you want to delete '{name}'? (y/n): ").strip().lower()
            if confirm in ("y", "yes"):
                success, msg = delete_contact(contacts, name)
                print(f">>> {msg}")
                if success:
                    save_contacts(storage_path, contacts)
            else:
                print("Deletion cancelled.")

        elif choice in ("6", "exit", "quit", "q"):
            print("Thank you for using Contact Book. Goodbye!")
            break
        else:
            print("[Invalid Choice] Please select a number between 1 and 6.")


if __name__ == "__main__":
    main()
