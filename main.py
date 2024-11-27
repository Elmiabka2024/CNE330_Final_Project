# number guessing game
import random
# a user has to guess a number between 1 and 100
low = 1
high = 100
guesses = 0
number = random.randint(low, high) # generate a random number using random module, range between low or high variable

# loops
while True:
    guess = int(input(f'Enter a number between ({low} - {high}): ')) # hint for the user input
    guesses += 1 # guess incrementation by one
    if guess < number:
        print(f'{guess} is low') # if the guess is lower than the number
    elif guess < number:
        print(f'{guess} is high') # if guess is higher than the number

    else:
        print(f'{guess} is correct') # if guess is equal the number
        break # escape the while loop

print(f'This round took you {guesses} guesses!')  #  the number it took to guess the right number
