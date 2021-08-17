# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

from bisect import bisect

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Check if target exists in list:
        if (target in nums):
            # Return the target index:
            return nums.index(target)
        else:
            # Otherwise, perform a bisect (binary search) to find position:
            return bisect(nums, target)
          
'''
# One-liner using bisec_left:
from bisect import bisect

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
            return bisect_left(nums, target)
'''
