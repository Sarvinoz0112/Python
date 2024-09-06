import json
import os

database_file = 'books_exchange.json'

# Initialize database if not exists
if not os.path.exists(database_file):
    with open(database_file, 'w') as db_file:
        json.dump({"users": []}, db_file)

# Function to load data from JSON file
def load_data():
    """Load data from the JSON database file."""
    with open(database_file, 'r') as db_file:
        return json.load(db_file)

# Function to save data to JSON file
def save_data(data):
    """Save data to the JSON database file."""
    with open(database_file, 'w') as db_file:
        json.dump(data, db_file, indent=4)


def register(username, password):
    """
    Register a new user with the given username and password.
    """
    data = load_data()
    # Check if username already exists
    if any(user['username'] == username for user in data['users']):
        return "User already exists"
    
    # Add new user to the database
    data['users'].append({"username": username, "password": password, "read_books": [], "wanted_books": []})
    save_data(data)
    return "Registration successful"


def login(username, password):
    """
    Login a user with the given username and password.
    """
    data = load_data()
    # Check if username and password match
    for user in data['users']:
        if user['username'] == username and user['password'] == password:
            return "Login successful"
    return "Invalid username or password"


def add_read_book(username, book_title):
    """
    Add a book to the read list of the specified user.
    """
    data = load_data()
    # Find the user and add the book to their read list
    for user in data['users']:
        if user['username'] == username:
            user['read_books'].append(book_title)
            save_data(data)
            return "Book added to read list"
    return "User not found"


def add_wanted_book(username, book_title):
    """
    Add a book to the wanted list of the specified user.
    """
    data = load_data()
    # Find the user and add the book to their wanted list
    for user in data['users']:
        if user['username'] == username:
            user['wanted_books'].append(book_title)
            save_data(data)
            return "Book added to wanted list"
    return "User not found"

# Function to find exchanges for a user based on their wanted and read books
def find_exchange(username):
    """
    Find potential book exchanges for the specified user.
    """
    data = load_data()
    user = next((user for user in data['users'] if user['username'] == username), None)
    if not user:
        return "User not found"
    
    exchanges = []
    # Iterate through other users to find potential exchanges
    for other_user in data['users']:
        if other_user['username'] != username:
            # Find common books between the current user's wanted books and other user's read books
            common_books = set(user['wanted_books']) & set(other_user['read_books'])
            if common_books:
                exchanges.append({
                    "with": other_user['username'],
                    "books": list(common_books)
                })
    return exchanges

# Function to exchange books between two users
def exchange_books(username, offered_book, requested_book):
    """
    Exchange books between two users based on offered and requested books.

    Args:
    - username: The username of the user initiating the exchange.
    - offered_book: The title of the book being offered by the initiating user.
    - requested_book: The title of the book being requested by the initiating user.

    Returns:
    - str: A message indicating success or failure of the exchange attempt.
    """
    data = load_data()
    user = next((user for user in data['users'] if user['username'] == username), None)
    if not user:
        return "User not found"
    
    # Find another user who has the requested book and wants the offered book
    for other_user in data['users']:
        if requested_book in other_user['read_books'] and offered_book in user['read_books']:
            # Exchange books between the two users
            user['read_books'].remove(offered_book)
            user['read_books'].append(requested_book)
            other_user['read_books'].remove(requested_book)
            other_user['read_books'].append(offered_book)
            save_data(data)
            return f"Exchange successful with {other_user['username']}"
    return "No suitable exchange found"


def main_menu():
    """Display main menu options and handle user input."""
    while True:
        print("\nMain Menu")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            print(register(username, password))
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            if login(username, password) == "Login successful":
                user_menu(username)
            else:
                print("Invalid username or password")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


def user_menu(username):
    """Display user menu options and handle user input for logged in users."""
    while True:
        print("\nUser Menu")
        print(f"Logged in as {username}")
        print("1. Add Read Book")
        print("2. Add Wanted Book")
        print("3. Find Exchange")
        print("4. Exchange Books")
        print("5. Logout")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            book_title = input("Enter the title of the book you read: ")
            print(add_read_book(username, book_title))
        elif choice == '2':
            book_title = input("Enter the title of the book you want: ")
            print(add_wanted_book(username, book_title))
        elif choice == '3':
            exchanges = find_exchange(username)
            if exchanges:
                for exchange in exchanges:
                    print(f"Exchange with {exchange['with']} for books: {', '.join(exchange['books'])}")
            else:
                print("No exchanges found")
        elif choice == '4':
            offered_book = input("Enter the title of the book you are offering: ")
            requested_book = input("Enter the title of the book you want in exchange: ")
            print(exchange_books(username, offered_book, requested_book))
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()