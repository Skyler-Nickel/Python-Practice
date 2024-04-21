#!/usr/bin/env python3

def get_float(prompt, low_validity, high_validity):
	while True:
		amount = float(input(prompt))
		if amount <= low_validity or amount > high_validity:
			print("Please enter a value greater than ", str(low_validity), " and less than ", str(high_validity), ". Try again.")
		else:
			break

	return amount

def get_int(prompt, low_validity, high_validity):
	while True:
		amount = int(input(prompt))
		if amount < low_validity or amount > high_validity:
			print("Please enter a value greater than ", str(low_validity), " and less than ", str(high_validity), ". Try again.")
		else:
			break

	return amount

def main():
	choice = "y"
	while choice.lower() == "y":
		# see if the user wants to continue
		choice = input("Continue? (y/n): ")
		print()

	print("Bye!")

if __name__ == "__main__":
	main()

