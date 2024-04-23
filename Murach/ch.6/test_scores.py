#!/usr/bin/env python3

def display_welcome():
	print("The Test Scores program")
	print("Enter 'x' to exit")
	print("")

def get_scores():
	scores = []
	while True:
		score = input("Enter test score: ")
		if score == "x":
			return scores
		else:
			score = int(score)
			if score >= 0 and score <= 100:
				scores.append(score)
			else:
				print("Test score must be from 0 through 100. " + "Score discarded. Try again.")

def process_scores(scores):
	total = 0
	for item in scores:
		total += item

	# calculate average score
	average =round(total / len(scores))
	median = len(scores) // 2

	# format and display the result
	print()
	print("Total:                ", total)
	print("Number of Scores:     ", len(scores))
	print("Average Score:        ", average)
	print("Low Score:            ", min(scores))
	print("High Score:           ", max(scores))
	print("Median score:         ", scores[median])

def main():
	display_welcome()
	score_total = get_scores()
	process_scores(score_total)
	print("")
	print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
	main()

