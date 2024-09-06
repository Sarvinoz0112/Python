import json
import os

contact_file = 'contacts.json'


def load_contacts():

    """Load contacts from the JSON file."""

    if os.path.exists(contact_file):
        with open(contact_file, 'r') as file:
            return json.load(file)
    return []


def save_contacts(contacts):

    """Save contacts to the JSON file."""

    with open(contact_file, 'w') as file:
        json.dump(contacts, file, indent=4)


def is_valid_email(email):
    """Validate the email format."""
    return (
        email.count('@') == 1 and             # Checks if there is exactly one '@' symbol
        email[0] != '@' and                    # Ensures the email doesn't start with '@'
        email.count('.') > 0 and               # Checks if there is at least one '.'
        email.rfind('.') > email.find('@')     # Ensures the last '.' comes after the '@'
    )


def add_contact():

    """Add a new contact."""

    full_name = input("Enter full name: ").strip().title()

    phone_number = input("Enter phone number: ")
    while not phone_number.isdigit():
        print("Invalid phone number format! Please enter a valid phone number.")
        phone_number = input("Enter phone number: ")

    email = input("Enter email: ")
    while not is_valid_email(email):
        print("Invalid email format! Please enter a valid email.")
        email = input("Enter email: ")

    contacts = load_contacts()
    for contact in contacts:
        if contact['phone_number'] == int(phone_number):
            print("This phone number is already in the contacts list!")
            return

    contacts.append({
        'full_name': full_name,
        'phone_number': int(phone_number),
        'email': email
    })
    save_contacts(contacts)
    print("Contact successfully added!")


def search_contact_by_name():

    """Search contacts by name."""

    name = input('Enter the name to search: ').strip().title()
    contacts = load_contacts()
    found = False
    for contact in contacts:
        if name in contact['full_name'].title():
            print(f"Name: {contact['full_name']}\nPhone: {contact['phone_number']}\nEmail: {contact['email']}")
            found = True
    if not found:
        print(f"No contact found with the name '{name}'.")


def delete_contact_by_phone(phone_number):

    """Delete contact by phone number."""

    if not phone_number.isdigit():
        print("Invalid input! Please enter a valid phone number.")
        return

    phone_number = int(phone_number)
    contacts = load_contacts()
    updated_contacts = [contact for contact in contacts if contact['phone_number'] != phone_number]
    save_contacts(updated_contacts)
    print("Contact successfully deleted!")


def update_contact_name(phone_number, new_full_name):

    """Update contact's name by phone number."""

    phone_number = int(phone_number)
    contacts = load_contacts()
    updated = False
    for contact in contacts:
        if contact['phone_number'] == phone_number:
            contact['full_name'] = new_full_name.title()
            save_contacts(contacts)
            print("Contact name successfully updated!")
            updated = True
            break
    if not updated:
        print("Phone number not found!")


def list_all_contacts():

    """List all contacts."""

    contacts = load_contacts()
    if not contacts:
        print("No contacts found.")
    else:
        print("List of all contacts:")
        for contact in contacts:
            print(f"\nName: {contact['full_name']}\nPhone: {contact['phone_number']}\nEmail: {contact['email']}\n")


def delete_all_contacts():

    """Delete all contacts."""

    if os.path.exists(contact_file):
        os.remove(contact_file)
        print("All contacts successfully deleted!")
    else:
        print("Contacts file not found!")


def menu():

    """Display menu options and handle user input."""
    
    while True:
        print("\n1. Add new contact")
        print("2. Search contact")
        print("3. Delete contact")
        print("4. Change contact name")
        print("5. View all contacts")
        print("6. Delete all contacts")
        print("7. Exit")
        choice = input("Choose an option (1-7): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            search_contact_by_name()
        elif choice == '3':
            phone_number = input("Enter phone number to delete: ")
            delete_contact_by_phone(phone_number)
        elif choice == '4':
            phone_number = input("Enter phone number to update: ")
            new_full_name = input("Enter new full name: ").strip()
            update_contact_name(phone_number, new_full_name)
        elif choice == '5':
            list_all_contacts()
        elif choice == '6':
            delete_all_contacts()
        elif choice == '7':
            print("Exiting the program.\nGoodbye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    menu()