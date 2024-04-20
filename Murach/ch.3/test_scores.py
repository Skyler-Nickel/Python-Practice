#!/usr/bin/env python3

# display a welcome message
print("The Test Scores program")
print()

# initialize variables
counter = 0
score_total = 0
next_entry = "y"

while next_entry.lower() == "y":
	test_score = 0
	print("Enter test scores")
	print("Enter 'end' to end input")
	print("=======================")
	while test_score != 'end':
		test_score = input("Enter test score: ")
		if test_score == 'end':
			break
		elif int(test_score) >= 0 and int(test_score) <= 100:
			score_total += int(test_score)
			counter += 1
		else:
			print(f"Test score must be from 0 through 100. "
				f"Score discarded. Try again.")

	# calculate average score
	average_score = round(score_total / counter)

	# format and display the result
	print("======================")
	print(f"Total Score: {score_total}"
		f"\nAverage Score: {average_score}")
	print()
	next_entry = input("Enter another set of test scores (y/n)? ")
	print()
print("Bye!")
