#!/usr/bin/python3

import math

# Open the file for reading and create masses list.
with open('day1.txt') as f:
    masses = (map(int, f.read().splitlines()))

# Create the fuel variable.
fuel = 0

# Iterate through list of masses. Calculate req for each. Add req to fuel.
for mass in masses:
    req = math.floor(mass/3) - 2
    fuel = fuel + req

print(f"Final Fuel: {fuel}")
