# n = []

# for _ in range(1, 11):
#     name = input("Ismingizi kiritin:")
#     n.append(name)

# print(name)



# n = [1, 2, 2.2, 3.3, 5, 10]
# int_n = []
# float_n = []

# for i in n:
#     if type(n) is int:
#         int_n.append(n)
#     else:
#         float_n.append(n)
# print(int_n, float_n)



# # Initializing the board and players
# board = [
#     ['_', '_', '_'],
#     ['_', '_', '_'],
#     ['_', '_', '_']
# ]
# player_a = "x"
# player_b = "o"

# # Display the board
# def display_board():
#     for row in board:
#         print(" ".join(row))
#     print()

# # Main game loop
# attempt = 1
# while attempt <= 9:
#     display_board()
#     if attempt % 2 == 1:
#         player = player_a
#         print("Player A's turn (x)")
#     else:
#         player = player_b
#         print("Player B's turn (o)")

#     user_input = int(input("Enter a number (1-9): "))

#     # Convert user input to board coordinates
#     if user_input == 1:
#         row, col = 0, 0
#     elif user_input == 2:
#         row, col = 0, 1
#     elif user_input == 3:
#         row, col = 0, 2
#     elif user_input == 4:
#         row, col = 1, 0
#     elif user_input == 5:
#         row, col = 1, 1
#     elif user_input == 6:
#         row, col = 1, 2
#     elif user_input == 7:
#         row, col = 2, 0
#     elif user_input == 8:
#         row, col = 2, 1
#     elif user_input == 9:
#         row, col = 2, 2
#     else:
#         print("Invalid input, please enter a number between 1 and 9.")
#         continue

#     if board[row][col] == '_':
#         board[row][col] = player
#     else:
#         print("That position is already taken. Try again.")
#         continue

#     # Check for a win
#     win = False
#     # Check rows
#     for r in range(3):
#         if board[r][0] == board[r][1] == board[r][2] == player:
#             win = True
#     # Check columns
#     for c in range(3):
#         if board[0][c] == board[1][c] == board[2][c] == player:
#             win = True
#     # Check diagonals
#     if board[0][0] == board[1][1] == board[2][2] == player:
#         win = True
#     if board[0][2] == board[1][1] == board[2][0] == player:
#         win = True

#     if win:
#         display_board()
#         print(f"Player {player} wins!")
#         break

#     attempt += 1
# else:
#     display_board()
#     print("It's a draw!")



board = [' ' for _ in range(9)]

print("Добро пожаловать в игру Крестики-Нолики!")
print("Индексы клеток от 0 до 8:")
print(" 0 | 1 | 2 ")
print("---+---+---")
print(" 3 | 4 | 5 ")
print("---+---+---")
print(" 6 | 7 | 8 ")
print()

current_player = 'X'
game_over = False
move_count = 0

while not game_over:

    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

    print(f"Ход игрока {current_player}")
    
    move = int(input("Введите индекс клетки (0-8): "))
    
    if board[move] == ' ':
        board[move] = current_player
        move_count += 1
    else:
        print("Клетка занята! Попробуйте снова.")
        continue
    
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # горизонтальные линии
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # вертикальные линии
        [0, 4, 8], [2, 4, 6]              # диагональные линии
    ]
    
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
            print(f" {board[0]} | {board[1]} | {board[2]} ")
            print("---+---+---")
            print(f" {board[3]} | {board[4]} | {board[5]} ")
            print("---+---+---")
            print(f" {board[6]} | {board[7]} | {board[8]} ")
            print(f"Игрок {current_player} победил!")
            game_over = True
            break
    
    if move_count == 9 and not game_over:
        print(f" {board[0]} | {board[1]} | {board[2]} ")
        print("---+---+---")
        print(f" {board[3]} | {board[4]} | {board[5]} ")
        print("---+---+---")
        print(f" {board[6]} | {board[7]} | {board[8]} ")
        print("Ничья!")
        game_over = True
    
    current_player = 'O' if current_player == 'X' else 'X'

print("Игра окончена!")