#!/usr/bin/env python3

# display a welcome message
print("The Area and Perimeter program")
print()

# get input from the user
length = float(input("Please enter the length: "))
width = float(input("Please enter the width:  "))

# calculate area and width
area = round(length * width)
perimeter = round(2 * length + 2 * width)

# format and display the result
print()
print(f"Area = {area}" + f"\nPerimeter = {perimeter}")
print()
print("Thanks for using this program!")

