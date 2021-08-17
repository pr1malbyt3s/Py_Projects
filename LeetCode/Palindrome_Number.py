# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Convert provided integer to string:
        xx = str(x)
        # Check if string is same forwards and backwards, returning boolean:
        return xx == xx[::-1]
