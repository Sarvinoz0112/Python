import json
import random

data = {
    "teachers": [],
    "groups": [],
    "students": [],
    "lessons": []
}

def load_data():
    '''Load data from file if it exists.'''
    try:
        with open('data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return data

def save_data(data):
    '''Save data to file.'''
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)

data = load_data()

def generate_random_id(length=5):
    '''Generate a random 5-digit ID.'''
    return ''.join(random.choices('0123456789', k=length))

def generate_random_password(length=5):
    '''Generate a random 5-digit password.'''
    return ''.join(random.choices('0123456789', k=length))

def is_valid_name(name):
    '''Check if the name is valid.'''
    return name.isalpha() and len(name) > 1

def is_valid_number(number):
    '''Check if the number is valid.'''
    return number.isdigit() and int(number) > 0


class Teacher:
    def create_teacher(name, subjects):
        '''Create a new teacher.'''
        data["teachers"].append({"id": len(data["teachers"]) + 1, "name": name, "subjects": subjects})
        save_data(data)

    def read_teachers():
        '''Return the list of teachers.'''
        return data["teachers"]

    def update_teacher(teacher_id, new_name, new_subjects):
        '''Update an existing teacher.'''
        for teacher in data["teachers"]:
            if teacher["id"] == teacher_id:
                teacher["name"] = new_name
                teacher["subjects"] = new_subjects
                save_data(data)
                return True
        return False

    def delete_teacher(teacher_id):
        '''Delete a teacher.'''
        for teacher in data["teachers"]:
            if teacher["id"] == teacher_id:
                data["teachers"].remove(teacher)
                save_data(data)
                return True
        return False

    def teacher_exists(name):
        '''Check if a teacher exists.'''
        return any(teacher["name"] == name for teacher in data["teachers"])


class Group:
    def create_group(name, subjects, teachers, student_count):
        '''Create a new group.'''
        data["groups"].append({
            "id": len(data["groups"]) + 1,
            "name": name,
            "subjects": subjects,
            "teachers": teachers,
            "student_count": student_count
        })
        save_data(data)

    def read_groups():
        '''Return the list of groups.'''
        return data["groups"]

    def update_group(group_id, new_name, new_subjects, new_teachers, new_student_count):
        '''Update an existing group.'''
        for group in data["groups"]:
            if group["id"] == group_id:
                group["name"] = new_name
                group["subjects"] = new_subjects
                group["teachers"] = new_teachers
                group["student_count"] = new_student_count
                save_data(data)
                return True
        return False

    def delete_group(group_id):
        '''Delete a group.'''
        for group in data["groups"]:
            if group["id"] == group_id:
                data["groups"].remove(group)
                save_data(data)
                return True
        return False

    def group_exists(group_name):
        '''Check if a group exists.'''
        return any(group["name"] == group_name for group in data["groups"])


class Student:
    def create_student(first_name, last_name, phone_number):
        '''Create a new student.'''
        student_id = generate_random_id()
        password = generate_random_password()
        data["students"].append({
            "id": student_id,
            "first_name": first_name,
            "last_name": last_name,
            "phone_number": phone_number,
            "password": password
        })
        save_data(data)
        print(f"Student created with ID: {student_id} and Password: {password}")

    def read_students():
        '''Return the list of students.'''
        return data["students"]

    def update_student(student_id, new_first_name, new_last_name):
        '''Update an existing student.'''
        for student in data["students"]:
            if student["id"] == student_id:
                student["first_name"] = new_first_name
                student["last_name"] = new_last_name
                save_data(data)
                return True
        return False

    def delete_student(student_id):
        '''Delete a student.'''
        for student in data["students"]:
            if student["id"] == student_id:
                data["students"].remove(student)
                save_data(data)
                return True
        return False


class Lesson:
    def create_lesson(group_name, teacher, time):
        '''Create a new lesson.'''
        data["lessons"].append({
            "id": len(data["lessons"]) + 1,
            "group_name": group_name,
            "teacher": teacher,
            "time": time
        })
        save_data(data)

    def read_lessons():
        '''Return the list of lessons.'''
        return data["lessons"]

    def teacher_has_lesson(teacher_name, time):
        '''Check if a teacher has a lesson at a specific time.'''
        for lesson in data["lessons"]:
            if lesson["teacher"] == teacher_name and lesson["time"] == time:
                return True
        return False

    def teacher_exists(name):
        '''Check if a teacher exists.'''
        return any(teacher["name"] == name for teacher in data["teachers"])


