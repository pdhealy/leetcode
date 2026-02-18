# 1: Two Sum

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         # Dictionary to store previously seen numbers and their indices
         prev_seen_map: dict[int, int] = {} # val : index

         for index, num in enumerate(nums):
            # Calculate the complement
            diff = target - num

            # Check if the complement exists in the dictionary
            if diff in prev_seen_map:
                # If found, return the indices
                return [prev_seen_map[diff], index]
            # Store the current number and its index in the dictionary
            prev_seen_map[num] = index
         # If no solution is found, return an empty list
         return []