import json

# File to store the data
DATA_FILE = 'teams.json'

# Team class
class Team:
    def __init__(self, name, leader, members):
        self.name = name
        self.leader = leader
        self.members = members

# Functions to save and load data from the file
def save_data(teams):
    '''
    Saves the list of teams to a JSON file.
    Converts the list of Team objects into a dictionary where keys are team names
    and values are the team details.
    '''
    teams_dict = {team.name: team.__dict__ for team in teams}
    with open(DATA_FILE, 'w') as file:
        json.dump(teams_dict, file, indent=4)

def load_data():
    '''
    Loads the list of teams from a JSON file.
    Converts the dictionary of teams back into a list of Team objects.
    '''
    try:
        with open(DATA_FILE, 'r') as file:
            teams_dict = json.load(file)
            return [Team(**team) for team in teams_dict.values()]
    except FileNotFoundError:
        return []

# Function to register a team
def register_team():
    '''
    Prompts the user to enter the team name, leader name, and member names.
    Ensures that the inputs are not empty and the number of members is between 3 and 10.
    Returns a Team object with the provided details.
    '''
    while True:
        name = input("Team name: ")
        if name:
            break
        else:
            print("Team name cannot be empty. Please enter a team name.")

    while True:
        leader = input("Leader name: ")
        if leader:
            break
        else:
            print("Leader name cannot be empty. Please enter a leader name.")
    
    while True:
        try:
            num_members = int(input("How many members in your team? (3 to 10): "))
            if 3 <= num_members <= 10:
                break
            else:
                print("The team must have at least 3 and at most 10 members.")
        except ValueError:
            print("Please enter a valid number.")
    
    members = []
    for _ in range(num_members - 1):  # Members other than the leader
        while True:
            member = input("Member name: ")
            if member:
                members.append(member)
                break
            else:
                print("Member name cannot be empty. Please enter a member name.")
    
    members.append(leader)  # Add the leader to the members list
    return Team(name, leader, members)

# Function for admin login
def admin_login():
    '''
    Prompts the user to enter the admin password.
    Returns True if the password is correct, otherwise False.
    '''
    password = input("Admin password: ")
    return password == "admin123"  # Simple hardcoded password for demo purposes

# Admin panel function
def admin_panel(teams):
    '''
    Displays the admin panel with options to view all teams, delete a team, or exit.
    Allows the admin to manage the registered teams.
    '''
    while True:
        print("\nAdmin panel")
        print("1. View all teams")
        print("2. Delete a team")
        print("3. Exit")
        choice = input("Choice: ")
        if choice == '1':
            for i, team in enumerate(teams, start=1):
                print(f"{i}. Team name: {team.name}, Leader: {team.leader}, Members: {', '.join(team.members)}")
        elif choice == '2':
            team_id = int(input("Enter the number of the team to delete: ")) - 1
            if 0 <= team_id < len(teams):
                del teams[team_id]
                save_data(teams)
                print("Team deleted.")
            else:
                print("Invalid number.")
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

# Main menu function
def menu():
    '''
    Displays the main menu with options to register a team, login as admin, or exit.
    Manages the overall program flow.
    '''
    teams = load_data()
    while True:
        print("\nMain menu")
        print("1. Register a team")
        print("2. Login as admin")
        print("3. Exit")
        choice = input("Choice: ")
        if choice == '1':
            team = register_team()
            teams.append(team)
            save_data(teams)
            print("Team registered successfully.")
        elif choice == '2':
            if admin_login():
                admin_panel(teams)
            else:
                print("Incorrect password.")
        elif choice == '3':
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")

# Run the program
if __name__ == "__main__":
    menu()