#!/usr/bin/env python3

import sys
from decimal import Decimal

def type_check(x):
	try:
		if isinstance(int(x), int) == True:
			return int(x)
	except ValueError:
		try:
			if isinstance(float(x), float) == True:
				return Decimal(x)
		except ValueError:
			return 0

def evenly_divisible(x, y):
	a = type_check(x)
	b = type_check(y)
	for i in range(1, b+1):
		if i % a == 0:
			print(i)

def main():
	first = []
	second = []
	with open(sys.argv[1], 'r') as f:
		for line in f:
			first.append(line.split()[0])
			second.append(line.split()[1])
	z = len(first)	
	for j in range(z-1):
		evenly_divisible(first[j], second[j])
		print()
	evenly_divisible(first[z-1], second[z-1])

if __name__ == "__main__":
	main()
