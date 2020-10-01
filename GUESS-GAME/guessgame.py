import random

random_num = random.randint(1,10)

guess = None
while guess != random_num:
    guess = input("Pick a number from 1 to 10: ")
    guess = int(guess)
    if guess > random_num:
        print("TOO HIGH!")
    elif guess < random_num:
        print("TOO LOW!")
    else:
        print("YOU WON")
        play_again = input("Do you want to play again? (y/n) ")
        if play_again == "y":
            random_num = random.randint(1,10)
            guess = None
        else:
            print("Thank you for playing!")

