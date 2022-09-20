# random module imported to generate a random number
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
        if player_guess != random_number and player_guess < random_number:
            print("Sorry, guess again. Too low")
        elif player_guess != random_number and player_guess > random_number:
            print("Sorry, guess again. Too righ")
        else:
            break       
    print(f"Congrats. You have guessed the number {random_number} correctly!")

    
guessing_game()


def menu():
    while True:
        print('(1) Play guess number game')
        print('(Q) Quit')
        choice = input('Enter your choice: ').lower()
        if choice == '1':
            guessing_game()
        elif choice == 'q':
            return False
        else:
            print(f'Not a correct choice: {choice}')

            
if __name__ == '__main__':
    menu()

