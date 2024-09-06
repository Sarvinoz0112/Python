import os

# File name to store results
RESULTS_FILE = "results.txt"

# Function to write result to file
def write_result_to_file(result):
    with open(RESULTS_FILE, "a") as file:
        file.write(result + "\n")

# Function to read all results from file
def read_results_from_file():
    if not os.path.exists(RESULTS_FILE):
        return []
    with open(RESULTS_FILE, "r") as file:
        results = file.readlines()
    return [result.strip() for result in results]

# Function to clear all results from file
def clear_results_file():
    if os.path.exists(RESULTS_FILE):
        os.remove(RESULTS_FILE)

# Function to print the menu
def print_menu():
    print("\nMenu:")
    print("1. Add two numbers")
    print("2. Subtract two numbers")
    print("3. Divide two numbers")
    print("4. Multiply two numbers")
    print("5. Raise a number to a power")
    print("6. View all results")
    print("7. View results by operation")
    print("8. Clear all results")
    print("9. Exit")

# Main calculator function
def calculator():
    while True:
        print_menu()
        choice = input("Enter your choice (1-9): ")
        
        if choice == "1":
            try:
                a = float(input("Enter the first number: "))
                b = float(input("Enter the second number: "))
                result = a + b
                print(f"Result: {result}")
                write_result_to_file(f"Addition: {a} + {b} = {result}")
            except ValueError:
                print("Invalid input. Please enter numbers.")
        
        elif choice == "2":
            try:
                a = float(input("Enter the first number: "))
                b = float(input("Enter the second number: "))
                result = a - b
                print(f"Result: {result}")
                write_result_to_file(f"Subtraction: {a} - {b} = {result}")
            except ValueError:
                print("Invalid input. Please enter numbers.")
        
        elif choice == "3":
            try:
                a = float(input("Enter the first number: "))
                b = float(input("Enter the second number: "))
                result = a / b
                print(f"Result: {result}")
                write_result_to_file(f"Division: {a} / {b} = {result}")
            except ValueError:
                print("Invalid input. Please enter numbers.")
            except ZeroDivisionError:
                print("Division by zero is not allowed.")
        
        elif choice == "4":
            try:
                a = float(input("Enter the first number: "))
                b = float(input("Enter the second number: "))
                result = a * b
                print(f"Result: {result}")
                write_result_to_file(f"Multiplication: {a} * {b} = {result}")
            except ValueError:
                print("Invalid input. Please enter numbers.")
        
        elif choice == "5":
            try:
                a = float(input("Enter the number: "))
                b = float(input("Enter the power: "))
                result = a ** b
                print(f"Result: {result}")
                write_result_to_file(f"Exponentiation: {a} ^ {b} = {result}")
            except ValueError:
                print("Invalid input. Please enter numbers.")
        
        elif choice == "6":
            results = read_results_from_file()
            if results:
                print("\nAll results:")
                for res in results:
                    print(res)
            else:
                print("No results available.")
        
        elif choice == "7":
            operation = input("Which operation results do you want to see? (Addition, Subtraction, Division, Multiplication, Exponentiation): ")
            results = read_results_from_file()
            filtered_results = [res for res in results if res.startswith(operation)]
            if filtered_results:
                print(f"\n{operation} results:")
                for res in filtered_results:
                    print(res)
            else:
                print(f"No results for {operation}.")
        
        elif choice == "8":
            clear_results_file()
            print("All results have been cleared.")
        
        elif choice == "9":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")

if __name__ == "__main__":
    calculator()