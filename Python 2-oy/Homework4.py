employees = dict()

def add_employee():
    employee_id = input("Enter employee ID: ")
    if employee_id in employees:
        print("This ID already exists.")
        return
    
    full_name = input("Enter employee's full name: ")

    while True:
        phone_number = input("Enter phone number: ")
        if phone_number.isdigit():
            break
        else:
            print("Invalid phone number. Please enter only digits.")

    salary = float(input("Enter salary: "))
    position = input("Enter position: ")
    
    employees[employee_id] = {
        'full_name': full_name,
        'phone_number': phone_number,
        'salary': salary,
        'position': position
    }
    print("New employee added.")

def view_employees():
    if not employees:
        print("No employees found.")
        return
    for employee_id, details in employees.items():
        print(f"ID: {employee_id}")
        for key, value in details.items():
            print(f"{key}: {value}")
        print()

def search_employee_by_name():
    search_name = input("Enter the name of the employee you are looking for: ").lower()
    found = False
    for details in employees.values():
        if details['full_name'].lower() == search_name:
            found = True
            for key, value in details.items():
                print(f"{key}: {value}")
            print()
    if not found:
        print("No employee found with that name.")

def delete_employee_by_id():
    employee_id = input("Enter the ID of the employee you want to delete: ")
    if employee_id in employees:
        del employees[employee_id]
        print("Employee deleted.")
    else:
        print("No employee found with that ID.")

def menu():
    while True:
        text = """
        1. Add a new employee
        2. View all employees
        3. Search employee by name
        4. Delete employee by ID
        5. Exit
        """
        print(text)
        choice = input("Enter your choice: ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee_by_name()
        elif choice == '4':
            delete_employee_by_id()
        elif choice == '5':
            print("Exiting program.\nGood bye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()