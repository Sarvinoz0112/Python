# from collections import namedtuple

# red = int(input("Qizil rang uchun qiymatni kiriting (0-255): "))
# green = int(input("Yashil rang uchun qiymatni kiriting (0-255): "))
# blue = int(input("Ko'k rang uchun qiymatni kiriting (0-255): "))

# color = namedtuple('Color', ['red', 'green', 'blue'])

# if 0 <= red <= 255 and 0 <= green <= 255 and 0 <= blue <= 255:
#     user_color = color(red, green, blue)
#     print(f"Foydalanuvchi kiritgan rang: {user_color}")
# else:
#     print("Qiymatlar 0 dan 255 gacha bo'lishi kerak.")

from decimal import Decimal

expenses = []

print("Sarflaringizni kiriting (namuna: 'reason, amount'). 'reason' deb yozganda umumiy miqdor hisoblanadi va ro'yxat chiqariladi.")
while True:
    entry = input()
    if entry.lower() == 'reason':
        total_expense = sum(amount for _, amount in expenses)
        
        print("\nSarf ro'yxati:")
        for reason, amount in expenses:
            print(f"- {reason}, {amount} dollar")
        
        print(f"\nUmumiy sarf: {total_expense} dollar")
        break
    try:
        reason, amount = entry.split(', ')
        amount = Decimal(amount)
        expenses.append((reason, amount))
    except ValueError:
        print("Noto'g'ri formatda kiritildi. Iltimos, 'reason, amount' ko'rinishida kiriting.")
