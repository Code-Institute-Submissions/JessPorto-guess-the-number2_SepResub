import random


def guessing_game():
    random_number = random.randint(1, 10)  
    while True:
        text = input('Guess a number from 1 to 10: ')        
        try:
            player_guess = int(text)
            if player_guess < 1 or player_guess > 10:
                raise ValueError             
        except ValueError:
            print('{} is not valid.'.format(text))
            continue        
       
        
guessing_game()

