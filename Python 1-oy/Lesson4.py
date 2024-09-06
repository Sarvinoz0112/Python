num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# while num2 <= num1:
#     num1 += 1
#     print(num1)
for num in range(num1, num2):
    print(num)



i = 0
while i < 10:
    i += 1
    if i == 5:
        continue  #pass => bo'shlig'ni to'ldirish
    print(i)



text = "Salom Men Menman"
text = text.lower()
#text = text.upper()
#text = text.title()
#text = text.capitalize()

print(text)



#counter = text.count("a")
index = text.find("a")
# index1 = text.index("a")

print(index)
# print(index, index1)



print(text.isalnum)


a = 0
i = 0
o = 0
u = 0
e = 0
text = input("Text: ")
while text is None:
    text = input("Text: ").strip().lower
else:
    for char in text:
        if char in "a":
            a += 1
        elif char in "i":
            i += 1
        elif char in "o":
            o += 1
        elif char in "u":
            u += 1
        elif char in "e":
            e += 1
            
print("a:", a)
print("i:", i)
print("o:", o)
print("u:", u)
print("e:", e)



num = int(input("Enter number: "))
summa = 0  # Summa o'zgaruvchisini e'lon qilingan va qiymati 0 ga tenglangan.
while num < 1:
    num = int(input("Num: "))
for number in range(1, num+1):
    summa += number ** 2  # Har bir raqamning kvadratini qo'shib borish.
print(summa)



from datetime import datetime
year = datetime.now().year
diff = year - 1826

summa = 24
for _ in range(diff):
    summa += summa * 0.06
    print(summa)




import random

num = random.randint(1, 100)
attempts = 0
while True:
    number = int(input("Bir son kiriting: "))  # Berilgan sonni so'rab yozilgan.
    attempts += 1
    if attempts == 7:
        print("Noto'g'ri urinishlar soni 7taga yetdi")
        break   
    if num < number:
        print("Kichigroq son o'yla!")
    elif num == number:
        print("To'g'ri!")
        break  # To'g'ri topilsa tsiklni to'xtatamiz.
    else:
        print("Kattaroq son o'yla!")