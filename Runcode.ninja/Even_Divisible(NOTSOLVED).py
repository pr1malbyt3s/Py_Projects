#!/usr/bin/env python
#This script will read from a file that contains pairs of numbers on each line. Using the pair, it will determine all the numbers between 1 and the larger number(inclusive) that are divisible by the first number.

#Import sys module to use sys.argv.
import sys

#Intitialize two lists, one lower number and one for higher number.
firstList = []
secondList = []

#Read from the file supplied to command arguments and create the two lists from its entries.	
file = open(sys.argv[1], "r")
for line in file:
	numCount = 0
	for num in line.split():
		numCount += 1
		if numCount % 2 == 0:
			secondList.append(num)
		else:
			firstList.append(num)

#Iterate the through the range of numbers for each pair and return the numbers that are divisible in the range.
for x in range(len(firstList) - 1):
	for y in range(1, int(secondList[x]) + 1):
		if y % int(firstList[x]) == 0:
			print(y)
	print("")
	
#Used to print the output from the last two numbers in each list to avoid a final space.
for z in range(1, int(secondList[len(firstList) - 1])):
	if z % int(firstList[len(firstList) - 1]) == 0:
		print(z)
			
