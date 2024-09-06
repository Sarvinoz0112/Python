import json
import time
import random

class Scooter:
    '''
    Initializes a new Scooter object with battery, location, price per minute, speed, and reserved status.
    '''
    def __init__(self, battery, location, price_per_minute, speed):
        self.id = random.randint(1000, 9999)
        self.battery = battery
        self.location = location
        self.price_per_minute = price_per_minute
        self.speed = speed
        self.reserved = False

class ScooterAdmin:
    '''
    Initializes the ScooterAdmin object and loads existing scooters from a JSON file.
    '''
    def __init__(self):
        self.scooters = self.load_scooters()

    '''
    Loads scooters from a JSON file and returns the list of scooters.
    If the file does not exist, returns an empty list.
    '''
    def load_scooters(self):
        try:
            with open('scooters.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    '''
    Saves the current list of scooters to a JSON file.
    '''
    def save_scooters(self):
        with open('scooters.json', 'w') as f:
            json.dump(self.scooters, f, indent=4)

    '''
    Adds a new scooter to the list with the provided battery, location, price per minute, and speed.
    '''
    def add_scooter(self, battery, location, price_per_minute, speed):
        new_scooter = Scooter(battery, location, price_per_minute, speed)
        self.scooters.append(new_scooter.__dict__)
        self.save_scooters()

    '''
    Updates the details of an existing scooter based on the provided scooter ID and optional parameters.
    '''
    def update_scooter(self, scooter_id, battery=None, location=None, price_per_minute=None, speed=None):
        for scooter in self.scooters:
            if scooter['id'] == scooter_id:
                if battery is not None:
                    scooter['battery'] = battery
                if location is not None:
                    scooter['location'] = location
                if price_per_minute is not None:
                    scooter['price_per_minute'] = price_per_minute
                if speed is not None:
                    scooter['speed'] = speed
                self.save_scooters()
                return scooter
        return None

    '''
    Lists all the scooters with their details.
    '''
    def list_scooters(self):
        for scooter in self.scooters:
            print(f"ID: {scooter['id']}, Battery: {scooter['battery']}%, Location: {scooter['location']}, "
                  f"Price per Minute: {scooter['price_per_minute']}, Speed: {scooter['speed']} km/h")
        return self.scooters

    '''
    Returns a list of all scooter IDs.
    '''
    def get_scooter_ids(self):
        return [scooter['id'] for scooter in self.scooters]

    '''
    Reserves a scooter by setting its reserved status to True.
    '''
    def reserve_scooter(self, scooter_id):
        for scooter in self.scooters:
            if scooter['id'] == scooter_id:
                if not scooter['reserved']:
                    scooter['reserved'] = True
                    self.save_scooters()
                    return True
                else:
                    return False
        return False

    '''
    Releases a scooter by setting its reserved status to False.
    '''
    def release_scooter(self, scooter_id):
        for scooter in self.scooters:
            if scooter['id'] == scooter_id:
                scooter['reserved'] = False
                self.save_scooters()
                return True
        return False

class ScooterUser:
    '''
    Initializes the ScooterUser object and loads active rides from a JSON file.
    '''
    def __init__(self):
        self.active_rides = self.load_rides()

    '''
    Loads active rides from a JSON file and returns the dictionary of active rides.
    If the file does not exist, returns an empty dictionary.
    '''
    def load_rides(self):
        try:
            with open('active_rides.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    '''
    Saves the current active rides to a JSON file.
    '''
    def save_rides(self):
        with open('active_rides.json', 'w') as f:
            json.dump(self.active_rides, f, indent=4)

    '''
    Starts a ride for the given scooter ID and records the start time.
    '''
    def start_ride(self, scooter_id):
        start_time = time.time()
        self.active_rides[scooter_id] = start_time
        self.save_rides()
        return start_time

    '''
    Stops the ride for the given scooter ID, calculates the duration in minutes, and returns the duration.
    '''
    def stop_ride(self, scooter_id):
        end_time = time.time()
        if scooter_id in self.active_rides:
            start_time = self.active_rides.pop(scooter_id)
            self.save_rides()
            duration_minutes = (end_time - start_time) / 60
            return duration_minutes
        return None

    '''
    Calculates the estimated trip time and cost for the given scooter ID and distance in kilometers.
    '''
    def calculate_trip(self, scooter_id, distance_km):
        scooters = admin.list_scooters()
        for scooter in scooters:
            if scooter['id'] == scooter_id:
                speed_kmh = scooter['speed']
                time_hours = distance_km / speed_kmh
                time_minutes = time_hours * 60
                cost = time_minutes * scooter['price_per_minute']
                return time_minutes, cost
        return None

'''
Calculates the cost of a ride based on the duration in minutes and price per minute.
'''
def calculate_cost(duration_minutes, price_per_minute):
    return duration_minutes * price_per_minute

'''
Displays the admin menu with options to add, update, list scooters, or exit.
'''
def admin_menu():
    while True:
        print("\nAdmin Menu")
        print("1. Add Scooter")
        print("2. Update Scooter")
        print("3. List Scooters")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            battery = int(input("Enter battery percentage: "))
            location = input("Enter location: ")
            price_per_minute = float(input("Enter price per minute: "))
            speed = int(input("Enter speed: "))
            admin.add_scooter(battery, location, price_per_minute, speed)
        elif choice == '2':
            scooter_id = int(input("Enter Scooter ID to update: "))
            battery = input("Enter new battery percentage (leave blank to skip): ")
            location = input("Enter new location (leave blank to skip): ")
            price_per_minute = input("Enter new price per minute (leave blank to skip): ")
            speed = input("Enter new speed (leave blank to skip): ")
            admin.update_scooter(
                scooter_id,
                battery=int(battery) if battery else None,
                location=location if location else None,
                price_per_minute=float(price_per_minute) if price_per_minute else None,
                speed=int(speed) if speed else None
            )
        elif choice == '3':
            admin.list_scooters()
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")

'''
Displays the user menu with options to start, stop, calculate a trip, or exit.
'''
def user_menu():
    while True:
        print("\nUser Menu")
        print("1. Start Ride")
        print("2. Stop Ride")
        print("3. Calculate Trip")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            print("Available Scooter IDs: ", admin.get_scooter_ids())
            while True:
                scooter_id = int(input("Enter Scooter ID to start ride: "))
                if scooter_id in admin.get_scooter_ids():
                    if admin.reserve_scooter(scooter_id):
                        start_time = user.start_ride(scooter_id)
                        print(f"Ride started at {time.ctime(start_time)}")
                        break
                    else:
                        print("Scooter is already reserved. Please choose another one.")
                else:
                    print("Scooter ID not found. Please enter a valid Scooter ID.")
        elif choice == '2':
            print("Available Scooter IDs: ", admin.get_scooter_ids())
            while True:
                scooter_id = int(input("Enter Scooter ID to stop ride: "))
                if scooter_id in admin.get_scooter_ids():
                    duration = user.stop_ride(scooter_id)
                    if duration:
                        scooters = admin.list_scooters()
                        scooter = next(s for s in scooters if s['id'] == scooter_id)
                        cost = calculate_cost(duration, scooter['price_per_minute'])
                        print(f"Ride stopped. Duration: {duration:.2f} minutes. Cost: {cost:.2f} units.")
                        admin.release_scooter(scooter_id)
                        break
                    else:
                        print("Ride not found.")
                else:
                    print("Scooter ID not found. Please enter a valid Scooter ID.")
        elif choice == '3':
            print("Available Scooter IDs: ", admin.get_scooter_ids())
            while True:
                scooter_id = int(input("Enter Scooter ID for trip calculation: "))
                if scooter_id in admin.get_scooter_ids():
                    distance_km = float(input("Enter distance in kilometers: "))
                    trip_time, trip_cost = user.calculate_trip(scooter_id, distance_km)
                    print(f"Estimated trip time: {trip_time:.2f} minutes. Estimated cost: {trip_cost:.2f} units.")
                    break
                else:
                    print("Scooter ID not found. Please enter a valid Scooter ID.")
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")

admin = ScooterAdmin()
user = ScooterUser()

'''
Displays the main menu with options for admin or user access.
'''
def main_menu():
    while True:
        print("\nMain Menu")
        print("1. Admin")
        print("2. User")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            admin_menu()
        elif choice == '2':
            user_menu()
        elif choice == '3':
            break
        else:
            print("Invalid choice, please try again.")

main_menu()
