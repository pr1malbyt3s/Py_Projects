# Write a function that reverses a string. The input string is given as an array of characters s.
class Solution:
    # We can use the built-in reverse function:
    def reverseString(self, s: List[str]) -> None:
        return s.reverse()

'''
# There's also a "Two pointer" method:
    def isPalindrome(self, s):
        beg, end = 0, len(s) - 1
        while beg <= end:
            while not s[beg].isalnum() and beg < end: beg += 1
            while not s[end].isalnum() and beg < end: end -= 1
            if s[beg] == s[end] or s[beg].upper() == s[end].upper():
                beg, end = beg + 1, end - 1
            else:
                return False
        return True
'''
