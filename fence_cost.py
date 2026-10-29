# Fence Cost Calculator
# S.CB
# 23/10/26

# Program that calculates the cost of fencing per meter

# Imported functions

# Wait function
from time import sleep

# Alternate print function
from rich import print # type: ignore

# Main functions

# Number checker function
def num_check(question):

    # Error message for a number less than or equal to zero
    error_message0 = "| Please enter a number that is more than zero. \n"

    # Error message for non-number
    error_message = "| Please enter a number. \n"

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
print("--------------------------------------------------------------")
print("| ☾⋆ Welcome to the official S.CB Fence Cost Calculator™! ｡⊹ |")
print("--------------------------------------------------------------\n")

sleep(1) # wait one second

# Program only keeps going if keep_going variable is empty, program will end if anything other than <enter> is typed
keep_going = ""
while keep_going == "":

    # "To begin" message
    print("----------------------------------------------")
    print("| ୨୧˚ To begin, please enter your values. ⋆｡ |")
    print("----------------------------------------------\n")

    # Get width, height, cost per meter
    width = num_check("| What is the width of your fence? ")
    height = num_check("| What is the height of your fence? ")
    cost = num_check("| What is the cost per meter of fencing? ")

    print()

    # Calculating/loading...
    print("----------------------------------------------")
    print("| ｡⊹ Thank you! Calculating values now... ☾⋆ |")
    print("|                    +-×÷                    |")
    print("----------------------------------------------\n")

    sleep(2.5) # wait 2.5 seconds for "calculation time"

    # Calculate perimeter
    perimeter = 2 * (width + height)

    # Calculate cost per meter
    price = perimeter * cost

    # Display values
    print("| Calculations complete!")
    print(f"| The perimeter equals to {perimeter} meters.")
    print(f"| The total cost per meter equal to {price:.2f} dollars.\n")

    # Ask user if they would like to perform another calculation, if <enter> go again, if other print thank you message
    keep_going = input("| Would you like to perform another calculation? Press <enter> to go again or any other key to exit. ")
    print()

# Thank you message + support message
print("| Thank you for using the official S.CB Fence Cost Calculator™! ")
print("| This is a project that relies on crowd funding. Any and all support is greatly appreciated!")
print("| Use the link [buyscbahotchocolate.com/joke] to buy me a hot chocolate.\n")

sleep(1) # wait one second

# Five star review + Credits
print("---------------------------------------------")
print("|                ★ ★ ★ ★ ★                  |")
print("|    Please leave me a five star review!    |")
print("|                  ☾ ⋆⁺｡⊹                   |")
print("| Created by S.CB. We hope you visit again! |")
print("---------------------------------------------\n")