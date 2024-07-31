import random

RESULTS_FILE = "results.txt"

def get_user_input(prompt):

    """Get user input and ensure it's an integer."""

    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input, please enter a number.")

def play_random_number_game():

    """Play the random number guessing game."""

    computer_guess = random.randint(1, 10)
    attempts = 3
    user_guesses = []
    
    print("The computer has guessed a number between 1 and 10. Try to guess it.")
    
    while attempts > 0:
        user_guess = get_user_input(f"Attempt {4 - attempts}/3: ")
        user_guesses.append(user_guess)
        
        if user_guess == computer_guess:
            print("Congratulations! You guessed correctly.")
            save_game_result(computer_guess, user_guesses, "User WON")
            return
        else:
            print("Incorrect. Try again.")
        
        attempts -= 1
    
    print("Your attempts are over. The computer won.")
    save_game_result(computer_guess, user_guesses, "Computer WON")

def save_game_result(computer_guess, user_guesses, result):

    """Save the game result to the results file."""

    game_number = get_total_games() + 1
    result_entry = (
        f"Game {game_number}: Computer guess {computer_guess} | "
        f"User guess {', '.join(map(str, user_guesses))} | {result}\n"
    )
    with open(RESULTS_FILE, "a") as file:
        file.write(result_entry)

def get_total_games():

    """Get the total number of games played."""

    try:
        with open(RESULTS_FILE, "r") as file:
            return len(file.readlines())
    except FileNotFoundError:
        return 0

def display_all_results():

    """Display all game results."""
     
    try:
        with open(RESULTS_FILE, "r") as file:
            results = file.readlines()
            if results:
                for result in results:
                    print(result.strip())
            else:
                print("No results found.")
    except FileNotFoundError:
        print("No results found.")

def display_winner_stats():

    """Display statistics on who won more games."""
     
    try:
        with open(RESULTS_FILE, "r") as file:
            results = file.readlines()
            user_wins = sum(1 for result in results if "User WON" in result)
            computer_wins = sum(1 for result in results if "Computer WON" in result)
            
            if user_wins > computer_wins:
                print(f"User won more games: {user_wins}")
            elif computer_wins > user_wins:
                print(f"Computer won more games: {computer_wins}")
            else:
                print(f"User and Computer won the same number of games: {user_wins}")
    except FileNotFoundError:
        print("No results found.")

def main_menu():

    """Display the main menu and handle user choices."""

    while True:
        print("\nMenu:")
        print("1: Play Random Number Game")
        print("2: Show All Results")
        print("3: Show Who Wins More")
        print("4: Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            play_random_number_game()
        elif choice == "2":
            display_all_results()
        elif choice == "3":
            display_winner_stats()
        elif choice == "4":
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()