num = float(input("Enter any number in seconds: "))

day = num // 86400
num = num % 86400

hour = num // 3600
num = num % 3600

minut = num // 60
num = num % 60

sec = num // 1
num = num % 1

print(f"{day} day, {hour} hour, {minut} minut, {sec} sec")