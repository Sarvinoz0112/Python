from abc import ABC, abstractmethod
import json

# Abstract base class for shapes
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Rectangle subclass with implementations for area and perimeter
class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return 2 * (self.a + self.b)

# Circle subclass with implementations for area and perimeter
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.14

    def area(self):
        return self.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * self.pi * self.radius

# Function to save results to a JSON file
def save_to_json(results):
    """
    Saves the results list to a JSON file.
    """
    with open('results.json', 'w') as file:
        json.dump(results, file, indent=4)

# Function to calculate the area of a circle
def calculate_circle_area(results):
    """
    Prompts the user to enter the radius of a circle, calculates the area,
    prints the result, and saves it to the results list and JSON file.
    """
    radius = float(input("Enter the radius of the circle: "))
    circle = Circle(radius)
    area = circle.area()
    print(f"Area of the circle: {area}")
    results.append({"shape": "Circle", "operation": "area", "radius": radius, "result": area})
    save_to_json(results)

# Function to calculate the perimeter of a circle
def calculate_circle_perimeter(results):
    """
    Prompts the user to enter the radius of a circle, calculates the perimeter,
    prints the result, and saves it to the results list and JSON file.
    """
    radius = float(input("Enter the radius of the circle: "))
    circle = Circle(radius)
    perimeter = circle.perimeter()
    print(f"Perimeter of the circle: {perimeter}")
    results.append({"shape": "Circle", "operation": "perimeter", "radius": radius, "result": perimeter})
    save_to_json(results)

# Function to calculate the area of a rectangle
def calculate_rectangle_area(results):
    """
    Prompts the user to enter the sides of a rectangle, calculates the area,
    prints the result, and saves it to the results list and JSON file.
    """
    a = float(input("Enter the first side of the rectangle: "))
    b = float(input("Enter the second side of the rectangle: "))
    rectangle = Rectangle(a, b)
    area = rectangle.area()
    print(f"Area of the rectangle: {area}")
    results.append({"shape": "Rectangle", "operation": "area", "a": a, "b": b, "result": area})
    save_to_json(results)

# Function to calculate the perimeter of a rectangle
def calculate_rectangle_perimeter(results):
    """
    Prompts the user to enter the sides of a rectangle, calculates the perimeter,
    prints the result, and saves it to the results list and JSON file.
    """
    a = float(input("Enter the first side of the rectangle: "))
    b = float(input("Enter the second side of the rectangle: "))
    rectangle = Rectangle(a, b)
    perimeter = rectangle.perimeter()
    print(f"Perimeter of the rectangle: {perimeter}")
    results.append({"shape": "Rectangle", "operation": "perimeter", "a": a, "b": b, "result": perimeter})
    save_to_json(results)

# Function to show all results nicely formatted
def show_all_results(results):
    """
    Prints all the results in a nicely formatted way.
    """
    print("\nAll results:")
    for result in results:
        shape = result["shape"]
        operation = result["operation"]
        if shape == "Circle":
            radius = result["radius"]
            res = result["result"]
            if operation == "area":
                print(f"Circle with radius {radius}: Area = {res}")
            elif operation == "perimeter":
                print(f"Circle with radius {radius}: Perimeter = {res}")
        elif shape == "Rectangle":
            a = result["a"]
            b = result["b"]
            res = result["result"]
            if operation == "area":
                print(f"Rectangle with sides {a} and {b}: Area = {res}")
            elif operation == "perimeter":
                print(f"Rectangle with sides {a} and {b}: Perimeter = {res}")

# Main function to provide the menu and handle user choices
def main():
    """
    Main function to provide a menu for the user to calculate areas and perimeters
    of circles and rectangles, show results, and exit the program.
    """
    results = []
    while True:
        print("\nMenu:")
        print("1. Calculate the area of a circle: radius")
        print("2. Calculate the perimeter of a circle: radius")
        print("3. Calculate the area of a rectangle: a, b")
        print("4. Calculate the perimeter of a rectangle: a, b")
        print("5. Show all results")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            calculate_circle_area(results)
        elif choice == 2:
            calculate_circle_perimeter(results)
        elif choice == 3:
            calculate_rectangle_area(results)
        elif choice == 4:
            calculate_rectangle_perimeter(results)
        elif choice == 5:
            show_all_results(results)
        elif choice == 6:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()