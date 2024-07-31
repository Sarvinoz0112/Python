import csv
import os

def save_to_csv(data, filename='users.csv'):
    """
    Appends a row of data to the CSV file. Adds headers if the file is new.

    Parameters:
    data (list): A list containing the data to be written to the CSV file.
    filename (str): The name of the CSV file (default is 'users.csv').
    """
    file_exists = os.path.isfile(filename)
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['name', 'age']) 
        writer.writerow(data)

def read_from_csv(filename='users.csv'):
    """
    Reads all rows from the CSV file where each row has exactly two columns.

    Parameters:
    filename (str): The name of the CSV file (default is 'users.csv').

    Returns:
    list: A list of rows, where each row is a list of strings.
    """
    with open(filename, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader, None) 
        return [row for row in reader if len(row) == 2]

def main():
    """
    Main function to handle user input, save it to a CSV file, and then print the contents of the file.
    """
    while True:
        user_input = input("Enter your name and age or write 'exit': ")

        if user_input.lower() == 'exit':
            break

        parts = user_input.split()
        if len(parts) != 2:
            print("Please include your name and age separated by a space.")
            continue

        name, age = parts

        try:
            age = int(age)
        except ValueError:
            print("Please enter a valid age.")
            continue

        save_to_csv([name, age])

    print("Entered data:")
    for row in read_from_csv():
        print(f"Name: {row[0]}, Age: {row[1]}")

if __name__ == "__main__":
    main()