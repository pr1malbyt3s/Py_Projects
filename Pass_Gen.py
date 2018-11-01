#!/usr/bin/python

import random
import string

#Assign desired number of digits, letters, and special characters.
numbers_count = input("Enter number of desired digits in password.")
letters_count = input("Enter number of desired letters in password.")
special_count = input("Enter number of desired special characters in password.")

numbers = (random.choice(string.digits)) for x in range(numbers_count)
letters = random.choice(string.letters) for x in range(letters_count)
special = random.choice(string.punctuation) for x in range(special_count)

password = numbers + letters + special

print ''.join(random.choice(password))
