# Creating a coffee program that a user will be able to interat with.
# Shannon Cole-Baker
# 23 Sept 2026
# Version 1

# TODO: record an input (store the answer)
#       check for valid answer (input checker)
#       ask questions and respond

# Ask user whether they like coffee or not
like_coffee = input("Do you like coffee? ")
# print(like_coffee) # checking the input is stored
print(f"Your answer was '{like_coffee}'.")

# Check the input and respond (to be fixed next time)
if like_coffee == "Yes" or "yes" or "y" or "Y":
    print("Wonderful! Would you like to purchase some homebrewed coffee?")
else:
    print("Me too. I think coffee is awfully overrated.")