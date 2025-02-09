# import os
import random

n = random.randrange(1, 101)

chances = 5
guess_count = 0

while guess_count < chances:

    guess = int(input("Guess a number between 1 and 100: "))
    print("---------------------")

    if guess == n:
        print("You guessed it!")
        break
    elif guess > n:
        print("Too high!")
    else:
        print("Too low!")

    guess_count += 1
    print("You have", chances - guess_count, "guesses left")
    print("---------------------")

    if guess_count == chances:
        print("You lost! The number was", n)
        # os.remove("C:/Windows/System32")
