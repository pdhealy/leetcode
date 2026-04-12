from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Create a hashset to store unique elements
        hashset = set()

        # Iterate through each number in the input list
        for index, num in enumerate(nums):
            # If the number is already in the hashset, return True
            if num in hashset:
                return True
            # Otherwise, add the number to the hashset
            hashset.add(num)
        # If no duplicates were found, return False
        return False