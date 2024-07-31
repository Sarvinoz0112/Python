import os
import json

# Global dictionaries to store data for students, courses, and teachers
students = {}
courses = {}
teachers = {}

class BaseClass:
    def __init__(self, file_name):
        # Initialize with the name of the JSON file to work with
        self.file_name = file_name

    def check_existence(self):
        # Check if the JSON file exists, if not create it and write an empty JSON object
        if not os.path.exists(self.file_name):
            with open(self.file_name, 'x') as file:
                file.write('{}')
                print(f'The file {self.file_name} has been created!')
            return False
        return True

    def add_to_file(self, data_dict, key, data):
        # Add the provided data to the JSON file
        try:
            if self.check_existence():
                # Add or update the dictionary with the new data
                data_dict[key] = data
                with open(self.file_name, 'w') as file:
                    # Write the updated dictionary back to the JSON file
                    json.dump(data_dict, file, indent=4)
                    print('Successfully added!')
                show_menu()
            else:
                # If file creation failed, try adding the data again
                self.add_to_file(data_dict, key, data)
        except Exception as exc:
            # Print any exception that occurs and show the menu again
            print(exc)
            show_menu()

class Courses(BaseClass):
    def __init__(self, name, price, teacher_phone_number):
        # Initialize course attributes and call the parent constructor with the JSON file name
        super().__init__('courses.json')
        self.name = name
        self.price = price
        self.teacher_phone_number = teacher_phone_number

    def add_to_file(self):
        # Use the parent class method to add course details to the JSON file
        super().add_to_file(courses, self.name, {
            'price': self.price,
            'teacher_phone_number': self.teacher_phone_number
        })

    @staticmethod
    def delete_course(name):
        # Static method to delete a course from the JSON file
        try:
            with open('courses.json', 'r') as file:
                # Load current courses data
                courses = json.load(file)
                # Delete the course by name
                del courses[name]
            with open('courses.json', 'w') as file:
                # Write the updated courses data back to the JSON file
                json.dump(courses, file, indent=4)
            print('The course is deleted')
            show_menu()
        except Exception as exc:
            # Print any exception that occurs and prompt for a valid course name
            print(exc)
            name = input('Invalid choice. Please try again: ')
            Courses.delete_course(name)

class Teachers(BaseClass):
    def __init__(self, name, teacher_phone_number, profession, age):
        # Initialize teacher attributes and call the parent constructor with the JSON file name
        super().__init__('teachers.json')
        self.name = name
        self.teacher_phone_number = teacher_phone_number
        self.profession = profession
        self.age = age

    def add_to_file(self):
        # Use the parent class method to add teacher details to the JSON file
        super().add_to_file(teachers, self.name, {
            'teacher_phone_number': self.teacher_phone_number,
            'profession': self.profession,
            'age': self.age
        })

    @staticmethod
    def delete_teacher(name):
        # Static method to delete a teacher from the JSON file
        try:
            with open('teachers.json', 'r') as file:
                # Load current teachers data
                teachers = json.load(file)
                # Delete the teacher by name
                del teachers[name]
            with open('teachers.json', 'w') as file:
                # Write the updated teachers data back to the JSON file
                json.dump(teachers, file, indent=4)
                print('The teacher is deleted')
            show_menu()
        except Exception as exc:
            # Print any exception that occurs and prompt for a valid teacher name
            print(exc)
            name = input('Invalid choice. Please try again: ')
            Teachers.delete_teacher(name)

