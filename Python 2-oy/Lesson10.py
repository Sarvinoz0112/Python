def collect_and_write_to_file():
    name = input("Enter your name: ")
    car_name = input("Enter your fav car name: ")
    horse_power = input("Nechta ot kuchi borligini kiriting: ")
    made_in = input("Qayerda ishlab chiqazilganini kiriting: ")
    color = input("Rangini kiriting: ")

    data = (f"Name: {name}\n"
            f"Favorite Car: {car_name}\n"
            f"Horse Power: {horse_power}\n"
            f"Manufactured In: {made_in}\n"
            f"Color: {color}\n")
    
    with open("car_info.txt", "w") as file:
        file.write(data)

    print("Data has been written to car_info.txt")
    return collect_and_write_to_file()

#--------------------------------------------------------------------------

import json, os


def write_into_json(filename, data):
    products = read_from_json(filename='products.json')
    products[data['product_id']] = data

    with open(filename, 'w') as write_file:
        json.dump(products, write_file, indent=4)
    return True


def read_from_json(filename):
    if not os.path.exists(filename):
        with open(file=filename, mode='x', encoding='UTF-8') as read_file:
            read_file.write("{}")

    with open(file=filename, encoding='UTF-8') as file:
        return json.load(file)


def check_product_id(product_id):
    products = read_from_json(filename='products.json')
    if product_id in products.keys():
        return True
    return False


def add_product():
    product_id = input("Enter product ID: ")
    if check_product_id(product_id):
        print("Product ID exists")
        add_product()
    product_name = input("Enter product name: ")
    product_price = input("Enter product price: ")
    product_quantity = input("Enter product quantity: ")
    product_color = input("Enter product color: ")
    data = {
        'product_id': product_id,
        'product_name': product_name,
        'product_price': product_price,
        'product_quantity': product_quantity,
        'product_color': product_color
    }

    if write_into_json(filename='products.json', data=data):
        print("Product is added")
        return show_menu()
    print("Product does not added")
    return show_menu()


def show_menu():
    text = """
    1: Add product
    2: Exit
    """
    print(text)

    user_input = int(input("Choice from menu: "))
    if user_input == 1:
        add_product()
    elif user_input == 2:
        print("Good bye")
        return


if __name__ == "__main__":
    show_menu()

#-----------------------------------------------------------------------

'''
json file ni csv file ga o'g'irish
'''
import os, json


def read_from_json(filename):
    if not os.path.exists(filename):
        with open(file=filename, mode='x') as read_file:
            read_file.write("{}")

    with open(file=filename, encoding='UTF-8') as file:
        return json.load(file)


def write_into_csv(filename):
    products = read_from_json(filename='products.json')
    if not os.path.exists(path=filename):
        with open(file=filename, mode='w') as new_file:
            new_file.write("id,name,price,quantity,color\n")

    with open(filename, 'a') as write_file:
        for product in products.values():
            row = ",".join(product.values()) + "\n"
            write_file.write(row)
    return True


write_into_csv(filename='products.csv')

os.mkdir('users')