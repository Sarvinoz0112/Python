class CarRental:
    def __init__(self):
        # Initializes an empty list to store cars
        self.__cars = []

    def add_car(self, name, model):
        """
        Adds a new car to the rental service.
        
        Parameters:
        name (str): The name of the car.
        model (str): The model of the car.
        """
        car = {"name": name, "model": model, "is_rented": False}
        self.__cars.append(car)
        print(f"Car added: {name} {model}")

    def rent_car(self, name):
        """
        Rents a car if it is available.
        
        Parameters:
        name (str): The name of the car to rent.
        
        Returns:
        dict: The car that was rented, or None if the car was not found or already rented.
        """
        car = self.__find_car_by_name(name)
        if car:
            if not car["is_rented"]:
                car["is_rented"] = True
                print("\n" + "="*30)
                print(f" Car rented successfully!")
                print(f" Name: {car['name']}")
                print(f" Model: {car['model']}")
                print("="*30 + "\n")
                return car
            else:
                print(f"Car {name} is already rented.")
        else:
            print(f"Car {name} not found.")
        return None

    def return_car(self, name):
        """
        Returns a rented car.
        
        Parameters:
        name (str): The name of the car to return.
        
        Returns:
        dict: The car that was returned, or None if the car was not found or was not rented.
        """
        car = self.__find_car_by_name(name)
        if car:
            if car["is_rented"]:
                car["is_rented"] = False
                print("\n" + "="*30)
                print(f" Car returned successfully!")
                print(f" Name: {car['name']}")
                print(f" Model: {car['model']}")
                print("="*30 + "\n")
                return car
            else:
                print(f"Car {name} was not rented.")
        else:
            print(f"Car {name} not found.")
        return None

    def __find_car_by_name(self, name):
        """
        Finds a car by its name.
        
        Parameters:
        name (str): The name of the car to find.
        
        Returns:
        dict: The car with the specified name, or None if no such car is found.
        """
        for car in self.__cars:
            if car["name"] == name:
                return car
        return None

    def display_available_cars(self):
        """
        Displays all available cars in the rental service.
        """
        available_cars = [car for car in self.__cars if not car["is_rented"]]
        if not available_cars:
            print("No cars available for rent.")
        else:
            print("\n" + "="*30)
            print(" Available cars:")
            for car in available_cars:
                print(f" Name: {car['name']}, Model: {car['model']}")
            print("="*30 + "\n")

    def display_all_cars(self):
        """
        Displays all cars in the rental service along with their rental status.
        """
        if not self.__cars:
            print("No cars available.")
        else:
            print("\n" + "="*30)
            print(" Current cars:")
            for car in self.__cars:
                rented_status = "Rented" if car["is_rented"] else "Available"
                print(f" Name: {car['name']}, Model: {car['model']} - Status: {rented_status}")
            print("="*30 + "\n")

def display_menu():
    """
    Displays the main menu options.
    """
    print("\n--- Car Rental Service Menu ---")
    print("1. Add Car")
    print("2. Rent Car")
    print("3. Return Car")
    print("4. Display All Cars")
    print("5. Exit")

def menu():
    """
    Main function to handle user interaction with the car rental service.
    """
    rental_service = CarRental()

    while True:
        display_menu()
        choice = input("Please select an option (1-5): ")

        if choice == "1":
            name = input("Enter car name: ")
            model = input("Enter car model: ")
            rental_service.add_car(name, model)
        elif choice == "2":
            rental_service.display_available_cars()
            name = input("Enter car name to rent: ")
            rental_service.rent_car(name)
        elif choice == "3":
            name = input("Enter car name to return: ")
            rental_service.return_car(name)
        elif choice == "4":
            rental_service.display_all_cars()
        elif choice == "5":
            print("Exiting the menu. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

# Example of running the menu:
menu()