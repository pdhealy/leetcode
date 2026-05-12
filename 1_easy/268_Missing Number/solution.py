# 268. Missing Number

from typing import List

class Solution:

    # Solution 1: Using the formula for the sum of the first n natural numbers and subtracting the sum of the given numbers
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)

        for i in range(len(nums)):
            result += (i - nums[i])

        return result

    # # Solution 2: Using a set to track seen numbers
    # def missingNumber(self, nums: List[int]) -> int:
    #     seen = set(nums)
    #     n = len(nums)
    #     for i in range(n + 1):
    #         if i not in seen:
    #             return i

    # # Solution 3: Using Gauss's formula to calculate the expected sum and subtracting the actual sum
    # def missingNumber(self, nums: List[int]) -> int:
    #     n = len(nums)

    #     expected_sum = n * (n + 1) // 2  # Sum of all integers from 0 to n using Gauss's formula
    #     actual_sum = sum(nums)

    #     return expected_sum - actual_sum

    # # Example 4: Using XOR to find the missing number
    # def missingNumber(self, nums: List[int]) -> int:
    #     n = len(nums)

    #     missing = n  # Start with n, which is the missing number if all 0 to n-1 are present
    #     for i in range(n):
    #         missing ^= i ^ nums[i]  # XOR with index and value
            
    #     return missing