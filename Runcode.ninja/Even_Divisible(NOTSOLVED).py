#!/usr/bin/env python
#This script will read from a file that contains pairs of numbers on each line. Using the pair, it will determine all the numbers between 1 and the larger number(inclusive) that are divisible by the first number.

#Import sys module to use sys.argv.
import sys

#Intitialize two lists, one lower number and one for higher number.
numList = []

#Read from the file supplied to command arguments and create the two lists from its entries.	
file = open(sys.argv[1], "r")
for line in file:
	for num in line.split():
		numList.append(num)

#Iterate the through the range of numbers for each pair and return the numbers that are divisible in the range.
for x in range(0, len(numList) - 3, 2):
	for y in range(int(numList[x]),int(numList[x+1])+1):
		if y % int(numList[x]) == 0:
			print(y)
	print("")
	
#Used to print the output from the last two numbers in each list to avoid a final space.
for z in range(int(numList[len(numList)-2]),int(numList[len(numList)-1])):
	if z % int(numList[len(numList)-2]) == 0:
		print(z)
			
