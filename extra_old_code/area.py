import math

closing_answer = ""
bye_msg = "Thanks for using this app. Hope you do so again soon..."
#Print opening remarks
print("Welcome to Area by Ugochukwu E. Nwachukwu")

while True:
      print("Do you want to continue? \n  Y - Yes\n   N - No")
      closing_answer = input("Input your ANSWER:  ")

      if closing_answer in ["y","yes"]:
            #Ask what modules the user wants
            print("1 - Triangle\n2 - Square\n3 - Circle")

            #Input result
            answer = int(input("Choose one of the above numbers: ")) 

            #Print User's choice
            if (answer == 1):
                  #Solve for triangle's Area
                  print("You chose TRIANGLE! ")
                  #Input the parameters
                  length = float(input("Input the lenght in cm, don't include the units:  "))
                  width = float(input("Input the width in cm, don't include the units:  "))

                  #Calculate the area of the triangle
                  area = round((length * width/2),2)

                  #Print the result
                  print("The area of Your Triangle is:", area)

            elif (answer == 2):
                  #Solve for square's Area
                  print("You chose Square!")
                  length = float(input("Input the lenght of the Square in cm, don't include the units:  "))
                  area = round((length * length),2)
                  print("The area of your Square is: ", area)

            elif (answer == 3):
                  #Solve for cicle's Area
                  print("You chose Circle!")
                  radius = float(input("Input the radius of the circle in cm, don't include the units: "))
                  area = round((radius * radius * math.pi),2)
                  #Print Answer and closing remarks
                  print("The area of the Circle is:", area)
            else:
                  print("You chose an invalid number!")
    
      else:
            print(bye_msg)
            print("Thanks!!! Goodbye!!!")
            break
