import hashlib
import json
import os

def hash_password(password):
    '''
    Function to hash a password using SHA-256
    '''
    return hashlib.sha256(password.encode()).hexdigest()


def verify_password(stored_password, provided_password):
    '''
    Function to verify if a provided password matches the stored hashed password
    '''
    return stored_password == hashlib.sha256(provided_password.encode()).hexdigest()

# Class to manage JSON file operations
class JsonFileManager:
    def __init__(self, filename):
        self.filename = filename
        self.data = self.load_data()

    
    def load_data(self):
        '''
        Load data from JSON file
        '''
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, 'r') as file:
            return json.load(file)

    
    def save_data(self):
        '''
        Save data to JSON file
        '''
        with open(self.filename, 'w') as file:
            json.dump(self.data, file, indent=4)

    
    def get_users(self):
        '''
        Get the list of users from loaded data
        '''
        return self.data.get('users', [])

    
    def save_users(self, users):
        '''
        Save the list of users to data and then save to file
        '''
        self.data['users'] = users
        self.save_data()

# Class to manage user operations like registration, login, applications, etc.
class UserManager:
    def __init__(self, json_file_manager):
        self.json_file_manager = json_file_manager
        self.users = self.json_file_manager.get_users()
        self.current_user = None

    
    def register(self, username, password):
        '''
        Register a new user
        '''
        for user in self.users:
            if user['username'] == username:
                return "Username already exists."

        hashed_password = hash_password(password)
        new_user = {
            'username': username,
            'password': hashed_password,
            'is_login': False,
            'applications': []
        }
        self.users.append(new_user)
        self.json_file_manager.save_users(self.users)
        return "Registration successful."

    
    def login(self, username, password):
        '''
        Login an existing user
        '''
        for user in self.users:
            if user['username'] == username and verify_password(user['password'], password):
                user['is_login'] = True
                self.current_user = user
                self.json_file_manager.save_users(self.users)
                return "Login successful."
        return "Invalid username or password."

    
    def logout(self):
        '''
        Logout the current user
        '''
        if self.current_user:
            self.current_user['is_login'] = False
            self.current_user = None
            self.json_file_manager.save_users(self.users)

    
    def submit_application(self, car_model, car_color, car_year):
        '''
        Submit an application for the current logged-in user
        '''
        if self.current_user:
            application = {
                'model': car_model,
                'color': car_color,
                'year': car_year
            }
            self.current_user['applications'].append(application)
            self.json_file_manager.save_users(self.users)
            return "Application submitted."
        return "No user is logged in."

    
    def view_applications(self):
        '''
        View applications of the current logged-in user
        '''
        if self.current_user:
            applications = self.current_user.get('applications', [])
            if applications:
                output = "Your applications:\n"
                for idx, app in enumerate(applications, 1):
                    output += f"{idx}Model: {app['model']}, Color: {app['color']}, Year: {app['year']}\n"
                return output.strip()
            else:
                return "You have no applications."
        return "No user is logged in."


def main():
    '''
    Main function to run the program
    '''
    json_file_manager = JsonFileManager('users.json')
    user_manager = UserManager(json_file_manager)

    while True:
        if not user_manager.current_user:
            print("\n1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                username = input("Enter username: ")
                password = input("Enter password: ")
                print(user_manager.register(username, password))

            elif choice == "2":
                username = input("Enter username: ")
                password = input("Enter password: ")
                print(user_manager.login(username, password))
                
            elif choice == "3":
                print("Exiting program.")
                break
        
        else:
            print("\n1. Submit Application")
            print("2. View Applications")
            print("3. Logout")
            print("4. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                car_model = input("Enter car model: ")
                car_color = input("Enter car color: ")
                while True:
                    try:
                        car_year = int(input("Enter car year: "))
                        break
                    except ValueError:
                        print("Please enter a valid year.")
                print(user_manager.submit_application(car_model, car_color, car_year))

            elif choice == "2":
                print(user_manager.view_applications())

            elif choice == "3":
                user_manager.logout()
                print("Logged out successfully.")
            
            elif choice == "4":
                user_manager.logout()
                print("Exiting program.")
                break

if __name__ == "__main__":
    main()