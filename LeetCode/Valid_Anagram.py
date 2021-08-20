# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Use Counter to check if the letter keys and count values match for each string, returning the boolean:
        return Counter(s) == Counter(t)
