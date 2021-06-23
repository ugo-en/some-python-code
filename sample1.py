# data types

# integers
number1 = 1
number2 = 2
total = number1 + number2

print(number1)
print(number2)
print(total)

# float (decimals)
float1 = 5.6
float2 = 6.78
total2 = float1 + float2
print("This is a floating number: ",float1)
print("This is another floating number: ",float2)
print("This is a floating number",total2)

print("This is the sum of a floating number and an integer: ",3.126731186386791 + 2)



# string (text)
name = "Emmanuella"
state = 'Lagos'
multiline_text = '''
    This is a multi-line text.
    It allows us write text in multiple lines.
'''
print("Name: ",name)
print("State: ", state)
print("Multi-line text: ", multiline_text)


# boolean
print(True,False)

age = 2
bool1 = age > 18
print("Is age above 18? ",bool1)



# list
names = ["Sarah","Emmanuella","Ugochukwu"]
list2 = ["String 1",1,9.23232,True]
names.append("John")
print(names)
print(list2)
print(list2[0])

# set
set1 = {1,2,3,4}
# print(set1[0])

# tuples
tup = (1,2,3)
# tup.append(4)
print(tup)


# dictionary
students = {
    1: "John",
    2: "Emmanuella",
    3: "Alexa",
    "biology": "Lucas",
    "physics": ["Debra","Louis","Max"],

}

print(students["physics"])

print(1=="1")
