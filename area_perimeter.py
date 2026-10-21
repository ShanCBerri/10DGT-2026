# Area & Perimeter Program
# S.CB
# 21/10/26

# Width/height + number checker
'''def num_check(question):

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

# Main routine

# Width
for item in range(0, 2):
    width = num_check("Width: ")
    print(width)

# Line break
print()

# Height
for item in range(0, 2):
    height = num_check("Height: ")
    print(height)'''

# Ask user for width and height
# (assume valid data is inputted)
width = float(input("Width: "))
height = float(input("Height"))

# Calculate area/perimeter
area = width * height
perimeter = 2 * (width + height)

# Output area and perimeter
print()
print(f"Perimeter: {perimeter} units")
print(f"Area: {area} square units")
