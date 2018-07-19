# Using random to create simple computer guessing game
# July 5, 2018
# CTI-110 P5HW2 - Random Number Guessing Game
# Ava Moore

# use random module
import random

# set minimum and maximum values (1-100)
MIN = 1
MAX = 100

def main():
    #variable to control loop
    again = 'y'

    #until the user is finished, repeat
    while again == 'y' or again == 'Y':
        guess = int(input("Guess what the secret number is: "))

        number = random.randint(1,100)
        #print("The number is",number)
        if guess < number:
            print("Too low, try again.")
        elif guess > number:
            print("Too high, try again.")
        else:
            print("Congratulations! You guess correctly!")
    

        again = input("Play again? (y for yes): ")



main()
