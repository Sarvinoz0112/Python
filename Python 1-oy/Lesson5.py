#Ex 1
import random

num = random.randint(100, 999)
attempts = 5
while True:
    number = int(input("Uch xonali son kiriting: "))
    attempts += 1
    if attempts == 5:
        print("Noto'g'ri urinishlar soni 5taga yetdi")
        break
    first = number[0]
    second = number[1]
    third = number[2]



number = int(input("Uch xonali son kiriting: "))
i = number // 2 # teng yarimiga bo'lish

while i > 0: #user son kiritsin va osha user kiritgan sonlarni bo'luvchilarini teskari tartibda yozbersin
    if num % i == 0:
        print(i)
        i -= 1



num = input("num: ")
digits = ""
for i in num:
    if i not in digits:
        digits += 1
        print