import os
import random

win_count = 0
lose_count = 0
tie_count = 0

choices = ["rock", "paper", "scissors"]

while True:
    computer_choice = random.choice(choices)
    user_choice = input(
        "Enter your choice (rock, paper, or scissors): "
    ).lower()

    if user_choice not in choices:
        print("Invalid choice.")
        continue

    print("You chose:", user_choice)
    print("The computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!")
        tie_count += 1
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "scissors" and computer_choice == "paper")
        or (user_choice == "paper" and computer_choice == "rock")
    ):
        print("You win!")
        win_count += 1
    else:
        print("You lose!")
        lose_count += 1

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != "y":
        break
    else:
        os.system("cls")

print("Game statistics:")
print("Wins:", win_count)
print("Losses:", lose_count)
print("Ties:", tie_count)