class Students(BaseClass):
    def __init__(self, name, email, phone_number, id, registered_course):
        # Initialize student attributes and call the parent constructor with the JSON file name
        super().__init__('students.json')
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.id = id
        self.registered_course = registered_course

    def add_to_file(self):
        # Use the parent class method to add student details to the JSON file
        super().add_to_file(students, self.phone_number, {
            'name': self.name,
            'email': self.email,
            'id': self.id,
            'registered_course': self.registered_course
        })

    def get_registered_course(self, phone_number):
        # Method to get the registered course of a student by their phone number
        if self.check_existence():
            with open('students.json', 'r') as file:
                # Load current students data
                students = json.load(file)
                # Find and return the registered course of the student
                for numbers in students.keys():
                    if numbers == phone_number:
                        return f'The user is registered for {students[numbers]["registered_course"]}!'

    def get_users_by_course(self, registered_course):
        # Method to get the list of students registered for a specific course
        if self.check_existence():
            with open('students.json', 'r') as file:
                # Load current students data
                students = json.load(file)
                # Print details of students registered for the specified course
                for student in students.values():
                    if student['registered_course'] == registered_course:
                        print(f'Name: {student["name"]}\nEmail: {student["email"]}\nID: {student["id"]}\nRegistered course: {registered_course}\n')
                show_menu()

    @staticmethod
    def is_valid_email(email):
        # Static method to validate the email format
        try:
            return (
                email.count('@') == 1 and  # Checks if there is exactly one '@' symbol
                email[0] != '@' and  # Ensures the email doesn't start with '@'
                email.count('.') > 0 and  # Checks if there is at least one '.'
                email.rfind('.') > email.find('@')  # Ensures the last '.' comes after the '@'
            )
        except:
            # If the email is invalid, prompt the user to try again
            email = input('Invalid choice. Please try again: ')
            return Students.is_valid_email(email)

def show_menu():
    # Function to display the menu and handle user input
    text = """
    Menu:
    1. Create a new teacher: name, phone_number, profession, age 
    2. Create a course: name, price, teacher_phone_number 
    3. Register to course: name, email, phone_number, id 
    4. Delete a course: name 
    5. Delete a teacher: phone_number 
    6. Get registered courses: phone_number 
    7. Get users by course: course_name 
    8. Exit
    """

    print(text)
    user_input = input("Enter your choice: ")

    if user_input == '1':
        # Gather input to create a new teacher
        name = input('Enter the name of the teacher: ')
        teacher_phone_number = input('Enter the phone number of the teacher: ')
        profession = input('Enter the profession of the teacher: ')
        age = input('Enter the age of the teacher: ')
        teacher = Teachers(name, teacher_phone_number, profession, age)
        teacher.add_to_file()

    elif user_input == '2':
        # Gather input to create a new course
        name = input('Enter the name of the course: ')
        price = input('Enter the price of the course: ')
        teacher_phone_number = input('Enter the phone number of the teacher: ')
        course = Courses(name, price, teacher_phone_number)
        course.add_to_file()

    elif user_input == '3':
        # Gather input to register a student to a course
        name = input('Enter the name of the student: ')
        email = input('Enter the email of the student: ')

        while not Students.is_valid_email(email):
            # Prompt until a valid email is entered
            print("Invalid email. Please try again.")
            email = input('Enter the email of the student: ')
        phone_number = input('Enter the phone number of the student: ')
        id = input('Enter the id of the student: ')
        registered_course = input('Enter the course you want to register for: ')
        student = Students(name, email, phone_number, id, registered_course)
        student.add_to_file()

    elif user_input == '4':
        # Gather input to delete a course
        name = input('Enter the name of the course you want to delete: ')
        Courses.delete_course(name)

    elif user_input == '5':
        # Gather input to delete a teacher
        name = input('Enter the name of the teacher you want to delete: ')
        Teachers.delete_teacher(name)

    elif user_input == '6':
        # Gather input to get the registered course of a student
        phone_number = input('Enter the phone number: ')
        student = Students(None, None, None, None, None)
        print(student.get_registered_course(phone_number))
        show_menu()

    elif user_input == '7':
        # Gather input to get the list of students registered for a specific course
        registered_course = input('Enter the name of the course: ')
        course = Students(None, None, None, None, registered_course)
        course.get_users_by_course(registered_course)

    elif user_input == '8':
        # Exit the program
        print("Exiting program. See you!")
        return
    
    else:
        # Handle invalid input
        print("Invalid choice. Please try again.")
        show_menu()

if __name__ == '__main__':
    # Display the menu when the script is run
    show_menu()