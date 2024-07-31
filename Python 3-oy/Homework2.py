import json

class Concert:
    def __init__(self, author, date, total_tickets, price):
        """
        Initialize Concert object with author, date, total tickets, and price.
        """
        self.author = author
        self.date = date
        self.total_tickets = total_tickets
        self.price = price
        self.sold_tickets = 0
        self.tickets = []  # List to store ticket sale details

    def get_price(self):
        """
        Get formatted price of a ticket.
        """
        return f"${self.price}"

    def get_full_info(self):
        """
        Get full information about the concert.
        """
        return f"Author: {self.author}, Date: {self.date}, Total Tickets: {self.total_tickets}, Price: {self.get_price()}"

    def buy_ticket(self, full_name, phone_number, quantity):
        """
        Buy tickets for the concert.
        """
        if quantity > self.available_tickets_count():
            print("Not enough tickets available.")
            return False
        
        # Create ticket information dictionary
        ticket_info = {
            'full_name': full_name,
            'phone_number': phone_number,
            'quantity': quantity
        }
        
        # Add ticket sale to tickets list, update sold and total tickets
        self.tickets.append(ticket_info)
        self.sold_tickets += quantity
        self.total_tickets -= quantity
        
        # Save ticket sales to file
        self.save_to_file()
        
        print("Tickets purchased successfully!")
        return True

    def save_to_file(self):
        """
        Save ticket sales information to a JSON file.
        """
        with open('tickets_data.json', 'w') as file:
            json.dump(self.tickets, file)

    def available_tickets_count(self):
        """
        Get the number of available tickets.
        """
        return self.total_tickets

    def sold_tickets_info(self):
        """
        Print information about sold tickets.
        """
        if not self.tickets:
            print("No tickets have been sold yet.")
            return
        
        # Initialize dictionary to track tickets sold per person
        tickets_sold_per_person = {}
        
        for ticket in self.tickets:
            full_name = ticket['full_name']
            quantity = ticket['quantity']
            
            # Update tickets sold per person
            if full_name in tickets_sold_per_person:
                tickets_sold_per_person[full_name] += quantity
            else:
                tickets_sold_per_person[full_name] = quantity
        
        # Print details of tickets sold per person
        for full_name, quantity in tickets_sold_per_person.items():
            print(f"{full_name} bought {quantity} tickets")
        
        # Calculate and print total tickets sold
        total_tickets_sold = sum(tickets_sold_per_person.values())
        print(f"Total tickets sold: {total_tickets_sold}")

    def read_data(self):
        """
        Read ticket sales data from JSON file.
        """
        try:
            with open('tickets_data.json', 'r') as file:
                self.tickets = json.load(file)
                self.sold_tickets = sum(ticket['quantity'] for ticket in self.tickets)
                self.total_tickets -= self.sold_tickets
        except FileNotFoundError:
            # If file does not exist, initialize tickets list and sold tickets count
            self.tickets = []
            self.sold_tickets = 0

def get_valid_input(prompt, input_type):
    """
    Prompt user for input of a specific type and validate it.
    """
    while True:
        try:
            return input_type(input(prompt))
        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__}.")

def menu():
    """
    Main menu of the concert ticket system.
    """
    # Initialize Concert object with initial data
    concert = Concert("Famous Singer", "2024-07-15", 100, 50)
    concert.read_data()  # Load previous data if exists

    while True:
        print("\n--- Concert Ticket System Menu ---")
        print("1. View concert info")
        print("2. View ticket price")
        print("3. Buy tickets")
        print("4. View available tickets")
        print("5. View sold tickets info")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            # Option to view full concert information
            print(concert.get_full_info())
        elif choice == '2':
            # Option to view ticket price
            print(f"Ticket price: {concert.get_price()}")
        elif choice == '3':
            # Option to buy tickets
            full_name = input("Enter your full name: ")
            phone_number = get_valid_input("Enter your phone number: ", int)
            quantity = get_valid_input("Enter number of tickets: ", int)
            concert.buy_ticket(full_name, phone_number, quantity)
        elif choice == '4':
            # Option to view available tickets
            print(f"Available tickets: {concert.available_tickets_count()}")
        elif choice == '5':
            # Option to view information about sold tickets
            concert.sold_tickets_info()
        elif choice == '6':
            # Exit the program
            print("Exiting the system.\nGoodbye!")
            break
        else:
            # Handle invalid choices
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()