#!/usr/bin/env/python

file = open("Day_1_Input.txt", "r")
freqLine = file.readline()
freqInt = int(freqLine)
freqArr = [0, freqInt]
i = 1
#print freqInt
#while freqInt != freqArr[i-1]:
    #line = file.readline()
    freqInt +=int(freqLine)
    freqArr[i] = freqInt
    ++i

print(freqInt)
