# Area & Perimeter Program
# S.CB
# 23/10/26

# Width/height + number checker
def num_check(question):

    # Error message
    error_message = "Please enter a number more than 0.\n"

    while True:
        try:
            # Ask user for a number
            response = float(input(question))

            # Check for a number more than zero
            if response > 0:
                return response
            else:
                print(error_message)

        except ValueError:
            print(error_message)

keep_going = ""
while keep_going == "":

    # Get width and height
    width = num_check("Width: ")
    height = num_check("Height: ")

    # Calculate area/perimeter
    area = width * height
    perimeter = 2 * (width + height)

    # Display output
    print()
    print(f"Perimeter: {perimeter} units")
    print(f"Area: {area} square units")

    # Ask user if they want to keep going
    keep_going = input("Press enter to keep going or any other key to quit. ")

print("Thank you for using the area/perimeter calculator :)")