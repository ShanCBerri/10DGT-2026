# Fence Cost Calculator
# S.CB
# 30/10/26

# Program that calculates the cost of fencing per meter

# Imported functions

# Wait function
from time import sleep

# Rich (adds colours)
from rich import print

# Main functions

# Number checker function
def num_check(question):

    # Error message for a number less than or equal to zero
    error_message0 = "[#FFFFFF]| Please enter a number that is more than zero. \n"

    # Error message for non-number
    error_message = "[#FFFFFF]| Please enter a number. \n"

    while True:
        try:
            # Ask user for a number
            response = float(input(question))
            
            # Check for a number more than zero
            if response > 0:
                    return response
            else: 
                print(error_message0) # Print the 0 error message if the number is not greater than zero
            
        except ValueError:
            print(error_message) # Print the error message if a number is not entered

# Main routine

# Welcome to the program
print()
print("[#FFFFFF]--------------------------------------------------------------")
print("[#FFFFFF]| ☾⋆ Welcome to the official S.CB Fence Cost Calculator™! ｡⊹ |")
print("[#FFFFFF]--------------------------------------------------------------\n")

sleep(1) # wait one second

# Program only keeps going if keep_going variable is empty, program will end if anything other than <enter> is typed
keep_going = ""
while keep_going == "":

    # "To begin" message
    print("[#FFFFFF]----------------------------------------------")
    print("[#FFFFFF]| ୨୧˚ To begin, please enter your values. ⋆｡ |")
    print("[#FFFFFF]----------------------------------------------\n")

    # Get width, height, cost per meter
    width = num_check("[#FFFFFF]| What is the width of your fence? ")
    height = num_check("[#FFFFFF]| What is the height of your fence? ")
    cost = num_check("[#FFFFFF]| What is the cost per meter of fencing? ")

    print()

    # Calculating/loading...
    print("[#FFFFFF]----------------------------------------------")
    print("[#FFFFFF]| ｡⊹ Thank you! Calculating values now... ☾⋆ |")
    print("[#FFFFFF]|                    +-×÷                    |")
    print("[#FFFFFF]----------------------------------------------\n")

    sleep(2.5) # wait 2.5 seconds for "calculation time"

    # Calculate perimeter
    perimeter = 2 * (width + height)

    # Calculate cost per meter
    price = perimeter * cost

    # Display values
    print("[#FFFFFF]| Calculations complete!")
    print(f"[#FFFFFF]| The perimeter equals to {perimeter} meters.")
    print(f"[#FFFFFF]| The total cost per meter equal to {price:.2f} dollars.\n")

    # Ask user if they would like to perform another calculation, if <enter> go again, if other print thank you message
    keep_going = input("| Would you like to perform another calculation? Press <enter> to go again or any other key to exit. ")
    print()

# Thank you message + support message
print("[#FFFFFF]| Thank you for using the official S.CB Fence Cost Calculator™! ")
print("[#FFFFFF]| This is a project that relies on crowd funding. Any and all support is greatly appreciated!")
print("[#FFFFFF]| Use the link [buyscbahotchocolate.com/joke] to buy me a hot chocolate.\n")

sleep(1) # wait one second

# Five star review + Credits
print("[#FFFFFF]---------------------------------------------")
print("[#FFFFFF]|                [wheat1]★ ★ ★ ★ ★[/wheat1]                  |")
print("[#FFFFFF]|    Please leave me a five star review!    |")
print("[#FFFFFF]|                  ☾ ⋆⁺｡⊹                   |")
print("[#FFFFFF]| Created by S.CB. We hope you visit again! |")
print("[#FFFFFF]---------------------------------------------\n")