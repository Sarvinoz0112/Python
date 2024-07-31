from datetime import datetime, timedelta
import json

# Mock file manager for demonstration
class TaxiAnnManager:
    @staticmethod
    def add_data(data):
        with open("taxi_announcements.json", "a") as file:
            file.write(json.dumps(data) + "\n")

    @staticmethod
    def load_data():
        try:
            with open("taxi_announcements.json", "r") as file:
                return [json.loads(line) for line in file]
        except FileNotFoundError:
            return []

    @staticmethod
    def update_data(data_list):
        with open("taxi_announcements.json", "w") as file:
            for data in data_list:
                file.write(json.dumps(data) + "\n")

taxi_ann_manager = TaxiAnnManager()

# Regions dictionary
regions = {
    "1": "Andijan", "2": "Namangan", "3": "Fergana"
}

# Base Announcement class
class Announcement:
    def __init__(self, from_place, to_place, price, expire_time):
        self.from_place = from_place
        self.to_place = to_place
        self.price = price
        self.expire_time = expire_time
        self.is_active = True
        self.created_at = str(datetime.now())

# ClientAnnouncement class inheriting from Announcement
class ClientAnnouncement(Announcement):
    pass

# TaxiAnnouncement class inheriting from Announcement
class TaxiAnnouncement(Announcement):
    def __init__(self, from_place, to_place, price, car_name, comment, expire_time, seats):
        super().__init__(from_place, to_place, price, expire_time)
        self.car_name = car_name
        self.comment = comment
        self.seats = seats

# Function to check and update the active status of announcements
def check_and_update_announcements():
    announcements = taxi_ann_manager.load_data()
    now = datetime.now()
    for ann in announcements:
        created_at = datetime.fromisoformat(ann['created_at'])
        expire_at = created_at + timedelta(hours=int(ann['expire_time']))
        if expire_at <= now:
            ann['is_active'] = False
    taxi_ann_manager.update_data(announcements)
    return announcements

# Function to add a taxi announcement
def add_announcement_as_taxi():
    try:
        announcements = check_and_update_announcements()
        
        print("Available regions:", regions)
        
        from_place = input("Where are you: ")
        while from_place not in regions:
            print("Invalid input. Please select a valid region number.")
            from_place = input("Where are you: ")
        from_place = regions[from_place]

        print("Available regions:", regions)
        
        to_place = input("Where do you want to go: ")
        while to_place not in regions:
            print("Invalid input. Please select a valid region number.")
            to_place = input("Where do you want to go: ")
        to_place = regions[to_place]

        if from_place == to_place:
            print("From and To places cannot be the same. Please try again.")
            return add_announcement_as_taxi()

        # Check for existing active announcements from the same place
        for ann in announcements:
            if ann['from_place'] == from_place and ann['is_active']:
                print("There is already an active announcement from this place.")
                return False

        price = input("How much is the cost per seat: ")
        expire_time = input("How many hours should it be valid: ")
        car_name = input("What kind of car: ")
        seats = input("How many seats are available: ")
        comment = input("Enter comment: ")

        taxi = TaxiAnnouncement(from_place, to_place, price, car_name, comment, expire_time, seats)
        print(taxi.__dict__)
        taxi_ann_manager.add_data(taxi.__dict__)
        print("Announcement added successfully!")
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Main function to run the script
def main():
    add_announcement_as_taxi()

if __name__ == "__main__":
    main()