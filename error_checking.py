# Error checkng
# S.CB
# 14 Oct 2026

# Code that tests whether a valid input was given (V1)
'''done = True # Boolean varaible set to true
while done:
    num = int(input("Please enter your value as a integer: "))
    done = False

    print(f"The number you entered is {num}.")'''

# Using a try and except method to check for valid input (V1.1)
'''# Use try and except method to catch errors
done = True
while done:
    try: # This method tries for a valid input
        num = float(input("Please enter a number: "))
        done = False

    except ValueError:
        print("That is not a valid number. Please try again \n")

print(f"The number you entered is {num}.")'''

# Check for valid input and recycling code with a function (V1.2)
# Create a function to call every time I ask the user for a number.
# A function is a chunk of code that  does something.
# Functions can be used over and over again
# To use a function (call it), write out its name with parenthesis at the end.
# To create a function, start with def

'''def input_check():
    while True:
        try: # This method tries for a valid input
            num = float(input("Please enter a number: "))
            break 
        except ValueError:
            print("That is not a valid float number. Please try again.\n")

    print(f"The number you entered is {num}.")

# Main routine
input_check() # Calls the function to be used.'''

# Valid input checker (V1.3)
# Use parameters in the the function
# More Pythonic

def input_check(question): # 'question' is a placeholder
    while True:
        error = "That is not a valid number."
        print(question)
        try:
            num = float(input())
            break
        except ValueError:
            print(error)

    return(num) # gives back the value of num so it can be used outside of the function

# Main routine
num1 = input_check("Please enter your first number:")
print(f"The number you stored is {num1}")

num2 = input_check("Please enter your seccond number:")
print(f"The second number you stored is {num2}")

sum = num1 + num2
print(f"Your numbers added together result in {sum}")