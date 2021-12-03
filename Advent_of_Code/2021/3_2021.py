# AOC 2021 Day 3

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
def power_consumption(input_list:list) -> int:
    diag_total_length = len(input_list)
    diag_length = len(input_list[0])
    gamma, epsilon = '', ''
    for i in range(0, diag_length):
        zero_count = 0
        one_count = diag_total_length
        for j in range(0, diag_total_length):
            if(int(input_list[j][i]) == 0):
                zero_count += 1
                one_count -= 1
        if(zero_count > one_count):
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'
    return int(gamma, 2) * int(epsilon, 2)

# Part 2: Calculate the submarine horizontal position and depth after accounting for aim.
def life_support(input_list:list) -> int:
    def bit_criteria(sub_list:list, gas:str) -> list:
        i = 0
        while(len(sub_list) != 1):
            sl = len(sub_list)
            zero_count = 0
            for j in range(0, sl):
                if(int(sub_list[j][i]) == 0):
                    zero_count += 1
            if(zero_count > (sl/2)):
                if(gas == 'o2'):
                    sub_list = [x for x in sub_list if int(x[i]) == 0]
                else:
                    sub_list = [x for x in sub_list if int(x[i]) == 1]
            else:
                if(gas == 'o2'):
                    sub_list = [x for x in sub_list if int(x[i]) == 1]
                else:
                    sub_list = [x for x in sub_list if int(x[i]) == 0]
            i += 1
        return sub_list
    oxy_gen = ''.join(bit_criteria(input_list, 'o2'))
    co2_scrub = ''.join(bit_criteria(input_list , 'co2'))
    return int(oxy_gen, 2) * int(co2_scrub, 2)

def main():
    input_list = read_file()
    #print(power_consumption(input_list))
    o = life_support(input_list)
    print(o)


if __name__ == "__main__":
    main()

'''
I was looking to do something like this but couldn't visualize it (courtesy hugh_tc on Reddit)
def p1(codes):
    length = len(codes[0])

    gamma = ""
    for i in range(length):
        column = "".join(code[i] for code in codes)
        if column.count("0") > column.count("1"):
            gamma += "0"
        else:
            gamma += "1"

    gamma = int(gamma, 2)
    eps = gamma ^ (pow(2, length) - 1)

    return gamma * eps

def p2(codes):
    length = len(codes[0])

    oxygen = set(codes)
    for i in range(length):
        column = "".join(code[i] for code in oxygen)
        if column.count("0") <= column.count("1"):
            bit = "1"
        else:
            bit = "0"

        oxygen = oxygen - set(code for code in oxygen if code[i] == bit)
        if len(oxygen) == 1:
            oxygen = int(max(oxygen), 2)
            break

    co2 = set(codes)
    for i in range(length):
        column = "".join(code[i] for code in co2)
        if column.count("0") > column.count("1"):
            bit = "1"
        else:
            bit = "0"

        co2 = co2 - set(code for code in co2 if code[i] == bit)
        if len(co2) == 1:
            co2 = int(max(co2), 2)
            break

    return oxygen * co2
'''
