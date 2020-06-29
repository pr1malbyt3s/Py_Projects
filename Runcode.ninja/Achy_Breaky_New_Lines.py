#!/usr/bin/env python3

# This script accepts an input file and removes extra line breaks between lines of text.

import sys

# List that will store all lines of input file.
lineList = []

# Read input file and check if line is empty (new line).
# If not, add it to the lineList.	
with open(sys.argv[1], "r") as f:
	for line in f:
		if line.isspace() != True:
			lineList.append(line)

# Print the result via lineList.
print(*lineList, sep="")
