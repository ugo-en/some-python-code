# CREATE A FUNCTION TO CONVERT FROM KG TO POUNDS

# NOTE: 1 KG == 2.205 lbs
def convert():
    print("this function will help us convert kg to lbs ")
    kg = float(input("how many kg do yoou want to lbs "))
    # 1kg == 2.205lbs
    result = kg * 2.205
    print(kg, "kilograms is equal to", result, "pounds")


convert()

