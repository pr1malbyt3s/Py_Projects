# Given a roman numeral, convert it to an integer.
class Solution:
    def romanToInt(self, s: str) -> int:
        # Create a dict to map individual Roman letters to integers:
        roman_numerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        # Set the previous (prev) and conversion (conv) values to zero:
        prev = 0
        conv = 0
        # Iterate through the string in reverse:
        for i in reversed(range(0, len(s))):
            # Check if previous value is less than or equal to current value:
            if(prev <= roman_numerals[s[i]]):
                # If so, update the total conversion by adding the current value:
                conv += roman_numerals[s[i]]
            # If the previous value is greater than the current value:
            else:
                # Update the total conversion by subtracting the current value:
                conv -= roman_numerals[s[i]]
            # Update the previous value to the current value for the next cycle:
            prev = roman_numerals[s[i]]
        return conv
    
