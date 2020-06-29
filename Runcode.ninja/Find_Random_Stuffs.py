#!/usr/bin/env python3

#This script will read an input file that contains a pair of numbers on each line.
#It will identify all numbers between the two divisible by 7 but that are not multiples of 5 (inclusive).
#It will then print all such numbers in a comma-separated sequence on a single line.

import sys

#Create a master list of all number pairs.
numList = []

#Read file contents.
with open(sys.argv[1], 'r') as f:
	for line in f:
		#Create a sublist of the number pair on each line.		
		subNumList = []
		for num in line.split():
			subNumList.append(int(num))
		#Add the sub number list to master list.		
		numList.append(subNumList)

#Function to perform the divisibility checks and print valid numbers.
def frs(n1, n2):
	frs_list = []
	for i in range(n1, n2+1):
		if i%7==0 and i%5!=0:
			frs_list.append(i)
	print(*frs_list, sep=",")

#Runt the master pair list through our frs function.
for j in range(len(numList)):
	frs(numList[j][0], numList[j][1])
