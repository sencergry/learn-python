import random
from words import words

lives = 10
secret_word = random.choice(words)
current_word = ''

while lives > 0:
    left = 0
    print(f'You have used these letters:{current_word}')

    for word in secret_word:
        if word in current_word:
            print(word)
        else:
            print('-')
            left += 1

    if left == 0:
        print('Cong you won!!!')
        break

    user_input = input('Guess a letter:').upper()

    if user_input in secret_word:
        current_word += user_input
    else:
        print(f'Incorrect. You have {lives} left')
        lives = lives -1
        if lives == 0:
            print('You lost!!')
            break