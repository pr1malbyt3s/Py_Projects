#!/usr/bin/env python
#Prints every argument passed to script on same line, not including the script name itself.

#Import sys module to use sys.argv
import sys

#For loop that iterates over the sys.argv list, starting with every argument past the script name.
for arg in sys.argv[1:]:
	#Prints each argument on the same line.
	print(arg),
