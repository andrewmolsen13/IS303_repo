# Imports random library to allow for selecting a random number
import random

# Welcome message/instructions, ask if user wants to play the computer generates the number between 1 and 100
ready = "Y"
guess_number = 0

while ready == "Y" :

    random_number = random.randint(1,100)
    guess = int(input("What is your first guess? "))
    guess_number += 1
    
    while guess != random_number :

        # Ask for a guess to what the number is
        guess = int(input("What is your next guess? "))

        guess_number += 1

        # If the guess is < 0 or > 100 print "invalid guess, please try again"
        while guess < 0 or guess > 100:
            guess = int(input("Invalid guess! Try again. "))

        if guess > random_number :
                    print("Lower! Try again! ")
        if guess < random_number :
                    print("Higher! Try again! ")

    print(f"You got it in {guess_number} tries!")

    if guess_number <= 3 :
        print("Amazing!")
    elif guess_number <= 5 :
        print("Impressive")
    elif guess_number <= 7 :
        print("Good Job")
    elif guess_number <= 9 :
        print("Took a little longer, but you got it!")        
    elif guess_number >= 10 :
        print("You need to lock in")

    ready = input("Would you like to try again?(Y/N) ").upper()
print("Have a great day!")