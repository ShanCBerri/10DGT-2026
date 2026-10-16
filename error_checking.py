# Error checkng
# S.CB
# 16 Oct 2026

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

'''def input_check(question): # 'question' is a placeholder
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
print(f"Your numbers added together result in {sum}")'''

# V1.4 Checking for a valid input using try/except method
# Using parameters (placeholders) to help make the code more pythonic
# Function that asks user to enter a number from a range.
def valid_num(question, low, high):
    error = f"Whoops, that is not an integer between {low} and {high}"
    while True:
        try:
            response = int(input(question))
            # if the response is >= to the low nr (number) or <= high nr, continue
            if low <= response <= high:
                break # Stop the loop

            else:
                print(f"{error}\n")

        except ValueError:
            print (error)
    return response # This makes the response available to be used outside the function

# Main routine
if __name__ =="__main__":

    num1 = valid_num("Enter a number between 1 and 10: ",1,10)
    print(f"The number you entered is {num1}.\n")

    num2 = valid_num("Enter a number between 15 and 20:",15,20)
    print(f"The number you entered is {num2}.\n")
    
    num3 = valid_num("Enter a number between 20 and 30:",20,30)
    print(f"The number you entered is {num3}.\n")

    # Multiply the result of num1, num2, and num3
    multiply = num1 * num2 * num3
    print(f"Your three numbers multiplied together result in {multiply}.")

    # Adding the numbers
    sum = num1 + num2 + num3
    print(f"Your numbers added together result in {sum}.")