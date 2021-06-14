# The goal of this challenge was reversing a supplied string.
# This was accomplished easily using extended slice syntax: [begin:end:step]

# Function to reverse string which accepts strParam value:
def FirstReverse(strParam):
  # Return the whole string in reverse order:
  return strParam[::-1]

# keep this function call here 
print(FirstReverse(input()))
