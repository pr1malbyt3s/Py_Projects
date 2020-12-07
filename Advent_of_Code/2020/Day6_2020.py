# Advent of Code 2020 Day 6 Challenge

import sys
import collections

# This function is used to read a file input from the command line. It returns the batch file contents as a list of lines separated by batch.
def read_file() -> list:
	# Open file at command line position 1:
	with open(sys.argv[1], 'r') as f:
		# Read the file:		
		lines = f.read()
		# Split the lines based on two sequential new-line characters, then replace remaining new-line characters with spaces:
		input_list = [line.replace('\n',' ') for line in lines.split('\n\n')]
	return input_list

# Solution to part 1.
# This function is used to identify the total count of unique questions answered on the customs form.
def form_parse_1(answers: str) -> int:
	# Initialize a question count variable:	
	question_count = 0
	# Assign a Counter object which identifies character counts in the answers string:
	count = collections.Counter(answers.replace(' ',''))
	# Update the question count based on the amount of characters identified by the Counter:	
	question_count += len(count)
	return question_count

# Solution to part 2.
# This function is used to identify the total count of unique questions answered by every member in each group.
def form_parse_2(answers: str) -> int:
	'''	
	# Alternative solution:
	# Initialize an empty list:
	s = []
	# Split the answers string and append each individuals answers to s:
	for x in answers.split():
		s.append(x)
	# Use set intersection to find characters shared between each list item converted into a set:	
	d = set.intersection(*map(set,s))
	# Return the length of the set intersection items:
	return len(d)
	'''
	# Initialize a question count variable:
	question_count = 0
	# Count the total number of members in each group:
	group_total = len(answers.split())
	# Assign a Counter object which identifies charater counts in the answers string:	
	count = collections.Counter(answers.replace(' ',''))
	# Iterate over each item returned by the Counter:
	for _, question in count.items():
		# Check if the letter count is equal to the groups member count:
		if question == group_total:
			# If so, update the question_count:
			question_count += 1
	return question_count	
	
def main():
	# Create the customs form question answers list:
	customs_answers = read_file()
	# Set a total count variable:	
	total_count = 0
	# Iterate over the sets of answers in our customs_answers list:
	for answers in customs_answers:
		# Update the total_count with the form_parse return:
		total_count += form_parse_2(answers)
	# Print the total count:	
	print(total_count)
	
if __name__ == "__main__":
	main()
