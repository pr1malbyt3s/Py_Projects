#!/usr/bin/env python3
# This script accepts a list of mixed type values (octal, binary, char, etc.) from an input file and prints the corresponding ascii.


import sys

# Create a list to store each item from the input file.
numList = []

# Read input file and store items to list.
with open(sys.argv[1], "r") as f:
	for line in f:
		for item in line.strip().split():			
			numList.append(item)

# data_chef function that processes and individual value and appends its ascii value to a list.
def data_chef(stuff, stufflist):
	if stuff.startswith('0x'):
		stufflist.append(chr(int(stuff,16)))
	elif stuff.startswith('0b'):
		stufflist.append(chr(int(stuff,2)))
	elif stuff.startswith('0'):
		stufflist.append(chr(int(stuff,8)))
	else:
		stufflist.append(chr(int(stuff)))

# Initiated list to use with the data_chef function.
charList = []
# Iterate through the numList and peform data_chef on each item.
for thing in (numList):
	data_chef(thing, charList)

# Print the ascii result via charList.
print(*charList, sep="")
