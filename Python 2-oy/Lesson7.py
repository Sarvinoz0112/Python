import os

name = input("Fayl nomini kiriting: ")

while len(name) < 5:
    if os.path.exists(name + '.txt'):
        print("Bunday fayl mavjud!")
    else:
        new_file = open(name + '.txt', 'x')
        new_file.close()
        print("Yangi fayl yaratildi!")

    if not os.path.exists(name + '.txt'):
        print("Bunday fayl mavjud emas!")
    else:
        with open(name + '.txt', 'w') as new_file:
            new_file.write("Yangi faylga yozilgan matn")
        print("Faylga yozildi!")

    name = input("Fayl nomini kiriting (kamida 5 ta belgidan iborat bo'lishi kerak): ")