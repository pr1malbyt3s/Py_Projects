#!/usr/bin/env python
#This script will read from a file that contains pairs of numbers on each line. Using the pair, it will determine all the numbers between 1 and the larger number(inclusive) that are divisible by the first number.

#Import sys module to use sys.argv.
import sys, binascii

#Intitialize two lists, one lower number and one for higher number.
numList = []

#Read from the file supplied to command arguments and create the two lists from its entries.	
file = open(sys.argv[1], "r")
for line in file:
	for num in line.split():
		numList.append(num)
print numList

def data_chef(stuff):
	if stuff.startswith('0x'):
		#print(stuff[:2].decode("hex"))
		print(stuff)
	elif stuff.startswith('0b'):
		sys.stdout.write(binascii.b2a_uu(stuff))

for thing in numList:
	data_chef(thing)
