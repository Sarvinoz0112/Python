#Ex 1 #TAKRORLASH
num = 1
for number in range(-80, 81):
    if number % 7 == 0 and number % 2 != 0:  #bu yerda toq sonlar va 7 ga karrali sonlarni tekshirishganman
        num *= number

print(f"Toqlarining ko'paytmasi {num} ga teng")



#Ex 2
num = 0
for number in range(4, 101):
    if number % 4 == 0:  #bu yerda 4 ga karrali sonlarni tekshirishganman
        num += number

print(f"4 ga karrali va 100 dan kichik butun musbat sonlarning yig'indisi {num} ga teng")



# #Ex 3
counter = 0
for a in range(10):
    for b in range(10):
        for c in range(10):
            if a + b + c == 13:
                counter +1




#Ex 4
n = int(input("Sinfda nechita o'quvchi borligini kiriting: "))

all_height = 0
for i in range(n):
    sum_of_height = 0
    height = float(input(f"{i+1}-o'quvchi bo'yi (metrda): ")) # i+1 o'quvchining tartibi raqamini ko'rsatadi, yani har bita o'quvchi soniga 1 qo'shib ketaveradi
    sum_of_height += height
    all_height += sum_of_height / n

average_height = all_height
print("O'rtacha bo'yi:", average_height, "metr")

# n = (input("son: "))

# for i in range (2, n):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i)


#Ex 5
def given_n_prime_number(n): 
    prime_number = []
    for i in range(2, n+1):
        if all(i % j != 0 for j in range(2, int(i**0.5)+1)):
            prime_number.append(i)
    return prime_number

n = int(input("Son kiriting: "))
print(f"Berilgan {n} sonigacha bo'lgan tub sonlar:")
print(given_n_prime_number(n))