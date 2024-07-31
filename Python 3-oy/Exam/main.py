import json

class Database:
    def __init__(self, filename='data.json'):
        """
        Initializes the Database with a filename and loads data from the JSON file.
        """
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        """
        Loads data from the JSON file. If the file doesn't exist, initializes with empty lists.
        """
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {"users": [], "houses": [], "interests": []}

    def save_data(self):
        """
        Saves data to the JSON file.
        """
        with open(self.filename, 'w') as file:
            json.dump(self.data, file, indent=4)

    def get_data(self):
        """
        Returns the current data dictionary.
        """
        return self.data

class User:
    def __init__(self, db):
        """
        Initializes the User manager with a Database instance.
        """
        self.db = db

    def register(self, username, password, phone_number):
        """
        Registers a new user with the provided username, password, and phone number.
        """
        for user in self.db.get_data()["users"]:
            if user["username"] == username:
                return "User already exists"

        new_user = {
            "id": len(self.db.get_data()["users"]) + 1,
            "username": username,
            "password": password,
            "phone_number": phone_number,
            "owned_houses": [],
            "interests": []
        }
        self.db.get_data()["users"].append(new_user)
        self.db.save_data()
        return "Registration successful"

    def login(self, username, password):
        """
        Logs in a user with the provided username and password.
        Returns the user ID if successful, None otherwise.
        """
        for user in self.db.get_data()["users"]:
            if user["username"] == username and user["password"] == password:
                return user["id"]
        return None

class House:
    def __init__(self, db):
        """
        Initializes the House manager with a Database instance.
        """
        self.db = db

    def add_house(self, owner_id, city, rooms, description):
        """
        Adds a new house with the provided owner ID, city, number of rooms, and description.
        """
        new_house = {
            "id": len(self.db.get_data()["houses"]) + 1,
            "owner_id": owner_id,
            "city": city,
            "rooms": rooms,
            "description": description,
            "interests": []
        }
        self.db.get_data()["houses"].append(new_house)
        
        owner = next((u for u in self.db.get_data()["users"] if u["id"] == owner_id), None)
        if owner:
            owner["owned_houses"].append(new_house["id"])
            self.db.save_data()
        
        return "House added"

    def view_houses(self):
        """
        Returns all houses in the database.
        """
        houses = self.db.get_data()["houses"]
        if not houses:
            return "No houses available"
        
        return houses

    def search_houses_by_rooms(self, rooms):
        """
        Searches and returns houses with the specified number of rooms.
        """
        houses = [house for house in self.db.get_data()["houses"] if house["rooms"] == rooms]
        if not houses:
            return "No houses available"
        
        return houses

    def search_houses_by_city(self, city):
        """
        Searches and returns houses in the specified city.
        """
        houses = [house for house in self.db.get_data()["houses"] if house["city"].lower() == city.lower()]
        if not houses:
            return "No houses available"
        
        return houses

    def request_interest(self, house_id, user_id, user_name, phone_number):
        """
        Records a user's interest in a house with the provided house ID.
        """
        house_found = False
        for house in self.db.get_data()["houses"]:
            if house["id"] == house_id:
                house_found = True
                house["interests"].append({
                    "user_id": user_id,
                    "user_name": user_name,
                    "phone_number": phone_number
                })
                self.db.save_data()

                owner_id = house["owner_id"]
                owner = next((u for u in self.db.get_data()["users"] if u["id"] == owner_id), None)
                if owner:
                    return f"Your request for the house owner has been sent. The landlord will contact you soon."
        
        if not house_found:
            return "House not found"

        return "Owner not found"

    def view_my_houses(self, owner_id):
        """
        Returns houses owned by the user with the provided owner ID.
        """
        houses = [house for house in self.db.get_data()["houses"] if house["owner_id"] == owner_id]
        if not houses:
            return "You don't own any houses"
        
        return houses

    def delete_house(self, house_id, owner_id):
        """
        Deletes a house with the provided house ID if the current user is the owner.
        """
        house_found = False
        for house in self.db.get_data()["houses"]:
            if house["id"] == house_id and house["owner_id"] == owner_id:
                house_found = True
                self.db.get_data()["houses"].remove(house)
                break

        if not house_found:
            return "House not found or you are not the owner"

        for user in self.db.get_data()["users"]:
            if user["id"] == owner_id:
                if house_id in user["owned_houses"]:
                    user["owned_houses"].remove(house_id)
                    break
        
        self.db.save_data()
        return "House deleted"

    def view_interests(self, owner_id):
        """
        Returns interests in houses owned by the user with the provided owner ID.
        """
        user_interests = []
        for house in self.db.get_data()["houses"]:
            if house["owner_id"] == owner_id:
                for interest in house["interests"]:
                    user_interests.append({
                        "house_id": house["id"],
                        "city": house["city"],
                        "rooms": house["rooms"],
                        "description": house["description"],
                        "interested_user_name": interest["user_name"],
                        "interested_user_phone": interest["phone_number"]
                    })

        if not user_interests:
            return "No interests reported"
        
        return user_interests

