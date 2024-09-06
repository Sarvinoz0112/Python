import json

class Course:
    file_name = "courses.json"  # JSON fayl nomi

    def read_data(self):  # JSON fayldan ma'lumotlarni o'qish funksiyasi
        try:
            with open(self.file_name, 'r') as file:  # Faylni o'qish rejimida ochamiz
                data = json.load(file)  # JSON fayldan ma'lumotlarni yuklaymiz
            return data  # Ma'lumotlarni qaytaramiz
        except FileNotFoundError:  # Agar fayl topilmasa
            return []  # Bo'sh ro'yxat qaytaramiz

    def write_data(self, data):  # JSON faylga ma'lumotlarni yozish funksiyasi
        with open(self.file_name, 'w') as file:  # Faylni yozish rejimida ochamiz
            json.dump(data, file, indent=4)  # Ma'lumotlarni JSON faylga yozamiz, chiroyli formatda (indent=4)

    def add_to_file(self, name, price, teacher):  # Yangi kurs qo'shish funksiyasi
        data = self.read_data()  # Avvalgi ma'lumotlarni o'qib olamiz
        data.append({"name": name, "price": price, "teacher": teacher})  # Yangi kursni ro'yxatga qo'shamiz
        self.write_data(data)  # Yangilangan ma'lumotlarni faylga yozamiz
        return "Added"  # "Qo'shildi" deb xabar qaytaramiz

    def get_info(self, course_name):  # Kurs haqida ma'lumot olish funksiyasi
        data = self.read_data()  # Ma'lumotlarni o'qib olamiz
        for course in data:  # Har bir kursni tekshiramiz
            if course["name"] == course_name:  # Agar kurs nomi berilgan nomga mos kelsa
                return f"Course: {course['name']}, Price: {course['price']}, Teacher: {course['teacher']}"  # Kurs haqida ma'lumot qaytaramiz
        return "No course found"  # Agar kurs topilmasa, xabar qaytaramiz

    def delete_course(self, course_name):  # Kursni o'chirish funksiyasi
        data = self.read_data()  # Ma'lumotlarni o'qib olamiz
        new_data = []  # Yangi ro'yxat yaratamiz
        found = False  # Kurs topilgan-topilmaganligini tekshirish uchun flag
        for course in data:  # Har bir kursni tekshiramiz
            if course["name"] != course_name:  # Agar kurs nomi berilgan nomga mos kelmasa
                new_data.append(course)  # Kursni yangi ro'yxatga qo'shamiz
            else:
                found = True  # Agar kurs topilsa, flagni o'zgartiramiz
        if not found:  # Agar flag hali ham False bo'lsa, kurs topilmagan
            return "No course found"  # Kurs topilmaganligini qaytaramiz
        self.write_data(new_data)  # Yangilangan ma'lumotlarni faylga yozamiz
        return "Deleted"  # "O'chirildi" deb xabar qaytaramiz

    def get_registered_users(self):  # Ro'yxatdan o'tgan foydalanuvchilarni olish funksiyasi
        try:
            with open("registrations.json", 'r') as file:  # Registratsiyalar faylini o'qish rejimida ochamiz
                data = json.load(file)  # JSON fayldan ma'lumotlarni yuklaymiz
                users = [entry for entry in data]  # Har bir foydalanuvchini ro'yxatga qo'shamiz
                return users  # Foydalanuvchilar ro'yxatini qaytaramiz
        except FileNotFoundError:  # Agar fayl topilmasa
            return "No registrations found"  # Registratsiyalar topilmaganligini qaytaramiz


def show_menu():
    menu = """
    Menu:
    1. Create a new course.
    2. Get course information.
    3. Delete a course.
    4. Get registered users.
    5. Exit.
    """
    print(menu)

    user_input = int(input("Choose an option (1-5): "))

    if user_input == 1:
        name = input("Enter course name: ")
        price = input("Enter course price: ")
        teacher = input("Enter teacher name: ")
        print(course.add_to_file(name, price, teacher))
    elif user_input == 2:
        course_name = input("Enter course name to get information: ")
        print(course.get_info(course_name))
    elif user_input == 3:
        course_name = input("Enter course name to delete: ")
        print(course.delete_course(course_name))
    elif user_input == 4:
        print(course.get_registered_users())
    elif user_input == 5:
        print("Exiting program. See you!")
        return
    else:
        print("Invalid choice. Please try again.")
    
    show_menu()  # Menyuni qayta ko'rsatamiz

if __name__ == "__main__":
    show_menu()