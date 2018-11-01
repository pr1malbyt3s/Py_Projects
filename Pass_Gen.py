#!/usr/bin/python

import random
import string

#Input validation function that enforces user to supply integer values between 0 and 10 for counts.
def input_validate(prompt):
  while True:
    try:
      value = int(input(prompt))
    except ValueError:
      print("Input could not be interpreted. Try again.")
      continue
    if value < 0 or value > 10:
      print("Supplied number must be between 0 and 10.")
      continue
    else:
      break
  return value

#Assign desired number of digits, letters, and special characters.
numbers_count = input_validate("Enter number of desired digits in password: ")
letters_count = input_validate("Enter number of desired letters in password: ")
special_count = input_validate("Enter number of desired special characters in password: ")

#Generate randomly assigned, desired length lists of numbers, letters, and special characters.
numbers = ''.join((random.choice(string.digits)) for i in range(numbers_count))
letters = ''.join((random.choice(string.letters)) for i in range(letters_count))
special = ''.join((random.choice(string.punctuation)) for i in range(special_count))

#Combine randomly generated lists into a single entity and assign password length variable.
numbers_to_string = ''
for i in range(numbers_count):
	numbers_to_string +=numbers[i]
password = numbers_to_string + letters + special
password_length = numbers_count + letters_count + special_count
password_as_list = list(password)
random.shuffle(password_as_list)

#Print generated password to STDOUT.
print ("Your generated password is: ")
print ''.join(password_as_list)
#for i in range(password_length))
#for i in range(numbers_count):
#	print numbers[i]
#print(numbers_to_string)
#print(type(numbers))
#print(letters)
#print(type(letters))
#print(special)
#print(type(special))
