#!/usr/bin/env python3

# This script accepts an input file containing numbers separated by lines.
# It determines if each number is even or odd, and prints the corresponding True or False beside the number.

import sys

# Function to determine if number is even or odd and print corresponding value.
def odd_or_even(x):
	if x%2 == 0:
		print("{} True".format(x))
	else:
		print("{} False".format(x))

#Read file contents.
def main():
	with open(sys.argv[1], 'r') as f:
		for line in f:
			odd_or_even(int(line))

if __name__ == "__main__":
	main()
