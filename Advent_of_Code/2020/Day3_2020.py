# Advent of Code 2020 Day 3 Challenge

import sys

# This function is used to read a file input from the command line. It returns the file contents as a list of lines.
def read_file() -> list:
	# Open file at command line position 1:	
	with open(sys.argv[1], 'r') as f:
		# Append each stripped line to a list: 		
		input_list = [line.strip() for line in f]
	return input_list

# This function is used to count the trees in a trajected path based on the map and slope.
# It accepts a list, representing, a lateral movement, x, and up/down movement, y.
# It returns the number of trees encountered in the trajected path.
def traject(tree_map: list, x: int, y: int) -> int:
	# Initialize the x, y, and tree_count variables:	
	current_x = current_y = tree_count = 0
	# Iterate until the bottom of the map (last line) is reached:
	while (current_y != len(tree_map) - 1):	
		# Set the x position (index in the current string) to update using modulus. This allows iterating through the list without exceeding the bounds:
		current_x = (current_x + x) % len(tree_map[y])
		# Update the y position:		
		current_y += y
		# Check if the current map position has a tree and update the count if so:
		if (tree_map[current_y][current_x] == '#'):
			tree_count += 1
	return tree_count

# Main function:
def main():
	# Create the input_list using the read_file function:
	input_list = read_file()
	# Part 2 path slope designations:
	paths = ((1,1),(3,1),(5,1),(7,1),(1,2))
	# Test each path's trajectory and count the trees:	
	for path in paths:
		print(traject(input_list, path[0], path[1]))

if __name__ == "__main__":
	main()
