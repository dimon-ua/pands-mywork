import random

number_to_guess = int(random.randint(0,100))

guess = int(input("Please guess the number:"))
while guess != number_to_guess:
    if guess < number_to_guess:
        print("too low")
        guess = int(input("Please guess again:"))
    else: 
        print("too high")
        guess = int(input("Please guess again:"))
print("Well done! Yes the number was ", number_to_guess)