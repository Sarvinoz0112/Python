import json

class Product:
    def __init__(self, name, price):
        """Initialize the product with a name and price."""
        self.name = name
        self.price = price

    def calculate_total_price(self):
        """Calculate the total price of the product."""
        return self.price

    def add_to_file(self, filename):
        """Add the product details to a JSON file."""
        product_data = {
            'type': self.__class__.__name__,
            'name': self.name,
            'price': self.price
        }
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []

        data.append(product_data)

        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    def show_data(self):
        """Print the product details."""
        print(f"\nAdded succesfully.\nType: {self.__class__.__name__},\nName: {self.name},\nPrice: {self.price}\n")

class Book(Product):
    def __init__(self, name, price, pages):
        """Initialize the book with name, price, and number of pages."""
        super().__init__(name, price)
        self.type = 'Book'
        self.pages = pages

    def calculate_total_price(self):
        """Calculate the total price of the book."""
        return self.price

    def add_to_file(self):
        """Add the book details to books.json."""
        super().add_to_file('books.json')

    def show_data(self):
        """Print the book details."""
        print(f"\nAdded succesfully.\nType: {self.type},\nName: {self.name},\nPrice: {self.price},\nPages: {self.pages}\n")

class Clothing(Product):
    def __init__(self, name, price, color):
        """Initialize the clothing item with name, price, and color."""
        super().__init__(name, price)
        self.type = 'Clothing'
        self.color = color

    def calculate_total_price(self):
        """Calculate the total price of the clothing item."""
        return self.price

    def add_to_file(self):
        """Add the clothing details to clothing.json."""
        super().add_to_file('clothing.json')

    def show_data(self):
        """Print the clothing details."""
        print(f"\nAdded succesfully.\nType: {self.type},\nName: {self.name},\nPrice: {self.price},\nColor: {self.color}\n")

class Electronics(Product):
    def __init__(self, name, price, made_in, year):
        """Initialize the electronics item with name, price, country of origin, and year of manufacture."""
        super().__init__(name, price)
        self.type = 'Electronics'
        self.made_in = made_in
        self.year = year

    def calculate_total_price(self):
        """Calculate the total price of the electronics item."""
        return self.price

    def add_to_file(self):
        """Add the electronics details to electronics.json."""
        super().add_to_file('electronics.json')

    def show_data(self):
        """Print the electronics details."""
        print(f"\nAdded succesfully.\nType: {self.type},\nName: {self.name},\nPrice: {self.price},\nMade in: {self.made_in},\nYear: {self.year}\n")

def get_float_input(prompt):
    """Prompt the user for a float input and validate it."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_int_input(prompt):
    """Prompt the user for an integer input and validate it."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer value.")

def main_menu():
    """Display the main menu and handle user choices."""
    while True:
        print("\nMain Menu:")
        print("1. Add Book")
        print("2. Add Clothing")
        print("3. Add Electronics")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_book()
        elif choice == '2':
            add_clothing()
        elif choice == '3':
            add_electronics()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def add_book():
    """Prompt the user to enter book details and add it to the file."""
    name = input("Enter book name: ")
    price = get_float_input("Enter book price: ")
    pages = get_int_input("Enter number of pages: ")
    book = Book(name, price, pages)
    book.show_data()
    book.add_to_file()

def add_clothing():
    """Prompt the user to enter clothing details and add it to the file."""
    name = input("Enter clothing name: ")
    price = get_float_input("Enter clothing price: ")
    color = input("Enter clothing color: ")
    clothing = Clothing(name, price, color)
    clothing.show_data()
    clothing.add_to_file()

def add_electronics():
    """Prompt the user to enter electronics details and add it to the file."""
    name = input("Enter electronics name: ")
    price = get_float_input("Enter electronics price: ")
    made_in = input("Enter country where it is made: ")
    year = get_int_input("Enter year of manufacture: ")
    electronics = Electronics(name, price, made_in, year)
    electronics.show_data()
    electronics.add_to_file()

if __name__ == "__main__":
    main_menu()
