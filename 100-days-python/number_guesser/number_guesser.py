import art
import random

continue_playing = True

print(art.logo)
print("Welcome to the Number Guessing Game!")

def start_game():
    global continue_playing

    difficulty = input("Choose a difficulty (attempts), Type 'easy' (10), 'hard' (5), or 'quit' (0): ").lower()
    attempts = difficulty_logic(difficulty)
    while continue_playing:
        print("I'm thinking of a number between 1 and 100.")
        number_guesser(attempts)

def difficulty_logic(difficulty):
    """Returns the number of attempts based on what difficulty is chosen"""
    global continue_playing

    if difficulty == "easy":
        return 10
    elif difficulty == "hard":
        return 5
    elif difficulty == "quit":
        continue_playing = False
    else:
        print("Invalid input.")

def number_guesser(attempts):
    random_number = number_generator()
    game_logic(random_number, attempts)

def game_logic(random_number, attempts):
    """Takes in a user input of a number, which it then compares to the random number and tells them to guess again if it's not correct."""
    guess = int(input("Guess a number: "))

    attempts -= 1

    if guess == random_number:
        print(f"You got it! The answer was {random_number}")
        start_game()
    elif guess > random_number:
        if attempts > 0:
            print(f"Too high.\nGuess again. {attempts} attempts remaining.")
            game_logic(random_number, attempts)
        else:
            end_game(random_number)
    elif guess < random_number:
        if attempts > 0:
            print(f"Too low.\nGuess again. {attempts} attempts remaining")
            game_logic(random_number, attempts)
        else:
            end_game(random_number)

def end_game(random_number):
    """Prints they ran out of guesses and informs them of the correct answer.  Restarts the game."""
    print(f"You've run out of guesses.  The number was {random_number}.")
    start_game()

def number_generator():
    """Returns a random whole number between 1 and 100"""
    generated_number = random.randint(1, 100)
    return generated_number

start_game()
