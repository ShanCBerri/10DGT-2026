# Area & Perimeter Program
# S.CB
# 23/10/26

# Width/height + number checker
def num_check(question):

    # Error message for numbers less than 0
    error_message0 = "Please enter a number more than 0.\n"

    # Error message for non-numbers
    error_message = "Please enter a number. \n"
    

    while True:
        try:
            # Ask user for a number
            response = float(input(question))

            # Check for a number more than zero
            if response > 0:
                return response
            else:
                print(error_message0)

        except ValueError:
            print(error_message)

keep_going = ""
while keep_going == "":

    # Get width and height
    width = num_check("What is your width? ")
    height = num_check("What is your height? ")

    # Get units
    units = input("What units should the area/perimeter be displayed as? ")

    # Calculate area/perimeter
    area = width * height
    perimeter = 2 * (width + height)

    # Display output
    print()
    print(f"Your perimeter is {perimeter} {units}.")
    print(f"Your area is {area} {units} squared.")

    # Ask user if they want to keep going
    keep_going = input("Press enter to keep going or any other key to quit. ")
    print()

print("Thank you for using the area/perimeter calculator :)\n")