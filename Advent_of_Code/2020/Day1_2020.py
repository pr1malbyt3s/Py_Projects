# Advent of Code 2020 Day 1 Challenge

import sys

# This function is used to find two numbers in a list which add to a given sum using a hash map.
# Reference: https://www.geeksforgeeks.org/given-an-array-a-and-a-number-x-check-for-pair-in-a-with-sum-as-x/
def sum_search_2(sum_list, sum_val):
	# Create an empty hash set:
	s = set()
	# Iterate over the list, adding each value to the hash map:
	for i in range(0, len(sum_list)):
		# Find the difference between the desired sum value and the current i-th position value in the list:			
		temp = sum_val - sum_list[i]
		# If the difference (temp) is in the hash map, these are the two solution values. Print them:		
		if (temp in s):
			print("Solution is: ({},{})".format(sum_list[i], temp))
		# Add each newly seen value to the hash map:		
		s.add(sum_list[i])

# This function is used to find three numbers in a list which add to a given sum using hash map.
# Reference: https://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/
def sum_search_3(sum_list, sum_val):
	# Iterate over the list, recursively:
	for i in range(0, len(sum_list) - 1):
		# Create an empty hash set:
		s = set()
		# Find the difference between the desired sum value and the current i-th position value in the list:
		temp = sum_val - sum_list[i]
		# Second iteration, adding each value to the hash map:
		for j in range(i + 1, len(sum_list)):
			# If the current difference (temp) minus the current j-th position value in the list is in the hash map, solution is found. Print it:
			if (temp - sum_list[j]) in s:
				print("Solution is: ({},{},{})".format(sum_list[i], sum_list[j], temp-sum_list[j]))
			# Add each newly seen value to the hash map:			
			s.add(sum_list[j])

def main():
	# Create input array:
	input_list = []
	# Read file input and apend each line to a list:
	with open(sys.argv[1], 'r') as f:
		for line in f:
			input_list.append(int(line.strip()))
	f.close()
	# Execute defined functions:
	sum_search_2(input_list, 2020)
	sum_search_3(input_list, 2020)

if __name__ == "__main__":
	main() 
