###Guess the number
import random
def guess(x):
    random_number = random.randint(1, x)
    while True:
        my_guess = int(input(f'Guess a number between 1 an {x}: '))
        if my_guess < random_number:
            print('Guess again. You are so low!!')
        elif my_guess > random_number:
            print('Guess again. You are so high!!')
        else:
            print(f'Your guess {my_guess} is correct!!')
            break
        
guess(10)

