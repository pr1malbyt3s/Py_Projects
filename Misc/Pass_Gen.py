#!/usr/bin/python3

import random
import string

#Input validation function that enforces user to supply integer values between 0 and 10 for counts.
def input_validate(prompt):
	while True:
		try:
			value = int(input(prompt))
			if 0 < value < 11:
				return value
			else:
				print("Supplied number must be between 0 and 10.")
		except ValueError:
	      		print("Input could not be interpreted. Try again.")

#Assign desired number of digits, letters, and special characters.
numbers_count = input_validate("Enter number of desired digits in password: ")
letters_count = input_validate("Enter number of desired letters in password: ")
special_count = input_validate("Enter number of desired special characters in password: ")

#Generate randomly assigned, desired length password of numbers, letters, and special characters.
password = []
for i in range(numbers_count): password.append(random.choice(string.digits))
for i in range(letters_count): password.append(random.choice(string.ascii_letters))
for i in range(special_count): password.append(random.choice(string.punctuation))
random.shuffle(password)

#Print generated password.
print ("Your generated password is: ")
print (*password,sep='')
