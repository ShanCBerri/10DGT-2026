# Error checkng
# S.CB
# 14 Oct 2026

# Code that tests whether a valid input was given (v1)
'''done = True # Boolean varaible set to true
while done:
    num = int(input("Please enter your value as a integer: "))
    done = False

    print(f"The number you entered is {num}.")'''

# Using a try and except method to check for valid input (V1.1)
# Use try and except method to catch errors
done = True
while done:
    try: # This method tries for a valid input
        num = float(input("Please enter a number: "))
        done = False

    except ValueError:
        print("That is not a valid number. Please try again \n")

print(f"The number you entered is {num}.")
