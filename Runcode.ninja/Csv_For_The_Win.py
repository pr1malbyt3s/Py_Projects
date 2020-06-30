#!/usr/bin/env python3

# This script takes a csv input file and sums all the numbers on each line, printing the result.

import sys
import csv
from decimal import Decimal

# Type_check function to determine if a supplied number is an integer or decimal.
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

def main():
	# Reading file input with the help of csv reader.
	with open(sys.argv[1], 'r') as f:
		readcsv = csv.reader(f, delimiter=',')
		# Read each row and generate the sum using type_check for mixed values.		
		for row in readcsv:
			sum = 0		
			for i in range(len(row)):		
				sum += type_check(row[i])
			print(sum)

if __name__ == "__main__":
	main()
