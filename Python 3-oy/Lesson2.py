# class Calculator:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
    
#     def addition(self):
#         return self.a + self.b
    
#     def subtraction(self):
#         return self.a - self.b
    
#     def division(self):
#         if self.b != 0:
#             return self.a / self.b
#         else:
#             return "Error! Division by zero."
    
#     def multiplication(self):
#         return self.a * self.b

# smth = Calculator(10,5)
# print(smth.addition())

#-------------------------------------------------------------------

import os
import csv

class CsvManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def check_existence(self):
        return os.path.exists(self.file_name)

    def create_csv_file(self):
        if not self.check_existence():
            with open(self.file_name, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['name', 'age'])  # Assuming the user data has 'name' and 'age' fields
            return "File is created"
        return "File exists"

    def read_csv_file(self):
        if self.check_existence():
            with open(self.file_name, 'r', newline='') as file:
                reader = csv.DictReader(file)
                return list(reader)
        return []

    def write_csv_data(self, data):
        with open(self.file_name, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['name', 'age'])
            writer.writeheader()
            writer.writerows(data)

    def add_user(self, user_data):
        users = self.read_csv_file()
        users.append(user_data)
        self.write_csv_data(users)
        return "User added"

    def see_all_users(self):
        return self.read_csv_file()

    def delete_one_user(self, user_data):
        users = self.read_csv_file()
        for user in users:
            if user['name'] == user_data['name'] and user['age'] == user_data['age']:
                users.remove(user)
                self.write_csv_data(users)
                return "User deleted"
        return "User not found"

    def delete_all_users(self):
        pass

manager = CsvManager('users.csv')
print(manager.add_user({'name': 'Alice', 'age': '30'}))