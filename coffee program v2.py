# Creating a coffee program that a user will be able to interat with.
# Shannon Cole-Baker
# 25 Sept 2026
# Version 2

# TODO: record an input (store the answer)
#       check for valid answer (input checker)
#       ask questions and respond

# Version 1
'''# Ask user whether they like coffee or not
like_coffee = input("Do you like coffee? ")
# print(like_coffee) # checking the input is stored
print(f"Your answer was '{like_coffee}'.")

# Check the input and respond
if like_coffee == "Yes" or like_coffee == "yes" or like_coffee == "y" or like_coffee == "Y":
    print("Wonderful! Would you like to purchase some homebrewed coffee?")
else:
    print("Me too. I think coffee is awfully overrated.")'''

# Version 2
# While loop to test the program
keep_going = ""
while keep_going == "":
    # Ask user whether they like coffee or not
    like_coffee = input("Do you like coffee? ")
    # print(like_coffee) # checking the input is stored
    print(f"Your answer was '{like_coffee}'.")

    # Check the input and respond (to be fixed next time)
    if like_coffee == "Yes" or like_coffee == "yes" or like_coffee == "y" or like_coffee == "Y":
        print("Wonderful! Would you like to purchase some homebrewed coffee?")
        keep_going = "exit"
    elif like_coffee == "No" or like_coffee == "no" or like_coffee == "n" or like_coffee == "N":
        print("Me too. I think coffee is awfully overrated.")
        keep_going = "exit"
    else:
        print("Not a viable answer. Please try again.")

