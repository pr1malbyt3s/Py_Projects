# Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Use regex to get only alphanumeric values and lower the case:
        p = re.sub('[^A-Za-z0-9]+','', s).lower()
        # Return the boolean comparison between the string and its reverse:
        return p == p[::-1]
