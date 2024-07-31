start = 0
end =10
step = 1
#range(1,10,2) => [1,3,5, ..., 9]
#print(list(range(1,10,2)))
for number in range (start, end): #for number in range (start, end, 2):
    print(number) #print(number, end=" ")


word= "Salom"
for letter in word:
    print(letter)


summ=0
for number in range (1,11):
    summ+=number
print(summ)


summ = 0
for number in range(0, 11):
    if number % 2 == 0:
        summ += number
print(summ)



name = input("Ismingizni kiriting: ")
for letter in name:
    if letter == "_"or letter=="-" or letter=="*" or letter==":" or letter==";":
      print(letter)

for letter in name:
    if letter in "_-*:;":
        print(letter)


number = 0
while number <= 10:
    print(number)
    number+=1


from time import sleep
password = input("Parol kiritilsin: ")
attempts = 0
# time = 0
while password != "1111":
    attempts += 1
    if attempts == 3:
        # time +=5
        print("Noto'g'ri urinishlar soni 3taga yetdi")
        print("Ilyimos 5 sonoya kuting") #print(f"Ilyimos {time} sonoya kuting")
        sleep(5) #sleep(time)
    print("Parol hato kiritildi")
    password = input("Parol kiritilsin: ")
print("Xush kelibsiz!")