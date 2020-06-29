#!/usr/bin/env python3

# This script is used to decode a special 'cipher'.
# The cipher pattern is each first word in a new sentence.

import sys

# Create a list to store each parsed first word from an input file.
message = []
with open(sys.argv[1], 'r') as f:
	cipher = f.read()

# While reading file, split the file by the '.' character, appending each first word (index 0) to the message list.
cipherSplit = cipher.split(". ")
for i in range(len(cipherSplit)):
	message.append(cipherSplit[i].split()[0])

# Print the message via the message list.
print(*message, sep = " ")