class Menu:
    def __init__(self):
        """
        Initializes the Menu with a Database instance, User and House managers, and sets current_user to None.
        """
        self.db = Database()
        self.user_manager = User(self.db)
        self.house_manager = House(self.db)
        self.current_user = None

    def main_menu(self):
        menu_options = {
            "1": "Register",
            "2": "Login",
            "3": "Exit"
        }
        while True:
            choice = self.display_menu(menu_options, "Choose: ")
            if choice == "1":
                username = self.get_valid_input("Username: ")
                password = self.get_valid_input("Password: ")
                phone_number = self.get_valid_input("Phone number: ")
                print(self.user_manager.register(username, password, phone_number))
            elif choice == "2":
                username = self.get_valid_input("Username: ")
                password = self.get_valid_input("Password: ")
                user_id = self.user_manager.login(username, password)
                if user_id:
                    self.current_user = user_id
                    print("Logged in successfully")
                    self.user_menu()
                else:
                    print("Incorrect username or password")
            elif choice == "3":
                break

    def user_menu(self):
        menu_options = {
            "1": "View all houses",
            "2": "Add a house",
            "3": "Search houses by number of rooms",
            "4": "Search houses by city name",
            "5": "Request interest for renting a house",
            "6": "View my owned houses",
            "7": "Delete a house",
            "8": "View interests in my houses",
            "9": "Logout"
        }
        while True:
            choice = self.display_menu(menu_options, "Choose: ")
            if choice == "1":
                houses = self.house_manager.view_houses()
                self.display_houses(houses)
            elif choice == "2":
                city = self.get_valid_input("City: ")
                rooms = self.get_valid_input("Number of rooms: ", int)
                description = self.get_valid_input("Description: ")
                print(self.house_manager.add_house(self.current_user, city, rooms, description))
            elif choice == "3":
                rooms = self.get_valid_input("Number of rooms: ", int)
                houses = self.house_manager.search_houses_by_rooms(rooms)
                self.display_houses(houses)
            elif choice == "4":
                city = self.get_valid_input("City: ")
                houses = self.house_manager.search_houses_by_city(city)
                self.display_houses(houses)
            elif choice == "5":
                house_id = self.get_valid_input("House ID: ", int)
                user_name = self.get_valid_input("Your name: ")
                phone_number = self.get_valid_input("Your phone number: ")
                message = self.house_manager.request_interest(house_id, self.current_user, user_name, phone_number)
                print(message)
            elif choice == "6":
                houses = self.house_manager.view_my_houses(self.current_user)
                self.display_houses(houses)
            elif choice == "7":
                house_id = self.get_valid_input("House ID: ", int)
                print(self.house_manager.delete_house(house_id, self.current_user))
            elif choice == "8":
                interests = self.house_manager.view_interests(self.current_user)
                self.display_interests(interests)
            elif choice == "9":
                self.current_user = None
                print("Logged out")
                break

    def display_menu(self, options, prompt):
        """
        Displays a menu with options and returns the user's choice.
        """
        while True:
            print("\nMenu:")
            for key, value in options.items():
                print(f"{key}: {value}")
            choice = input(prompt).strip()
            if choice in options:
                return choice
            else:
                print("Invalid choice. Please try again.")

    def get_valid_input(self, prompt, input_type=str):
        """
        Validates and returns user input of a specified type.
        """
        while True:
            try:
                value = input_type(input(prompt))
                if isinstance(value, str) and not value.strip():
                    raise ValueError("Cannot be empty")
                return value
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")

    def display_houses(self, houses):
        """
        Displays houses from a list of houses.
        """
        if isinstance(houses, str):
            print(houses)
        else:
            if not houses:
                print("No houses available")
            else:
                for house in houses:
                    print(f"House ID: {house['id']}, City: {house['city']}, Rooms: {house['rooms']}, Description: {house['description']}")

    def display_interests(self, interests):
        """
        Displays interests in houses from a list of interests.
        """
        if isinstance(interests, str):
            print(interests)
        else:
            if not interests:
                print("No interests reported")
            else:
                for interest in interests:
                    print(f"\nHouse ID: {interest['house_id']}\nCity: {interest['city']}\nRooms: {interest['rooms']}\nDescription: {interest['description']}\nInterested user name: {interest['interested_user_name']}\t(Phone: {interest['interested_user_phone']})")

if __name__ == "__main__":
    menu = Menu()
    menu.main_menu()
