#!/usr/bin/env python
#This script will read from a file that contains pairs of numbers on each line. Using the pair, it will determine the sum of all numbers in their range difference.

#Import sys module to use sys.argv.
import sys

#Intitialize list to store numbers from file.
numList = []

#Read from the file supplied to command arguments and create the list from its entries.	
file = open(sys.argv[1], "r")
for line in file:
	for num in line.split():
		numList.append(num)

#Iterate the through each pair.
for x in range(0, len(numList) - 1, 2):
	z = 0
  #Determine which number of the pair is higher and create the sum from the determined range of the pair.
	if int(numList[x+1]) > int(numList[x]):
		for y in range(int(numList[x]),int(numList[x+1])+1):
			z+=y
		print(z)
	else:
		for y in range(int(numList[x+1]),int(numList[x])+1):
			z+=y
		print(z)
