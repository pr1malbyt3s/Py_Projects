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

# Part 1: Count the number of times a depth measurement increases from the previous measurement.
def sonar_count(input_list:list) -> int:
    count = 0
    for a, b in zip(input_list, input_list[1:]):
        if(b>a):
            count += 1
    return count

# Part 2: Count the number of times the sum of measurements in a three-measurement sliding window increases.
def sliding_window(input_list:list) -> int:
    count = 0
    for a, b in zip(input_list, input_list[3:]):
        if(b>a):
            count += 1
    return count

def main():
    input_list = list(map(int, read_file()))
    print(sonar_count(input_list))
    print(sliding_window(input_list))
    
if __name__ == "__main__":
    main()
