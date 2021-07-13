#Opening remarks
print("This app calculates your Body Mass Index (BMI)")

#Input variables
weight = float(input("Input your weight in kg but don't include the units: "))
height = float(input("Input your height in m but don't include the units: "))

#Calculate the bmi rnd round off to 1 decimal place
bmi = weight / (height * height)
bmi = round(bmi, 1)

#Print bmi
print("Your BMI is: ", bmi)
#Determine the person's status

if  bmi < 18.5:
     print("You're underweight")

elif bmi >= 18.5 and bmi <= 24.9:
     print("You're normal")

elif bmi >= 25.9 and bmi  <= 29.9:
     print("You're overweight")

else :
     print("You're obese")
    
#Closing remarks
print("Thanks")

