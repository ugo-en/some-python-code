# FUNCTIONS

def convert():
    print("This function will help us convert from centimeters to inches!")
    cm = float(input("How many centimeters do you want to convert to inches? "))

    # 1cm == 0.394 inches
    result = cm * 0.394
    print(cm,"centimeters is equal to",result,"inches")


convert()

