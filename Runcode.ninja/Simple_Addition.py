#!/usr/bin/env python3

# This script accepts an input file of mixed value pairs separated by lines.
# It check that each value pair can be added and if so, prints the corresponding sum.

import sys
from decimal import Decimal

# Create a master list of all number pairs.
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

# Read file contents.
with open(sys.argv[1], 'r') as f:
	for line in f:		
		# Create a sublist of the number pair on each line.		
		subNumList = []
		# Perform type_check on each number pair.		
		for num in line.split():
			subNumList.append(type_check(num))
		# Ensure appended line has two values and None is not one of them.		
		if len(subNumList) == 2 and None not in subNumList:
			numList.append(subNumList)

# Print the subList pairs.
for subList in numList:
	print(subList[0] + subList[1])

