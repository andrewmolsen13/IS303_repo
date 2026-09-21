# Imports random library to allow for selecting a random number
import random

# Welcome message/instructions, ask if user wants to play the computer generates the number between 1 and 100
ready = input("Welcome to the number guessing game!" \
"\nI am going to think of a number between 1-100 and you have to guess it!" \
"\nReady? (Y/N) ").upper()

while ready == "Y" :

    guess_number = 0 #tracks number of guesses

    random_number = random.randint(1,100)

    # Ask for a guess to what the number is
    guess = int(input("What is your first guess? "))



    # If the guess is < 0 or > 100 print "invalid guess, please try again"
    while guess < 0 or guess > 100:
        guess = int(input("Invalid guess! Try again. "))

    

    if guess != random_number :
        while guess != random_number :
            if guess > random_number :
                guess = int(input("Lower! Try again! "))
            if guess < random_number :
                guess = int(input("Higher! Try again! "))
            guess_number += 1

    guess_number += 1

    print(f"You got it in {guess_number} tries!")

    if guess_number <= 3 :
        print("Amazing!")
    elif guess_number <= 5 :
        print("Great Work")
    elif guess_number <= 9 :
        print("Good Job")
    elif guess_number > 10 :
        print("Nice try")

    ready = input("Would you like to try again?(Y/N) ").upper()
print("Have a great day!")