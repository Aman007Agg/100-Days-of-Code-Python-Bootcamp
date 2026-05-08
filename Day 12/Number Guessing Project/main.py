from random import random, choice

from art import logo

def guess_number_game():
    print(logo)
    print("Welcome to the Number guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    attempts_remaining = 0
    choose_difficulty_level = False

    difficulty_level = input("Choose a difficulty . Type 'easy' or or 'hard': ").lower()
    while not choose_difficulty_level:
        if difficulty_level == "hard":
            attempts_remaining = 5
            choose_difficulty_level = True
        elif difficulty_level == "easy":
            attempts_remaining = 10
            choose_difficulty_level = True
        else:
            print("Invalid input, choose the correct difficulty level")
            difficulty_level = input("Choose a difficulty . Type 'easy' or or 'hard': ").lower()
            choose_difficulty_level = False

    # print(difficulty_level)
    computer_guess = choice(range(0,101))

    while attempts_remaining > 0:
        print(f"You have {attempts_remaining} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess:"))
        if user_guess == computer_guess:
            return print("You Win")

        elif user_guess > computer_guess:
            print("Too high")
            print("Guess again")
            attempts_remaining -= 1
            print(attempts_remaining)
        elif user_guess < computer_guess:
            print("Too low")
            print("Guess again")
            attempts_remaining -= 1
            print(attempts_remaining)
    print("You exceeds no of attempts. You loose.")



guess_number_game()