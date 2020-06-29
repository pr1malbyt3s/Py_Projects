#!/usr/bin/env python3

# This script accepts an input file containing lines of binary numbers.
# It parses each line, and prints the corresponding integer total sum.

import sys

#Read file contents.
with open(sys.argv[1], 'r') as f:
	# Iterate each line.	
	for line in f:
		x = 0
		# Add each number in the line using base2 for binary.		
		for num in line.split():
			x += int(num,2)
		print(x)
