#!/usr/bin/env python
#This script will read from a file that contains a word on each line and determine if the word on that line is a palindrome.

#Import sys module to use sys.argv.
import sys

#Intitialize a list that stores all the words read from the input file.
wordList = []

#Read from the file supplied to command arguments and create the list of words from its entries.	
file = open(sys.argv[1], "r")
for line in file:
	wordList.append(line.strip())
	
#Palindrome checker function. Will accept a string as a parameter, reverse it, and check to see if the two match.
def palindrome_check(word):
	rev_word = word[::-1]
	if rev_word == word:
		print("True")
	else:
		print("False")

#Iterate through the word list using the palindrome checker function to determine which words are and are not palindromes.
for x in range(0, len(wordList)):
	palindrome_check(wordList[x])
