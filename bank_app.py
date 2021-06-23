# This is a simple bank application!

# Define our variables
name = "Emmanuella"
password = "1234"
amount = 1000000.00
max_tries = 5
tries = 0

# loop
while max_tries > tries:
    
    # accept input
    user_pass = input("Enter your password: ")

    if user_pass == password:
        print("Welcome",name,"!")
        print("You have $",amount)
        break
    else:
        print("Invalid password! Please try again later!")
        tries += 1
        remaining_tries = max_tries - tries 
        print("You have",remaining_tries,"tries left.")

