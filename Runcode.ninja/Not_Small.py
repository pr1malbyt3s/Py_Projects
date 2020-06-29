#!/usr/bin/env python3

# This script accepts an input file containing mixed integer and decimal values.
# It parses all values and returns the largest value found.

import sys
from decimal import Decimal

# List that will store input values.
numList = []

# Type check function to determine if value is integer or decimal.
# After determining type, value is translated and returned.
def type_check(x):
	try:
		if isinstance(int(x), int) == True:
			return int(x)
	except ValueError:
		try:
			if isinstance(float(x), float) == True:
				return Decimal(x)
		except ValueError:
			return

# Read file contents into type_check function and perform max() on final numList.
def main():
	with open(sys.argv[1], 'r') as f:
		for line in f:
			numList.append(type_check(line))
	print(max(numList))

if __name__ == "__main__":
	main()
