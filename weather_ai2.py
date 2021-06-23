# WEATHER AI ADVANCED

# true | false values
isCloudy = False
isClear = False
isRainy = False
isThunderstorm = False
isWindy = False
isSnowy = False

temperature = input("Enter the temperature in Celsius: ")  # accepted the temperature from the user
temperature = int(temperature)  # convert temperature

# ask the user for other weather conditions
cloudyAns = input("Is it cloudy? (Y/N) ")
rainyAns = input("Is it raining? (Y/N) ")
thunderAns = input("Is there a thunderstorm? (Y/N) ")
windyAns = input("Is it windy? (Y/N) ")
snowyAns = input("Is it snowy? (Y/N) ")

# set true or false values
if cloudyAns.upper() == "Y":
    isCloudy = True
else:
    isClear = True

if rainyAns.upper() == "Y":
    isRainy = True

if windyAns.upper() == "Y":
    isWindy = True

if thunderAns.upper() == "Y":
    isThunderstorm = True

if snowyAns.upper() == "Y":
    isSnowy = True


message = ""  # This contains the final message

# Nested condition
if temperature > 30:  # it is hot
    message = "It is hot"
    if isCloudy:
        message = message + " and it is cloudy"
    if isClear:
        message += " and it is clear"
    if isWindy:
        message += " and it is windy"
    if isRainy:
        message += " but it cannot rain at "+str(temperature)+"°C"
    if isThunderstorm:
        message += " and there is a thunderstorm"
    if isSnowy:
        message += " but it cannot snow at "+str(temperature)+"°C"

elif temperature >= 25 and temperature <= 30:
    message = "It is temperate"
    if isCloudy:
        message = message + " and it is cloudy"
    if isClear:
        message += " and it is clear"
    if isWindy:
        message += " and it is windy"
    if isRainy:
        message += " and but it is raining"
    if isThunderstorm:
        message += " and there is a thunderstorm"
    if isSnowy:
        message += " but it cannot snow at "+str(temperature)+"°C"
elif 17 <= temperature <= 25:
    message = "It is a bit cold"
    if isCloudy:
        message = message + " and it is cloudy"
    if isClear:
        message += " and it is clear"
    if isWindy:
        message += " and it is windy"
    if isRainy:
        message += " and it is raining"
    if isThunderstorm:
        message += " and there is a thunderstorm"
    if isSnowy:
        message += " but it cannot snow at "+str(temperature)+"°C"

elif 0 <= temperature <= 17:
    message = "It is cold"
    if isCloudy:
        message = message + " and it is cloudy"
    if isClear:
        message += " and it is clear"
    if isWindy:
        message += " and it is windy"
    if isRainy:
        message += " and is raining"
    if isThunderstorm:
        message += " and there is a thunderstorm"
    if isSnowy:
        message += " and it is snowing"

elif temperature <= 0:
    message = "It is freezing"
    if isCloudy:
        message = message + " and it is cloudy"
    if isClear:
        message += " and it is clear"
    if isWindy:
        message += " and it is windy"
    if isRainy:
        message += " and but it cannot rain at "+str(temperature)+"°C but if you insist that it is raining, it is probably snow or hail"
    if isThunderstorm:
        message += " and there is a thunderstorm"
    if isSnowy:
        message += " it is snowing"

print(message)  # show the message to the user
