#!/usr/bin/env python3

# This script accepts an input file containing numbers on multiple lines.
# It adds the total numbers on a line to the total count of numbers on each line.
# Example: '3 3 3' yields 12 (3+3+3 plus 3 numbers on the line).

import sys
from decimal import Decimal

# type_check function to evaluate whether number is a integer or decimal.
def type_check(x):
	try:
		if isinstance(int(x), int) == True:
			return int(x)
	except ValueError:
		try:
			if isinstance(float(x), float) == True:
				return Decimal(x)
		except ValueError:
			return 0

# num_calc function that splits a provided line of numbers, gets the number count, and gets the sum using the type_check function.
def num_calc(s):
	split_s = s.split()
	lCount = len(split_s)
	dCount = sum(type_check(y) for y in split_s) 
	print(lCount + dCount)

def main():
	# Read file in put.
	with open(sys.argv[1], 'r') as f:
		for line in f:
			# Perform num calc for each line.
			num_calc(line.strip())

if __name__ == "__main__":
	main()
