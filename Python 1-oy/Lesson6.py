# num = float(input("Istalgan sonni mm da kiriting: "))
# km = num // 1000000
# num = num % 1000000

# m = num // 1000
# num = num % 1000

# dm = num // 100
# num = num % 100

# sm = num // 10
# num = num % 10

# mm = num

# print(f"{km} km, {m} m, {dm} dm, {sm} sm, {mm} mm")



# import random

# words = ["rock", "paper", "scissors"]

# smball = 0
# randomball = 0

# while True:
#     sm = input("Enter your choice (rock, paper, or scissors): ").lower()
#     if sm not in words:
#         print("Invalid choice, please try again.")
#         continue
    
#     computer_choice = random.choice(words)
#     print(f"Computer choice: {computer_choice}")

#     if sm == 3:
#         print("You win!")
#     elif computer_choice == 3:
#         print("You win!")
#         break
    
#     if sm == computer_choice:
#         print("It's a tie!")
#     elif (sm == "rock" and computer_choice == "scissors") or \
#          (sm == "scissors" and computer_choice == "paper") or \
#          (sm == "paper" and computer_choice == "rock"):
#         smball += 1
#         print(smball, " : ", randomball) 
#     else:
#         randomball += 1
#         print(smball, " : ", randomball)
    
#     print(f"Score: You {smball} - Computer {randomball}")



m = int(input("m ni kiriting: "))
n = int(input("n ni kiriting: "))

for i in range(1, n):
    if i**n > m and i == n-1:
        print(n-1)
        break
else:
    print("Mavjud emas!")