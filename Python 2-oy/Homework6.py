courses = dict()
registrations = dict()


def add_course():

    course_name = input("Course name: ")

    if course_name in courses:
        print(f"The course '{course_name}' already exists.")
    else:
        courses[course_name] = []
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
    elif (phone, full_name) in courses[course_name]:
        print(f"You have already registered for the course '{course_name}'.")
    else:
        courses[course_name].append((phone, full_name))
    
        if (phone, full_name) not in registrations:
            registrations[(phone, full_name)] = []
        registrations[(phone, full_name)].append(course_name)
        print(f"You have successfully registered for the course '{course_name}'.")



def list_user_courses():

    phone = input("Phone number: ")
    full_name = input("Full name: ")
    user = (phone, full_name)

    if user not in registrations or not registrations[user]:
        print("You have not registered for any courses.")
    else:
        print(f"Courses registered for {full_name}:")
        for course in registrations[user]:
            print(f"- {course}")



def main():

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