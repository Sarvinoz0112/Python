import os
import json
import logging
from datetime import datetime

logging.basicConfig(filename='operations.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def get_int_input(prompt):
    """Get an integer input from the user. Repeats if invalid input is provided."""
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a non-negative integer.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_valid_email(prompt):
    """Get a valid email address from the user. Repeats if the format is incorrect."""
    while True:
        email = input(prompt)
        if (
            email.count('@') == 1 and           # Checks if there is exactly one '@' symbol
            email[0] != '@' and                # Ensures the email doesn't start with '@'
            email.count('.') > 0 and           # Checks if there is at least one '.'
            email.rfind('.') > email.find('@') # Ensures '.' is after '@'
        ):
            return email
        else:
            print("Invalid email format. Please enter a valid email address.")

def load_data(filename):
    """Load data from a JSON file. Returns an empty dictionary if the file does not exist."""
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return {}

def save_data(filename, data):
    """Save data to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

class Auth:
    """Class for user authentication."""
    
    def __init__(self):
        """Load user data and add admin user if it does not exist."""
        self.users = load_data('users.json')
        if "admin" not in self.users:
            self.users["admin"] = "admin"
            save_data('users.json', self.users)

    def register(self):
        """Register a new user."""
        try:
            username = input("Username: ")
            password = input("Password: ")
            if username in self.users:
                print("User already exists!")
                return
            self.users[username] = password
            save_data('users.json', self.users)
            logging.info(f"User registered: {username}")
            print("Registration successful.")
        except Exception as e:
            logging.error(f"Error during registration: {e}")

    def login(self):
        """Authenticate user login."""
        try:
            username = input("Username: ")
            password = input("Password: ")
            if self.users.get(username) == password:
                logging.info(f"User logged in: {username}")
                return username
            else:
                print("Invalid credentials!")
                return None
        except Exception as e:
            logging.error(f"Error during login: {e}")

class Admin:
    """Class for admin functionalities."""
    
    def __init__(self):
        """Load data for planes, airports, and flights."""
        self.planes = load_data('planes.json')
        self.airports = load_data('airports.json')
        self.flights = load_data('flights.json')

    def add_plane(self):
        """Add a new plane."""
        try:
            plane_id = input("Plane ID: ")
            name = input("Plane Name: ")
            capacity = get_int_input("Capacity: ")
            self.planes[plane_id] = {"name": name, "capacity": capacity}
            save_data('planes.json', self.planes)
            logging.info(f"Plane added: {plane_id}")
            print("Plane added successfully.")
        except Exception as e:
            logging.error(f"Error during adding plane: {e}")

    def delete_plane(self):
        """Delete a plane."""
        try:
            plane_id = input("Enter Plane ID to delete: ")
            if plane_id in self.planes:
                del self.planes[plane_id]
                save_data('planes.json', self.planes)
                logging.info(f"Plane deleted: {plane_id}")
                print("Plane deleted successfully.")
            else:
                print("Plane not found.")
        except Exception as e:
            logging.error(f"Error during deleting plane: {e}")

    def update_plane(self):
        """Update a plane's details."""
        try:
            plane_id = input("Enter Plane ID to update: ")
            if plane_id in self.planes:
                name = input("New Plane Name: ")
                capacity = get_int_input("New Capacity: ")
                self.planes[plane_id] = {"name": name, "capacity": capacity}
                save_data('planes.json', self.planes)
                logging.info(f"Plane updated: {plane_id}")
                print("Plane updated successfully.")
            else:
                print("Plane not found.")
        except Exception as e:
            logging.error(f"Error during updating plane: {e}")

    def view_planes(self):
        """Display all planes."""
        try:
            if self.planes:
                for plane_id, plane in self.planes.items():
                    print(f"Plane ID: {plane_id}")
                    for key, value in plane.items():
                        print(f"  {key}: {value}")
            else:
                print("No planes found.")
            logging.info("Displayed all planes.")
        except Exception as e:
            logging.error(f"Error during viewing planes: {e}")

    def add_airport(self):
        """Add a new airport."""
        try:
            name = input("Airport Name: ")
            country = input("Country: ")
            self.airports[name] = {"country": country}
            save_data('airports.json', self.airports)
            logging.info(f"Airport added: {name}")
            print("Airport added successfully.")
        except Exception as e:
            logging.error(f"Error during adding airport: {e}")

    def delete_airport(self):
        """Delete an airport."""
        try:
            name = input("Enter Airport Name to delete: ")
            if name in self.airports:
                del self.airports[name]
                save_data('airports.json', self.airports)
                logging.info(f"Airport deleted: {name}")
                print("Airport deleted successfully.")
            else:
                print("Airport not found.")
        except Exception as e:
            logging.error(f"Error during deleting airport: {e}")

    def update_airport(self):
        """Update an airport's details."""
        try:
            name = input("Enter Airport Name to update: ")
            if name in self.airports:
                country = input("New Country: ")
                self.airports[name] = {"country": country}
                save_data('airports.json', self.airports)
                logging.info(f"Airport updated: {name}")
                print("Airport updated successfully.")
            else:
                print("Airport not found.")
        except Exception as e:
            logging.error(f"Error during updating airport: {e}")

    def view_airports(self):
        """Display all airports."""
        try:
            if self.airports:
                for name, airport in self.airports.items():
                    print(f"Airport Name: {name}")
                    for key, value in airport.items():
                        print(f"  {key}: {value}")
            else:
                print("No airports found.")
            logging.info("Displayed all airports.")
        except Exception as e:
            logging.error(f"Error during viewing airports: {e}")

    def add_flight(self):
        """Add a new flight."""
        try:
            plane_id = input("Plane ID: ")
            from_airport = input("From Airport: ")
            to_airport = input("To Airport: ")
            flight_time = get_int_input("Flight Time (in hours): ")
            landing_time = get_int_input("Landing Time (in hours): ")
            status = input("Status: ")
            price = float(input("Ticket Price: "))
            flight_id = len(self.flights) + 1
            if plane_id in self.planes:
                capacity = self.planes[plane_id]["capacity"]
                self.flights[flight_id] = {
                    "plane_id": plane_id,
                    "from_airport": from_airport,
                    "to_airport": to_airport,
                    "flight_time": flight_time,
                    "landing_time": landing_time,
                    "status": status,
                    "tickets_sold": 0,
                    "price": price,
                    "capacity": capacity
                }
                save_data('flights.json', self.flights)
                logging.info(f"Flight added: {flight_id}")
                print("Flight added successfully.")
            else:
                print("Plane not found.")
        except Exception as e:
            logging.error(f"Error during adding flight: {e}")

    def show_all_flights(self):
        """Display all flights."""
        try:
            for flight_id, flight in self.flights.items():
                print(f"Flight ID: {flight_id}")
                for key, value in flight.items():
                    print(f"  {key}: {value}")
            logging.info("Displayed all flights.")
        except Exception as e:
            logging.error(f"Error during displaying all flights: {e}")

    def admin_menu(self):
        """Admin menu for managing planes, airports, and flights."""
        while True:
            print("\nAdmin Menu:")
            print("1. Manage Planes")
            print("2. Manage Airports")
            print("3. Add Flight")
            print("4. Show All Flights")
            print("5. Logout")
            choice = input("Choose an option: ")
            
            if choice == '1':
                self.plane_menu()
            elif choice == '2':
                self.airport_menu()
            elif choice == '3':
                self.add_flight()
            elif choice == '4':
                self.show_all_flights()
            elif choice == '5':
                break
            else:
                print("Invalid choice!")

    def plane_menu(self):
        """Menu for managing planes."""
        while True:
            print("\nPlane Management Menu:")
            print("1. Add plane")
            print("2. Delete plane")
            print("3. Update plane")
            print("4. View planes")
            print("5. Back to Admin Menu")
            choice = input("Choose an option: ")
            
            if choice == '1':
                self.add_plane()
            elif choice == '2':
                self.delete_plane()
            elif choice == '3':
                self.update_plane()
            elif choice == '4':
                self.view_planes()
            elif choice == '5':
                break
            else:
                print("Invalid choice!")

    def airport_menu(self):
        """Menu for managing airports."""
        while True:
            print("\nAirport Management Menu:")
            print("1. Add airport")
            print("2. Delete airport")
            print("3. Update airport")
            print("4. View airports")
            print("5. Back to Admin Menu")
            choice = input("Choose an option: ")
            
            if choice == '1':
                self.add_airport()
            elif choice == '2':
                self.delete_airport()
            elif choice == '3':
                self.update_airport()
            elif choice == '4':
                self.view_airports()
            elif choice == '5':
                break
            else:
                print("Invalid choice!")

class User:
    """Class for user functionalities."""
    
    def __init__(self, username, flights):
        """Initialize user with username and their booked flights."""
        self.username = username
        self.flights = flights
        self.bookings = load_data(f'{username}_bookings.json')

    def search_flights(self):
        """Search for flights based on departure and destination airports."""
        try:
            from_airport = input("Enter departure airport: ")
            to_airport = input("Enter destination airport: ")
            available_flights = [
                (fid, flight) for fid, flight in self.flights.items()
                if flight["from_airport"] == from_airport and flight["to_airport"] == to_airport
            ]
            if available_flights:
                for fid, flight in available_flights:
                    print(f"Flight ID: {fid}")
                    for key, value in flight.items():
                        print(f"  {key}: {value}")
            else:
                print("No flights found.")
            logging.info(f"Searched flights from {from_airport} to {to_airport} by user: {self.username}")
        except Exception as e:
            logging.error(f"Error during searching flights: {e}")

    def buy_ticket(self):
        """Buy a ticket for a flight."""
        try:
            flight_id = get_int_input("Enter Flight ID to buy ticket: ")
            if flight_id in self.flights:
                flight = self.flights[flight_id]
                available_tickets = flight["capacity"] - flight["tickets_sold"]
                num_tickets = get_int_input(f"How many tickets do you want to buy (Available: {available_tickets}): ")
                if num_tickets <= available_tickets:
                    passport_number = input("Passport Number: ")
                    email = get_valid_email("Email: ")
                    flight["tickets_sold"] += num_tickets
                    self.bookings[flight_id] = {
                        "passport_number": passport_number,
                        "email": email,
                        "num_tickets": num_tickets
                    }
                    save_data(f'{self.username}_bookings.json', self.bookings)
                    logging.info(f"Ticket(s) bought: Flight ID {flight_id}, Number of tickets: {num_tickets} by {self.username}")
                    print("Ticket(s) bought successfully.")
                else:
                    print("Not enough tickets available.")
            else:
                print("Flight not found.")
        except Exception as e:
            logging.error(f"Error during buying ticket: {e}")

    def view_booked_flights(self):
        """View flights that the user has booked."""
        try:
            if self.bookings:
                for flight_id, booking in self.bookings.items():
                    print(f"Flight ID: {flight_id}")
                    for key, value in booking.items():
                        print(f"  {key}: {value}")
            else:
                print("No booked flights found.")
            logging.info(f"Viewed booked flights for user: {self.username}")
        except Exception as e:
            logging.error(f"Error during viewing booked flights: {e}")

    def user_menu(self):
        """User menu for searching flights, buying tickets, and viewing booked flights."""
        while True:
            print(f"\nUser Menu ({self.username}):")
            print("1. Search flights")
            print("2. Buy ticket")
            print("3. View booked flights")
            print("4. Logout")
            choice = input("Choose an option: ")
            
            if choice == '1':
                self.search_flights()
            elif choice == '2':
                self.buy_ticket()
            elif choice == '3':
                self.view_booked_flights()
            elif choice == '4':
                break
            else:
                print("Invalid choice!")

def main():
    """Main function to run the program."""
    auth = Auth()
    admin = Admin()

    while True:
        print("\nMain Menu:")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            username = auth.login()
            if username:
                if username == "admin":
                    admin.admin_menu()
                else:
                    user = User(username, admin.flights)
                    user.user_menu()
        elif choice == '2':
            auth.register()
        elif choice == '3':
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()