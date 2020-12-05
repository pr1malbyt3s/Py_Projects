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

def seat_decode(code: str) -> int:
	row_range = [0, 127]
	col_range = [0, 7]	
	for letter in code:
		if (letter == 'F'):
			row_range[1] = math.floor(sum(row_range)/2)
		elif (letter == 'B'):
			row_range[0] = math.ceil(sum(row_range)/2)
		elif (letter == 'L'):
			col_range[1] = math.floor(sum(col_range)/2)
		elif (letter == 'R'):
			col_range[0] = math.ceil(sum(col_range)/2)
	return row_range[0] * 8 + col_range[0]

# Main function:
def main():
	# Create the input_list using the read_file function:
	input_list = read_file()
	filled_seats = set()
	for code in input_list:
		filled_seats.add(seat_decode(code))	
	for seat in filled_seats:
		if (seat + 1 not in filled_seats and seat < max(filled_seats)):
			print(seat + 1)

if __name__ == "__main__":
	main()
