#!/usr/bin/env python
#This script will read from a file, determine the highest 'group of ten' range, and return a count for each 'group of ten' range up to the highest.

#Import sys module to use sys.argv.
import sys

#Intitialize two lists, one used for counting and one used to store file contents.
countList = []
fileList = []

#Define function that will compare values in different 'tens groups' and add count to countList.
def tens_counter(low, high, y, x):
	if low <= x < high:
		countList[y] += 1

#Read from the file supplied to command arguments and create a list of its entries.	
file = open(sys.argv[1], "r")
for line in file:
  number = int(line)
  fileList.append(number)

#Determine the max number in the fileList list, check if its divisible by ten.
#If not divisible by ten, add one until it is.
maxNum = max(fileList)
while maxNum % 10 != 0:
  maxNum += 1

#Determine the number of 'groups of ten'.
maxNumDiv = maxNum / 10

#Create the counter list using the number of 'groups of ten'.
for x in range(maxNumDiv):
  countList.append(0)

#Iterate through the number of 'groups of ten' and perform the counting function for reach group.
for y in range(len(countList)):
	for item in fileList:
		tens_counter(y*10, (y*10)+10, y, item)

#Print the counts of each group.
for num in countList:
	str_num = str(num)
	sys.stdout.write(str_num)
