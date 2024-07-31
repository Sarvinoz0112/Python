class People:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.__gender = gender

def get_gender(self):
    return self.__gender


def set_geneder(self, new_gender):
    self.__gender = new_gender


class Vehicle:
    def __init__(self, name, price):
        self.name = name
        self._price = price

class Car(Vehicle):
    def __init__(self, name, price, color):
        super().__init__(name, price)
        self.color = color

#---------------------------------------------------------

class BankAccount:
    def __init__(self, owner, deposit):
        self.owner = owner
        self.__deposit = deposit

    def add_money(self, amount):
        if amount > 0:
            self.__deposit += amount
            print(f"{amount} qo'shildi. Hozirgi balans: {self.__deposit}")
        else:
            print("Summani to'g'ri kiriting.")

    def subtract_money(self, amount):
        if amount > 0:
            if self.__deposit >= amount:
                self.__deposit -= amount
                print(f"{amount} yechildi. Hozirgi balans: {self.__deposit}")
            else:
                print("Balans yetarli emas.")
        else:
            print("Summani to'g'ri kiriting.")

    def show_deposit(self):
        print(f"Hozirgi balans: {self.__deposit}")

account = BankAccount("Ali", 100)
account.add_money(50)

#------------------------------------------------------

class Library:
    def __init__(self):
        self.__books = []

    def add_book(self, book_name):
        self.__books.append(book_name)
        print(f"'{book_name}' kitobi qo'shildi.")

    def get_book(self, book_name):
        if book_name in self.__books:
            self.__books.remove(book_name)
            print(f"'{book_name}' kitobi olingan.")
            return book_name
        else:
            print(f"'{book_name}' kitobi mavjud emas.")

    def show_books(self):
        print("\nHozirgi kitoblar ro'yxati:")
        for book in self.__books:
            print(f"{book}")

library = Library()
library.add_book("Python Programming")
library.show_books()