# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
class Solution:
    # We use a function which accepts a list of integers, a target integer value, and returns a list of integers:  
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create an empty dict to represent a hash map:
        hash_dict = {}
        # Enumerate the nums list:
        for index, i in enumerate(nums):
            # Create a temp number to store difference between target and current list value:
            temp = target - i
            # If the temp value is already in our hash map, then we've found our solution pairing:
            if (temp in hash_dict):
                # Return the solution pairing once found:
                return hash_dict[temp], index
            # Add each new discovered index value to the hash map keyed by its number value in the list:
            hash_dict[i] = index
