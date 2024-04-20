#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon program")
print()

next_entry = "y"
while next_entry.lower() == "y":
	# get input from the user
	miles_driven = float(input("Enter miles driven:         "))
	gallons_used = float(input("Enter gallons of gas used:  "))
	gallons_cost = float(input("Enter the cost per gallon:  "))
	print()

	if miles_driven <= 0:
		print("Miles driven must be greater than zero. Please try again.")
	elif gallons_used <= 0:
		print("Gallons used must be greater than zero. Please try again.")
	elif gallons_cost <= 0:
		print("Cost must be greater than zero. Please try again.")
	else:
		# calculate and display miles per gallon
		mpg = round(miles_driven / gallons_used, 2)
		total_cost = round(gallons_cost * gallons_used, 2)
		cost_mile = round(gallons_cost /mpg, 1)
		print("Miles Per Gallon:       ", mpg)
		print("Total Gas Cost:         ", total_cost)
		print("Cost Per Mile:          ", cost_mile)
		print()
	
	next_entry = input("Get entries for another trip (y/n)? ")

print()
print("Bye!")
