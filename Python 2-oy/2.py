import json
import os

contact_file = 'contacts.json'

def load_contacts():
    if os.path.exists(contact_file):
        with open(contact_file, 'r') as file:
            return json.load(file)
    return []

def save_contacts(contacts):
    with open(contact_file, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    full_name = input("Enter full name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email: ")
    
    contacts = load_contacts()
    for contact in contacts:
        if contact['phone_number'] == phone_number:
            print("Bu telefon raqam allaqachon ro'yxatda mavjud!")
            return
    contacts.append({
        'full_name': full_name,
        'phone_number': phone_number,
        'email': email
    })
    print("Kontakt muvaffaqiyatli qo'shildi!")

def search_contact_by_name():
    full_name = input("Enter full name to search: ")
    contacts = load_contacts()
    results = [contact for contact in contacts if contact['full_name'] == full_name]
    for result in results:
        print(result)

def delete_contact_by_phone():
    phone_number = input("Enter phone number to delete: ")
    contacts = load_contacts()
    contacts = [contact for contact in contacts if contact['phone_number'] != phone_number]
    print("Kontakt muvaffaqiyatli o'chirildi!")

def update_contact_name():
    phone_number = input("Enter phone number to update: ")
    new_full_name = input("Enter new full name: ")
    contacts = load_contacts()
    for contact in contacts:
        if contact['phone_number'] == phone_number:
            contact['full_name'] = new_full_name
            print("Kontakt nomi muvaffaqiyatli o'zgartirildi!")
        else:
            print("Telefon raqam topilmadi!")

def list_all_contacts():
    contacts = load_contacts()
    for contact in contacts:
        print(contact)

def delete_all_contacts():
    save_contacts([])
    print("Barcha kontaktlar muvaffaqiyatli o'chirildi!")

def menu():
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
            delete_contact_by_phone()
        elif choice == '4':
            update_contact_name()
        elif choice == '5':
            list_all_contacts()
        elif choice == '6':
            delete_all_contacts()
        elif choice == '7':
            print("Exiting the program.\nGood bye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    menu()