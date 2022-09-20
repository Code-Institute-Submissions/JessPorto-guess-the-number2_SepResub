import random


def guessing_game(x):
    random_number = random.randint(1, x)
    player_guess = 0
    while player_guess != random_number:
        player_guess = int(input("Guess a number between 1 an 10: "))
        if player_guess < random_number:
            print("Sorry, guess again. Too low")
        elif player_guess > random_number:
            print("Sorry, guess again. Too righ")
    print(f"Congrats. You have guessed the number {random_number} correctly!")


guessing_game(0)