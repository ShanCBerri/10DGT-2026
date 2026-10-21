# Area & Perimeter Program
# S.CB
# 21/10/26

# Error message
error_message = "Please enter a number.\n"

while True:
    try:
        # Ask user for width
        width = float(input("Width: "))

        # Check for a number more than zero
        if width > 0:
            break
        else:
            print(error_message)

    except ValueError:
        print(error_message)