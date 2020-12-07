# Advent of Code 2020 Day 5 Challenge

import sys
import math

# This function is used to read a file input from the command line. It returns the file contents as a list of lines.
def read_file() -> list:
	# Open file at command line position 1:	
	with open(sys.argv[1], 'r') as f:
		# Append each stripped line to a list: 		
		input_list = [line.strip() for line in f]
	return input_list

# This function is used to decode each seat code into its corresponding seat ID.
def seat_decode(code: str) -> int:
	# Set a range for the rows, 0-127:
	row_range = [0, 127]
	# Set a range for the columns, 0-7:
	col_range = [0, 7]
	# Iterate over the letters in the code:
	for letter in code:
		# F means lower half. Row range is updated to the current range lower half:
		if (letter == 'F'):
			row_range[1] = math.floor(sum(row_range)/2)
		# B means upper half. Row range is updated to the current range upper half:
		elif (letter == 'B'):
			row_range[0] = math.ceil(sum(row_range)/2)
		# L means lower half. Column range is updated to the current range lower half:
		elif (letter == 'L'):
			col_range[1] = math.floor(sum(col_range)/2)
		# R means upper half. Column range is updated to the current range upper half:
		elif (letter == 'R'):
			col_range[0] = math.ceil(sum(col_range)/2)
	# Return seat ID - rows times 8 plus column number:
	return row_range[0] * 8 + col_range[0]

# Main function:
def main():
	# Create the input_list using the read_file function:
	input_list = read_file()
	# Create an empty set which will store filled seats:
	filled_seats = set()
	# Iterate over each code in the list:
	for code in input_list:
		# Add the seat ID to filled_seats:
		filled_seats.add(seat_decode(code))	
	# Iterate over the filled seats:
	for seat in filled_seats:
		# Check if any seat IDs below the max don't have a filled seat next to them. This is your seat:
		if (seat + 1 not in filled_seats and seat < max(filled_seats)):
			print(seat + 1)

if __name__ == "__main__":
	main()
