from random import randint
roll_again = ""
while  (roll_again.lower() != "e"):
     roll_again = input("Ready to roll?  ENTER = Roll ; E = Exit")
     if (roll_again.lower() != "e"):
          num_rolled = randint(1, 6)
          num_rolled2 = randint(1,6)
          print("You rolled a ", num_rolled, " and a ",num_rolled2)
          Total = num_rolled + num_rolled2
          print("That's a total of ",Total)
     else:
          pass              
print("Thanks for playing!!!")
