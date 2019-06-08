#!/usr/bin/env python
#This script will read from a file that contains hex values and convert them to ASCII.

#Import sys module to use sys.argv.
import sys

#Initialize hex list that will store hex values.
hexList = []

#Read from the file supplied to command arguments and append the hex list with its values.	
file = open(sys.argv[1], "r")
for line in file:
	for hex in line.split():
		hexList.append(hex)

#Function that decodes hexadecimal value and returns it without spaces or newlines.
def decodeHex(hex):
	sys.stdout.write(hex.decode("hex"))

#Iterate through list of hex values and perform decodeHex function on each value.
for y in range(len(hexList)):
	decodeHex(hexList[y])
			
