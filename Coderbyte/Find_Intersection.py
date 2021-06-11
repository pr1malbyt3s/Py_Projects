# This challenge is used to read a list of strings containing ordered numbers.
# The goal is to return an ordered, comma-separated string containing the numbers found in both supplied strings.
# If none are shared, False is returned.

def FindIntersection(strArr):
  # Parse the first string from the list:
  l1 = [int(i) for i in strArr[0].split(", ")]
  # Parse the second string from the list:
  l2 = [int(i) for i in strArr[1].split(", ")]
  # Sort the intersection as numbers:
  lx = sorted(list(set(l1).intersection(l2)))
  # Recreate the list as string values:
  ls = [str(i) for i in lx]
  # Return the list as comma-separated strings if not empty:
  if (len(ls) != 0):
    return ','.join(ls)
  # Default return False:
  return False
# keep this function call here 
print(FindIntersection(input()))
