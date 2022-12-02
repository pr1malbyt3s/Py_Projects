# AOC 2022 Day 1
import sys

# This function is used to read a file input from the command line.
# It parses the rations input list to create a list of lists, with each list item being the calorie count of each ration in an elf's total rations.
def parse_file() -> list:
    if len(sys.argv) != 2:
        print("Specify puzzle input file")
        sys.exit(-1)
    else:
        with open(sys.argv[1], 'r') as f:
            # First, split the list into entities separated by the blank lines ('\n\n').
            # Tnen, split those entities into separate lists, creating a list of lists.
            raw_rations = [line.split() for line in f.read().split('\n\n')]
            # Convert each item in each list to an integer for the entire list.
            rations = [[int(item) for item in ration] for ration in raw_rations]
    return rations

# Part 1: Find the elf carrying the most calories. Return the total calories.
def single_calorie_count(rations:list) -> int:
    # Find the list item (individual elf) with the max value based on each list sum.
    most_calories = sum(max(rations, key=sum))
    return most_calories

# Part 2: Find the top three elves carring the most calories. Return their total.
def top_three_calorie_count(rations:list) -> int:
    # Create a list of the elves with the top three calorie counts using sorting.
    top_three_rations = [sum(ration) for ration in sorted(rations, key=sum)[-3:]]
    # Return the summation of the new list of three elves.
    total_calories = sum(top_three_rations)
    return total_calories

def main():
    rations = parse_file()
    print("Highest calories for single elf: {}".format(single_calorie_count(rations)))
    print("Total calories for top three elves: {}".format(top_three_calorie_count(rations)))

if __name__ == "__main__":
    main()
