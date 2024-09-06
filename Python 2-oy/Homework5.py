database = dict()

def add_restaurants():
    restaurant = input("Enter the name of the restaurant: ").lower()
    if restaurant in database:
        print(f"{restaurant} already exists in the database.")
    else:
        dishes = dict()
        while True:
            dish_name = input("Enter the name of the dish (or 'done' to finish): ").lower()
            if dish_name == "done":
                break
            price = float(input(f"Enter the price for {dish_name}: "))
            dishes[dish_name] = price
        database[restaurant] = dishes
        print(f"{restaurant} has been added with its dishes.")
    return menu()

def add_dishes():
    restaurant = input("Enter the name of the restaurant to add dishes: ").lower()
    if restaurant in database:
        while True:
            dish_name = input("Enter the name of the dish (or 'done' to finish): ").lower()
            if dish_name == "done":
                break
            price = float(input(f"Enter the price for {dish_name}: "))
            database[restaurant][dish_name] = price
        print(f"Dishes have been added to {restaurant}.")
    else:
        print(f"{restaurant} not found in the database.")
    return menu()

def view_all_restaurants():
    if database:
        for restaurant in database.keys():
            print(f"Restaurant: {restaurant}")
    else:
        print("No restaurant found.")
    return menu()

def view_all_dishes():
    restaurant_name = input("Enter the name of the restaurant: ").lower()
    if restaurant_name in database:
        print(f"Dishes in {restaurant_name}:")
        for dish, price in database[restaurant_name].items():
            print(f"{dish}: {price} UZS")
    else:
        print(f"{restaurant_name} not found in the database.")
    return menu()

def search_dish():
    dish_name = input("Enter the name of the dish: ").lower()
    found = False
    for restaurant, dishes in database.items():
        if dish_name in dishes:
            print(f"{dish_name} is available in {restaurant} for {dishes[dish_name]} UZS")
            found = True
    if not found:
        print(f"{dish_name} not found in any kitchen.")
    return menu()

def delete_restaurant():
    restaurant_name = input("Enter the name of the restaurant you want to delete: ").lower()
    if restaurant_name in database:
        del database[restaurant_name]
        print(f"{restaurant_name} has been deleted from the database.")
    else:
        print(f"{restaurant_name} not found in the database.")
    return menu()

def menu():
    text = """
    0. Add a kitchen and its dishes
    1. View all kitchens
    2. View all dishes of a kitchen
    3. Search for a dish by name
    4. Delete a kitchen by name
    5. Add dishes to an existing kitchen
    6. Exit
    """
    print(text)
    choice = input("Enter your choice: ")

    if choice == '0':
        add_restaurants()
    elif choice == '1':
        view_all_restaurants()
    elif choice == '2':
        view_all_dishes()
    elif choice == '3':
        search_dish()
    elif choice == '4':
        delete_restaurant()
    elif choice == '5':
        add_dishes()
    elif choice == '6':
        print("Exiting program.\nGoodbye!")
    else:
        print("Invalid choice. Please try again.")
        return menu()

if __name__ == "__main__":
    menu()