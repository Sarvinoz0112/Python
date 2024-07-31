from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def age(self):
        raise NotImplementedError("Not implemented")
    
    @abstractmethod
    def sound(self):
        raise NotImplementedError("Not implemented")
    

class Cat(Animal):
    def sound(self):
        return "Meow"
    
    def age(self):
        return 22
    
a1 = Cat()
print(a1.age())

#--------------------------------------------------------------------

import json
import os
from abc import ABC, abstractmethod

class JsonManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def check_existence(self):
        return os.path.exists(self.file_name)

    def read(self):
        if self.check_existence():
            if os.path.getsize(self.file_name) != 0:
                with open(self.file_name, 'r') as file:
                    data = json.load(file)
                    return data
            return []
        return []

    def write(self, all_data):
        with open(self.file_name, mode='w') as file:
            json.dump(all_data, file, indent=4)
            return "Data is added"

    def add(self, data: dict):
        all_data = self.read()
        all_data.append(data)
        return self.write(all_data)

    def update(self, updated_data: dict):
        all_data = self.read()
        for index, course in enumerate(all_data):
            if course['name'] == updated_data['name'] and course['teacher'] == updated_data['teacher']:
                all_data[index] = updated_data
                break
        else:
            all_data.append(updated_data)
        return self.write(all_data)

class Course(ABC, JsonManager):
    def __init__(self, name, price, teacher):
        super().__init__(file_name="courses.json")
        self.name = name
        self.price = price
        self.teacher = teacher
        self.users = []

    def parent_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "teacher": self.teacher,
            "users": self.users
        }

    @abstractmethod
    def register(self, user):
        raise NotImplementedError("You must implement register method")

    @abstractmethod
    def cancel_register(self, user):
        raise NotImplementedError("You must implement cancel_register")

    @abstractmethod
    def show_users(self):
        raise NotImplementedError("You must implement show_users")

class Math(Course):
    def __init__(self, name, price, teacher, time):
        super().__init__(name, price, teacher)
        self.file_name = "math.json"
        self.time = time

    def dict(self):
        data = self.parent_dict()
        data["time"] = self.time
        return data

    def add_to_file(self):
        return self.add(self.dict())

    def register(self, user):
        self.users.append(user)
        self.update(self.dict())
        print(f"{user} has been registered for the Math course.")

    def cancel_register(self, user):
        if user in self.users:
            self.users.remove(user)
            self.update(self.dict())
            print(f"{user} has been removed from the Math course.")
        else:
            print(f"{user} is not registered in the Math course.")

    def show_users(self):
        data = self.read()
        for course in data:
            if course['name'] == self.name and course['teacher'] == self.teacher:
                self.users = course['users']
                break
        print("Registered users in Math course:")
        for user in self.users:
            print(user)

class Dance(Course):
    def __init__(self, name, price, teacher, age):
        super().__init__(name, price, teacher)
        self.age = age
        self.file_name = "dance.json"

    def dict(self):
        data = self.parent_dict()
        data["age"] = self.age
        return data

    def add_to_file(self):
        return self.add(self.dict())

    def register(self, user):
        self.users.append(user)
        self.update(self.dict())
        print(f"{user} has been registered for the Dance course.")

    def cancel_register(self, user):
        if user in self.users:
            self.users.remove(user)
            self.update(self.dict())
            print(f"{user} has been removed from the Dance course.")
        else:
            print(f"{user} is not registered in the Dance course.")

    def show_users(self):
        data = self.read()
        for course in data:
            if course['name'] == self.name and course['teacher'] == self.teacher:
                self.users = course['users']
                break
        print("Registered users in Dance course:")
        for user in self.users:
            print(user)

class Music(Course):
    def __init__(self, name, price, teacher, type_of_music):
        super().__init__(name, price, teacher)
        self.type_of_music = type_of_music
        self.file_name = "music.json"

    def dict(self):
        data = self.parent_dict()
        data["type_of_music"] = self.type_of_music
        return data

    def add_to_file(self):
        return self.add(self.dict())

    def register(self, user):
        self.users.append(user)
        self.update(self.dict())
        print(f"{user} has been registered for the Music course.")

    def cancel_register(self, user):
        if user in self.users:
            self.users.remove(user)
            self.update(self.dict())
            print(f"{user} has been removed from the Music course.")
        else:
            print(f"{user} is not registered in the Music course.")

    def show_users(self):
        return self.read()

math_course = Math(name="Math 01", price=10000, teacher="Sanjarbek", time="10:00")
math_course.add_to_file()
math_course.register("Alice")
math_course.show_users()
math_course.cancel_register("Alice")
math_course.show_users()

dance_course = Dance(name="Ballet 01", price=15000, teacher="Sarvinoz", age="12+")
dance_course.add_to_file()
dance_course.register("Bob")
dance_course.show_users()

music_course = Music(name="Guitar 01", price=20000, teacher="Alisher", type_of_music="Guitar")
music_course.add_to_file()
music_course.register("Charlie")
music_course.show_users()