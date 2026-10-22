# Area & Perimeter Calculator
# S.CB
# 21/10/26

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