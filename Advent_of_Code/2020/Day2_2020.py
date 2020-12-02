# Advent of Code 2020 Day 2 Challenge

import sys
import re

# This function is used to check if a given password meets the old challenge policy.
# It checks if a character, c, is in a given password, pw, between provided least, l, and most, m, counts.
def policy_process_old(l, m, c, pw):
	# Count the amount of times c is in pw:	
	count = pw.count(c)
	# If count is between l and m, return true:
	if l <= count and count <= m:
		return True
	return False

# This function is used to check if a given password meets the new challenge policy.
# It checks if a character, c, is in a given password, pw, at specific indices.
# The organization does not follow zero-index, so it's important to adjust.
def policy_process_new(l, m, c, pw):
	# If the provided character is at one of the possible indexes, but not the other, return true:
	if (pw[l-1] == c and pw[m-1] != c) or (pw[l-1] !=c and pw[m-1] == c):
		return True
	return False

# This function is used to process a line, with the example format "2-4 d: xxdfvp".
# It separates the numbers, given character, and string.
def line_process(s):
	# Identify digits using regex:
	find_nums = re.findall(r'\d+', s)
	# Create a list of found digits:
	nums = list(map(int, find_nums))
	# Parse the character:
	char = s.split()[1].replace(":","")
	# Parse the password string:	
	pw = s.split()[2]
	# Return a list containing the list of 2 numbers, the character to check, and the password string:
	return [nums, char, pw]

def main():
	# Create input array:
	input_list = []
	# Read file input and append each line to a list:
	with open(sys.argv[1], 'r') as f:
		for line in f:
			input_list.append(line.strip())
	f.close()
	# Set an initial counter for valid passwords:
	valid = 0
	# Iterate over each input_list line, performing line processing and password policy checks, adding to count if policy met:
	for item in input_list:
		if (policy_process_new(line_process(item)[0][0], line_process(item)[0][1], line_process(item)[1], line_process(item)[2])):
			valid += 1
	# Print total valid password count:	
	print(valid)
	

if __name__ == "__main__":
	main()
