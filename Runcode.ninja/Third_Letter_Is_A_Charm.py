#!/usr/bin/env python3

# This script accepts an input file containing words with misplaced letters.
# Conveniently, the misplaced letter is always from the third position in the word and is at the beginning.

import sys

# rotate function to perform letter rotation on a provided string.
# It first checks to ensure the string is at least three letters long.
# If not, it inserts the first letter of the provided word into the third (i[2]) spot.
def rotate(s):
	if(len(s) < 3):
		return s
	c = s[0]
	#print(c)
	a = s[1:3]
	#print(a)
	b = s[3::]
	#print(b)
	f = a + c + b
	return f

def main():
	# Read file input.
	with open(sys.argv[1], 'r') as f:
		for line in f:
			# List that will be used for each line.
			inputList = []
			# Append each word to the list, rotate it, and print all words once done.
			for word in line.split():				
				inputList.append(rotate(word))
			print(*inputList)
	f.close()
					
if __name__ == "__main__":
	main()
