class Book:
    def __init__(self, title, author, quantity, price):
        self.title = title
        self.author = author
        self.quantity = quantity
        self.price = price

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.purchased_books = []

class Admin(User):
    pass

class Store:
    def __init__(self):
        self.books = []
        self.users = []
        self.admins = []

    def add_book(self, title, author, quantity, price):
        pass

    def remove_book(self, title):
        pass

    def update_quantity(self, title, quantity):
        pass

    def search_book(self, title):
        pass

    def list_books(self):
        return self.books

class AuthenticationService:
    def __init__(self, store):
        self.store = store

    def register_user(self, username, password):
        pass

    def register_admin(self, username, password):
        pass

    def login(self, username, password):
        pass

class UserService:
    def __init__(self, user, store):
        self.user = user
        self.store = store

    def list_books(self):
        pass

    def search_book(self, title):
        pass

    def buy_book(self, title, quantity):
        pass

    def view_purchased_books(self):
        pass

class AdminService(UserService):
    def add_book(self, title, author, quantity, price):
        pass

    def remove_book(self, title):
        pass

    def update_quantity(self, title, quantity):
        pass

    def list_users(self):
        pass
    
store = Store()
auth_service = AuthenticationService(store)