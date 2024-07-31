import logging
import json
from functools import wraps

# Logging konfiguratsiyasi
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# JSON fayl nomi
file_name = 'users.json'

def handle_exceptions(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"Xato {func.__name__} funksiyasida: {e}")
            raise
    return wrapper

@handle_exceptions
def load_users():
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        logging.info("JSON fayli topilmadi, yangi fayl yaratiladi.")
        return []
    except json.JSONDecodeError:
        logging.error("JSON faylni o'qishda xato. Bo'sh ro'yxat qaytariladi.")
        return []

@handle_exceptions
def save_users(users):
    with open(file_name, 'w') as file:
        json.dump(users, file, indent=4)
    logging.info("Foydalanuvchilar JSON faylga saqlandi.")

@handle_exceptions
def add_user(users):
    logging.info("Foydalanuvchilarni qo'shish boshlandi.")
    while True:
        name = input("Ism: ")
        if name.lower() == 'done':
            break
        surname = input("Familiya: ")
        age = input("Yosh: ")
        users.append({'name': name, 'surname': surname, 'age': age})
        logging.info(f"Foydalanuvchi qo'shildi: {name} {surname}, {age} yosh.")
    save_users(users)

def show_users(users):
    if users:
        logging.info("Foydalanuvchilar ro'yxati:")
        for user in users:
            print(f"Ism: {user['name']}, Familiya: {user['surname']}, Yosh: {user['age']}")
    else:
        logging.info("Hozircha foydalanuvchilar mavjud emas.")

def main():
    users = load_users()
    while True:
        print("\nMenu:")
        print("1. Foydalanuvchi qo'shish")
        print("2. Foydalanuvchilarni ko'rsatish")
        choice = input("Tanlovingizni kiriting: ")
        
        if choice == '1':
            add_user(users)
        elif choice == '2':
            show_users(users)
        else:
            logging.warning("Noto'g'ri tanlov. Iltimos, qaytadan urinib ko'ring.")

if __name__ == "__main__":
    main()
