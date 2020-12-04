# Advent of Code 2020 Day 4 Challenge

import sys

# This function is used to read a file input from the command line. It returns the batch file contents as a list of lines separated by batch.
def read_file() -> list:
	# Open file at command line position 1:
	with open(sys.argv[1], 'r') as f:
		# Read the file:		
		lines = f.read()
		# Split the lines based on two sequential new-line characters, then replace remaining new-line characters with spaces:
		input_list = [line.replace('\n',' ') for line in lines.split('\n\n')]
	return input_list

# Function to check birth year is between 1920 and 2002.
def byr_check(year: str) -> bool:
	return 1920 <= int(year) <= 2002

# Function to check issue year is between 2010 and 2020.
def iyr_check(year: str) -> bool:
	return 2010 <= int(year) <= 2020

# Function to check expiration year is between 2020 and 2030.
def eyr_check(year: str) -> bool:
	return 2020 <= int(year) <= 2030

# Function to check for valid height.
def hgt_check(height: str) -> bool:
	# Parse the numbers from the input string:
	hgt = int(''.join(filter(lambda i: i.isdigit(), height)))	
	# Check if height is inches and within range:	
	if (height.endswith('in')):
		return 59 <= hgt <= 76
	# Check if height is centimeters and within range:	
	elif (height.endswith('cm')):
		return hgt >= 150 <= hgt <= 193
	# If no measurement given return false:	
	return False

# Variable to define acceptable hair code numbers:
good_hair = 'abcdef0123456789'
# Function to check for valid hair code.
def hcl_check(hair: str) -> bool:
	# Check if hair code is 7 characters and starts with #:
	if (len(hair) == 7 and hair[0] == '#'):
		# Return boolean for all remaining numbers in good_hair:
		return all([h in good_hair for h in hair[1:]])

# Variable to define acceptable eye colors:
good_eyes = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
# Function to check for valid eye color.
def ecl_check(eye: str) -> bool:
	return eye in good_eyes

# Function to check for valid passport ID.
def pid_check(num: str) -> bool:
	# Ensure there are 9 numbers and all are numeric:
	return len(num) == 9 and num.isnumeric()

# Dictionary to map passport fields to relevant function names:
func_map = {'byr': byr_check, 'iyr': iyr_check, 'eyr': eyr_check, 'hgt': hgt_check, 'hcl': hcl_check, 'ecl': ecl_check, 'pid': pid_check}
# Function to check that passport field passes respective check.
def field_check(batch_fields: list) -> bool:
	# Create an empty boolean list:	
	fields = []
	# Remove all 'cid' fields from batch:
	batch_fields = [field for field in batch_fields if 'cid' not in field]
	# Parse each item as the field, [0], and its value [1],	
	for item in batch_fields:
		key = item.split(':')[0]
		val = item.split(':')[1]
		# Append the output of the respective check function for each field to the fields list:
		fields.append(func_map[key](val))		
	# Return the boolean for all checked fields:	
	return all(fields)

# Variable to define required passport fields:		
req_fields = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
# Function to check each passport in the passport list.
def passport_check(batch_list: list) -> int:
	# Initialize valid passport count:	
	valid = 0
	# Iterate over each batch (passport) in the list:
	for batch in batch_list:
		# Check that all fields required fields are present:		
		if (all(fields in batch for fields in req_fields)): # Use only this line for part 1.
			# Call the field check function for each passport:
			if (field_check(batch.split())): # Subsuqent line added for part 2.			
				# Increase valid count if all checks passed:				
				valid += 1
	return valid

def main():
	# Create the passport batch list:
	batch_list = read_file()
	# Run the passport checks for the batch list:
	count = passport_check(batch_list)
	# Print the result:
	print(count)
	
if __name__ == "__main__":
	main()
