import hashlib

class User:
    def __init__(self, first_name, last_name, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

class Store:
    def __init__(self):
        self.users = []

    def register(self):
        first_name = input("Ismingizni kiriting: ")
        last_name = input("Familiyangizni kiriting: ")
        username = input("Foydalanuvchi nomini kiriting: ")

        if username in self.users:
            return "Bu foydalanuvchi nomi allaqachon band."

        while True:
            password = input("Parol yarating: ")
            confirm_password = input("Parolni tasdiqlang: ")

            if password != confirm_password:
                print("Parollar mos kelmadi. Qaytadan urinib ko'ring.")
            else:
                break

        self.users[username] = User(first_name, last_name, username, password)
        return "Ro'yxatdan o'tish muvaffaqiyatli."

    def login(self):
        username = input("Foydalanuvchi nomini kiriting: ")
        password = input("Parolni kiriting: ")

        if username not in self.users:
            return "Bunday foydalanuvchi mavjud emas."

        user = self.users[username]
        if user.password == hashlib.sha256(password.encode()).hexdigest():
            return "Tizimga kirish muvaffaqiyatli."
        return "Parol noto'g'ri."


store = Store()
print(store.register())
print(store.login())