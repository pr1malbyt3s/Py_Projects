# AOC 2021 Day 1

import sys

# This function is used to read a file input from the command line. It returns the file contents as a list of lines.
def read_file() -> list:
    if len(sys.argv) != 2:
        print("Specify puzzle input file")
        sys.exit(-1)
    else:
        # Open file at command line position 1:	
	    with open(sys.argv[1], 'r') as f:
		# Append each stripped line to a list: 		
		    input_list = [line.strip() for line in f]
	    return input_list

# Part 1: Calculate the submarine horizontal position and depth after following the planned course.
def position_finder(input_list:list) -> int:
    depth, horizontal = 0, 0
    for x in input_list:
        cmd, units = x.split()
        units = int(units)
        if(cmd == 'forward'):
            horizontal += units
        elif(cmd == 'down'):
            depth += units
        else:
            depth -= units
    return horizontal * depth

# Part 2: Calculate the submarine horizontal position and depth after accounting for aim.
def aim_finder(input_list:list) -> int:
    aim, depth, horizontal = 0, 0, 0
    for x in input_list:
        cmd, units = x.split()
        units = int(units)
        if(cmd == 'forward'):
            horizontal += units
            depth += (aim * units)
        elif(cmd == 'down'):
            aim += units
        else:
            aim -= units
    return horizontal * depth
    
def main():
    input_list = read_file()
    print(position_finder(input_list))
    print(aim_finder(input_list))

if __name__ == "__main__":
    main()
