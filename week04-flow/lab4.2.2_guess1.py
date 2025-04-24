winner_number = 30
guessing_number = int(input("Please guess a number: "))

while guessing_number != winner_number:
    print("Please guess again: ")
    guessing_number = int(input("Please guess a number: "))
    
print("Well Done")