class Admin:
    def admin_menu():
        '''Display the admin menu.'''
        while True:
            print("\nAdmin Menu:")
            print("1. Teacher -> CRUD")
            print("2. Group -> CRUD")
            print("3. Student -> CRUD")
            print("4. Manage lessons")
            print("5. Show lessons table")
            print("6. Logout")
            choice = input("Choose an option: ")

            if choice == '1':
                Admin.manage_teachers()
            elif choice == '2':
                Admin.manage_groups()
            elif choice == '3':
                Admin.manage_students()
            elif choice == '4':
                Admin.manage_lessons()
            elif choice == '5':
                Admin.show_lessons()
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")

    def manage_teachers():
        '''Manage teachers.'''
        while True:
            print("\nTeachers Menu:")
            print("1. Create Teacher")
            print("2. Read Teachers")
            print("3. Update Teacher")
            print("4. Delete Teacher")
            print("5. Back to Admin Menu")
            choice = input("Choose an option: ")

            if choice == '1':
                name = input("Enter teacher name: ")
                if not is_valid_name(name):
                    print("Invalid name. Please enter a valid name.")
                    continue
                num_subjects = input("How many subjects does this teacher teach? ")
                if not is_valid_number(num_subjects):
                    print("Invalid number. Please enter a positive integer.")
                    continue
                num_subjects = int(num_subjects)
                subjects = [input(f"Enter subject {i+1}: ") for i in range(num_subjects)]
                Teacher.create_teacher(name, subjects)
            elif choice == '2':
                teachers = Teacher.read_teachers()
                for teacher in teachers:
                    print(f"ID: {teacher['id']}, Name: {teacher['name']}, Subjects: {', '.join(teacher['subjects'])}")
            elif choice == '3':
                teacher_id = input("Enter teacher ID: ")
                if not is_valid_number(teacher_id):
                    print("Invalid ID. Please enter a valid integer.")
                    continue
                teacher_id = int(teacher_id)
                new_name = input("Enter new teacher name: ")
                if not is_valid_name(new_name):
                    print("Invalid name. Please enter a valid name.")
                    continue
                num_subjects = input("How many subjects does this teacher teach? ")
                if not is_valid_number(num_subjects):
                    print("Invalid number. Please enter a positive integer.")
                    continue
                num_subjects = int(num_subjects)
                new_subjects = [input(f"Enter subject {i+1}: ") for i in range(num_subjects)]
                if Teacher.update_teacher(teacher_id, new_name, new_subjects):
                    print("Teacher updated successfully.")
                else:
                    print("Teacher not found.")
            elif choice == '4':
                teacher_id = input("Enter teacher ID: ")
                if not is_valid_number(teacher_id):
                    print("Invalid ID. Please enter a valid integer.")
                    continue
                teacher_id = int(teacher_id)
                if Teacher.delete_teacher(teacher_id):
                    print("Teacher deleted successfully.")
                else:
                    print("Teacher not found.")
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")

    def manage_groups():
        '''Manage groups.'''
        while True:
            print("\nGroups Menu:")
            print("1. Create Group")
            print("2. Read Groups")
            print("3. Update Group")
            print("4. Delete Group")
            print("5. Back to Admin Menu")
            choice = input("Choose an option: ")

            if choice == '1':
                name = input("Enter group name: ")
                if not is_valid_name(name):
                    print("Invalid name. Please enter a valid name.")
                    continue
                num_subjects = input("How many subjects does this group have? ")
                if not is_valid_number(num_subjects):
                    print("Invalid number. Please enter a positive integer.")
                    continue
                num_subjects = int(num_subjects)
                subjects = [input(f"Enter subject {i+1}: ") for i in range(num_subjects)]
                num_teachers = input("How many teachers are in this group? ")
                if not is_valid_number(num_teachers):
                    print("Invalid number. Please enter a positive integer.")
                    continue
                num_teachers = int(num_teachers)
                teachers = [input(f"Enter teacher {i+1} name: ") for i in range(num_teachers)]
                num_students = input("How many students are in this group? ")
                if not is_valid_number(num_students):
                    print("Invalid number. Please enter a positive integer.")
                    continue
                num_students = int(num_students)
                Group.create_group(name, subjects, teachers, num_students)
            elif choice == '2':
                groups = Group.read_groups()
                for group in groups:
                    print(f"ID: {group['id']}, Name: {group['name']}, Subjects: {', '.join(group['subjects'])}, Teachers: {', '.join(group['teachers'])}, Student Count: {group['student_count']}")
            elif choice == '3':
                group_id = input("Enter group ID: ")
                if not is_valid_number(group_id):
                    print("Invalid ID. Please enter a valid integer.")
                    continue
                group_id = int(group_id)
                new_name = input("Enter new group name: ")
                if not is_valid_name(new_name):
                    print("Invalid name. Please enter a valid name.")
                    continue
                num_subjects = input("How many subjects does this group have? ")
                if not is_valid_number(num_subjects):
                    print("Invalid number. Please enter a positive integer.")
                    continue
                num_subjects = int(num_subjects)
                new_subjects = [input(f"Enter subject {i+1}: ") for i in range(num_subjects)]
                num_teachers = input("How many teachers are in this group? ")
                if not is_valid_number(num_teachers):
                    print("Invalid number. Please enter a positive integer.")
                    continue
                num_teachers = int(num_teachers)
                new_teachers = [input(f"Enter teacher {i+1} name: ") for i in range(num_teachers)]
                new_student_count = input("Enter new student count: ")
                if not is_valid_number(new_student_count):
                    print("Invalid number. Please enter a positive integer.")
                    continue
                new_student_count = int(new_student_count)
                if Group.update_group(group_id, new_name, new_subjects, new_teachers, new_student_count):
                    print("Group updated successfully.")
                else:
                    print("Group not found.")
            elif choice == '4':
                group_id = input("Enter group ID: ")
                if not is_valid_number(group_id):
                    print("Invalid ID. Please enter a valid integer.")
                    continue
                group_id = int(group_id)
                if Group.delete_group(group_id):
                    print("Group deleted successfully.")
                else:
                    print("Group not found.")
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")

    def manage_students():
        '''Manage students.'''
        while True:
            print("\nStudents Menu:")
            print("1. Create Student")
            print("2. Read Students")
            print("3. Update Student")
            print("4. Delete Student")
            print("5. Back to Admin Menu")
            choice = input("Choose an option: ")

            if choice == '1':
                first_name = input("Enter student first name: ")
                if not is_valid_name(first_name):
                    print("Invalid first name. Please enter a valid name.")
                    continue
                last_name = input("Enter student last name: ")
                if not is_valid_name(last_name):
                    print("Invalid last name. Please enter a valid name.")
                    continue
                phone_number = input("Enter student phone number: ")
                Student.create_student(first_name, last_name, phone_number)
            elif choice == '2':
                students = Student.read_students()
                for student in students:
                    print(f"ID: {student['id']}, Name: {student['first_name']} {student['last_name']}")
            elif choice == '3':
                student_id = input("Enter student ID: ")
                if not is_valid_number(student_id):
                    print("Invalid ID. Please enter a valid integer.")
                    continue
                student_id = int(student_id)
                new_first_name = input("Enter new first name: ")
                if not is_valid_name(new_first_name):
                    print("Invalid first name. Please enter a valid name.")
                    continue
                new_last_name = input("Enter new last name: ")
                if not is_valid_name(new_last_name):
                    print("Invalid last name. Please enter a valid name.")
                    continue
                if Student.update_student(student_id, new_first_name, new_last_name):
                    print("Student updated successfully.")
                else:
                    print("Student not found.")
            elif choice == '4':
                student_id = input("Enter student ID: ")
                if not is_valid_number(student_id):
                    print("Invalid ID. Please enter a valid integer.")
                    continue
                student_id = int(student_id)
                if Student.delete_student(student_id):
                    print("Student deleted successfully.")
                else:
                    print("Student not found.")
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")

    def manage_lessons():
        '''Manage lessons.'''
        group_name = input("Enter group name: ")
        if not Group.group_exists(group_name):
            print("Group does not exist. Please enter a valid group name.")
            return
        teacher_name = input("Enter teacher name: ")
        if not Teacher.teacher_exists(teacher_name):
            print("Teacher does not exist. Please enter a valid teacher name.")
            return
        time = input("Enter lesson time (e.g., '2024-07-25 10:00'): ")
        if Lesson.teacher_has_lesson(teacher_name, time):
            print("The teacher already has a lesson at this time.")
        else:
            Lesson.create_lesson(group_name, teacher_name, time)
            print("Lesson created successfully.")

    def show_lessons():
        '''Show the list of lessons.'''
        lessons = Lesson.read_lessons()
        for lesson in lessons:
            print(f"ID: {lesson['id']}, Group: {lesson['group_name']}, Teacher: {lesson['teacher']}, Time: {lesson['time']}")

def main():
    '''Main program.'''
    while True:
        print("\nAuth Menu:")
        print("1. Login")
        print("2. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            if username == "admin" and password == "admin":
                Admin.admin_menu()
            else:
                print("Invalid credentials. Please try again.")
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
