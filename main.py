import random
low = 1
high = 100
guesses = 0
number = random.randint(low, high)

while True:
    guess = int(input(f'Enter a number between ({low} - {high})'))
    guesses += 1
    if guess < number:
        print(f'{guess} is low')
    elif guess < number:
        print(f'{guess} is high')

    else:
        print(f'{guess} is correct')
        break

print(f'This round took you {guesses} guesses')