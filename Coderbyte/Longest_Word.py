# The purpose of this challenge was to identify the largest word in a supplied sentence.
# Words could contain numbers but not special characters.
# It was assumed the supplied sentence would not be empty.

# Import the regex library:
import re

def LongestWord(sen):
  # Set the regex pattern for anything not a letter or number:
  regex = re.compile('[^a-zA-Z0-9]+')
  # Create the list of parsed words from the sentence:
  parsed = [re.sub(regex, "", i) for i in sen.split()]
  # Find the largest word in the parsed list using the length as the key:
  return max(parsed, key=len)

# keep this function call here 
print(LongestWord(input()))

# After reviewing solutions, I discovered re has its own split function.
# This could have been accomplished a little simpler using:
'''
regex = re.compile(r'\W+')
parsed = pattern.split(sen)
'''
