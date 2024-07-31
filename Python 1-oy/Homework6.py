#Ex 1
result = 0

for i in range(1, 101):
    if i % 5 == 0:
        result += i
        print("Result:", i)



#x 2
name= input("Enter your name: ")

vowel_latters = "aouie"

result = ""
for latter in name:
    result += latter
    if latter in vowel_latters:
        result += '$'
print(result)



#Ex 3
a = input("Enter any two-digit number (a): ")
b = input("Enter any two-digit number (b): ")

total_a = 0
total_b = 0

for number in a:
    total_a += int(number)
    
    for number in b:
        total_b += int(number)

if total_a > total_b:
    print(f"The number with the larger sum of digits is: {a} (Sum of digits: {total_a})")
elif total_b > total_a:
    print(f"The number with the larger sum of digits is: {b} (Sum of digits: {total_b})")
else:
    print("The sum of the digits of both numbers is equal!")