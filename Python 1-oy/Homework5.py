#Ex 1
num = input("Istalgan sonni kiriting: ")
digits = []

for digit in num:
    if digit in digits:
        digits[digit] += 1
    else:
        digits[digit] = 1

for digit, times in digits.items():
    print(f"{digit} soni {times} marta takrorlangan")




#Ex 2
num = int(input("Istalgan sonni mm da kiriting: "))

km = num // 1000000

m = num // 1000

dm = num // 100

sm = num // 10

mm = num // 1

print(f"Metr: {m}")
print(f"Destimetr: {dm}")
print(f"Santimetr: {sm}")
print(f"Milimetr: {mm}")



#Ex 3
result = []
for num in range(1, 1001):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count == 5:
        result.append(num)

print(result)




#Ex 4
for i in range(2, 10):
    for j in range(1, 11):
        a = i * j
        print(i, "*", j, "=", a )



#Ex 5
palindromes = [num for num in range(1, 101) if str(num) == str(num)[::-1]]

print(f"100 dan kichik palindrom sonlar: {palindromes}")