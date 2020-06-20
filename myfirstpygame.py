#GuessingGame

import random

print("Welcome to the Guessing Game \nWhat is your name? ")
name = input()

print("Hi %s, Happy to have you here %s, Are you ready to play, %s ? \n%s, Please press YES OR NO " %(name,name,name,name))


ready = input()

if ready == "YES":
    print("Yaaay %s, Now pick a random number between 1 and 6" %(name))
    number = (input)
    roll = random.randint(1,6)

    number = int(input())

    if number == roll:
        print("You guessed right")

    elif number < roll:
        print("Your guess is too low")

    elif number > roll:
        print("Your guess is too high") 

else:
    exit()




