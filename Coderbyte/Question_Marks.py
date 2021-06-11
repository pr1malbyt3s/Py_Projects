# This function accepts a string of numbers, letters, and question marks.
# The goal is to check if there are exactly 3 question marks between every 2 numbers that add up to 10.
# If so, it returns True. Otherwise, it returns False.

def QuestionsMarks(strParam:str) -> bool:
  # Initiate list for number indices in string:
  index_list = []
  # Initiate list for checks on question mark counts:
  check_list = []
  # Iterate through provided string:
  for index, i in enumerate(strParam):
    # Check if the value is numeric:
    if(i.isnumeric()):
      # If so, append its index to the index_list:
      index_list.append(index)
  # Iterate through the index list:
  for i in range(len(index_list) - 1):
    # Check if the two numbers in the string add up to 10:
    if(int(strParam[index_list[i]]) + int(strParam[index_list[i+1]]) == 10):
      # If so, check if there are 3 or more question marks between them, appending the result to check_list:
      check_list.append(strParam[index_list[i]:index_list[i+1]].count('?') == 3)
  # Ensure check_list isn't empty:
  if(len(check_list) != 0):
    # Check value of all boolean elements in check_list:
    return all(check_list)
  # Return False by default:
  return False

# keep this function call here 
print(QuestionsMarks(input()))
