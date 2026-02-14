# 1: Two Sum

## Difficulty: Easy
## Category: Array, Hash Table
## Link: https://leetcode.com/problems/two-sum/
## Tutorial: https://www.youtube.com/watch?v=KLlXCFG5TnA

## Solution:

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

## Test cases:

if __name__ == "__main__":

    solution = Solution()

    # Example 1:
    # nums = [2, 7, 11, 15]
    # target = 9

    # Example 2:
    nums = [3, 2, 4]
    target = 6
    
    result = solution.twoSum(nums, target)
    print(f"Indices of the two numbers that add up to {target} are: {result}")

## Summary: For the current number ('num'), we calculate the complement ('diff') that we need to find in order to reach the target. We check if this complement exists in our dictionary of previously seen numbers. If it does, we return the indices of the complement and the current number. If it doesn't, we add the current number and its index to the dictionary for future reference.