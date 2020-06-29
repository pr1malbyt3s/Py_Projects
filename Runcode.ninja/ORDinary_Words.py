#!/usr/bin/env python3

# This script accepts an input file containing ascii numeric values.
# It translates each number into the corresponding ascii value and prints the decoded string.

import sys

#Read file contents.
with open(sys.argv[1], 'r') as f:
	for line in f:
		x = ''		
		for num in line.split():
			x += chr(int(num))
		print(x)
