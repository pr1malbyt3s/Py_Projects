# Checking to see if a supplied username meets the criteria:
# 1. Is between 4 and 25 characters
# 2. Starts with a letter
# 3. Contains only letters, numbers, and the underscore character
# 4. Does not end with an underscore

def CodelandUsernameValidation(strParam: str) -> bool:
  # Check if length is between 4 and 25:
  strLen = len(strParam) in range(4,26)
  # Check if first character is letter:
  strFirst = strParam[0].isalpha()
  # Check all characters are letter, number, or underscore:
  strParsed = strParam.replace("_", "")
  strChars = strParsed.isalnum()
  # Check if last character is not underscore:
  strLast = False
  if (strParam[-1] != "_"):
    strLast = True
  # Check that all checks are true:
  checkList = [strLen, strFirst, strChars, strLast]
  return all(checkList)

# keep this function call here 
print(CodelandUsernameValidation(input()))
