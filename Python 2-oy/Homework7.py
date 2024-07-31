import json
import os

courses_file = "courses.json"
users_file = "users.json"

courses = {}
registrations = {}


def load_data():
    global courses, registrations # global bu funksiyada 'courses' va 'registrations' o'zgaruvchilari yangi lokal nusxalarini yaratish o'rniga, dastur boshida e'lon qilingan global o'zgaruvchilarni ishlatadi.

    if os.path.exists(courses_file):
        with open(courses_file, "r") as f:
            courses = json.load(f)

    if os.path.exists(users_file):
        with open(users_file, "r") as f:
            registrations = json.load(f)

    print("Data loaded:")
    print("Courses:", courses)
    print("Registrations:", registrations)


def save_data():
    with open(courses_file, "w") as f:
        json.dump(courses, f)

    with open(users_file, "w") as f:
        json.dump(registrations, f)

    print("Data saved:")
    print("Courses:", courses)
    print("Registrations:", registrations)


def add_course():
    course_name = input("Course name: ")

    if course_name in courses:
        print(f"The course '{course_name}' already exists.")
    else:
        courses[course_name] = []
        save_data()
        print(f"The course '{course_name}' has been added successfully.")


def list_courses():
    if not courses:
        print("There are currently no courses available.")
    else:
        print("Available courses:")
        for course in courses:
            print(f"- {course}")


def register_for_course():
    course_name = input("Course name: ")
    phone = input("Phone number: ")
    full_name = input("Full name: ")

    if course_name not in courses:
        print(f"The course '{course_name}' does not exist.")
    elif any(reg["phone"] == phone and reg["full_name"] == full_name for reg in courses[course_name]):
        print(f"You have already registered for the course '{course_name}'.")
    else:
        courses[course_name].append({"phone": phone, "full_name": full_name})

        if phone not in registrations:
            registrations[phone] = []
        registrations[phone].append({"full_name": full_name, "course_name": course_name})
        
        save_data()  # yangi ro'yxatdan o'tish qo'shilgandan keyin ma'lumotlarni saqlash
        print(f"You have successfully registered for the course '{course_name}'.")


def list_user_courses():
    phone = input("Phone number: ")
    full_name = input("Full name: ")

    if phone not in registrations or not any(reg["full_name"] == full_name for reg in registrations[phone]):
        print("You have not registered for any courses.")
    else:
        print(f"Courses registered for {full_name}:")
        for reg in registrations[phone]:
            if reg["full_name"] == full_name:
                print(f"- {reg['course_name']}")


def main():
    load_data() # dastur boshlanishida ma'lumotlarni yuklash

    while True:
        print("\n1. Add a course")
        print("2. List all courses")
        print("3. Register for a course")
        print("4. List registered courses")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_course()
        elif choice == '2':
            list_courses()
        elif choice == '3':
            register_for_course()
        elif choice == '4':
            list_user_courses()
        elif choice == '5':
            print("Exiting the program.\nGood bye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()