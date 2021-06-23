# WEATHER AI APP
weather = input("What is the weather? ")  # ask user for the weather
weather = weather.lower()

# start chained conditions
if weather == "rainy":
    print("It is raining! Take an umbrella!")
elif weather == "cloudy":
    print("There is a possibility of rain. You may want to carry an umbrella!")
elif weather == "sunny":
    print("It's sunny! Take your sunglasses!")
else:
    print("THe weather you entered is not valid. Please try again!")

