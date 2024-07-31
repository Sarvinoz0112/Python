#Ex 1
students = dict()
num_students = 0

while num_students < 3:
    name = input("Ismingizni kiriting: ")
    physics = int(input("Fizikadan bahoyingizni kiriting: "))
    math = int(input("Matenatikadan bahoyingizni kiriting: "))
    music = int(input("Musiqadan bahoyingizni kiriting: "))

    students[name] = {
        'fizika': physics,
        'math': math,
        'music': music
    }
    
    num_students += 1

print(students)


#Ex 2
contacts = dict()

def add_contact():
    name = input('Enter the name of the contact: ')
    if name in contacts:
        print("This contact already exists")
    else:       
        number = input('Enter the number of the contact: ')
        contacts[name] = number
    return show_menu()

def search_contact():
    name = input('Enter the name of the contact to search: ')
    if name in contacts:
        print(f"Contact found: {name} - {contacts[name]}")
    else:
        print("Contact not found")
    return show_menu()

def edit_contact():
    name = input('Enter the name of the contact to edit: ')
    if name in contacts:
        new_number = input(f'Enter the new number for {name}: ')
        contacts[name] = new_number
        print(f"Contact updated: {name} - {contacts[name]}")
    else:
        print("Contact not found")
    return show_menu()

def delete_contact():
    name = input('Enter the name of the contact to delete: ')
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted")
    else:
        print("Contact not found")
    return show_menu()

def show_all_contacts():
    if contacts:
        for name, number in contacts.items():
            print(f"{name}:\t{number}")
    else:
        print("No contacts found")
    return show_menu()

def show_menu():
    text = """
1. Add contact
2. Search contact by name
3. Edit contact
4. Delete contact
5. Show all contacts
6. Exit
"""
    print(text)
    user_input = int(input("Choose from the menu: "))
    if user_input == 1:
        add_contact()
    elif user_input == 2:
        search_contact()
    elif user_input == 3:
        edit_contact()
    elif user_input == 4:
        delete_contact()
    elif user_input == 5:
        show_all_contacts()
    else:
        print("Goodbye!")
        return

show_menu()