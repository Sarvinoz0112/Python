import datetime

def timer(func):
    def wrapper():
        start_time = datetime.datetime.now()
        func()
        end_time = datetime.datetime.now()
        execution_time = end_time - start_time
        print(f"Funktsiya {execution_time} soniyada ishladi")
    return wrapper

@timer
def get_user_info():
    name = input("Ismingizni kiriting: ")
    phone = input("Telefon raqamingizni kiriting: ")
    print(f"Ism: {name}, Telefon raqam: {phone}")

get_user_info()