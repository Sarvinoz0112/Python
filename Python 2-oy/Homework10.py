import os
import json
import csv

# Directory where user data will be stored
users_directory = 'users'


def ensure_directory_exists(directory):

    """Ensure the specified directory exists."""

    if not os.path.exists(directory):
        os.makedirs(directory)


def get_file_path(email, file_type):

    """Get the file path for a given email and file type."""

    return os.path.join(users_directory, f'{email}.{file_type}')


def email_exists(email):

    """Check if an email already exists in any file type."""

    for file_type in ["json", "csv", "txt"]:
        if os.path.exists(get_file_path(email, file_type)):
            return True
    return False


def save_to_json(file_path, data):

    """Save data to a JSON file."""

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def save_to_csv(file_path, data):

    """Save data to a CSV file."""

    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Email"])
        writer.writerow([data["name"], data["email"]])


def save_to_txt(file_path, data):

    """Save data to a TXT file."""

    with open(file_path, 'w') as file:
        file.write(f"Name: {data['name']}\nEmail: {data['email']}")


def save_personal_data():

    """Save personal data to a file."""

    name = input("Name: ")
    email = input("Email: ")

    if email_exists(email):
        print(f"The email '{email}' already exists. Please use a different email.")
        return

    file_type = input("File type (csv, json, txt): ").lower()
    if file_type not in ["csv", "json", "txt"]:
        print("Invalid file type. Please choose either csv, json, or txt.")
        return

    user_data = {"name": name, "email": email}
    file_path = get_file_path(email, file_type)

    if file_type == 'json':
        save_to_json(file_path, user_data)
    elif file_type == 'csv':
        save_to_csv(file_path, user_data)
    elif file_type == 'txt':
        save_to_txt(file_path, user_data)

    print(f"Data for {name} has been saved successfully.")


def read_from_json(file_path):

    """Read data from a JSON file."""

    with open(file_path, 'r') as file:
        data = json.load(file)
    print(f"Name: {data['name']}\nEmail: {data['email']}")


def read_from_csv(file_path):

    """Read data from a CSV file."""

    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        data = next(reader)
    print(f"Name: {data[0]}\nEmail: {data[1]}")


def read_from_txt(file_path):

    """Read data from a TXT file."""

    with open(file_path, 'r') as file:
        print(file.read())


def read_personal_data():

    """Read personal data from a file."""

    email = input("Enter email to read data: ")

    for file_type in ["json", "csv", "txt"]:
        file_path = get_file_path(email, file_type)
        if os.path.exists(file_path):
            if file_type == 'json':
                read_from_json(file_path)
            elif file_type == 'csv':
                read_from_csv(file_path)
            elif file_type == 'txt':
                read_from_txt(file_path)
            return

    print(f"No data found for email: {email}")


def delete_personal_data():

    """Delete personal data files."""

    email = input("Enter email to delete data: ")
    deleted = False

    for file_type in ["json", "csv", "txt"]:
        file_path = get_file_path(email, file_type)
        if os.path.exists(file_path):
            os.remove(file_path)
            deleted = True

    if deleted:
        print(f"Data for email {email} has been deleted.")
    else:
        print(f"No data found for email: {email}")


def menu():

    """Display the menu and handle user choices."""

    ensure_directory_exists(users_directory)

    while True:
        print("\n1: Save personal data")
        print("2: Read personal data")
        print("3: Delete personal data")
        print("4: Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            save_personal_data()
        elif choice == '2':
            read_personal_data()
        elif choice == '3':
            delete_personal_data()
        elif choice == '4':
            print("Exiting the program.\nGoodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    menu()