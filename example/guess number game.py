from random import randrange
secret_number = randrange(10)
guess_count = 0
guess_limit = 3
did_guess = False
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        did_guess = True
        break
    if guess_count == guess_limit and  not did_guess:
        print(f'You lost the secret number was {secret_number} !!!')

