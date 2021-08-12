# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # We can use the python Counter object to create a dict of values:value_counts:
        c = Counter(nums)
        # Iterate through keys and values:
        for k,v in c.items():
            # Find where the value_count is 1:
            if (v == 1):
                # Return that key:
                return k
              
'''
# Another method is to use an XOR operation:
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Set a beginning operation value to zero:
        r = 0
        # Iterate through the nums list:
        for num in nums:
            # Perform XOR between current r and each num:
            r ^= num
        # Return the final result, which will be our unique value:    
        return r
'''
