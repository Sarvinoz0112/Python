import json
import os
import random
from datetime import datetime, timedelta

# File names for storing card and transfer information
cards_file = 'cards.json'
transfers_file = 'transfers.json'

# Function to load cards from file
def load_cards():
    if os.path.exists(cards_file):
        with open(cards_file, 'r') as file:
            return json.load(file)
    return {}

# Function to save cards to file
def save_cards(cards):
    with open(cards_file, 'w') as file:
        json.dump(cards, file, indent=4)

# Function to load transfers from file
def load_transfers():
    if os.path.exists(transfers_file):
        with open(transfers_file, 'r') as file:
            return json.load(file)
    return []

# Function to save transfers to file
def save_transfers(transfers):
    with open(transfers_file, 'w') as file:
        json.dump(transfers, file, indent=4)

# Function to generate a unique card number
def generate_card_number(cards):
    while True:
        card_number = ''.join([str(random.randint(0, 9)) for _ in range(8)])
        if card_number not in cards:
            return card_number

# Function to generate expiration date for the card (3 years from now)
def generate_expiration_date():
    expiration_date = datetime.now() + timedelta(days=3*365)
    return expiration_date.strftime("%m/%y")

# Function to create a new card
def create_card(cards):
    full_name = input("Enter your full name: ")
    passport_number = input("Enter your passport number: ")
    password = input("Enter your password: ")
    card_number = generate_card_number(cards)
    expiration_date = generate_expiration_date()
    cards[card_number] = {
        'full_name': full_name,
        'passport_number': passport_number,
        'password': password,
        'balance': 0.0,
        'expiration_date': expiration_date
    }
    save_cards(cards)
    print(f"New card created. Card number: {card_number}, Expiration date: {expiration_date}")

# Function to add money to a card
def add_money_to_card(cards, transfers):
    card_number = input("Card number: ")
    password = input("Password: ")
    if card_number in cards and cards[card_number]['password'] == password:
        money = float(input("Amount: "))
        cards[card_number]['balance'] += money
        transfers.append({'card_number': card_number, 'amount': money})
        save_cards(cards)
        save_transfers(transfers)
        print(f"{money} added to the card.")
    else:
        print("Card number or password is incorrect.")

# Function to view card information
def view_card_info(cards):
    card_number = input("Card number: ")
    password = input("Password: ")
    if card_number in cards and cards[card_number]['password'] == password:
        card = cards[card_number]
        print(f"Full name: {card['full_name']}")
        print(f"Passport number: {card['passport_number']}")
        print(f"Balance: {card['balance']}")
        print(f"Expiration date: {card['expiration_date']}")
    else:
        print("Card number or password is incorrect.")

# Main menu function
def menu():
    cards = load_cards()
    transfers = load_transfers()
    while True:
        print("\n1. Purchase a new card")
        print("2. Add money to a card")
        print("3. View card information")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            create_card(cards)
        elif choice == '2':
            add_money_to_card(cards, transfers)
        elif choice == '3':
            view_card_info(cards)
        elif choice == '4':
            print("Exiting the program.\nGoodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    menu()