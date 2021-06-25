# SPECIAL NUMBER GAME
number = 7  # created the variable
guess = input("Guess the special number: ")  # accepted input
guess = int(guess)  # convert it to an integer

if number == guess:  # compare them
    print("You have guessed the correct number!")
else:
    print("Incorrect number!")

