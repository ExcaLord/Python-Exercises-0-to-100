# Guess the Number Game #

import random

difficulty_choice = input("Choose the difficulty of the game: easy, medium, or hard: ")
number1 = 1
easy_number2 = 10
medium_number2 = 50
hard_number2 = 100

if difficulty_choice == "easy":
    computer = random.randint(number1, easy_number2)
    print(
        "You have chosen the easy difficulty and you will need to "
        "guess a number between 1 and 10."
    )
elif difficulty_choice == "medium":
    computer = random.randint(number1, medium_number2)
    print(
        "You have chosen the medium difficulty and you will need to "
        "guess a number between 1 and 50."
    )
elif difficulty_choice == "hard":
    computer = random.randint(number1, hard_number2)
    print(
        "You have chosen the hard difficulty and you will need to "
        "guess a number between 1 and 100."
    )
else:
    print("Please choose a valid difficulty: easy, medium, or hard.")
    exit()

while True:
    if difficulty_choice == "easy":
        user_choice = int(input("Choose a number between 1 and 10: "))
        if user_choice == computer:
            print("You win!")
            break
        elif user_choice < computer:
            print("That's lower than the correct number.")
        elif user_choice > computer:
            print("That's higher than the correct number.")
    elif difficulty_choice == "medium":
        user_choice = int(input("Choose a number between 1 and 50: "))
        if user_choice == computer:
            print("You win!")
            break
        else:
            print("That's not correct.")
    elif difficulty_choice == "hard":
        user_choice = int(input("Choose a number between 1 and 100: "))
        if user_choice == computer:
            print("You win!")
            break
        else:
            print("That's not correct.")
    else:
        print("Invalid difficulty choice.")
        difficulty_choice = input(
            "Choose the difficulty of the game: easy, medium, or hard: "
        )
