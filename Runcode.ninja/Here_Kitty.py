#!/usr/bin/env python
#Script that prints out data directly received from a file.

#Import sys module to use sys.argv.
import sys

#Create a file variable that opens a file passed as an argument.
file = open(sys.argv[1], "r")
#Iterate over each line in the file and print it.
for line in file:
	print line,
